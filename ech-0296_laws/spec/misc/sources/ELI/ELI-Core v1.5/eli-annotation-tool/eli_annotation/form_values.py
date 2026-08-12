# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import datetime as dtm
import logging

from .eligraph import (ELI_LANG_PREFIX, ELI_FORMAT_PREFIX,
                       ELI_LANG_PROPERTY, ELI_FORMAT_PROPERTY,
                       ELIX_ABSTRACT_RESOURCE, ELI_RESOURCE,
                       ELI_EXPRESSION, ELI_FORMAT,
                       ELIX_RES_TYPE_PROPERTY, ELIX_LANGS_LIST,
                       ELIX_FORMATS_LIST, ELIX_URI_PROPERTIES)
from eli_annotation import vocabs
from .errors import IncorrectResource

class ELIFormValues:
    """
    Class containing the values read inside a form.

    The values are organized in a tree-like structure:
    general properties at first level, language properties
    at second level, format properties at third level.
    """
    def __init__(self):
        self._values = {}

    def __getitem__(self, name):
        """
        Gets the value of the property whose name is ``name``.

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")
        """
        if isinstance(name, str):
            name = (name,)
        return self._values[name]

    def __setitem__(self, name, value):
        """
        Sets the value of the property whose name is ``name``.

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")

        Raise an error if a property with the same name is already defined
        """
        if isinstance(name, str):
            name = (name,)
        if name in self._values:
            msg = ("A value is already defined for property {}"
                   "").format("/".join(name))
            raise IncorrectResource("incorrectFormValues", msg)
        self._values[name] = value

    def get(self, name, default=None):
        """
        Gets the value of the property whose name is ``name`` or returns
        ``default`` if it doesn't exist.

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")
        """
        if isinstance(name, str):
            name = (name,)
        return self._values.get(name, default)

    def __contains__(self, name):
        """
        Returns True if there is a value for the property whose name is ``name``.

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")
        """
        if isinstance(name, str):
            name = (name,)
        return self._values.__contains__(name)

    def pop(self, name):
        """
        Deletes the value of the property whose name is ``name`` from this object but
        returns it.

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")
        """
        if isinstance(name, str):
            name = (name,)
        return self._values.pop(name)

    @classmethod
    def load_from_json(cls, values_data):
        """
        Return an ELIFormValues object built from the JSON data in
        ``values_data``.
        """
        form_values = cls()
        for prop0, value0 in values_data.items():
            if prop0.startswith(ELI_LANG_PREFIX):
                lang = value0.get(ELI_LANG_PROPERTY, {}).get("value")
                if lang is None or len(lang) == 0:
                    msg = ("Inconsistent form values. No value for eli:language "
                           "property in {0}").format(prop0)
                    raise IncorrectResource("incorrectFormValues", msg)
                lang = lang[0]
                for prop1, value1 in value0.items():
                    if prop1.startswith(ELI_FORMAT_PREFIX):
                        frmt = value1.get(ELI_FORMAT_PROPERTY, {}).get("value")
                        if frmt is None or len(frmt) == 0:
                              msg = ("Inconsistent form values. No value for "
                                     "eli:format property in {0}/{1}"
                                     "").format(prop0, prop1)
                              raise IncorrectResource(
                                  "incorrectFormValues", msg)
                        frmt = frmt[0]
                        for prop2, value2 in value1.items():
                            val = value2.get("value")
                            if val is None or val == "":
                                val = []
                            elif not isinstance(val, list):
                                val = [val]
                            form_values[(lang, frmt, prop2)] = \
                                [v for v in val if v is not None and v != ""]
                    else:
                        val = value1.get("value")
                        if val is None or val == "":
                            val = []
                        elif not isinstance(val, list):
                            val = [val]
                        form_values[(lang, prop1)] = \
                                [v for v in val if v is not None and v != ""]
            else:
                val = value0.get("value")
                if val is None or val == "":
                    val = []
                elif not isinstance(val, list):
                    val = [val]
                form_values[(prop0,)] = \
                                [v for v in val if v is not None and v != ""]
        return form_values

    def get_property_values(self, prop_name, lang=None, frmt=None):
        """
        Gets the values of a property inside a given context (general,
        a chosen language, or a chosen language and a chosen format).

        This function can be usefully called when building the URI from
        the URI scheme of an entity. The ``lang`` and ``frmt`` parameters
        give the level at which the property is searched, If it is not found
        at this level, it is searched at the parent level and so on.

        Returns the list of the values for the property.
        """
        if lang is None and frmt is not None:
            raise ValueError(
                "Inconsistent context specfication. language URI can't be None "
                "if format URI is specified:\nlang={0} format={1}"
                "".format(lang, frmt))
        if lang is not None and frmt is not None:
            name = (lang, frmt, prop_name)
        elif lang is not None:
            name = (lang, prop_name)
        else:
            name = (prop_name,)
        value = []
        while value == [] and len(name) > 0:
            value = self.get(name, [])
            # Name for parent level
            if len(name) == 3:
                name = (name[0], name[2])
            else:
                name = name[1:]
        return value

    def get_context_properties(self, lang=None, frmt=None):
        """
        Gets all the properties inside a given context (general,
        a chosen language, or a chosen language and a chosen format).

        This function can be usefully called when gathering the properties
        of a given entity. If ``lang`` and ``frmt`` are ``None``, returns
        all the properties whose name doesn't start with a language URI or a
        format URI. If ``lang`` is set to a URI and ``frmt`` is ``None``,
        returns all the properties whose name starts with the given URI but
        doesn't contain a format URI. If both ``lang`` and ``frmt`` are set
        to URIs, returns all the properties whose name starts with the two given
        URIs.

        Returns a dictionary whose keys are the property local name (i.e. without
        the lang and format URIs) and the values are the list of these property
        values.
        """
        if lang is None and frmt is None:
            sel_names = [name for name in self._values
                         if len(name) == 1]
        elif frmt is None:
            sel_names = [name for name in self._values
                         if len(name) == 2 and name[0] == lang]
        elif lang is not None:
            sel_names = [name for name in self._values
                         if len(name) == 3 and name[0]==lang and name[1]==frmt]
        else:
            raise ValueError(
                "Inconsistent context specfication. language URI can't be None "
                "if format URI is specified:\nlang={0} format={1}"
                "".format(lang, frmt))
        return {name[-1]: self._values[name] for name in sel_names}

    def extract_eli_entities(self):
        """
        From the values, extract the ELI entities: abstract legal resource,
        legal resource, legal expressions and formats.

        Returns a dictionary whose keys are the type of extracted entities
        and the values are the associated lang and formats URIs (which can be
        ``None`` if they are not relevant).
        """
        entities = {}
        for name, vals in self._values.items():
            if len(name) == 1:
                # The property describes the general entities (legal resources)
                if len(vals) == 0:
                    # Skips empty properties
                    continue
                if name in (*((fld,) for fld in ELIX_URI_PROPERTIES),
                            (ELIX_RES_TYPE_PROPERTY,), (ELIX_LANGS_LIST,),
                            (ELIX_FORMATS_LIST,)):
                    # Skips properties only used by the tool
                    continue
                if ELI_RESOURCE not in entities:
                    entities[ELI_RESOURCE] = {(None, None)}
                    entities[ELIX_ABSTRACT_RESOURCE] = {(None, None)}
            elif len(name) == 2:
                # The property describes the lang entities (legal expresssions)
                if len(vals) == 0:
                    # Skips empty properties
                    continue
                if name[1] == ELI_LANG_PROPERTY:
                    # Skips properties defining the language
                    continue
                if ELI_EXPRESSION not in entities:
                    entities[ELI_EXPRESSION] = set()
                # Keeps language URI of this lang entity
                entities[ELI_EXPRESSION].add((name[0], None))
            elif len(name) == 3:
                # The property describes the format entities (formats)
                if len(vals) == 0:
                    # Skips empty properties
                    continue
                if name[2] == ELI_FORMAT_PROPERTY:
                    # Skips properties defining the format
                    continue
                if ELI_FORMAT not in entities:
                    entities[ELI_FORMAT] = set()
                # Keeps the couple (language URI, format URI) of this format
                # entity
                entities[ELI_FORMAT].add(name[:2])
        # Keeps consistency by adding missing parent entities
        for lang,frmt in entities.get(ELI_FORMAT,[]):
            if ELI_EXPRESSION not in entities:
                entities[ELI_EXPRESSION] = set()
            entities[ELI_EXPRESSION].add((lang, None))
        for lang,frmt in entities.get(ELI_EXPRESSION,[]):
            if ELI_RESOURCE not in entities:
                entities[ELI_RESOURCE] = {(None, None)}
                entities[ELIX_ABSTRACT_RESOURCE] = {(None, None)}
        # Returns extracted entities
        return entities

    def json_export(self):
        """
        Saves this object values into a data dictionary that can
        be sent to the client side of the application in JSON format.
        """
        data = {}
        sub_dicts = {}
        for name, vals in self._values.items():
            # Prepares values for JSON export
            values = []
            for val in vals:
                if isinstance(val, dtm.date):
                    values.append(val.strftime("%Y-%m-%d"))
                elif isinstance(val, vocabs.VocabValue):
                    values.append(val.uri)
                elif (val == "" or val is None):
                    continue
                else:
                    values.append(str(val))
            # Stores values in a tree structure of dictionaries
            if len(name) == 1:
                # Property is in the main context
                data[name[-1]] = {"value": values}
            elif len(name) == 2:
                # Property is in a language context
                lang = name[0]
                if lang not in sub_dicts:
                    lang_last_part = \
                                lang[max(lang.rfind("/"), lang.rfind("#"))+1:]
                    lang_prefix = ELI_LANG_PREFIX + lang_last_part
                    index = 0
                    while lang_prefix in data:
                        index += 1
                        lang_prefix = (ELI_LANG_PREFIX + lang_last_part
                                       + "-{0}".format(index))
                    sub_dicts[lang] = {}
                    data[lang_prefix] = sub_dicts[lang]
                sub_dicts[lang][name[-1]] = {"value": values}
            elif len(name) == 3:
                # Property is in a format context
                lang, frmt = name[0:2]
                if (lang, frmt) not in sub_dicts:
                    if lang not in sub_dicts:
                        lang_last_part = \
                                lang[max(lang.rfind("/"), lang.rfind("#"))+1:]
                        lang_prefix = ELI_LANG_PREFIX + lang_last_part
                        index = 0
                        while lang_prefix in data:
                            index += 1
                            lang_prefix = (ELI_LANG_PREFIX + lang_last_part
                                           + "-{0}".format(index))
                        sub_dicts[lang] = {}
                        data[lang_prefix] = sub_dicts[lang]
                    frmt_last_part = \
                                frmt[max(frmt.rfind("/"), frmt.rfind("#"))+1:]
                    frmt_prefix = ELI_FORMAT_PREFIX + frmt_last_part
                    index = 0
                    while frmt_prefix in sub_dicts[lang]:
                        index += 1
                        frmt_prefix = (ELI_FORMAT_PREFIX + frmt_last_part
                                       + "-{0}".format(index))
                    sub_dicts[(lang, frmt)] = {}
                    sub_dicts[lang][frmt_prefix] = sub_dicts[(lang, frmt)]
                sub_dicts[(lang, frmt)][name[-1]] = {"value": values}
        return data
