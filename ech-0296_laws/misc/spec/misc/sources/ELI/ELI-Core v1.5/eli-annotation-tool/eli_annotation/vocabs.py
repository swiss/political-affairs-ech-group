# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import os
import os.path as osp
import glob, rdflib, json, zipfile, shutil
from operator import attrgetter
import logging

from rdflib.namespace import RDF, SKOS, DCTERMS

from eli_annotation import any2skos, eligraph
from .xslt_transform import WHOLE_PAGE

from .errors import IncorrectResource, ELIError


STANDARD_VOCAB_FILES = ["in-force.ttl", "languages.ttl", "legal-value.ttl",
                        "media-types.ttl"]


class VocabularyIndex:
    """
    Given a directory where SKOS vocabularies are stored
    as RDF/XML files with extension .rdf, manage an index
    that behaves like a dict of {ConceptSchemeURI: filename}.

    >>> idx = VocabularyIndex('some/path/to/vocabs')
    >>> idx['http://publications.europa.eu/resource/authority/language']
    'languages-skos'
    >>> idx.load('http://publications.europa.eu/resource/authority/language')
    <Vocabulary ...>
    """

    def __init__(self, vocabs_dir):
        self.basedir = vocabs_dir
        self._data = self.read()

    @property
    def index_path(self):
        return osp.join(self.basedir,'index.json')

    def __getitem__(self, uri):
        if isinstance(uri, rdflib.term.URIRef):
            uri = str(uri)
        return self._data[uri]

    def __delitem__(self, uri):
        if isinstance(uri, rdflib.term.URIRef):
            uri = str(uri)
        del self._data[uri]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def items(self):
        return self._data.items()

    def path(self, uri):
        if isinstance(uri, rdflib.term.URIRef):
            uri = str(uri)
        return osp.join(self.basedir, self._data[uri])

    def regenerate(self, force=False):
        fpaths = glob.glob(osp.join(self.basedir,'*.rdf'))
        if not force and osp.exists(self.index_path):
            mtime = max((osp.getmtime(fpath) for fpath in fpaths), default=0)
            if mtime < osp.getmtime(self.index_path):
                # Skips regeneration as index is more recent than files
                return
        vocabs = {}
        for fpath in fpaths:
            try:
                g = rdflib.Graph()
                g.parse(fpath)
                name = g.value(None, RDF.type, SKOS.ConceptScheme)
                if name is None:
                    raise ValueError(
                        "RDF graph doesn't contain a SKOS Vocabulary")
                vocabs[str(name)] = osp.splitext(osp.basename(fpath))[0]
            except Exception as exc:
                logging.warning(
                    "In vocabulary directory, skipping {} that doesn't contain "
                    "a valid SKOS vocabulary".format(fpath))
        self.write(vocabs)

    def read(self):
        self.regenerate()
        with open(self.index_path, encoding='utf-8') as fp:
            data = json.load(fp)
        return data

    def write(self, data=None):
        if data is None:
            data = self._data
        with open(self.index_path, 'w', encoding='utf-8') as out:
            json.dump(data, out, indent=2, sort_keys=True)
        self._data = data

    def load(self, uri):
        filename = self.path(uri)+'.rdf'
        if not osp.isfile(filename):
            msg = "Can't find the SKOS/RDF file for vocabulary: {0}".format(uri)
            raise IncorrectResource("missingVocabulary", msg, str(uri))
        try:
            graph = rdflib.Graph()
            graph.parse(filename)
            vocs = Vocabulary.load_from_skos(graph)
        except Exception as exc:
            msg = ("An error occurred while reading the SKOS/RDF file for "
                   "vocabulary: {0}".format(uri))
            raise IncorrectResource("incorrectVocabulary", msg,
                                    str(uri)) from exc
        if len(vocs) == 0:
            msg = ("Can't find a ConceptScheme in SKOS/RDF file for vocabulary"
                   ": {0}").format(uri)
            raise IncorrectResource("incorrectVocabulary", msg, str(uri))
        if len(vocs) > 1:
            msg = ("Found multiple ({0}) ConceptScheme in SKOS/RDF file for "
                   "vocabulary: {1}").format(len(vocs), uri)
            raise IncorrectResource("incorrectVocabulary", msg, str(uri))
        return vocs[0]


# Deletes vocabulary ##########################################################

def delete_vocab(uri, vocab_idx):
    """
    Deletes a vocabulary whose URI is ``uri`` from the ``vocab_idx`` index.
    """
    assert isinstance(vocab_idx, VocabularyIndex), type(vocab_idx)
    try:
        pth = vocab_idx.path(uri)
    except KeyError:
        return # Already deleted
    for fpath in glob.glob(pth+'.*'):
        os.remove(fpath)
    if osp.isdir(pth+"_html"):
        shutil.rmtree(pth+"_html")
    del vocab_idx[uri]
    vocab_idx.write()


# Adds vocabulary from various formats ########################################

def add_xml_vocab(input_file, vocab_idx, localizations_dir,
                  html_langs, index_lang="en", html_rendering=WHOLE_PAGE):
    """
    Reads the data from the ``input_file`` opened file, builds a vocabulary
    RDF graph, adds it to the vocabulary index and saves it in various formats
    (RDF, CSV, HTML).

    ``input_file`` is expected to be an RDF-XML file.

    ``vocab_idx`` is the vocabulary index.

    ``localizations_dir`` is the directory containing the glossary.xml file
    used for XSLT transforms (cf. ``l10n_dir`` attribute of DataIndex).

    ``html_langs`` is the list of the languages (2-letters codes) in which
    the vocabulary must be rendered in HTML. E.g. ``["en", "fr"]``

    Returns the list of URIs of the added vocabularies and the list of warnings.
    """
    graph = rdflib.Graph()
    graph.parse(input_file, format='xml')
    uri = generate_vocabs_formats(graph, vocab_idx, localizations_dir,
                                  html_langs, index_lang, html_rendering)
    return [str(uri)], []


def add_turtle_vocab(input_file, vocab_idx, localizations_dir,
                     html_langs, index_lang="en", html_rendering=WHOLE_PAGE):
    """
    Reads the data from the ``input_file`` opened file, builds a vocabulary
    RDF graph, adds it to the vocabulary index and saves it in various formats
    (RDF, CSV, HTML).

    ``input_file`` is expected to be an RDF-Turtle file.

    ``vocab_idx`` is the vocabulary index.

    ``localizations_dir`` is the directory containing the glossary.xml file
    used for XSLT transforms (cf. ``l10n_dir`` attribute of DataIndex).

    ``html_langs`` is the list of the languages (2-letters codes) in which
    the vocabulary must be rendered in HTML. E.g. ``["en", "fr"]``

    Returns the list of URIs of the added vocabularies and the list of warnings.
    """
    graph = rdflib.Graph()
    graph.parse(input_file, format='turtle')
    uri = generate_vocabs_formats(graph, vocab_idx, localizations_dir,
                                  html_langs, index_lang, html_rendering)
    return [str(uri)], []


def add_excel_vocab(input_file, vocab_idx, localizations_dir,
                    html_langs, index_lang="en", html_rendering=WHOLE_PAGE):
    """
    Reads the data from the ``input_file`` opened file, builds a vocabulary
    RDF graph, adds it to the vocabulary index and saves it in various formats
    (RDF, CSV, HTML).

    ``input_file`` is expected to be an Excel file.

    ``vocab_idx`` is the vocabulary index.

    ``localizations_dir`` is the directory containing the glossary.xml file
    used for XSLT transforms (cf. ``l10n_dir`` attribute of DataIndex).

    ``html_langs`` is the list of the languages (2-letters codes) in which
    the vocabulary must be rendered in HTML. E.g. ``["en", "fr"]``

    Returns the list of URIs of the added vocabularies and the list of warnings.
    """
    warnings = []
    uris = []
    skos_properties = any2skos.get_skos_properties()
    dcmi_properties = any2skos.get_dcmi_properties()
    result, warns = any2skos.xl2skos(input_file,
                                     skos_properties | dcmi_properties)
    warnings.extend(warns)
    for uri, graph in result.items():
        try:
            voc_uri = generate_vocabs_formats(
                graph, vocab_idx, localizations_dir, html_langs, index_lang,
                html_rendering)
            assert str(uri) == str(voc_uri), "Unexpected vocabulary URI"
            uris.append(str(uri))
        except ELIError as exc:
            exc.context = str(uri)
            warnings.append(exc)
    return uris, warnings


# Adds vocabulary graph and generates various formats (RDF, CSV, HTML) ########

def generate_vocabs_formats(graph, vocab_idx, localizations_dir,
                            html_langs, index_lang="en",
                            html_rendering=WHOLE_PAGE):
    """
    Saves ``graph`` vocabulary in several formats and updates the ``vocab_idx``
    index.

    ``localizations_dir`` is the directory containing the glossary.xml file
    used for XSLT transforms (cf. ``l10n_dir`` attribute of DataIndex).

    ``html_langs`` is the list of the languages (2-letters codes) in which
    the vocabulary must be rendered in HTML. E.g. ``["en", "fr"]``

    This function is called by the ``add_xxx_vocab`` functions.
    """
    assert isinstance(vocab_idx, VocabularyIndex), type(vocab_idx)
    uri = graph.value(None, RDF.type, SKOS.ConceptScheme)
    if uri is None:
        msg = ("Can't find a ConceptScheme in RDF graph. It doesn't seem to "
               "define a SKOS vocabulary.")
        raise IncorrectResource("incorrectVocabulary", msg)
    # Try to load the SKOS graph into a Vocabulary object, just to check
    # everything is ok.
    vocs = Vocabulary.load_from_skos(graph)
    if len(vocs) == 0:
        msg = ("Can't find a ConceptScheme in SKOS/RDF graph for vocabulary: "
               "{0}").format(str(uri))
        raise IncorrectResource("incorrectVocabulary", msg, str(uri))
    if len(vocs) > 1:
        msg = ("Found multiple ({0}) ConceptScheme in SKOS/RDF graph for "
               "vocabulary: {1}").format(len(vocs), str(uri))
        raise IncorrectResource("incorrectVocabulary", msg, str(uri))
    voc = vocs[0]
    # If the vocabulary is the language vocabulary, check all the vocabulary
    # values (Concept) have a notation
    if uri.strip() in (eligraph.LANG_VOCAB_URI, eligraph.FILETYPE_VOCAB_URI):
        no_notation = [val for val in voc.values() if val.notation is None]
        if len(no_notation) > 0:
            val_uris = [val.uri for val in no_notation]
            msg = "The {0} vocabulary defines the ".format(str(uri))
            if uri.strip()  == eligraph.LANG_VOCAB_URI:
                msg += ("languages. All its concepts must have a notation "
                        "property giving the 2-letters code of the "
                        "corresponding language. This code will be "
                        "used in the URIs of the ELI entities.\n")
            else:
                msg += ("filetypes. All its concepts must have a notation "
                        "property giving the term that will be used in the "
                        "URIs of the ELI entities.\n")
            msg += ("The following concepts don't have any notation defined:\n"
                    "{0}".format(" ".join(val_uris)))
            raise IncorrectResource("missingNotationForConceptInVocabulary",
                                    msg, str(uri))
    # Generates various formats and saves them
    filename = eligraph.uri2filename(uri)
    fpath_rdf = osp.join(vocab_idx.basedir,filename+'.rdf')
    fpath_html = osp.join(vocab_idx.basedir,filename+'_html')
    fpath_csv = osp.join(vocab_idx.basedir,filename+'.csv')
    fpath_jsonld = osp.join(vocab_idx.basedir,filename+'.jsonld')
    fpath_zip = osp.join(vocab_idx.basedir,filename+'.zip')
    try:
        with open(fpath_rdf, 'wb') as out:
            out.write(graph.serialize(format='xml').encode('utf-8'))
        any2skos.skos2csv(fpath_rdf, fpath_csv)
        with open(fpath_jsonld, 'wb') as out:
            out.write(graph.serialize(format='json-ld',indent=2).encode('utf-8'))
        any2skos.skos2html(fpath_rdf, fpath_html, filename, localizations_dir,
                           html_langs, index_lang, html_rendering)
        # Generates archive file
        with zipfile.ZipFile(fpath_zip, 'w') as zip_inp:
            for html_fname in os.listdir(fpath_html):
                if html_fname == "index.html":
                    continue
                zip_inp.write(osp.join(fpath_html, html_fname), html_fname)
            for res_fname in ['static/eli-tool.css',
                              'static/bootstrap/css/bootstrap.min.css',
                              'static/bootstrap/js/bootstrap.min.js',
                              'static/jquery/jquery.min.js']:
                zip_inp.write(osp.join(osp.dirname(__file__), res_fname),
                              res_fname)
    except Exception as exc:
        # Before raising the exception, cleans the files that might have been
        # written and that might contain erroneous data
        for pth in [fpath_rdf, fpath_csv, fpath_jsonld, fpath_zip]:
            try:
                os.remove(pth)
            except Exception:
                pass
        if osp.isdir(fpath_html):
            try:
                shutil.rmtree(fpath_html)
            except Exception:
                pass
        vocab_idx.regenerate()
        raise exc
    # Regenerates index
    vocab_idx.regenerate()
    return uri


# Deploy standard vocabularies in index #######################################

def deploy_standard_vocabs(vocab_idx, localizations_dir,
                           html_langs, index_lang="en"):
    assert isinstance(vocab_idx, VocabularyIndex), type(vocab_idx)
    for fname in STANDARD_VOCAB_FILES:
        fpath = osp.join(any2skos.STANDARD_VOCABS_DIR, fname)
        with open(fpath, "rb") as inp:
            add_turtle_vocab(inp, vocab_idx, localizations_dir,
                             html_langs, index_lang)


# Vocabulary objects ##########################################################

class Vocabulary:
    """
    Class describing a vocabulary that contains values (e.g. a ConceptScheme
    in a SKOS graph)

    This class contains a dictionary of VocabValue.
    """
    def __init__(self, uri):
        self.uri = uri
        self._values = {}

    def add_value(self, uri, notation=None, labels=None):
        """
        Adds the vocabulary value whose URI is ``uri``.

        The vocabulary value is added as a ``VocabValue`` object.
        ``labels`` is a dictionary of language codes associated to the
        corresponding labels of this vocabulary value.
        """
        if uri in self._values:
            value = self._values[uri]
            if notation is not None:
                value.notation = notation
            value.set_labels(labels)
            return
        value = VocabValue(uri, self, notation, labels)
        self._values[uri] = value

    def __getitem__(self, uri):
        """
        Gets the vocabulary value whose URI is ``uri``.
        """
        return self._values[uri]

    def get(self, uri, default=None):
        """
        Gets the vocabulary value whose URI is ``uri`` or returns ``default``
        if it doesn't exist.
        """
        return self._values.get(uri, default)

    def values(self):
        """
        Returns the list of all the VocabValue objects
        """
        return sorted(self._values.values(), key=attrgetter("uri"))

    @classmethod
    def load_from_skos(cls, graph):
        """
        Reads a RDF/SKOS graph and returns a list of Vocabulary objects
        corresponding to the ConceptScheme defined in this graph.
        """
        vocabularies = []
        for sch in graph.subjects(RDF.type, SKOS.ConceptScheme):
            vocab = cls(str(sch))
            concepts = set(graph.subjects(SKOS.inScheme, sch)).union(
                set(graph.objects(sch, SKOS.hasTopConcept)))
            for cpt in concepts:
                labels = {}
                notation = None
                for notat in graph.objects(cpt, SKOS.notation):
                    notation = str(notat)
                for ttl in graph.objects(cpt, DCTERMS.title):
                    labels[ttl.language] = str(ttl)
                for lbl in graph.objects(cpt, SKOS.prefLabel):
                    labels[lbl.language] = str(lbl)
                vocab.add_value(str(cpt), notation, labels)
            vocabularies.append(vocab)
        return vocabularies


class VocabValue:
    """
    Class describing a value inside a vocabulary (e.g. Concept in a SKOS graph)

    This class only contains the complete URI, the local identifier inside the
    vocabulary and all the defined labels for the languages.
    """
    def __init__(self, uri, vocab, notation=None, labels=None):
        self.vocabulary = vocab
        self.uri = uri
        self.notation = notation
        self.labels = {}
        self.set_labels(labels)

    def set_labels(self, labels):
        """
        Sets the labels of this vocabulary value.

        ``labels`` is a dictionary associating language codes to the actual
        labels.
        """
        if labels is None:
            return
        self.labels.update(labels)

    def __repr__(self):
        return "<VocabValue {}>".format(self.uri)
