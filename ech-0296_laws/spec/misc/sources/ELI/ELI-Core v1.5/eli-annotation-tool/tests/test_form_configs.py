# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import unittest
import os, json, copy
import datetime as dtm

from eli_annotation import form_configs, vocabs, form_values

try:
    from .fake_form_values import VALUES_DATA, ENGLISH, FRENCH, PRINT, PDF
    from .helpers import silence_logging_warning
except SystemError:
    from fake_form_values import VALUES_DATA, ENGLISH, FRENCH, PRINT, PDF
    from helpers import silence_logging_warning


def get_datafile(fname):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),'data',fname))


RAW_VALUES = form_values.ELIFormValues()
RAW_VALUES._values.update(VALUES_DATA)
EXPECTED_CONFIG = {
    ('elix:abstractLegalResourceUriScheme',): {'class': 'ELIFormTextProp',
                                               'enabled': True,
                                               'mandatory': True,
                                               'multiple': False},
    ('elix:legalResourceUriScheme',): {'class': 'ELIFormTextProp',
                                       'enabled': True,
                                       'mandatory': True,
                                       'multiple': False},
    ('elix:legalExpressionUriScheme',): {'class': 'ELIFormTextProp',
                                         'enabled': True,
                                         'mandatory': True,
                                         'multiple': False},
    ('elix:formatUriScheme',): {'class': 'ELIFormTextProp',
                                'enabled': True,
                                'mandatory': True,
                                'multiple': False},
    ('elix:languages_list',): {'class': 'ELIFormVocabProp',
                               'enabled': True,
                               'mandatory': True,
                               'multiple': True,
                               'vocab': {"http://publications.europa.eu/resource/authority/language"}},
    ('elix:formats_list',): {'class': 'ELIFormVocabProp',
                             'enabled': True,
                             'mandatory': True,
                             'multiple': True,
                             'vocab': {"https://www.iana.org/assignments/media-types"}},
    ('eli:consolidates',): {'class': 'ELIFormURIProp',
                            'enabled': False,
                            'mandatory': False,
                            'multiple': False},
    ('eli:corrects',): {'class': 'ELIFormURIProp',
                        'enabled': False,
                        'mandatory': False,
                        'multiple': False},
    ('eli:date_document',): {'class': 'ELIFormDateProp',
                             'enabled': True,
                             'mandatory': True,
                             'multiple': False},
    ('eli:id_local',): {'class': 'ELIFormTextProp',
                        'enabled': True,
                        'mandatory': False,
                        'multiple': True},
    ('eli:is_about',): {'class': 'ELIFormVocabProp',
                        'enabled': True,
                        'mandatory': False,
                        'multiple': True,
                        'vocab': {"http://data.sparna.fr/vocabularies/days"}},
    ('eli:number',): {'class': 'ELIFormTextProp',
                      'enabled': True,
                      'mandatory': False,
                      'multiple': False},
    ('eli:transposes',): {'class': 'ELIFormURIProp',
                          'enabled': True,
                          'mandatory': False,
                          'multiple': True},
    ('eli:type_document',): {'class': 'ELIFormVocabProp',
                             'enabled': True,
                             'mandatory': True,
                             'multiple': False,
                             'vocab': {"http://test.logilab.org/document"}},
    (ENGLISH, 'eli:language'): {'class': 'ELIFormVocabProp',
                                'enabled': True,
                                'mandatory': False,
                                'multiple': False,
                                'vocab': {"http://publications.europa.eu/resource/authority/language"}},
    (ENGLISH, 'eli:id_local'): {'class': 'ELIFormTextProp',
                                'enabled': True,
                                'mandatory': False,
                                'multiple': True},
    (ENGLISH, 'eli:title'): {'class': 'ELIFormTextProp',
                             'enabled': True,
                             'mandatory': False,
                             'multiple': False},
    (ENGLISH, PRINT, 'eli:format'): {'class': 'ELIFormVocabProp',
                                     'enabled': True,
                                     'mandatory': False,
                                     'multiple': False,
                                     'vocab': {"https://www.iana.org/assignments/media-types"}},
    (ENGLISH, PRINT, 'eli:published_in'): {'class': 'ELIFormTextProp',
                                           'enabled': True,
                                           'mandatory': False,
                                           'multiple': True},
    (ENGLISH, PDF, 'eli:format'): {'class': 'ELIFormVocabProp',
                                   'enabled': True,
                                   'mandatory': False,
                                   'multiple': False,
                                   'vocab': {"https://www.iana.org/assignments/media-types"}},
    (ENGLISH, PDF, 'eli:id_local'): {'class': 'ELIFormTextProp',
                                     'enabled': True,
                                     'mandatory': False,
                                     'multiple': True},
    (ENGLISH, PDF, 'eli:is_exemplified_by'): {'class': 'ELIFormURIProp',
                                              'enabled': True,
                                              'mandatory': False,
                                              'multiple': True},
    (FRENCH, 'eli:language'): {'class': 'ELIFormVocabProp',
                               'enabled': True,
                               'mandatory': False,
                               'multiple': False,
                               'vocab': {"http://publications.europa.eu/resource/authority/language"}},
    (FRENCH, 'eli:id_local'): {'class': 'ELIFormTextProp',
                               'enabled': True,
                               'mandatory': False,
                               'multiple': True},
    (FRENCH, 'eli:title'): {'class': 'ELIFormTextProp',
                            'enabled': True,
                            'mandatory': False,
                            'multiple': False},
    (FRENCH, PRINT, 'eli:format'): {'class': 'ELIFormVocabProp',
                                    'enabled': True,
                                    'mandatory': False,
                                    'multiple': False,
                                    'vocab': {"https://www.iana.org/assignments/media-types"}},
    (FRENCH, PRINT, 'eli:id_local'): {'class': 'ELIFormTextProp',
                                      'enabled': True,
                                      'mandatory': False,
                                      'multiple': False},
    (FRENCH, PRINT, 'eli:published_in'): {'class': 'ELIFormTextProp',
                                          'enabled': True,
                                          'mandatory': False,
                                          'multiple': True},
    (FRENCH, PDF, 'eli:format'): {'class': 'ELIFormVocabProp',
                                  'enabled': True,
                                  'mandatory': False,
                                  'multiple': False,
                                    'vocab': {"https://www.iana.org/assignments/media-types"}},
    (FRENCH, PDF, 'eli:is_exemplified_by'): {'class': 'ELIFormURIProp',
                                             'enabled': True,
                                             'mandatory': False,
                                             'multiple': True},
}


class FormConfigTC(unittest.TestCase):
    def setUp(self):
        self.vocab_index = vocabs.VocabularyIndex(get_datafile('vocabs'))

    def test_ELIFormConfig_load_from_json(self):
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(json.load(fp), RAW_VALUES, self.vocab_index)
        self.assertEqual(len(cfg._properties), len(EXPECTED_CONFIG))
        for name, prop in cfg._properties.items():
            with self.subTest(name=name):
                exp = EXPECTED_CONFIG.get(name)
                self.assertIsNotNone(exp)
                self.assertEqual(prop.__class__.__name__, exp["class"])
                self.assertEqual(prop.enabled, exp["enabled"])
                self.assertEqual(prop.mandatory, exp["mandatory"])
                self.assertEqual(prop.multiple, exp["multiple"])
                if exp["class"] == 'ELIFormVocabProp':
                    self.assertSetEqual({voc.uri for voc in prop.vocabularies},
                                        exp["vocab"])

    def test_ELIFormConfig_read_values(self):
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(json.load(fp), RAW_VALUES, self.vocab_index)
        values = cfg.read_form_values(RAW_VALUES)
        exp_keys = set(RAW_VALUES._values.keys()).difference(
            {('eli:consolidates',)})
        self.assertEqual(set(values._values.keys()), exp_keys)
        with self.subTest(name=('eli:id_local',)):
            vals = values[('eli:id_local',)]
            self.assertEqual(len(vals), 1)
            self.assertEqual(vals[0], "ID1")
        with self.subTest(name=('eli:date_document',)):
            vals = values[('eli:date_document',)]
            self.assertEqual(len(vals), 1)
            self.assertIsInstance(vals[0], dtm.date)
            self.assertEqual(vals[0], dtm.date(2017,9,4))
        with self.subTest(name=(ENGLISH, PDF, 'eli:is_exemplified_by')):
            vals = values[(ENGLISH, PDF, 'eli:is_exemplified_by')]
            self.assertEqual(len(vals), 1)
            self.assertIsInstance(vals[0], form_configs.URIValue)
            self.assertEqual(vals[0], "http://document/english/pdf")
        with self.subTest(name=('eli:type_document',)):
            vals = values[('eli:type_document',)]
            self.assertEqual(len(vals), 1)
            self.assertIsInstance(vals[0], vocabs.VocabValue)
            self.assertEqual(vals[0].uri, "http://test.logilab.org/document#ABC")

    def test_ELIFormConfig_read_too_much_values(self):
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(json.load(fp), RAW_VALUES, self.vocab_index)
        raw = copy.deepcopy(RAW_VALUES)
        raw[('eli:date_document',)].append("2017-01-01")
        with silence_logging_warning():
            values = cfg.read_form_values(raw)
        vals = values[('eli:date_document',)]
        self.assertEqual(len(vals), 1)
        self.assertIsInstance(vals[0], dtm.date)
        self.assertEqual(vals[0], dtm.date(2017,9,4))

    def test_ELIFormConfig_read_not_enough_values(self):
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(json.load(fp), RAW_VALUES, self.vocab_index)
        raw = copy.deepcopy(RAW_VALUES)
        raw[('eli:date_document',)].pop()
        with self.assertRaises(Exception):
            values = cfg.read_form_values(raw)

    def test_ELIFormConfig_read_values_then_json_export(self):
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(json.load(fp), RAW_VALUES, self.vocab_index)
        values = cfg.read_form_values(RAW_VALUES)
        with silence_logging_warning():
            data = values.json_export()
        jsonfile = get_datafile('act-01-exported.json')
        with open(jsonfile) as inp:
            expected = json.load(inp)
        expected.pop("eli:consolidates")
        self.assertEqual(data, expected)

    def test_ELIFormConfig_get_config_level0(self):
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(json.load(fp), RAW_VALUES, self.vocab_index)
        confs = cfg.get_context_configs()
        self.assertEqual(set(confs.keys()),
                         {name[0] for name in EXPECTED_CONFIG if len(name) == 1})
        self.assertTrue(all([isinstance(val, form_configs.ELIFormProp) for val in confs.values()]))

    def test_ELIFormConfig_get_config_level1(self):
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(json.load(fp), RAW_VALUES, self.vocab_index)
        confs = cfg.get_context_configs(lang=ENGLISH)
        self.assertEqual(set(confs.keys()),
                         {name[1] for name in EXPECTED_CONFIG if len(name) == 2 and name[0] == ENGLISH})
        self.assertTrue(all([isinstance(val, form_configs.ELIFormProp) for val in confs.values()]))

    def test_ELIFormConfig_get_config_level2(self):
        cfgfile = get_datafile(os.path.join('forms','act.json'))
        with open(cfgfile) as fp:
            cfg = form_configs.ELIFormConfig.load_from_json(json.load(fp), RAW_VALUES, self.vocab_index)
        confs = cfg.get_context_configs(lang=ENGLISH, frmt=PDF)
        self.assertEqual(set(confs.keys()),
                         {name[2] for name in EXPECTED_CONFIG if len(name) == 3 and name[0:2] == (ENGLISH, PDF)})
        self.assertTrue(all([isinstance(val, form_configs.ELIFormProp) for val in confs.values()]))


class FormPropTC(unittest.TestCase):

    def test_ELIFormProp_read_text(self):
        prp = form_configs.ELIFormTextProp(('eli:id_local',),
                                           enabled=True, mandatory=False)
        prp.multiple = True
        val = prp.read_value("ID1")
        self.assertEqual(val, "ID1")

    def test_ELIFormProp_read_date(self):
        prp = form_configs.ELIFormDateProp(('eli:date_document',),
                                           enabled=True, mandatory=True)
        prp.multiple = False
        val = prp.read_value("2017-09-04")
        self.assertIsInstance(val, dtm.date)
        self.assertEqual(val, dtm.date(2017,9,4))

    def test_ELIFormProp_read_uri(self):
        prp = form_configs.ELIFormURIProp(
            (ENGLISH, PDF, 'eli:is_exemplified_by'),
            enabled=True, mandatory=False)
        prp.multiple = True
        val = prp.read_value("http://document/english/pdf")
        self.assertIsInstance(val, form_configs.URIValue)
        self.assertEqual(val, "http://document/english/pdf")

    def test_ELIFormProp_read_uri_text(self):
        prp = form_configs.ELIFormURIProp(
            (ENGLISH, PDF, 'eli:is_exemplified_by'),
            enabled=True, mandatory=False)
        prp.multiple = True
        val = prp.read_value("non/conform/uri")
        self.assertIsInstance(val, str)
        self.assertEqual(val, "non/conform/uri")

    def test_ELIFormProp_read_vocab(self):
        vocab_index = vocabs.VocabularyIndex(get_datafile('vocabs'))
        prp = form_configs.ELIFormVocabProp(('eli:type_document',),
                                            enabled=True, mandatory=True)
        prp.multiple = False
        prp.vocabularies.append(vocab_index.load("http://test.logilab.org/document"))
        val = prp.read_value("http://test.logilab.org/document#ABC")
        self.assertIsInstance(val, vocabs.VocabValue)
        self.assertEqual(val.uri, "http://test.logilab.org/document#ABC")


READ_VALUES = form_values.ELIFormValues()
READ_VALUES._values.update(VALUES_DATA)
READ_VALUES._values[('eli:date_document',)] = [dtm.date(2017,9,4)]
READ_VALUES._values[('eli:type_document',)] = [vocabs.VocabValue("http://document/ABC", None, "ABC")]
READ_VALUES._values[(ENGLISH, 'eli:language')] = [vocabs.VocabValue(ENGLISH, None, "EN")]
READ_VALUES._values[(ENGLISH, PRINT, 'eli:format')] = [vocabs.VocabValue(PRINT, None, "PRINT")]
READ_VALUES._values[(ENGLISH, PRINT, 'eli:format')] = [vocabs.VocabValue(PDF, None, "PDF")]
READ_VALUES._values[(FRENCH, 'eli:language')] = [vocabs.VocabValue(FRENCH, None, "FR")]
READ_VALUES._values[(FRENCH, PRINT, 'eli:format')] = [vocabs.VocabValue(PRINT, None, "PRINT")]
READ_VALUES._values[(FRENCH, PDF, 'eli:format')] = [vocabs.VocabValue(PDF, None, "PDF")]


class URISchemeTC(unittest.TestCase):

    def test_URIScheme_abstract_resource(self):
        usch = form_configs.URIScheme("elix:AbstractLegalResource",
                                      "http://test/{eli:type_document}/{eli:number}/{eli:date_document|year}")
        self.assertEqual(usch.entity_name, "elix:AbstractLegalResource")
        self.assertEqual(usch.scheme, "http://test/{0[eli:type_document]}/{0[eli:number]}/{0[eli:date_document|year]}")
        self.assertEqual(usch._used_fields, {'day': set(),
                                             'month': set(),
                                             'whole': {"eli:type_document", "eli:number"},
                                             'year': {"eli:date_document"}})

    def test_URIScheme_resource(self):
        usch = form_configs.URIScheme("eli:LegalResource",
                                      "http://test/{eli:type_document}/{eli:number}/{eli:date_document|year}/act")
        self.assertEqual(usch.entity_name, "eli:LegalResource")
        self.assertEqual(usch.scheme, "http://test/{0[eli:type_document]}/{0[eli:number]}/{0[eli:date_document|year]}/act")
        self.assertEqual(usch._used_fields, {'day': set(),
                                             'month': set(),
                                             'whole': {"eli:type_document", "eli:number"},
                                             'year': {"eli:date_document"}})
    def test_URIScheme_expression(self):
        usch = form_configs.URIScheme("eli:LegalExpression",
                                      "http://test/{eli:type_document}/{eli:number}/{eli:date_document|year}/act/{eli:language}")
        self.assertEqual(usch.entity_name, "eli:LegalExpression")
        self.assertEqual(usch.scheme, "http://test/{0[eli:type_document]}/{0[eli:number]}/{0[eli:date_document|year]}/act/{0[eli:language]}")
        self.assertEqual(usch._used_fields, {'day': set(),
                                             'month': set(),
                                             'whole': {"eli:type_document", "eli:number", "eli:language"},
                                             'year': {"eli:date_document"}})
    def test_URIScheme_format(self):
        usch = form_configs.URIScheme("eli:Format",
                                      "http://test/{eli:type_document}/{eli:number}/{eli:date_document|year}/act/{eli:language}/{eli:format}")
        self.assertEqual(usch.entity_name, "eli:Format")
        self.assertEqual(usch.scheme, "http://test/{0[eli:type_document]}/{0[eli:number]}/{0[eli:date_document|year]}/act/{0[eli:language]}/{0[eli:format]}")
        self.assertEqual(usch._used_fields, {'day': set(),
                                             'month': set(),
                                             'whole': {"eli:type_document", "eli:number", "eli:language", "eli:format"},
                                             'year': {"eli:date_document"}})

    def test_URIScheme_with_dates(self):
        usch = form_configs.URIScheme("eli:LegalResource",
                                      "http://test/{eli:type_document}/{eli:date_document|year}{eli:date_document|month}{eli:date_document|day}/act/{eli:date_document}/{eli:number}")
        self.assertEqual(usch.scheme, "http://test/{0[eli:type_document]}/{0[eli:date_document|year]}{0[eli:date_document|month]}{0[eli:date_document|day]}/act/{0[eli:date_document]}/{0[eli:number]}")
        self.assertEqual(usch._used_fields, {'day': {"eli:date_document"},
                                             'month': {"eli:date_document"},
                                             'whole': {"eli:type_document", "eli:number", "eli:date_document"},
                                             'year': {"eli:date_document"}})

    def test_build_uri_abstract_resource(self):
        usch = form_configs.URIScheme("elix:AbstractLegalResource",
                                      "http://test/{eli:type_document}/{eli:number}/{eli:date_document|year}")
        uri = usch.build_uri(READ_VALUES)
        self.assertEqual(uri, "http://test/ABC/412/2017")

    def test_build_uri_resource(self):
        usch = form_configs.URIScheme("eli:LegalResource",
                                      "http://test/{eli:type_document}/{eli:number}/{eli:date_document|year}/act")
        uri = usch.build_uri(READ_VALUES)
        self.assertEqual(uri, "http://test/ABC/412/2017/act")

    def test_build_uri_expression(self):
        usch = form_configs.URIScheme("eli:LegalExpression",
                                      "http://test/{eli:type_document}/{eli:number}/{eli:date_document|year}/act/{eli:language}")
        uri = usch.build_uri(READ_VALUES, lang=ENGLISH)
        self.assertEqual(uri, "http://test/ABC/412/2017/act/EN")

    def test_build_uri_format(self):
        usch = form_configs.URIScheme("eli:Format",
                                      "http://test/{eli:type_document}/{eli:number}/{eli:date_document|year}/act/{eli:language}/{eli:format}")
        uri = usch.build_uri(READ_VALUES, lang=FRENCH, frmt=PDF)
        self.assertEqual(uri, "http://test/ABC/412/2017/act/FR/PDF")

    def test_build_uri_with_dates(self):
        usch = form_configs.URIScheme("eli:LegalResource",
                                      "http://test/{eli:type_document}/{eli:date_document|year}{eli:date_document|month}{eli:date_document|day}/act/{eli:date_document}/{eli:number}")
        uri = usch.build_uri(READ_VALUES)
        self.assertEqual(uri, "http://test/ABC/20170904/act/2017-09-04/412")


if __name__ == '__main__':
    unittest.main()
