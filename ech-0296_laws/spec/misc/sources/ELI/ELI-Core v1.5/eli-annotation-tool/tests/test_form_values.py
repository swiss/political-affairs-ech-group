# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import unittest
import os, json, copy

from eli_annotation import form_values
from eli_annotation .eligraph import (ELI_LANG_PROPERTY, ELI_FORMAT_PROPERTY,
                                      ELIX_URI_PROPERTIES, ELIX_LANGS_LIST,
                                      ELIX_FORMATS_LIST, ELIX_ABSTRACT_RESOURCE,
                                      ELI_RESOURCE, ELI_EXPRESSION, ELI_FORMAT,
                                      ELIX_RES_TYPE_PROPERTY)

try:
    from .fake_form_values import VALUES_DATA, ENGLISH, FRENCH, PDF, PRINT
    from .helpers import silence_logging_warning
except SystemError:
    from fake_form_values import VALUES_DATA, ENGLISH, FRENCH, PDF, PRINT
    from helpers import silence_logging_warning


def get_datafile(fname):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),'data',fname))


class FormValuesTC(unittest.TestCase):

    def test_ELIFormValues_load_from_json(self):
        valfile = get_datafile('act-01.json')
        with open(valfile) as fp:
            vals = form_values.ELIFormValues.load_from_json(json.load(fp))
        self.assertDictEqual(vals._values, VALUES_DATA)

    def test_ELIFormValues_get_prop_val_level0(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        self.assertEqual(vals.get_property_values("eli:type_document"),
                         ['http://test.logilab.org/document#ABC'])
        self.assertEqual(vals.get_property_values("eli:id_local"),
                         ['ID1'])
        self.assertEqual(vals.get_property_values("UNKNOWN"),
                         [])

    def test_ELIFormValues_get_prop_val_level1(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        self.assertEqual(vals.get_property_values("eli:language", lang=ENGLISH),
                         [ENGLISH])
        self.assertEqual(vals.get_property_values("eli:type_document", lang=ENGLISH),
                         ['http://test.logilab.org/document#ABC'])
        self.assertEqual(vals.get_property_values("eli:id_local", lang=ENGLISH),
                         ['ID1-ENG'])
        self.assertEqual(vals.get_property_values("UNKNOWN", lang=ENGLISH),
                         [])

    def test_ELIFormValues_get_prop_val_level2(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        self.assertEqual(vals.get_property_values("eli:format", lang=ENGLISH, frmt=PDF),
                         [PDF])
        self.assertEqual(vals.get_property_values("eli:language", lang=ENGLISH, frmt=PDF),
                         [ENGLISH])
        self.assertEqual(vals.get_property_values("eli:type_document", lang=ENGLISH, frmt=PDF),
                         ['http://test.logilab.org/document#ABC'])
        self.assertEqual(vals.get_property_values("eli:id_local", lang=ENGLISH, frmt=PDF),
                         ['ID1-ENG-PDF'])
        self.assertEqual(vals.get_property_values("UNKNOWN", lang=ENGLISH, frmt=PDF),
                         [])

    def test_ELIFormValues_extract_entities(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        ents = vals.extract_eli_entities()
        exp = {ELIX_ABSTRACT_RESOURCE: {(None, None)},
               ELI_RESOURCE: {(None, None)},
               ELI_EXPRESSION: {(ENGLISH, None), (FRENCH, None)},
               ELI_FORMAT: {(ENGLISH, PRINT), (ENGLISH, PDF),
                            (FRENCH,PRINT), (FRENCH, PDF)}
        }
        self.assertEqual(ents, exp)

    def test_ELIFormValues_extract_no_entity(self):
        vals = form_values.ELIFormValues()
        for key in (*ELIX_URI_PROPERTIES,
                    ELIX_RES_TYPE_PROPERTY, ELIX_LANGS_LIST,
                    ELIX_FORMATS_LIST):
            vals[(key,)] = VALUES_DATA[(key,)][:]
        ents = vals.extract_eli_entities()
        self.assertEqual(ents, {})

    def test_ELIFormValues_extract_no_format_entity(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        for name in list(vals._values.keys()):
            if len(name) == 3 and name[2] != ELI_FORMAT_PROPERTY:
                vals._values.pop(name)
        ents = vals.extract_eli_entities()
        exp = {ELIX_ABSTRACT_RESOURCE: {(None, None)},
               ELI_RESOURCE: {(None, None)},
               ELI_EXPRESSION: {(ENGLISH, None), (FRENCH, None)}
        }
        self.assertEqual(ents, exp)

    def test_ELIFormValues_extract_no_lang_format_entity(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        for name in list(vals._values.keys()):
            if len(name) == 3 and name[2] != ELI_FORMAT_PROPERTY:
                vals._values.pop(name)
            if len(name) == 2 and name[1] != ELI_LANG_PROPERTY:
                vals._values.pop(name)
        ents = vals.extract_eli_entities()
        exp = {ELIX_ABSTRACT_RESOURCE: {(None, None)},
               ELI_RESOURCE: {(None, None)}
        }
        self.assertEqual(ents, exp)

    def test_ELIFormValues_extract_entities_add_lang_entities(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        for name in list(vals._values.keys()):
            if len(name) == 2:
                vals._values.pop(name)
        ents = vals.extract_eli_entities()
        exp = {ELIX_ABSTRACT_RESOURCE: {(None, None)},
               ELI_RESOURCE: {(None, None)},
               ELI_EXPRESSION: {(ENGLISH, None), (FRENCH, None)},
               ELI_FORMAT: {(ENGLISH, PRINT), (ENGLISH, PDF),
                            (FRENCH,PRINT), (FRENCH, PDF)}
        }
        self.assertEqual(ents, exp)

    def test_ELIFormValues_extract_entities_add_resource_lang_entities(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        for name in list(vals._values.keys()):
            if len(name) <= 2:
                vals._values.pop(name)
        ents = vals.extract_eli_entities()
        exp = {ELIX_ABSTRACT_RESOURCE: {(None, None)},
               ELI_RESOURCE: {(None, None)},
               ELI_EXPRESSION: {(ENGLISH, None), (FRENCH, None)},
               ELI_FORMAT: {(ENGLISH, PRINT), (ENGLISH, PDF),
                            (FRENCH,PRINT), (FRENCH, PDF)}
        }
        self.assertEqual(ents, exp)

    def test_ELIFormValues_extract_entities_add_resource_entities(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        for name in list(vals._values.keys()):
            if len(name) == 1:
                vals._values.pop(name)
        ents = vals.extract_eli_entities()
        exp = {ELIX_ABSTRACT_RESOURCE: {(None, None)},
               ELI_RESOURCE: {(None, None)},
               ELI_EXPRESSION: {(ENGLISH, None), (FRENCH, None)},
               ELI_FORMAT: {(ENGLISH, PRINT), (ENGLISH, PDF),
                            (FRENCH,PRINT), (FRENCH, PDF)}
        }
        self.assertEqual(ents, exp)

    def test_ELIFormValues_get_context_properties(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        with self.subTest(lang=None, format=None):
            exp = {name[-1]:values for name,values in VALUES_DATA.items()
                   if len(name) == 1}
            props = vals.get_context_properties()
            self.assertEqual(props, exp)
        for lang in (ENGLISH, FRENCH):
            with self.subTest(lang=lang, format=None):
                exp = {name[-1]:values for name,values in VALUES_DATA.items()
                       if len(name) == 2 and name[0]==lang}
                props = vals.get_context_properties(lang=lang)
                self.assertEqual(props, exp)

        for lang,frmt in ((ENGLISH, PRINT), (ENGLISH, PDF),
                          (FRENCH, PRINT), (FRENCH, PDF)):
            with self.subTest(lang=lang, format=frmt):
                exp = {name[-1]:values for name,values in VALUES_DATA.items()
                       if len(name) == 3 and name[0]==lang and name[1]==frmt}
                props = vals.get_context_properties(lang=lang, frmt=frmt)
                self.assertEqual(props, exp)

    def test_ELIFormValues_json_export(self):
        vals = form_values.ELIFormValues()
        vals._values = copy.deepcopy(VALUES_DATA)
        with silence_logging_warning():
            data = vals.json_export()
        jsonfile = get_datafile('act-01-exported.json')
        with open(jsonfile) as inp:
            expected = json.load(inp)
        self.assertEqual(data, expected)


if __name__ == '__main__':
    unittest.main()
