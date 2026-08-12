# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import unittest
import os, tempfile, json, rdflib
from os import path as osp
from rdflib.namespace import RDF, SKOS

from eli_annotation import notices, datamanager, eligraph, any2eli


try:
    from .helpers import silence_logging_warning
except SystemError:
    from helpers import silence_logging_warning


def get_datafile(fname):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),'data',fname))


class NoticesTC(unittest.TestCase):

    def test_noticeindex_regenerate(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            idx = datamanager.DataIndex(tmpdir)
            notice_dir = idx.notice_index.basedir
            rdf_graph = rdflib.Graph()
            with open(get_datafile("act-01.ttl")) as inp:
                rdf_graph.parse(inp, format="turtle")
            uri = any2eli.ensure_single_legal_resource(rdf_graph)
            fpath = os.path.join(notice_dir,
                                 eligraph.uri2filename(uri))
            with open(fpath+'.rdf', "wb") as out:
                 out.write(rdf_graph.serialize(format="xml"))
            idx.notice_index.regenerate(force=True)
            expected = {
                'http://example/2017/ABC/ACT': {
                    'filename': 'http__example_2017_ABC_ACT',
                    'type': "elix:Act",
                    'datetime': '2017-09-22T12:00:01+00:00'
                }
            }
            self.assertEqual(len(idx.notice_index), 1)
            self.assertEqual(idx.notice_index.items(),
                             expected.items())

    def test_noticeindex_regenerate_with_erroneous_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            idx = datamanager.DataIndex(tmpdir)
            notice_dir = idx.notice_index.basedir
            rdf_graph = rdflib.Graph()
            with open(get_datafile("act-01.ttl")) as inp:
                rdf_graph.parse(inp, format="turtle")
            uri = any2eli.ensure_single_legal_resource(rdf_graph)
            fpath = os.path.join(notice_dir,
                                 eligraph.uri2filename(uri))
            with open(fpath+'.rdf', "wb") as out:
                 out.write(rdf_graph.serialize(format="xml"))
            graph = rdflib.Graph()
            graph.add( (rdflib.URIRef("http://EX/Empty"),
                        RDF.type, SKOS.ConceptScheme) )
            with open(osp.join(notice_dir, "http_EX_Empty.rdf"), "wb") as out:
                graph.serialize(out, format="xml")
            with open(osp.join(notice_dir, "http_WRONG.rdf"), "w") as out:
                out.write("WRONG CONTENT")
            with silence_logging_warning():
                idx.notice_index.regenerate(force=True)
            expected = {
                'http://example/2017/ABC/ACT': {
                    'filename': 'http__example_2017_ABC_ACT',
                    'type': "elix:Act",
                    'datetime': '2017-09-22T12:00:01+00:00'
                }
            }
            self.assertEqual(len(idx.notice_index), 1)
            self.assertEqual(idx.notice_index.items(),
                             expected.items())

    def test_notice_write_then_delete(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            idx = datamanager.DataIndex(tmpdir)
            rdf_graph = rdflib.Graph()
            with open(get_datafile("act-01.ttl")) as inp:
                rdf_graph.parse(inp, format="turtle")
            uri = any2eli.ensure_single_legal_resource(rdf_graph)
            with open(get_datafile("act-01.json")) as inp:
                json_data = json.load(inp)
            notices.write_notice(uri, rdf_graph, json_data,
                                 idx.notice_index, idx.l10n_dir)
            self.assertEqual(len(idx.notice_index), 1)
            files = sorted(os.listdir(idx.notice_index.basedir))
            self.assertEqual(files,
                             ['http__example_2017_ABC_ACT.json',
                              'http__example_2017_ABC_ACT.rdf',
                              'http__example_2017_ABC_ACT.zip',
                              'http__example_2017_ABC_ACT_html',
                              'index.json'])
            notices.delete_notice(uri, idx.notice_index)
            self.assertEqual(len(idx.notice_index), 0)
            files = sorted(os.listdir(idx.vocab_index.basedir))
            self.assertEqual(files, ['index.json'])



if __name__ == '__main__':
    unittest.main()
