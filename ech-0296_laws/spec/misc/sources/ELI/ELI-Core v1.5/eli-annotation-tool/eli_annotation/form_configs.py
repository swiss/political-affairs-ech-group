# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

from functools import reduce
from os import path as osp
import datetime as dtm
import json, re, logging

from .vocabs import VocabularyIndex, VocabValue
from .form_values import ELIFormValues
from .errors import IncorrectResource
from .eligraph import (
    ACT_RESOURCE, JOURNAL_RESOURCE, CONSOLIDATION_RESOURCE, ELI_ENTITIES,
    ELI_EXPRESSION, ELI_FORMAT, ELI_DATE_PROPERTIES, ELI_URI_PROPERTIES,
    ELI_VOCAB_PROPERTIES, ELI_TEXT_PROPERTIES, ELIX_RES_TYPE_PROPERTY,
    ELI_LANG_PROPERTY, ELI_FORMAT_PROPERTY, ELI_LANG_PREFIX, ELI_FORMAT_PREFIX,
    ELIX_LANGS_LIST, ELIX_FORMATS_LIST, URI_SCHEME_ENTITY)


class FormConfigIndex:
    """
    Given a directory where form configurations are stored
    as JSON files with extension .json, manage an index that
    behaves like a dict of {elix:resource_type => filename}
    """
    FNAME = {
        ACT_RESOURCE: "act",
        JOURNAL_RESOURCE: "journal",
        CONSOLIDATION_RESOURCE: "consolidation"
    }
    VNAME = {
        ACT_RESOURCE: "act-values",
        JOURNAL_RESOURCE: "journal-values",
        CONSOLIDATION_RESOURCE: "consolidation-values"
    }

    def __init__(self, form_dir):
        self.basedir = form_dir

    def path(self, filename):
        return osp.join(self.basedir, filename)

    def load(self, resource_type, vocab_index, values=None):
        assert isinstance(vocab_index, VocabularyIndex), type(vocab_index)
        assert values is None or isinstance(values, ELIFormValues), type(values)
        # Tries to load default values if none is given.
        if values is None:
            values = self.load_default_values(resource_type)
        # Reads config.
        filename = self.path(self.FNAME[resource_type]) + ".json"
        if not osp.isfile(filename):
            msg = ("Can't find the form configuration file for resource: {0}"
                   "").format(resource_type)
            raise IncorrectResource("missingFormConfig", msg, resource_type)
        try:
            with open(filename, encoding='utf-8') as fp:
                cfg = ELIFormConfig.load_from_json(json.load(fp), values,
                                                   vocab_index)
        except Exception as exc:
            msg = ("An error occurred while reading the form configuration "
                   "file for resource: {0}").format(resource_type)
            raise IncorrectResource(
                "incorrectFormConfig", msg, resource_type) from exc
        return cfg

    def load_default_values(self, resource_type, recover_from_exceptions=True):
        filename =  self.path(self.VNAME[resource_type]) + ".json"
        if not recover_from_exceptions and not osp.isfile(filename):
            msg = ("Can't find the form default values file for resource: {0}"
                   "").format(resource_type)
            raise IncorrectResource("missingFormDefaultValues", msg,
                                    resource_type)
        try:
            with open(filename, encoding="utf-8") as fp:
                values = ELIFormValues.load_from_json(json.load(fp))
        except Exception as exc:
            if recover_from_exceptions:
                values = ELIFormValues()
                values[(ELIX_RES_TYPE_PROPERTY,)] = [resource_type]
            else:
                msg = ("An error occurred while reading the form default values "
                       "file for resource: {0}").format(resource_type)
                raise IncorrectResource(
                    "incorrectDefaultFormValues", msg, resource_type) from exc
        return values


class ELIFormConfig:
    """
    Class describing the configuration of the form getting the data describing
    a legal resource (e.g. a act, an official journal or a consolidation)

    The properties in the configuration are organized in a tree-like structure:
    general properties at first level, language properties at second level,
    format properties at third level.

    This class contains a dictionary of ELIFormProp.
    """
    def __init__(self, legal_resource_type):
        assert legal_resource_type in (ACT_RESOURCE, JOURNAL_RESOURCE,
                                       CONSOLIDATION_RESOURCE)
        self.resource_type = legal_resource_type
        self.uri_schemes = {}
        self._properties = {}

    def __setitem__(self, name, prop):
        """
        Adds the configuration of a property to the form configuration.

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")

        ``prop`` is an ELIFormProp object.
        """
        if isinstance(name, str):
             name = (name,)
        if name in self._properties:
            msg = ("In form configuration, a property is already defined for: "
                   "") .format(" / ".join(name))
            raise IncorrectResource("incorrectFormConfig", msg, self.resource_type)
        if not isinstance(prop, ELIFormProp):
            raise ValueError("Property associated to {0} should be an "
                             "ELIFormProp object".format(" / ".join(name)))
        self._properties[name] = prop

    def __getitem__(self, name):
        """
        Gets the property whose name is ``name``.

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")
        """
        if isinstance(name, str):
            name = (name,)
        return self._properties[name]

    def get(self, name, default=None):
        """
        Gets the property whose name is ``name`` or returns ``default``
        if it doesn't exist.

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")
        """
        if isinstance(name, str):
            name = (name,)
        return self._properties.get(name, default)

    def __contains__(self, name):
        """
        Returns True if the config contains a property whose name is ``name``.

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")
        """
        if isinstance(name, str):
            name = (name,)
        return self._properties.__contains__(name)

    def pop(self, name):
        """
        Deletes the config of the property whose name is ``name`` from this object but
        returns it.

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")
        """
        if isinstance(name, str):
            name = (name,)
        return self._properties.pop(name)

    @classmethod
    def load_from_json(cls, form_config, raw_values, vocab_index):
        """
        Return an ELIFormConfig object built from the JSON data in
        ``form_config``.

        ``raw_values`` contains the values of a given notice or the default
        values, stored inside an ELIFormValues object.

        ``vocab_index`` is a VocabIndex object that allows to access the
        vocabularies used in the properties configurations.
        """
        assert isinstance(raw_values, ELIFormValues), type(raw_values)
        assert isinstance(vocab_index, VocabularyIndex), type(vocab_index)
        # Gets resource type concerned by this form configuration
        res_type = form_config.get(ELIX_RES_TYPE_PROPERTY)
        if res_type not in (ACT_RESOURCE, JOURNAL_RESOURCE,
                            CONSOLIDATION_RESOURCE):
            msg = ("The form configuraton concerns an unknown legal resource. "
                   "Expected {0} (act), {1} (official journal) or {2} "
                   "(consolidation) and got: {3}"
                   "").format(ACT_RESOURCE, JOURNAL_RESOURCE,
                             CONSOLIDATION_RESOURCE, res_type)
            raise IncorrectResource("incorrectFormConfig", msg)
        # Checks the values concern the same resource type
        val_type = raw_values.get((ELIX_RES_TYPE_PROPERTY,))
        val_type = val_type[0] if len(val_type) > 0 else None
        if  val_type != res_type:
            msg = ("The form configuration concerns a legal resource different "
                   "from the one in the form values: {0} vs. {1}"
                   "").format(val_type, res_type)
            raise IncorrectResource("incorrectFormConfig", msg, res_type)
        # Builds the form configuration object
        cfg = cls(res_type)
        # Loads the URI Schemes
        for prop_name, entity in URI_SCHEME_ENTITY.items():
            val = raw_values.get((prop_name,), [])
            if len(val) == 0:
                msg = ("Can't find the URI scheme for {0}. It should be "
                       "defined inside the form values in property: {1}"
                       "").format(entity, prop_name)
                raise IncorrectResource("incorrectFormValues", msg)
            cfg.uri_schemes[entity] = URIScheme(entity, val[0])
        # First, creates the tree-structure of the properties and stores inside
        # the JSON specif of each property. On the way, notes the URIs of all
        # the vocabularies used in the property configuration.
        json_specifs = {}
        vocab_uris = set()
        for prop0, value0 in form_config.get("properties", {}).items():
            if prop0.startswith(ELI_LANG_PREFIX):
                lang = value0.get("title")
                if lang is None:
                    msg = ("Inconsistent form configuration. No URI defined "
                           "for the language associated to: {0}").format(prop0)
                    raise IncorrectResource("incorrectFormConfig", msg, res_type)
                for prop1, value1 in value0.get("properties", {}).items():
                    if prop1.startswith(ELI_FORMAT_PREFIX):
                        frmt = value1.get("title")
                        if frmt is None:
                            msg = ("Inconsistent form configuration. No URI "
                                   "defined for the format associated to: "
                                   "{0}/{1}").format(prop0, prop1)
                            raise IncorrectResource("incorrectFormConfig",
                                                    msg, res_type)

                        for prop2, value2 in value1.get("properties", {}).items():
                            json_specifs[(lang, frmt, prop2)] = value2
                            if value2.get("enabled") and value2.get("vocab"):
                                vocab_uris.add(value2["vocab"])
                    else:
                        json_specifs[(lang, prop1)] = value1
                        if value1.get("enabled") and value1.get("vocab"):
                            vocab_uris.add(value1["vocab"])
            else:
                json_specifs[(prop0,)] = value0
                if value0.get("enabled") and value0.get("vocab"):
                    vocab_uris.add(value0["vocab"])
        # Loads the used vocabularies
        vocabs = {vocab_uri: vocab_index.load(vocab_uri) for vocab_uri in vocab_uris}
        # Finally, loads the property configurations
        all_eli_props = set(ELI_DATE_PROPERTIES + ELI_URI_PROPERTIES +
                            ELI_VOCAB_PROPERTIES + ELI_TEXT_PROPERTIES)
        for name, json_spec in json_specifs.items():
            local_name = name[-1]
            if local_name not in all_eli_props:
                continue
            # Gets vocabulary for language and format
            if local_name == ELI_LANG_PROPERTY:
                json_spec['vocab'] = json_specifs[(ELIX_LANGS_LIST,)]['vocab']
            elif local_name == ELI_FORMAT_PROPERTY:
                json_spec['vocab'] = json_specifs[(ELIX_FORMATS_LIST,)]['vocab']
            # Creates the property config from the JSON spec and adds it
            prop = ELIFormProp.create_from_json(name, json_spec, vocabs)
            cfg[name] = prop
        return cfg

    def read_form_values(self, raw_values, check_mandatory=True):
        """
        Reads the form raw values and builds Python objects depending on the
        property type (date, URI, VocabValue, etc.)

        ``raw_values`` is an ELIFormValues object and contains, for each
        property, the string values read in the form.

        Returns an ELIFormValues object with only the properties that are
        enabled in the configuration, with only one value when the property
        can't have multiple values (cf. configuration). The values of the
        property are Python objects built thanks to the property type and the
        configuration. An exception is raised if a mandatory property doesn't
        have a value.
        """
        assert isinstance(raw_values, ELIFormValues), type(raw_values)
        values = ELIFormValues()
        values[ELIX_RES_TYPE_PROPERTY] = raw_values[ELIX_RES_TYPE_PROPERTY]
        missing = set()
        for name, cfg in self._properties.items():
            if not cfg.enabled:
                continue
            vals = [cfg.read_value(val)
                    for val in raw_values.get(name, [])]
            if not cfg.multiple and len(vals) > 1:
                logging.warning(
                    "Multiple values provided for {0} property whereas "
                    "configuration allows only one."
                    "Keeping only first value.".format(" / ".join(name)))
                vals = vals[:1]
            if check_mandatory and cfg.mandatory and len(vals) == 0:
                missing.add(name)
            values[name] = vals
        if len(missing) > 0:
            msg = ("Missing values for the following mandatory properties:\n{0}"
                   "").format("\n".join([" / ".join(name) for name in missing]))
            raise IncorrectResource("missingMandatoryFormValues", msg)
        return values

    def get_context_configs(self, lang=None, frmt=None):
        """
        Gets all the property configurations inside a given context (general,
        a chosen language, or a chosen language and a chosen format).

        This function can be usefully called when gathering the property
        configurations of a given entity. If ``lang`` and ``frmt`` are ``None``,
        returns all the property configurations whose name doesn't start with a
        language URI or a format URI. If ``lang`` is set to a URI and ``frmt``
        is ``None``, returns all the properties whose name starts with the given
        URI but doesn't contain a format URI. If both ``lang`` and ``frmt`` are
        set to URIs, returns all the properties whose name starts with the two
        given URIs.

        Returns a dictionary whose keys are the property local name (i.e. without
        the lang and format URIs) and the values are the property configuration
        (``ELIFormProp`` object).
        """
        if lang is None and frmt is None:
            sel_names = [name for name in self._properties
                         if len(name) == 1]
        elif frmt is None:
            sel_names = [name for name in self._properties
                         if len(name) == 2 and name[0] == lang]
        elif lang is not None:
            sel_names = [name for name in self._properties
                         if len(name) == 3 and name[0]==lang and name[1]==frmt]
        else:
            raise ValueError(
                "Inconsistent context specfication. language URI can't be None "
                "if format URI is specified:\nlang={0} format={1}"
                "".format(lang, frmt))
        return {name[-1]: self._properties[name] for name in sel_names}


class ELIFormProp:
    """
    Class describing the configuration of a property inside the form
    configuration of a legal resource (e.g. a act, an official journal or a
    consolidation).

    This a base class. Several derived classes exist for each kind of
    property.
    """
    def __init__(self, prop_name, enabled=True, mandatory=False):
        if isinstance(prop_name, str):
            prop_name = (prop_name,)
        if not enabled and mandatory:
            msg = ("In configuration, a mandatory property is not "
                   "activated : {0}").format(" / ".join(prop_name))
            raise IncorrectResource("notEnabledMandatoryPropertyInConfig", msg,
                                    " / ".join(prop_name))
        self.name = prop_name
        self.enabled = enabled
        self.mandatory = mandatory
        self.multiple = False

    def read_value(self, str_value):
        """
        Reads a value specified in a form data and returns the corresponding
        Python object (building this object depends on the property
        configuration: date, vocabulary value, etc.).

        See derived classes.
        """
        return str(str_value)

    @classmethod
    def create_from_json(cls, name, prop_specif, vocabs):
        """
        Creates and returns an ELIFormProp object, using the configuration
        described in ``prop_specif``.

        The actual class of the built object depends on the property (cf.
        derived classes).

        ``name`` is a tuple giving the identifier of the property at each level
        (e.g. ``("http://.../ENG", "http://.../PDF", "eli:exemplified_by")

        ``vocabs`` contains a dictionary with  all the vocabularies, indexed
        by their name, that might be used in the property configuration.
        """
        if isinstance(name, str):
            name = (name,)
        local_name = name[-1]
        enabled = prop_specif.get("enabled", False)
        mandatory = prop_specif.get("mandatory", False) and enabled
        prop_cfg = ELI_PROP_CLASS[local_name](name, enabled, mandatory)
        if not prop_cfg.enabled:
            return prop_cfg
        prop_cfg.multiple = prop_specif.get("type", "") == "array"
        # Adds the vocabularies if necessary
        if isinstance(prop_cfg, ELIFormVocabProp):
            vocab_name = prop_specif.get("vocab")
            if vocab_name is None or vocab_name == "":
                msg = ("Configuration should contain the specification of the "
                       "vocabulary used to define values for property: {0}"
                       "").format(" / ".join(name))
                raise IncorrectResource(
                    "missingVocabularyInPropertyConfig", msg, " / ".join(name))
            if vocab_name in vocabs:
                prop_cfg.vocabularies.append(vocabs[vocab_name])
            else:
                msg =("Can't find the vocabulary ({0}) specified in the "
                      "configuration of property: {1}"
                      "").format(vocab_name, " / ".join(name))
                raise IncorrectResource(
                    "unknownVocabularyInPropertyConfig", msg, " / ".join(name))
        return prop_cfg


class ELIFormTextProp(ELIFormProp):
    """
    Class describing the configuration of a property that contain regular
    text.
    """
    pass


class ELIFormDateProp(ELIFormProp):
    """
    Class describing the configuration of a property that contain a date.
    """
    def read_value(self, str_value):
        """
        Reads the value given in the form data and returns a date object.
        """
        try:
            val = dtm.datetime.strptime(str_value.strip(), "%Y-%m-%d")
        except (TypeError, ValueError) as exc:
            msg = ("Value specified can't be read as a date for property: {1}"
                   "").format(" / ".join(self.name))
            raise IncorrectResource(
                "incorrectValueForDateProperty", msg,
                " / ".join(self.name)) from exc
        return val.date()


class ELIFormURIProp(ELIFormProp):
    """
    Class describing the configuration of a property that contain a URI.
    """
    def read_value(self, str_value):
        """
        Reads the value given in the form data and returns a URIValue object.
        If the value doesn't seem to be an URI, returns the value
        """
        if str_value.strip().startswith("urn:") \
           or str_value.strip().startswith("http://") \
           or str_value.strip().startswith("https://") :
            return URIValue(str_value.strip())
        else:
            return str_value


class URIValue(str):
    """
    String subclass containing an URI.
    """
    pass


class ELIFormVocabProp(ELIFormProp):
    """
    Class describing the configuration of a property that contain a vocabulary
    value.
    """
    def __init__(self, prop_name, enabled=True, mandatory=False):
        super().__init__(prop_name, enabled, mandatory)
        self.vocabularies = []

    def _find_vocab_value(self, uri):
        """
        Tries to find the vocabulary value object (cf. vocabs.VocabValue)
        in the vocabularies specified in the property configuration.
        """
        uri = uri.strip()
        for vocab in self.vocabularies:
            val = vocab.get(uri)
            if val is not None:
                return val
        return None

    def read_value(self, str_value):
        """
        Reads the value (URI) given in the form data and returns the vocabulary
        value object corresponding to this URI (cf. vocabs.VocabValue)
        """
        val = self._find_vocab_value(str_value)
        if val is None:
            msg = ("Can't find value \"{0}\" in the vocabularies ({2}) "
                   "configured for property: {1}"
                   "").format(str_value, " / ".join(self.name),
                              ", ".join(v.uri for v in self.vocabularies))
            raise IncorrectResource("wrongValueForVocabularyProperty", msg,
                                    " / ".join(self.name))
        return val


ELI_PROP_CLASS = {}
for name in ELI_DATE_PROPERTIES:
    ELI_PROP_CLASS[name] = ELIFormDateProp
for name in ELI_URI_PROPERTIES:
    ELI_PROP_CLASS[name] = ELIFormURIProp
for name in ELI_VOCAB_PROPERTIES:
    ELI_PROP_CLASS[name] = ELIFormVocabProp
for name in ELI_TEXT_PROPERTIES:
    ELI_PROP_CLASS[name] = ELIFormTextProp


# URI Schemes #################################################################


URI_SCHEMA_PROP_NAMES = re.compile(r"\{(.*?)\}")
"""
Regular expression for extracting the field specifications from a URI scheme.
"""
WHOLE = "whole"
"""
Constant meaning a field is used as a whole in a URI scheme.
"""
YEAR = "year"
"""
Operator used for extracting the year from a date field used in a URI Scheme.
"""
MONTH = "month"
"""
Operator used for extracting the month from a date field used in a URI Scheme.
"""
DAY = "day"
"""
Operator used for extracting the day from a date field used in a URI Scheme.
"""
DATE_FORMAT_SPEC = {WHOLE: "%Y-%m-%d", YEAR: "%Y", MONTH: "%m", DAY: "%d"}
"""
Format specification for each operator to be used with the date fields of the
URI Scheme.
"""


class URIScheme:
    """
    Class defining a URI Scheme that describes the URI of an ELI object using
    some of the fields that describe this object.
    """
    def __init__(self, eli_entity_name, uri_pattern):
        assert eli_entity_name in ELI_ENTITIES, \
            "Unknown entity name:\n{}".format(eli_entity_name)
        self.entity_name = eli_entity_name
        self._used_fields = {WHOLE: set(), YEAR: set(), MONTH: set(),
                             DAY: set()}
        self._raw_scheme = uri_pattern
        # Collects fields used in URI Scheme
        for item in URI_SCHEMA_PROP_NAMES.findall(uri_pattern):
            if '|' in item:
                field, operator = item.split('|')
            else:
                field, operator = item, WHOLE
            assert operator in (WHOLE, DAY, MONTH, YEAR), \
                ("Unknown operator found in URI scheme for field {0}:\n{1}"
                 "".format(field, operator))
            self._used_fields[operator].add(field)
        # Re-writes the string formatting specification to have it working even
        # if the field names contain ":" characters
        self.scheme = self._raw_scheme
        for operator,fields in self._used_fields.items():
            suffix = ""
            if operator != WHOLE:
                suffix = "|{0}".format(operator)
            for name in fields:
                spec = "{0}{1}".format(name, suffix)
                self.scheme = self.scheme.replace(
                    "{{{0}}}".format(spec), "{{0[{0}]}}".format(spec))

    @property
    def used_fields(self):
        return reduce(set.union, self._used_fields.values())

    def build_uri(self, values, lang=None, frmt=None):
        """
        Builds the URI of an ELI object using the form values given
        in ``values``.

        ``lang`` (language) and ``frmt`` (format) can contain the URI of
        the language and the format associated to the ELI object. Of
        course, they can be ``None`` if the object is not associated to
        a language or a format.
        """
        assert isinstance(values, ELIFormValues), type(values)
        if self.entity_name == ELI_EXPRESSION:
            assert lang is not None and frmt is None, \
                ("Specified context inconsistent with eli:LegalExpression "
                 "entity:\nlang={0} format={1}".format(lang, frmt))
        elif self.entity_name == ELI_FORMAT:
            assert lang is not None and frmt is not None, \
                ("Specified context inconsistent with eli:Format entity:\n"
                 "lang={0} format={1}".format(lang, frmt))
        else:
            assert lang is None and frmt is None, \
                ("Specified context inconsistent with {0} entity:\n"
                 "lang={1} format={2}".format(self.entity_name, lang, frmt))
        # Prepares values for each of the fields used in the URI Scheme
        field_values = {}
        for operator,fields in self._used_fields.items():
            suffix = ""
            if operator != WHOLE:
                suffix = "|{0}".format(operator)
            for local_name in fields:
                uri_field = "{0}{1}".format(local_name, suffix)
                values_list = values.get_property_values(local_name, lang, frmt)
                if len(values_list) == 0:
                    msg = ("Can't find a value for a field necessary for "
                           "building a URI: {0}").format(local_name)
                    raise IncorrectResource("missingValueForUriBuilding",
                                            msg, local_name)
                value = values_list[0]
                if isinstance(value, VocabValue):
                    if value.notation is None:
                        msg = ("Vocabulary concept doesn't have a notation "
                               "for building a URI: {0}").format(value.uri)
                        raise IncorrectResource(
                            "missingNotationForConceptInVocabulary",
                            msg, str(value.vocabulary.uri))
                    value = value.notation
                elif isinstance(value, dtm.date):
                    value = value.strftime(DATE_FORMAT_SPEC[operator])
                field_values[uri_field] = value
        # Builds the URI from the scheme and the field values.
        return self.scheme.format(field_values)
