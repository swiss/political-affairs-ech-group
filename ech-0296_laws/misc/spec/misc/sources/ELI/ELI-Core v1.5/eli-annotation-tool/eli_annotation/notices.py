# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import os
import os.path as osp
import glob, json, shutil, zipfile, logging
from dateutil.parser import parse as datetime_parse
import rdflib
from rdflib.namespace import FOAF

from eli_annotation import any2eli
from .eligraph import ELI, ELIX, PROV, uri2filename, compact_uri
from .xslt_transform import WHOLE_PAGE


def write_notice(uri, rdf_notice, json_notice, notice_idx, localizations_dir,
                 index_lang="en", html_rendering=WHOLE_PAGE):
    assert isinstance(notice_idx, NoticeIndex), type(notice_idx)
    fpath = osp.join(notice_idx.basedir, uri2filename(uri))
    try:
        # Writes RDF
        with open(fpath+'.rdf', "wb") as out:
            out.write(rdf_notice.serialize(format="xml").encode('utf-8'))
        # Writes HTML (multiple files)
        any2eli.eli2html(fpath+'.rdf', fpath+"_html", localizations_dir,
                         index_lang, html_rendering)
        # Writes JSON
        with open(fpath+'.json', 'w', encoding='utf-8') as out:
            json.dump(json_notice, out, indent=2, sort_keys=True)
        # Generates archive file
        with zipfile.ZipFile(fpath+".zip", 'w') as zip_inp:
            for subdir in (any2eli.EXPRESSIONS_SUBDIR, any2eli.FORMATS_SUBDIR):
                dirname = osp.join(fpath+"_html", subdir)
                if not osp.isdir(dirname):
                    continue
                for html_fname in os.listdir(dirname):
                    if html_fname == "index.html":
                        continue
                    zip_inp.write(osp.join(dirname, html_fname),
                                  osp.join(subdir, html_fname))
            for res_fname in ['static/eli-tool.css',
                              'static/bootstrap/css/bootstrap.min.css',
                              'static/bootstrap/js/bootstrap.min.js',
                              'static/jquery/jquery.min.js']:
                zip_inp.write(osp.join(osp.dirname(__file__), res_fname),
                              res_fname)
    except Exception as exc:
        # Before raising the exception, cleans the files that might have been
        # written and that might contain erroneous data
        for pth in glob.glob(fpath+'.*'):
            try:
                os.remove(pth)
            except Exception:
                pass
        if osp.isdir(fpath+"_html"):
            try:
                shutil.rmtree(fpath+"_html")
            except Exception:
                pass
        notice_idx.regenerate()
        raise exc
    # Regenerates the notices index
    notice_idx.regenerate()
    return uri


def delete_notice(uri, notice_idx):
    assert isinstance(notice_idx, NoticeIndex), type(notice_idx)
    try:
        pth = notice_idx.path(uri)
    except KeyError:
        return # Already deleted
    for fpath in glob.glob(pth+'.*'):
        os.remove(fpath)
    if osp.isdir(pth+"_html"):
        shutil.rmtree(pth+"_html")
    del notice_idx[uri]
    notice_idx.write()


class NoticeIndex:
    """
    Given a directory where notices are stored, manages an index
    that behaves like a dict of {NoticeURI: filename}

    >>> idx = NoticeIndex('some/path/to/notices')
    >>> idx['http://legilux.lu/eli/path/to/act']
    'http___legilux.lu_eli_path_to_act'
    """

    def __init__(self, basedir):
        self.basedir = osp.abspath(basedir)
        self._data = self.read()

    @property
    def index_path(self):
        return osp.join(self.basedir, 'index.json')

    def __getitem__(self, uri):
        return self._data[uri]

    def __delitem__(self, uri):
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
        return osp.join(self.basedir, self._data[uri]["filename"])

    def resource_type(self, uri):
        if isinstance(uri, rdflib.term.URIRef):
            uri = str(uri)
        return self._data[uri]["type"]

    def datetime(self, uri):
        if isinstance(uri, rdflib.term.URIRef):
            uri = str(uri)
        return self._data[uri]["datetime"]

    def regenerate(self, force=False):
        fpaths = glob.glob(osp.join(self.basedir,'*.rdf'))
        if not force and osp.exists(self.index_path):
            mtime = max((osp.getmtime(fpath) for fpath in fpaths), default=0)
            if mtime < osp.getmtime(self.index_path):
                # Skips regeneration as index is more recent than files
                return
        notices = {}
        for fpath in fpaths:
            try:
                g = rdflib.Graph()
                g.parse(fpath)
                # Reads URI of LegalResource
                uri = g.value(None, rdflib.RDF.type, ELI.LegalResource)
                if uri is None:
                    raise ValueError(
                        "RDF graph doesn't contain an ELI LegalResource")
                # Reads resource type of LegalResource
                res_type = g.value(uri, ELIX.resource_type, None)
                if res_type is None:
                    raise ValueError(
                        "In RDF graph, ELI LegalResource doesn't have a "
                        "resource type")
                # Reads creation datetime of LegalResource
                dtime_val = None
                crea_uri = g.value(None, FOAF.primaryTopic, uri)
                if crea_uri is not None:
                    str_dtime = g.value(crea_uri, PROV.generatedAtTime, None)
                    try:
                        dtime = datetime_parse(str_dtime)
                        dtime_val = dtime.isoformat()
                    except Exception as exc:
                        pass
                notices[str(uri)] = {
                    "filename": osp.splitext(osp.basename(fpath))[0],
                    "type": compact_uri(res_type),
                    "datetime": dtime_val}
            except Exception:
                logging.warning(
                    "In notices directory, skipping {} that doesn't contain "
                    "a valid ELI notice".format(fpath))
        self.write(notices)

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

