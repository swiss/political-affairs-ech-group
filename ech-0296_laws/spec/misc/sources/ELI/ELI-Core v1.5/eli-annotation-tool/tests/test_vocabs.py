# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import unittest
import os, tempfile, json, rdflib
from os import path as osp
from rdflib.namespace import RDF

from eli_annotation import vocabs, datamanager, any2skos
from eli_annotation.eligraph import ELI, ELIGraph


try:
    from .helpers import silence_logging_warning
except SystemError:
    from helpers import silence_logging_warning


def get_datafile(fname):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),'data',fname))


class VocabsTC(unittest.TestCase):

    def test_vocabindex_regenerate(self):
        vocab_dir = get_datafile('vocabs')
        idx = vocabs.VocabularyIndex(vocab_dir)
        os.remove(idx.index_path)
        idx.regenerate(force=True)
        self.assertEqual(len(idx), 4)
        expected = {
            "http://publications.europa.eu/resource/authority/language": "languages-skos",
            "http://data.sparna.fr/vocabularies/days": "weekdays",
            "http://test.logilab.org/document": "document_types",
            "https://www.iana.org/assignments/media-types": "mediatypes-skos",
        }
        self.assertEqual(idx.items(), expected.items())

    def test_vocabindex_regenerate_with_erroneous_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            idx = datamanager.DataIndex(tmpdir)
            vocab_dir = idx.vocab_index.basedir
            skos_properties = any2skos.get_skos_properties()
            dcmi_properties = any2skos.get_dcmi_properties()
            graph = ELIGraph()
            with open(get_datafile('test00.ttl'), "rb") as inp:
                graph.parse(inp, format="turtle")
            vocabs.generate_vocabs_formats(graph, idx.vocab_index, idx.l10n_dir,
                                           ["en", "fr"])
            graph = ELIGraph()
            graph.add( (rdflib.URIRef("http://EX/Empty"), RDF.type, ELI.LegalResource) )
            with open(osp.join(vocab_dir, "http_EX_Empty.rdf"), "wb") as out:
                graph.serialize(out, format="xml")
            with open(osp.join(vocab_dir, "http_WRONG.rdf"), "w") as out:
                out.write("WRONG CONTENT")
            with silence_logging_warning():
                idx.vocab_index.regenerate(force=True)
            #self.assertEqual(len(idx.vocab_index), 1)
            expected = {
                "http://data.sparna.fr/vocabularies/days": "http__data.sparna.fr_vocabularies_days",
            }
            self.maxDiff = None
            self.assertEqual(idx.vocab_index.items(), expected.items())

    def test_generate_formats_then_delete(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            idx = datamanager.DataIndex(tmpdir)
            skos_properties = any2skos.get_skos_properties()
            dcmi_properties = any2skos.get_dcmi_properties()
            result, warns = any2skos.xl2skos(get_datafile('test00.xlsx'), skos_properties | dcmi_properties)
            uri = 'http://data.sparna.fr/vocabularies/days'
            graph = result[uri]
            vocabs.generate_vocabs_formats(graph, idx.vocab_index, idx.l10n_dir,
                                           ["en", "fr"])
            self.assertEqual(len(idx.vocab_index), 1)
            files = sorted(os.listdir(idx.vocab_index.basedir))
            self.assertEqual(files,
                             ['http__data.sparna.fr_vocabularies_days.csv',
                              'http__data.sparna.fr_vocabularies_days.jsonld',
                              'http__data.sparna.fr_vocabularies_days.rdf',
                              'http__data.sparna.fr_vocabularies_days.zip',
                              'http__data.sparna.fr_vocabularies_days_html',
                              'index.json'])
            files = sorted(os.listdir(
                os.path.join(idx.vocab_index.basedir,
                             'http__data.sparna.fr_vocabularies_days_html')))
            self.assertEqual(files,
                             ['http__data.sparna.fr_vocabularies_days.en.html',
                              'http__data.sparna.fr_vocabularies_days.fr.html',
                              'index.html'])
            vocabs.delete_vocab(uri, idx.vocab_index)
            files = sorted(os.listdir(idx.vocab_index.basedir))
            self.assertEqual(len(idx.vocab_index), 0)
            self.assertEqual(files, ['index.json'])

    def test_add_xml_vocab(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            idx = datamanager.DataIndex(tmpdir)
            with open(get_datafile("in-force.xml"), "rb") as inp:
                uris, warns = vocabs.add_xml_vocab(
                    inp, idx.vocab_index, idx.l10n_dir, ["en", "fr"])
            self.assertEqual(uris,
                              ["http://data.europa.eu/eli/ontology#InForce-"])
            files = sorted(os.listdir(idx.vocab_index.basedir))
            self.assertEqual(files,
                             ['http__data.europa.eu_eli_ontology_InForce-.csv',
                              'http__data.europa.eu_eli_ontology_InForce-.jsonld',
                              'http__data.europa.eu_eli_ontology_InForce-.rdf',
                              'http__data.europa.eu_eli_ontology_InForce-.zip',
                              'http__data.europa.eu_eli_ontology_InForce-_html',
                              'index.json'])
            files = sorted(os.listdir(
                os.path.join(idx.vocab_index.basedir,
                             'http__data.europa.eu_eli_ontology_InForce-_html')))
            self.assertEqual(files,
                             ['http__data.europa.eu_eli_ontology_InForce-.en.html',
                              'http__data.europa.eu_eli_ontology_InForce-.fr.html',
                              'index.html'])

    def test_add_ttl_vocab(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            idx = datamanager.DataIndex(tmpdir)
            with open(get_datafile("in-force.ttl"), "rb") as inp:
                uris, warns = vocabs.add_turtle_vocab(
                    inp, idx.vocab_index, idx.l10n_dir, ["en", "fr"])
            self.assertEqual(uris,
                              ["http://data.europa.eu/eli/ontology#InForce-"])
            files = sorted(os.listdir(idx.vocab_index.basedir))
            self.assertEqual(files,
                             ['http__data.europa.eu_eli_ontology_InForce-.csv',
                              'http__data.europa.eu_eli_ontology_InForce-.jsonld',
                              'http__data.europa.eu_eli_ontology_InForce-.rdf',
                              'http__data.europa.eu_eli_ontology_InForce-.zip',
                              'http__data.europa.eu_eli_ontology_InForce-_html',
                              'index.json'])
            files = sorted(os.listdir(
                os.path.join(idx.vocab_index.basedir,
                             'http__data.europa.eu_eli_ontology_InForce-_html')))
            self.assertEqual(files,
                             ['http__data.europa.eu_eli_ontology_InForce-.en.html',
                              'http__data.europa.eu_eli_ontology_InForce-.fr.html',
                              'index.html'])

    def test_add_excel_vocab(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            idx = datamanager.DataIndex(tmpdir)
            with open(get_datafile("test03.xlsx"), "rb") as inp:
                uris, warns = vocabs.add_excel_vocab(
                    inp, idx.vocab_index, idx.l10n_dir, ["en", "fr"])
            self.assertEqual(sorted(uris),
                              ['http://data.sparna.fr/vocabularies/days',
                               'http://test.logilab.org/document'])
            self.assertEqual(len(idx.vocab_index), 2)
            files = sorted(os.listdir(idx.vocab_index.basedir))
            self.assertEqual(files,
                             ['http__data.sparna.fr_vocabularies_days.csv',
                              'http__data.sparna.fr_vocabularies_days.jsonld',
                              'http__data.sparna.fr_vocabularies_days.rdf',
                              'http__data.sparna.fr_vocabularies_days.zip',
                              'http__data.sparna.fr_vocabularies_days_html',
                              'http__test.logilab.org_document.csv',
                              'http__test.logilab.org_document.jsonld',
                              'http__test.logilab.org_document.rdf',
                              'http__test.logilab.org_document.zip',
                              'http__test.logilab.org_document_html',
                              'index.json'])
            files = sorted(os.listdir(
                os.path.join(idx.vocab_index.basedir,
                             'http__data.sparna.fr_vocabularies_days_html')))
            self.assertEqual(files,
                             ['http__data.sparna.fr_vocabularies_days.en.html',
                              'http__data.sparna.fr_vocabularies_days.fr.html',
                              'index.html'])
            files = sorted(os.listdir(
                os.path.join(idx.vocab_index.basedir,
                             'http__test.logilab.org_document_html')))
            self.assertEqual(files,
                             ['http__test.logilab.org_document.en.html',
                              'http__test.logilab.org_document.fr.html',
                              'index.html'])

    def test_deploy_standard_vocabs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            idx = datamanager.DataIndex(tmpdir)
            self.assertEqual(len(idx.vocab_index), 0)
            vocabs.deploy_standard_vocabs(idx.vocab_index, idx.l10n_dir,
                                          ["en", "fr"])
            self.assertEqual(len(idx.vocab_index), 4)
            expected = {
                "https://www.iana.org/assignments/media-types": "https__www.iana.org_assignments_media-types",
                "http://publications.europa.eu/resource/authority/language": "http__publications.europa.eu_resource_authority_language",
                "http://data.europa.eu/eli/ontology#LegalValue-": "http__data.europa.eu_eli_ontology_LegalValue-",
                "http://data.europa.eu/eli/ontology#InForce-": "http__data.europa.eu_eli_ontology_InForce-",
            }
            self.assertEqual(idx.vocab_index.items(), expected.items())


if __name__ == '__main__':
    unittest.main()
