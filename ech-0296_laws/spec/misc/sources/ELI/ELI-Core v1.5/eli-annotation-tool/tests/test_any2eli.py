# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import unittest
import os
import tempfile
import json, rdflib
import datetime as dtm
from rdflib.namespace import RDF, XSD
from rdflib import URIRef, Literal

from eli_annotation import form_configs, vocabs, form_values, xslt_transform
from eli_annotation.eligraph import (ELIX_ABSTRACT_RESOURCE, ELI_RESOURCE,
                                     ELI_EXPRESSION, ELI_FORMAT, ELI, ELIX,
                                     ACT_RESOURCE, JOURNAL_RESOURCE, parse_uri,
                                     PROV)
from eli_annotation import any2eli
from eli_annotation import vocabs, form_configs, eligraph, xslt_transform


try:
    from .fake_form_values import ENGLISH, FRENCH, PRINT, PDF, VALUES_DATA
    from .helpers import silence_logging_warning
except SystemError:
    from fake_form_values import ENGLISH, FRENCH, PRINT, PDF, VALUES_DATA
    from helpers import silence_logging_warning


def get_datafile(fname):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),'data',fname))


EXPECTED_URIS = {
    ELIX_ABSTRACT_RESOURCE: {(None, None): 'http://example/2017/ABC'},
    ELI_RESOURCE: {(None, None): 'http://example/2017/ABC/ACT'},
    ELI_EXPRESSION: {(ENGLISH, None): 'http://example/2017/ABC/ACT/EN',
                     (FRENCH, None): 'http://example/2017/ABC/ACT/FR'},
    ELI_FORMAT: {(ENGLISH, PRINT): 'http://example/2017/ABC/ACT/EN/PRINT',
                 (ENGLISH,PDF): 'http://example/2017/ABC/ACT/EN/PDF',
                 (FRENCH, PRINT): 'http://example/2017/ABC/ACT/FR/PRINT',
                 (FRENCH,PDF): 'http://example/2017/ABC/ACT/FR/PDF'}
}

class Form2EliTC(unittest.TestCase):
    def setUp(self):
        self.vocab_index = vocabs.VocabularyIndex(get_datafile('vocabs'))

    def assertSubGraph(self, graph, expected):
        for s,p,o in graph:
            with self.subTest(subject=s, predicate=p):
                exp_o = list(expected.objects(s,p))
                self.assertIn(o, exp_o)

    def test_build_uri(self):
        valfile = get_datafile('act-01.json')
        with open(valfile) as fp:
            raw_vals = form_values.ELIFormValues.load_from_json(json.load(fp))
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(
                json.load(fp), raw_vals, self.vocab_index)
        vals = cfg.read_form_values(raw_vals)
        ents = vals.extract_eli_entities()
        uris = any2eli.build_uris_for_entities(ents, cfg, vals)
        self.assertEqual(uris, EXPECTED_URIS)

    def test_collect_properties(self):
        valfile = get_datafile('act-01.json')
        with open(valfile) as fp:
            raw_vals = form_values.ELIFormValues.load_from_json(json.load(fp))
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(
                json.load(fp), raw_vals, self.vocab_index)
        vals = cfg.read_form_values(raw_vals)
        ents = vals.extract_eli_entities()
        props = any2eli.collect_entities_properties(EXPECTED_URIS, vals)
        self.assertEqual(set(props.keys()),
                         {'http://example/2017/ABC/ACT',
                          'http://example/2017/ABC/ACT/EN',
                          'http://example/2017/ABC/ACT/FR',
                          'http://example/2017/ABC/ACT/EN/PRINT',
                          'http://example/2017/ABC/ACT/EN/PDF',
                          'http://example/2017/ABC/ACT/FR/PRINT',
                          'http://example/2017/ABC/ACT/FR/PDF'})
        self.assertEqual(
            set(props['http://example/2017/ABC/ACT'].keys()),
            {'elix:resource_type', 'elix:abstractLegalResourceUriScheme',
             'elix:legalResourceUriScheme', 'elix:legalExpressionUriScheme',
             'elix:formatUriScheme', 'elix:languages_list', 'elix:formats_list',
             'rdf:type', 'eli:date_document', 'eli:id_local', 'eli:is_about',
             'eli:number', 'eli:transposes', 'eli:type_document',
             'eli:is_member_of'})
        self.assertEqual(
            set(props['http://example/2017/ABC/ACT/EN'].keys()),
            {'rdf:type', 'eli:language', 'eli:title', 'eli:id_local',
             'eli:realizes',})
        self.assertEqual(
            set(props['http://example/2017/ABC/ACT/FR'].keys()),
            {'rdf:type', 'eli:language', 'eli:title', 'eli:id_local',
             'eli:realizes'})
        self.assertEqual(
            set(props['http://example/2017/ABC/ACT/EN/PDF'].keys()),
            {'rdf:type', 'eli:format', 'eli:is_exemplified_by', 'eli:id_local',
             'eli:embodies',})
        self.assertEqual(
            set(props['http://example/2017/ABC/ACT/EN/PRINT'].keys()),
            {'rdf:type', 'eli:format', 'eli:published_in', 'eli:embodies',})
        self.assertEqual(
            set(props['http://example/2017/ABC/ACT/FR/PDF'].keys()),
            {'rdf:type', 'eli:format', 'eli:is_exemplified_by', 'eli:embodies',})
        self.assertEqual(
            set(props['http://example/2017/ABC/ACT/FR/PRINT'].keys()),
            {'rdf:type', 'eli:format', 'eli:published_in', 'eli:id_local',
             'eli:embodies',})
        exp_types = {'http://example/2017/ABC/ACT': ELI.LegalResource,
                     'http://example/2017/ABC/ACT/EN': ELI.LegalExpression,
                     'http://example/2017/ABC/ACT/FR': ELI.LegalExpression,
                     'http://example/2017/ABC/ACT/EN/PRINT': ELI.Format,
                     'http://example/2017/ABC/ACT/EN/PDF': ELI.Format,
                     'http://example/2017/ABC/ACT/FR/PRINT': ELI.Format,
                     'http://example/2017/ABC/ACT/FR/PDF': ELI.Format}
        for uri, typ in exp_types.items():
            self.assertEqual(props[uri]['rdf:type'], [typ])
        exp_parents = {
            'http://example/2017/ABC/ACT': ('eli:is_member_of',
                                            'http://example/2017/ABC'),
            'http://example/2017/ABC/ACT/EN': ('eli:realizes',
                                               'http://example/2017/ABC/ACT'),
            'http://example/2017/ABC/ACT/FR': ('eli:realizes',
                                               'http://example/2017/ABC/ACT'),
            'http://example/2017/ABC/ACT/EN/PRINT':
                ('eli:embodies','http://example/2017/ABC/ACT/EN'),
            'http://example/2017/ABC/ACT/EN/PDF':
                ('eli:embodies','http://example/2017/ABC/ACT/EN'),
            'http://example/2017/ABC/ACT/FR/PRINT':
                ('eli:embodies','http://example/2017/ABC/ACT/FR'),
            'http://example/2017/ABC/ACT/FR/PDF':
                ('eli:embodies','http://example/2017/ABC/ACT/FR')
        }
        for uri, (prop, par_uri) in exp_parents.items():
            self.assertEqual(props[uri][prop], [par_uri])
        exp_ids_local = {
            'http://example/2017/ABC/ACT': 'ID1',
            'http://example/2017/ABC/ACT/EN': 'ID1-ENG',
            'http://example/2017/ABC/ACT/FR': 'ID1-FRA',
            'http://example/2017/ABC/ACT/EN/PDF': 'ID1-ENG-PDF',
            'http://example/2017/ABC/ACT/FR/PRINT': 'ID1-FRA-PRINT'}
        for uri, loc in exp_ids_local.items():
            self.assertEqual(props[uri]['eli:id_local'], [loc])

    def test_entities_to_graph(self):
        valfile = get_datafile('act-01.json')
        with open(valfile) as fp:
            raw_vals = form_values.ELIFormValues.load_from_json(json.load(fp))
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(
                json.load(fp), raw_vals, self.vocab_index)
        vals = cfg.read_form_values(raw_vals)
        ents = vals.extract_eli_entities()
        props = any2eli.collect_entities_properties(EXPECTED_URIS, vals)
        graph = any2eli.entities2eli_graph(props)
        expected = rdflib.Graph()
        grphfile = get_datafile('act-01-no-prov.ttl')
        with open(grphfile) as fp:
            expected.parse(fp, format="turtle")
        self.assertEqual(len(graph), len(expected))
        self.assertSubGraph(graph, expected)
        self.assertSubGraph(expected, graph)

    def test_add_creator_to_graph(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01-no-prov.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        now = dtm.datetime(2017,9,22,12,0,1)
        any2eli.add_creator_to_eli_graph(graph, "http://example/users/bob42",
                                         now)
        expected = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            expected.parse(fp, format="turtle")
        self.assertEqual(len(graph), len(expected))
        self.assertSubGraph(graph, expected)
        self.assertSubGraph(expected, graph)

    def test_add_no_creator_to_graph(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01-no-prov.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        now = dtm.datetime(2017,9,22,12,0,1)
        any2eli.add_creator_to_eli_graph(graph, None,
                                         now)
        expected = rdflib.Graph()
        grphfile = get_datafile('act-01-no-prov.ttl')
        with open(grphfile) as fp:
            expected.parse(fp, format="turtle")
        self.assertEqual(len(graph), len(expected))
        self.assertSubGraph(graph, expected)
        self.assertSubGraph(expected, graph)

    def test_add_creator_to_graph_with_creator(self):
        # Loads graph with PROV properties
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        now = dtm.datetime(2017,9,22,12,0,1)
        # Changes existing PROV property values
        graph.remove( (URIRef("http://example/2017/ABC/ACT/prov/createEntity"),
                       PROV.generatedAtTime, None) )
        graph.add( (URIRef("http://example/2017/ABC/ACT/prov/createEntity"),
                    PROV.generatedAtTime,
                    Literal("2017-08-15T16:08:42Z", datatype=XSD.datetime)) )
        graph.remove( (URIRef("http://example/2017/ABC/ACT/prov/createEntity"),
                       PROV.wasAttributedTo, None) )
        graph.add( (URIRef("http://example/2017/ABC/ACT/prov/createEntity"),
                    PROV.wasAttributedTo,
                    URIRef("http://example/users/sam28")) )
        graph.remove( (URIRef("http://example/2017/ABC/ACT/prov/createEntity/activity"),
                       PROV.wasAssociatedWith, None) )
        graph.add( (URIRef("http://example/2017/ABC/ACT/prov/createEntity/activity"),
                    PROV.wasAssociatedWith,
                    URIRef("http://example/users/sam28")) )
        graph.remove( (URIRef("http://example/2017/ABC/ACT/prov/createEntity/association"),
                       PROV.agent, None) )
        graph.add( (URIRef("http://example/2017/ABC/ACT/prov/createEntity/association"),
                    PROV.agent, URIRef("http://example/users/sam28")) )
        graph.remove( (URIRef("http://example/users/bob42"), None, None) )
        graph.add( (URIRef("http://example/users/sam28"),
                    RDF.type, PROV.Agent) )
        self.assertEqual(len(graph), 81)
        # Calls function to be tested
        any2eli.add_creator_to_eli_graph(graph, "http://example/users/bob42",
                                         now)
        # Checks result
        expected = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            expected.parse(fp, format="turtle")
        self.assertEqual(len(graph), len(expected))
        self.assertSubGraph(graph, expected)
        self.assertSubGraph(expected, graph)

    def test_form_to_eli(self):
        basedir = get_datafile('forms')
        fconfig_index = form_configs.FormConfigIndex(basedir)
        valfile = get_datafile('act-01.json')
        with open(valfile) as fp:
            form_data = json.load(fp)
        now = dtm.datetime(2017,9,22,12,0,1)
        root_uri, graph = any2eli.form2eli(form_data, fconfig_index,
                                           self.vocab_index,
                                           "http://example/users/bob42", now)
        self.assertEqual(str(root_uri), 'http://example/2017/ABC/ACT')
        expected = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            expected.parse(fp, format="turtle")
        self.assertEqual(len(graph), len(expected))
        self.assertSubGraph(graph, expected)
        self.assertSubGraph(expected, graph)


class Eli2FormTC(unittest.TestCase):
    def setUp(self):
        self.vocab_index = vocabs.VocabularyIndex(get_datafile('vocabs'))
        self.config_index = form_configs.FormConfigIndex(get_datafile('forms'))

    def test_get_rdf_property_values(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        # Adds another property for testing reverse property gathering
        graph.add( (rdflib.URIRef("http://example/2017/ABC/ACT"),
                    ELI.is_realized_by,
                    rdflib.URIRef("http://another/resource")) )
        with self.subTest(type="eli:LegalResource", context="", name="eli:date_document"):
            vals = any2eli.get_rdf_property_values(
                graph, "http://example/2017/ABC/ACT", "eli:date_document")
            self.assertEqual(vals, ["2017-09-04"])
        with self.subTest(type="eli:LegalResource", context="", name="eli:id_local"):
            vals = any2eli.get_rdf_property_values(
                graph, "http://example/2017/ABC/ACT", "eli:id_local")
            self.assertEqual(vals, ["ID1"])
        with self.subTest(type="eli:LegalResource", context="", name="eli:is_about"):
            vals = any2eli.get_rdf_property_values(
                graph, "http://example/2017/ABC/ACT", "eli:is_about")
            self.assertEqual(set(vals),
                        {"http://data.sparna.fr/vocabularies/days#friday",
                         "http://data.sparna.fr/vocabularies/days#saturday"})
        with self.subTest(type="eli:LegalResource", context="", name="eli:is_realized_by"):
            vals = any2eli.get_rdf_property_values(
                graph, "http://example/2017/ABC/ACT", "eli:is_realized_by")
            self.assertEqual(set(vals),
                        {"http://example/2017/ABC/ACT/EN",
                         "http://example/2017/ABC/ACT/FR",
                         "http://another/resource"})
        with self.subTest(type="eli:LegalExpression", context="EN", name="eli:id_local"):
            vals = any2eli.get_rdf_property_values(
                graph, "http://example/2017/ABC/ACT/EN", "eli:id_local")
            self.assertEqual(vals, ["ID1-ENG"])
        with self.subTest(type="eli:Format", context="EN/PDF", name="eli:id_local"):
            vals = any2eli.get_rdf_property_values(
                graph, "http://example/2017/ABC/ACT/EN/PDF", "eli:id_local")
            self.assertEqual(vals, ["ID1-ENG-PDF"])
        with self.subTest(type="eli:Format", context="EN/PRINT", name="eli:id_local"):
            vals = any2eli.get_rdf_property_values(
                graph, "http://example/2017/ABC/ACT/EN/PRINT", "eli:id_local")
            self.assertEqual(vals, [])

    def test_ensure_single_legal_resource(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        # Adds abstract resource to graph
        graph.add( (rdflib.URIRef("http://example/2017/ABC"),
                    RDF.type,
                    ELI.LegalResource) )
        graph.add( (rdflib.URIRef("http://example/2017/ABC"),
                    ELI.id_local,
                    rdflib.Literal("AnotherID", datatype=XSD.string)) )
        uri = any2eli.ensure_single_legal_resource(graph)
        self.assertEqual(uri, "http://example/2017/ABC/ACT")

    def test_ensure_single_legal_resource_but_multiple(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        # Adds another resource to graph
        graph.add( (rdflib.URIRef("http://example/2017/CDE/ACT"),
                    RDF.type,
                    ELI.LegalResource) )
        graph.add( (rdflib.URIRef("http://example/2017/CDE/ACT"),
                    ELI.id_local,
                    rdflib.Literal("AnotherID", datatype=XSD.string)) )
        with self.assertRaises(Exception):
            uri = any2eli.ensure_single_legal_resource(graph)

    def test_ensure_single_legal_resource_but_none(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        # Removes resource from the graph
        graph.remove( (rdflib.URIRef("http://example/2017/ABC/ACT"),
                       None, None) )
        with self.assertRaises(Exception):
            uri = any2eli.ensure_single_legal_resource(graph)

    def test_define_resource_type(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        # Defines legal resource type
        any2eli.define_resource_type(graph, JOURNAL_RESOURCE)
        res_type = list(graph.objects(
            rdflib.URIRef("http://example/2017/ABC/ACT"), ELIX.resource_type))
        self.assertEqual(len(res_type), 1)
        self.assertEqual(str(res_type[0]), str(parse_uri(JOURNAL_RESOURCE)))

    def test_collect_graph_properties_on_resource(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        # Adds values to enabled property
        graph.add( (rdflib.URIRef("http://example/2017/ABC/ACT"),
                    ELI.transposes,
                    rdflib.URIRef("http://example/something/else")) )
        # Adds values to not enabled property
        graph.add( (rdflib.URIRef("http://example/2017/ABC/ACT"),
                    ELI.corrects,
                    rdflib.URIRef("http://example/something/else")) )
        # Adds values outside specified vocabulary
        graph.add( (rdflib.URIRef("http://example/2017/ABC/ACT"),
                    ELI.is_about,
                    rdflib.URIRef("http://data.sparna.fr/vocabularies/days#birthday")) )
        cfg = self.config_index.load(ACT_RESOURCE, self.vocab_index)
        with silence_logging_warning():
            vals = any2eli.collect_graph_properties(
                graph, "http://example/2017/ABC/ACT", cfg)
        self.assertEqual(set(vals._values.keys()),
                         {('elix:abstractLegalResourceUriScheme',),
                          ('elix:legalResourceUriScheme',),
                          ('elix:legalExpressionUriScheme',),
                          ('elix:formatUriScheme',), ('elix:formats_list',),
                          ('elix:languages_list',), ('eli:date_document',),
                          ('eli:id_local',), ('eli:is_about',), ('eli:number',),
                          ('eli:transposes',), ('eli:type_document',)})
        name = ('elix:legalResourceUriScheme',)
        with self.subTest(name=name):
            self.assertEqual(vals[name], [])
        name = ('elix:languages_list',)
        with self.subTest(name=name):
            self.assertEqual(vals[name], [])
        name = ('elix:formats_list',)
        with self.subTest(name=name):
            self.assertEqual(vals[name], [])
        name = ('eli:date_document',)
        with self.subTest(name=name):
            self.assertEqual(vals[name], [dtm.date(2017,9,4)])
        name = ('eli:is_about',)
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 2)
            self.assertIsInstance(vals[name][0], vocabs.VocabValue)
            self.assertIsInstance(vals[name][1], vocabs.VocabValue)
            self.assertEqual({val.uri for val in vals[name]},
                              {"http://data.sparna.fr/vocabularies/days#friday",
                               "http://data.sparna.fr/vocabularies/days#saturday"})
        name = ('eli:transposes',)
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['http://example/something/else'])
        name = ('eli:corrects',)
        with self.subTest(name=name):
            self.assertTrue(name not in vals)

    def test_collect_graph_properties_on_expression(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        # Adds several values to single-valued property
        graph.add( (rdflib.URIRef("http://example/2017/ABC/ACT/EN"),
                    ELI.title,
                    rdflib.Literal("Another title", datatype=XSD.string)) )
        cfg = self.config_index.load(ACT_RESOURCE, self.vocab_index)
        with silence_logging_warning():
            vals = any2eli.collect_graph_properties(
                graph, "http://example/2017/ABC/ACT/EN", cfg, lang=ENGLISH)
        self.assertEqual(set(vals._values.keys()),
                         {(ENGLISH, 'eli:language',),
                          (ENGLISH, 'eli:id_local',),
                          (ENGLISH, 'eli:title',)})
        name = (ENGLISH, 'eli:language')
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 1)
            self.assertIsInstance(vals[name][0], vocabs.VocabValue)
            self.assertEqual(vals[name][0].uri, ENGLISH)
        name = (ENGLISH, 'eli:title')
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 1)
        name = (ENGLISH, 'eli:id_local')
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['ID1-ENG'])

    def test_collect_graph_properties_on_format(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        cfg = self.config_index.load(ACT_RESOURCE, self.vocab_index)
        vals = any2eli.collect_graph_properties(
            graph, "http://example/2017/ABC/ACT/EN/PDF", cfg,
            lang=ENGLISH, frmt=PDF)
        self.assertEqual(set(vals._values.keys()),
                         {(ENGLISH, PDF, 'eli:format',),
                          (ENGLISH, PDF, 'eli:id_local',),
                          (ENGLISH, PDF, 'eli:is_exemplified_by',)})
        name = (ENGLISH, PDF, 'eli:format')
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 1)
            self.assertIsInstance(vals[name][0], vocabs.VocabValue)
            self.assertEqual(vals[name][0].uri, PDF)
        name = (ENGLISH, PDF, 'eli:id_local')
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['ID1-ENG-PDF'])

    def test_collect_graph_properties_into_default_values(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        cfg = self.config_index.load(ACT_RESOURCE, self.vocab_index)
        raw_vals = self.config_index.load_default_values(ACT_RESOURCE, False)
        vals = cfg.read_form_values(raw_vals, check_mandatory=False)
        vals[('eli:corrects',)] = ["http://anything"]
        ret_vals = any2eli.collect_graph_properties(
            graph, "http://example/2017/ABC/ACT", cfg, vals)
        self.assertEqual(ret_vals, vals)
        ret_vals = any2eli.collect_graph_properties(
            graph, "http://example/2017/ABC/ACT/EN", cfg, vals, lang=ENGLISH)
        self.assertEqual(ret_vals, vals)
        ret_vals = any2eli.collect_graph_properties(
            graph, "http://example/2017/ABC/ACT/EN/PDF", cfg, vals,
            lang=ENGLISH, frmt=PDF)
        self.assertEqual(ret_vals, vals)
        ret_vals = any2eli.collect_graph_properties(
            graph, "http://example/2017/ABC/ACT/EN/PRINT", cfg, vals,
            lang=ENGLISH, frmt=PRINT)
        self.assertEqual(ret_vals, vals)
        ret_vals = any2eli.collect_graph_properties(
            graph, "http://example/2017/ABC/ACT/FR/PRINT", cfg, vals,
            lang=FRENCH, frmt=PRINT)
        self.assertEqual(ret_vals, vals)
        exp_keys = set(VALUES_DATA.keys())
        exp_keys.difference_update({('eli:consolidates',)})
        self.assertEqual(set(vals._values.keys()), exp_keys)
        name = ('elix:resource_type',)
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['elix:Act'])
        name = ('elix:legalResourceUriScheme',)
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['http://example/{eli:date_document|year}/{eli:type_document}/ACT'])
        name = ('elix:languages_list',)
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 2)
            self.assertIsInstance(vals[name][0], vocabs.VocabValue)
            self.assertIsInstance(vals[name][1], vocabs.VocabValue)
            self.assertEqual({val.uri for val in vals[name]},
                              {ENGLISH, FRENCH})
        name = ('elix:formats_list',)
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 2)
            self.assertIsInstance(vals[name][0], vocabs.VocabValue)
            self.assertIsInstance(vals[name][1], vocabs.VocabValue)
            self.assertEqual({val.uri for val in vals[name]},
                              {PRINT, PDF})
        name = ('eli:corrects',)
        with self.subTest(name=name):
            self.assertTrue(name not in vals)
        name = ('eli:id_local',)
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['ID1'])
        name = (ENGLISH, 'eli:id_local')
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['ID1-ENG'])
        name = (ENGLISH, PDF, 'eli:id_local')
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['ID1-ENG-PDF'])
        name = ('eli:type_document',)
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 1)
            self.assertIsInstance(vals[name][0], vocabs.VocabValue)
            self.assertEqual(vals[name][0].uri, "http://test.logilab.org/document#ABC")
        name = ('eli:is_about',)
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 2)
            self.assertIsInstance(vals[name][0], vocabs.VocabValue)
            self.assertIsInstance(vals[name][1], vocabs.VocabValue)
            self.assertEqual({val.uri for val in vals[name]},
                              {"http://data.sparna.fr/vocabularies/days#friday",
                               "http://data.sparna.fr/vocabularies/days#saturday"})
        name = (ENGLISH, PRINT, 'eli:published_in')
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['The English journal'])
        name = (FRENCH, PRINT, 'eli:published_in')
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 2)
            self.assertEqual(set(vals[name]),
                              {"N'importe quel journal", "Le journal français"})

    def test_eli2form(self):
        graph = rdflib.Graph()
        grphfile = get_datafile('act-01.ttl')
        with open(grphfile) as fp:
            graph.parse(fp, format="turtle")
        uri, vals = any2eli.eli2form(graph, ACT_RESOURCE, self.config_index,
                                     self.vocab_index)
        self.assertEqual(uri, "http://example/2017/ABC/ACT")
        exp_keys = set(VALUES_DATA.keys())
        exp_keys.difference_update({('eli:consolidates',)} )
        self.assertEqual(set(vals._values.keys()), exp_keys)
        name = ('eli:corrects',)
        with self.subTest(name=name):
            self.assertTrue(name not in vals)
        name = ('eli:id_local',)
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['ID1'])
        name = (ENGLISH, 'eli:id_local')
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['ID1-ENG'])
        name = (ENGLISH, PDF, 'eli:id_local')
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['ID1-ENG-PDF'])
        name = ('eli:type_document',)
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 1)
            self.assertIsInstance(vals[name][0], vocabs.VocabValue)
            self.assertEqual(vals[name][0].uri, "http://test.logilab.org/document#ABC")
        name = ('eli:is_about',)
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 2)
            self.assertIsInstance(vals[name][0], vocabs.VocabValue)
            self.assertIsInstance(vals[name][1], vocabs.VocabValue)
            self.assertEqual({val.uri for val in vals[name]},
                              {"http://data.sparna.fr/vocabularies/days#friday",
                               "http://data.sparna.fr/vocabularies/days#saturday"})
        name = (ENGLISH, PRINT, 'eli:published_in')
        with self.subTest(name=name):
            self.assertEqual(vals[name], ['The English journal'])
        name = (FRENCH, PRINT, 'eli:published_in')
        with self.subTest(name=name):
            self.assertEqual(len(vals[name]), 2)
            self.assertEqual(set(vals[name]),
                              {"N'importe quel journal", "Le journal français"})

    def test_eli2form_with_rdfa(self):
        filepath = get_datafile('legilux_eli_etat_leg_rgd_2017_05_22_a563_jo.html')
        graph = eligraph.ELIGraph()
        with open(filepath) as fp:
            graph.parse(fp, format='rdfa', media_type="text/html")
        self.assertEqual(len(graph), 71)
        with silence_logging_warning():
            uri, vals = any2eli.eli2form(graph, ACT_RESOURCE, self.config_index,
                                         self.vocab_index)
        self.assertEqual(uri, "http://data.legilux.public.lu/eli/etat/leg/rgd/2017/05/22/a563/jo")
        self.assertEqual(vals[(FRENCH, "eli:title")],
                         ["Règlement grand-ducal du 22 mai 2017 modifiant le "
                          "règlement grand-ducal du 25 juillet 2015 portant "
                          "exécution de l’article 4, paragraphe 1er, de la loi "
                          "du 25 juillet 2015 relative à l’archivage "
                          "électronique."])
        self.assertEqual(vals[("eli:date_document",)], [dtm.date(2017, 5, 22)])


class Eli2HtmlTC(unittest.TestCase):

    def test_eli2html(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Builds XML glossary
            xslt_transform.build_xml_glossary(tmpdir)
            data = get_datafile('act-01.rdf')
            any2eli.eli2html(data, os.path.join(tmpdir, 'html'), tmpdir)
            sorted_dir = lambda x: sorted(os.listdir(os.path.join(tmpdir,x)))
            self.assertEqual(sorted_dir(''), ['glossary.xml', 'html'])
            self.assertEqual(sorted_dir('html'),
                             ['formats','index.html','legal-expressions'])
            self.assertEqual(sorted_dir('html/formats'),
                             ['EN_PDF.html','EN_PRINT.html','FR_PDF.html',
                              'FR_PRINT.html'])
            self.assertEqual(sorted_dir('html/legal-expressions'),
                             ['EN.html','FR.html'])

    def test_build_filenames_from_near_uris(self):
        uris = ['http://logilab.fr/eli/1234/expr/FR',
                'http://logilab.fr/eli/1234/expr/EN']
        expected = {uris[0]: 'FR.html', uris[1]: 'EN.html'}
        fnames = any2eli.build_filenames_from_uris(uris)
        self.assertEqual(fnames, expected)

    def test_build_filenames_from_more_distinct_uris(self):
        uris = ['http://logilab.fr/eli/1234/expr/FR',
                'http://logilab.fr/eli/1234/expr/EN',
                'http://logilab.fr/eli/1238/expr/EN']
        expected = {uris[0]: '1234_expr_FR.html',
                    uris[1]: '1234_expr_EN.html',
                    uris[2]: '1238_expr_EN.html'}
        fnames = any2eli.build_filenames_from_uris(uris)
        self.assertEqual(fnames, expected)


if __name__ == '__main__':
    unittest.main()
