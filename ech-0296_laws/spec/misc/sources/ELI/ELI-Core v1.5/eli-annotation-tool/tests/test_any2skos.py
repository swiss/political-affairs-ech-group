# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import unittest
import os
import tempfile

from eli_annotation import any2skos, errors, eligraph
from rdflib.namespace import DCTERMS, SKOS, RDF
import rdflib

try:
    from .helpers import silence_logging_warning
except SystemError:
    from helpers import silence_logging_warning


SKOS_PROPERTIES = any2skos.get_skos_properties()
DCMI_PROPERTIES = any2skos.get_dcmi_properties()
PROPERTIES = SKOS_PROPERTIES | DCMI_PROPERTIES


def get_datafile(fname):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),'data',fname))

def convert_workbook(datafile):
    with open(get_datafile(datafile),'rb') as workbook:
        result, warnings = any2skos.xl2skos(workbook, PROPERTIES)
    for uri, graph in result.items():
        with tempfile.TemporaryFile() as outfile:
            outfile.write(graph.serialize(format='xml').encode('utf-8'))
    return result, warnings


class ConvertTC(unittest.TestCase):

    def assertSubGraph(self, graph, expected):
        for s,p,o in graph:
            with self.subTest(subject=s, predicate=p):
                exp_o = list(expected.objects(s,p))
                self.assertIn(o, exp_o)

    def test_convert_test00_xls(self):
        result, warnings = convert_workbook('test00.xlsx')
        self.assertEqual(len(warnings), 0)
        self.assertEqual(len(result), 1)
        self.assertIn("http://data.sparna.fr/vocabularies/days", result)
        graph = result["http://data.sparna.fr/vocabularies/days"]
        expected = rdflib.Graph()
        with open(get_datafile("test00.ttl")) as fp:
            expected.parse(fp, format="turtle")
        self.assertEqual(len(graph), len(expected))
        self.assertSubGraph(graph, expected)
        self.assertSubGraph(expected, graph)

    def test_convert_test01_xls(self):
        convert_workbook('test01.xlsx')

    def test_convert_test02_xls(self):
        convert_workbook('test02.xlsx')

    def test_convert_testF0_xls(self):
        with open(get_datafile('testF0.xlsx'),'rb') as workbook:
            result, warnings = any2skos.xl2skos(workbook, PROPERTIES)
        self.assertEqual(len(warnings), 1)
        self.assertIsInstance(warnings[0], errors.ConversionWarnings)
        self.assertEqual(len(warnings[0]), 1)

    def test_convert_testF1_xls(self):
        with silence_logging_warning():
            with open(get_datafile('testF1.xlsx'),'rb') as workbook:
                result, warnings = any2skos.xl2skos(workbook, PROPERTIES)
        self.assertEqual(len(warnings), 2)
        self.assertIsInstance(warnings[0], errors.ConversionError)
        self.assertIsInstance(warnings[1], errors.ConversionWarnings)
        self.assertEqual(len(warnings[1]), 5)
        self.assertEqual(len(result), 1)
        self.assertIn("http://test.logilab.org/document", result)
        graph = result["http://test.logilab.org/document"]
        self.assertEqual(len(list(graph.subjects(RDF.type, SKOS.Concept))), 2)
        cs = rdflib.URIRef("http://test.logilab.org/document")
        c1 = rdflib.URIRef("http://test.logilab.org/document#GHI")
        c2 = rdflib.URIRef("http://test.logilab.org/document#ABC")
        self.assertEqual(list(graph.objects(c1, SKOS.notation)),
                         [rdflib.Literal("GHI")])
        self.assertEqual(set(graph.objects(c2, SKOS.inScheme)),
                         {rdflib.Literal("http://not anUri"), cs})
        props = [pred for pred, obj in graph.predicate_objects(c1)]
        self.assertEqual(len(props), 5)
        self.assertEqual(set(props), {RDF.type, SKOS.prefLabel, SKOS.notation,
                                      SKOS.inScheme})
        props = [pred for pred, obj in graph.predicate_objects(cs)]
        self.assertEqual(len(props), 5)
        self.assertEqual(set(props), {RDF.type, DCTERMS.title,
                                      DCTERMS.description})


class ExportToCSVTC(unittest.TestCase):

    def test_csv_test00(self):
        with open(get_datafile('test00.xlsx'),'rb') as workbook:
            result, warnings = any2skos.xl2skos(workbook, PROPERTIES)
        graph = result['http://data.sparna.fr/vocabularies/days']
        rows = any2skos.graph2table(graph)


class HelpingFunctions(unittest.TestCase):

    def test_parse_prop_name_basic_dct(self):
        name = "dct:title"
        pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)
        self.assertEqual(pred, DCTERMS.title)
        self.assertEqual(lang, None)
        self.assertEqual(sep, None)

    def test_parse_prop_name_basic_skos(self):
        name = "skos:notation"
        pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)
        self.assertEqual(pred, SKOS.notation)
        self.assertEqual(lang, None)
        self.assertEqual(sep, None)

    def test_parse_prop_name_basic_custom_prefix(self):
        name = "eli:date_document"
        prefixes={"eli": eligraph.ELI}
        pred, lang, sep = any2skos._parse_prop_name(name, prefixes,
                                                    PROPERTIES)
        self.assertEqual(pred, eligraph.ELI.date_document)
        self.assertEqual(lang, None)
        self.assertEqual(sep, None)

    def test_parse_prop_name_with_lang(self):
        name = "dct:title@en"
        pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)
        self.assertEqual(pred, DCTERMS.title)
        self.assertEqual(lang, "en")
        self.assertEqual(sep, None)

    def test_parse_prop_name_with_separator_double_quotes(self):
        name = 'dct:title[separator=";"]'
        pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)
        self.assertEqual(pred, DCTERMS.title)
        self.assertEqual(lang, None)
        self.assertEqual(sep, ";")

    def test_parse_prop_name_with_separator_simple_quotes(self):
        name = "dct:title[separator='::']"
        pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)
        self.assertEqual(pred, DCTERMS.title)
        self.assertEqual(lang, None)
        self.assertEqual(sep, "::")

    def test_parse_prop_name_with_separator_empty_double_quotes(self):
        name = 'dct:title[separator=""]'
        pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)
        self.assertEqual(pred, DCTERMS.title)
        self.assertEqual(lang, None)
        self.assertEqual(sep, None)

    def test_parse_prop_name_with_separator_empty_simple_quotes(self):
        name = "dct:title[separator='']"
        pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)
        self.assertEqual(pred, DCTERMS.title)
        self.assertEqual(lang, None)
        self.assertEqual(sep, None)

    def test_parse_prop_name_with_lang_and_separator(self):
        name = 'dct:title@fr[separator="||"]'
        pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)
        self.assertEqual(pred, DCTERMS.title)
        self.assertEqual(lang, "fr")
        self.assertEqual(sep, "||")

    def test_parse_prop_name_with_optional_spaces(self):
        name = ' dct:title@fr [ separator = "|" ] '
        pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)
        self.assertEqual(pred, DCTERMS.title)
        self.assertEqual(lang, "fr")
        self.assertEqual(sep, "|")

    def test_parse_prop_name_no_prefix(self):
        name = 'title@fr[separator="|"]'
        with self.assertRaises(ValueError):
            pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)

    def test_parse_prop_name_wrong_option(self):
        name = 'dct:title@fr[multiple=true]'
        with self.assertRaises(ValueError):
            pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)

    def test_parse_prop_name_wrong_option_syntax_1(self):
        name = 'dct:title@fr[separator="|")'
        with self.assertRaises(ValueError):
            pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)

    def test_parse_prop_name_wrong_option_syntax_2(self):
        name = 'dct:title@fr[separator]'
        with self.assertRaises(ValueError):
            pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)

    def test_parse_prop_name_wrong_option_syntax_3(self):
        name = 'dct:title@fr[separator=;]'
        with self.assertRaises(ValueError):
            pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)

    def test_parse_prop_name_wrong_option_syntax_4(self):
        name = 'dct:title@fr(separator=";")'
        with self.assertRaises(ValueError):
            pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)

    def test_parse_prop_name_unknown_dct_prop(self):
        name = 'dct:unknown@fr[separator=";"]'
        with self.assertRaises(ValueError):
            pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)

    def test_parse_prop_name_unknown_dct_prop(self):
        name = 'dct:unknown@fr[separator=";"]'
        with self.assertRaises(ValueError):
            pred, lang, sep = any2skos._parse_prop_name(name, {}, PROPERTIES)

    def test_parse_prop_name_unknown_prefix(self):
        prefixes={"eli": eligraph.ELI}
        name = 'unk:title@fr[separator=";"]'
        with self.assertRaises(ValueError):
            pred, lang, sep = any2skos._parse_prop_name(name, prefixes,
                                                        PROPERTIES)

    def test_build_rdf_uri_correct(self):
        str_uri = "http://example.com"
        uri = any2skos._build_rdf_uri(str_uri)
        self.assertEqual(uri, rdflib.URIRef("http://example.com"))

    def test_build_rdf_uri_wrong(self):
        str_uri = "http://example.com not'correct"
        with silence_logging_warning():
            with self.assertRaises(ValueError):
                uri = any2skos._build_rdf_uri(str_uri)

    def test_build_rdf_value_string(self):
        str_val = "This is some text"
        val = any2skos._build_rdf_value(str_val, None)
        self.assertEqual(val, rdflib.Literal("This is some text"))

    def test_build_rdf_value_string_with_lang(self):
        str_val = "This is some text"
        val = any2skos._build_rdf_value(str_val, "en")
        self.assertEqual(val, rdflib.Literal("This is some text", lang="en"))

    def test_build_rdf_value_url(self):
        str_val = "http://example.com"
        val = any2skos._build_rdf_value(str_val, None)
        self.assertEqual(val, rdflib.URIRef("http://example.com"))

    def test_build_rdf_value_urn(self):
        str_val = "urn:example.com:"
        val = any2skos._build_rdf_value(str_val, None)
        self.assertEqual(val, rdflib.URIRef("urn:example.com:"))

    def test_build_rdf_value_wrong_url(self):
        str_val = "http://example.com not'correct"
        with silence_logging_warning():
            val = any2skos._build_rdf_value(str_val, None)
        self.assertEqual(val, rdflib.Literal("http://example.com not'correct"))

if __name__ == '__main__':
    unittest.main()
