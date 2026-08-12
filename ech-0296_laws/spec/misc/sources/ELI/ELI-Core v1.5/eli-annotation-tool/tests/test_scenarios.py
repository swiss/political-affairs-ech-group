# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import unittest
import os, json, tempfile, shutil, rdflib
import datetime as dtm
from lxml import html
from operator import itemgetter

from eli_annotation import datamanager, vocabs, any2skos, notices, any2eli, eligraph


def get_datafile(fname):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),'data',fname))


class ScenarioOneTC(unittest.TestCase):

    def test_scenario(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            idx = datamanager.DataIndex(tmpdir)

            # Adds vocabularies
            fname = get_datafile("test03.xlsx")
            with open(fname, "rb") as inp:
                vocabs.add_excel_vocab(inp, idx.vocab_index,
                                       idx.l10n_dir, ["en"])
            fname = get_datafile('in-force.ttl')
            with open(fname, "rb") as inp:
                vocabs.add_turtle_vocab(inp, idx.vocab_index,
                                        idx.l10n_dir, ["en"])
            fname = get_datafile(os.path.join('vocabs', 'languages-skos.rdf'))
            with open(fname, "rb") as inp:
                vocabs.add_xml_vocab(inp, idx.vocab_index,
                                     idx.l10n_dir, ["en"])
            fname = get_datafile(os.path.join('vocabs', 'mediatypes-skos.rdf'))
            with open(fname, "rb") as inp:
                vocabs.add_xml_vocab(inp, idx.vocab_index,
                                     idx.l10n_dir, ["en"])
            files = sorted(os.listdir(idx.vocab_index.basedir))
            self.assertEqual(len(files), 26)
            with open(idx.vocab_index.index_path) as inp:
                json_idx = json.load(inp)
            self.assertEqual(json_idx, {
                'http://data.sparna.fr/vocabularies/days': 'http__data.sparna.fr_vocabularies_days',
                'http://test.logilab.org/document': 'http__test.logilab.org_document',
                'http://data.europa.eu/eli/ontology#InForce-': 'http__data.europa.eu_eli_ontology_InForce-',
                'http://publications.europa.eu/resource/authority/language': 'http__publications.europa.eu_resource_authority_language',
                'https://www.iana.org/assignments/media-types': 'https__www.iana.org_assignments_media-types'})

            # Configures form
            shutil.copy(get_datafile(os.path.join("forms", "act.json")),
                        os.path.join(tmpdir, "forms", "act.json"))
            shutil.copy(get_datafile(os.path.join("forms", "act-values.json")),
                        os.path.join(tmpdir, "forms", "act-values.json"))

            # Fills out form
            fname = os.path.join(tmpdir,'forms','act-values.json')
            with open(fname) as inp:
                formdata = json.load(inp)
            formdata['eli:date_document']['value'] = "2017-09-10"
            formdata['eli:id_local']['value'] = ["id001", "id001-a"]
            formdata['eli:is_about']['value'] = "http://data.sparna.fr/vocabularies/days#monday"
            formdata['eli:number']['value'] = "1234"
            formdata['eli:type_document']['value'] = "http://test.logilab.org/document#ABC"
            formdata['lang_ENG']['eli:id_local']['value'] = "id001-eng"
            formdata['lang_ENG']['eli:title']['value'] = "The title of my notice"
            formdata['lang_ENG']['format_PRINT']['eli:published_in']['value'] = "A very famous journal"
            formdata['lang_ENG']['format_pdf']['eli:id_local']['value'] = "id001-eng/pdf"
            formdata['lang_ENG']['format_pdf']['eli:is_exemplified_by']['value'] = 'http://example/some/PDF/document'
            formdata['lang_FRA']['eli:id_local']['value'] = "id001-fra"
            formdata['lang_FRA']['eli:title']['value'] = "Le titre de ma notice"
            formdata['lang_FRA']['format_PRINT']['eli:id_local']['value'] = "id001-fra/print"
            # Keeping default value for
            # formdata['lang_FRA']['format_PRINT']['eli:published_in']['value']
            formdata['lang_FRA']['format_pdf']['eli:is_exemplified_by']['value'] = 'http://example/un/document/PDF'

            # Builds rdf from form
            now = dtm.datetime(2017,9,22,12,0,1)
            uri, rdf_notice = any2eli.form2eli(
                formdata, idx.form_index, idx.vocab_index,
                "http://example/users/bob42", now)
            # Saves form in various formats
            notices.write_notice(uri, rdf_notice, formdata, idx.notice_index,
                                 idx.l10n_dir)
            files = sorted(os.listdir(idx.notice_index.basedir))
            self.assertEqual(files, [
                'http__example_2017_ABC_ACT.json',
                'http__example_2017_ABC_ACT.rdf',
                'http__example_2017_ABC_ACT.zip',
                'http__example_2017_ABC_ACT_html',
                'index.json'])
            dirpath = idx.notice_index.path(uri)+'_html/legal-expressions'
            files = sorted(os.listdir(dirpath))
            self.assertEqual(files, ['EN.html', 'FR.html'])
            dirpath = idx.notice_index.path(uri)+'_html/formats'
            files = sorted(os.listdir(dirpath))
            self.assertEqual(files, ['EN_PDF.html', 'EN_PRINT.html',
                                     'FR_PDF.html', 'FR_PRINT.html'])

            # Imports RDFA data inserted in HTML
            filepath = idx.notice_index.path(uri)+'_html/formats/FR_PRINT.html'
            graph = eligraph.ELIGraph()
            with open(filepath) as fp:
                graph.parse(fp, format="rdfa", media_type="text/html")
            # Checks the RDFA graph read in the HTML file in the same as the
            # initial graph
            exp = rdflib.Graph()
            exp.parse(idx.notice_index.path(uri)+".rdf", format="xml")
            self.assertEqual(len(exp), len(graph))
            for s,p,o in graph:
                with self.subTest(subject=s, predicate=p):
                    exp_o = list(exp.objects(s,p))
                    # If lang is not specified, the rdf-a reader sets it to
                    # the lang of the HTML document
                    for val in exp_o[:]:
                        if isinstance(val, rdflib.Literal) \
                           and val.language is None and val.datatype is None:
                            exp_o[exp_o.index(val)] = rdflib.Literal(str(val),
                                                                     lang="fr")
                    self.assertIn(o, exp_o)

            # Imports Schema.Org data inserted in HTML (expression)
            filepath = idx.notice_index.path(uri)+'_html/legal-expressions/FR.html'
            root = html.parse(filepath)
            scr_elt = root.find(".//script[@type='application/ld+json']")
            self.assertIsNotNone(scr_elt)
            data = json.loads(scr_elt.text)
            # Checks the schema.org data
            data.get("encoding",[]).sort(key=itemgetter("@id"))
            data.get("identifier", []).sort()
            with open(get_datafile("act-01-sch_org-expression.json")) as inp:
                exp = json.load(inp)
                exp.get("encoding", []).sort(key=itemgetter("@id"))
                exp.get("identifier", []).sort()
            self.assertDictEqual(data, exp)

            # Imports Schema.Org data inserted in HTML (format)
            filepath = idx.notice_index.path(uri)+'_html/formats/EN_PDF.html'
            root = html.parse(filepath)
            scr_elt = root.find(".//script[@type='application/ld+json']")
            self.assertIsNotNone(scr_elt)
            data = json.loads(scr_elt.text)
            data.get("identifier", []).sort()
            # Checks the schema.org data
            with open(get_datafile("act-01-sch_org-format.json"))as inp:
                exp = json.load(inp)
                exp.get("identifier", []).sort()
            self.assertDictEqual(data, exp)

if __name__ == '__main__':
    unittest.main()
