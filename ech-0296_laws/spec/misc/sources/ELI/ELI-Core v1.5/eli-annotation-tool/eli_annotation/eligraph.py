# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import rdflib
from rdflib.namespace import RDF, RDFS, OWL, SKOS, DC, DCTERMS


# Standard namespaces used by rdflib

ELI = rdflib.Namespace("http://data.europa.eu/eli/ontology#")
"""
ELI namespace for rdflib
"""
ELIX = rdflib.Namespace("urn:eli-annotation-tool:eli:ontology-extension:")
"""
ELI Extension namespace for rdflib

For the annotation tool, we need supplementary properties that are positionned
into this ELIX namespace.
"""
PROV = rdflib.Namespace("http://www.w3.org/ns/prov#")
"""
PROV namespace for rdflib

PROV is used to save the user that created an ELI graph.
"""
PROVX = rdflib.Namespace("urn:eli-annotation-tool:prov:ontology-extension:")
"""
PROVExtension namespace for rdflib

For the annotation tool, we need supplementary properties that are positionned
into this PROVX namespace.
"""

# Standard SKOS vocabularies for filetypes and languages

LANG_VOCAB_URI = "http://publications.europa.eu/resource/authority/language"
FILETYPE_VOCAB_URI = "https://www.iana.org/assignments/media-types"


# Prefixes used in JSON format to mark a subobject containing language-related
# or format-related properties

ELI_LANG_PREFIX = "lang_"
ELI_FORMAT_PREFIX = "format_"


# Various ELI (or ELIX) entities

ELIX_ABSTRACT_RESOURCE = "elix:AbstractLegalResource"
"""
Entity name for an abstract legal resource (ELI extension).
"""
ELI_RESOURCE = "eli:LegalResource"
"""
Entity name for a legal resource (ELI standard).
"""
ELI_EXPRESSION = "eli:LegalExpression"
"""
Entity name for a legal expression (ELI standard).
"""
ELI_FORMAT = "eli:Format"
"""
Entity name for a format embodying a legal expression (ELI standard).
"""
ELI_ENTITIES = [ELIX_ABSTRACT_RESOURCE, ELI_RESOURCE, ELI_EXPRESSION, ELI_FORMAT]
"""
Hierarchical list of the ELI entities (starting with ELIX Abstract Resource).
"""


# Types of legal resources

ACT_RESOURCE = "elix:Act"
"""
URN corresponding to an act described with ELI.
"""
JOURNAL_RESOURCE = "elix:OfficialJournal"
"""
URN corresponding to an official journal described with ELI.
"""
CONSOLIDATION_RESOURCE = "elix:Consolidation"
"""
URN corresponding to a consolidation object described with ELI.
"""


# Properties used to structure the entities

ELIX_RES_TYPE_PROPERTY = "elix:resource_type"
ELIX_LANGS_LIST = "elix:languages_list"
ELIX_FORMATS_LIST = "elix:formats_list"
ELI_LANG_PROPERTY = "eli:language"
ELI_FORMAT_PROPERTY = "eli:format"
ELI_PARENT_PROPERTY = {ELI_RESOURCE: "eli:is_member_of",
                       ELI_EXPRESSION: "eli:realizes",
                       ELI_FORMAT: "eli:embodies"}
ELI_CHILD_PROPERTY = {ELIX_ABSTRACT_RESOURCE: "eli:has_member",
                      ELI_RESOURCE: "eli:is_realized_by",
                      ELI_EXPRESSION: "eli:is_embodied_by"}

# Properties used to define URI Scheme
URI_SCHEME_ENTITY = {
    "elix:abstractLegalResourceUriScheme": ELIX_ABSTRACT_RESOURCE,
    "elix:legalResourceUriScheme": ELI_RESOURCE,
    "elix:legalExpressionUriScheme": ELI_EXPRESSION,
    "elix:formatUriScheme": ELI_FORMAT}
ELIX_URI_PROPERTIES = tuple(URI_SCHEME_ENTITY.keys())

# Type of the data inside the ELI properties

ELI_DATE_PROPERTIES = ("eli:date_document", "eli:date_publication",
                       "eli:date_applicability", "eli:first_date_entry_in_force",
                       "eli:version_date", "eli:date_no_longer_in_force")
ELI_URI_PROPERTIES = ("eli:transposes", "eli:applies", "eli:consolidates",
                      "eli:based_on", "eli:is_another_publication_of",
                      "eli:related_to", "eli:cites", "eli:changes",
                      "eli:commences", "eli:repeals", "eli:corrects",
                      "eli:amends", "eli:is_exemplified_by",
                      "eli:published_in_format", "eli:licence",
                      "eli:is_part_of", "eli:has_part",
                      "eli:is_member_of", "eli:has_member")
ELI_VOCAB_PROPERTIES = ("eli:type_document", "eli:version", "eli:in_force",
                        "eli:is_about", "eli:relevant_for", "eli:juridiction",
                        "eli:passed_by", "eli:responsibility_of_agent",
                        "eli:language", "eli:format", "eli:publisher_agent",
                        "eli:legal_value", "eli:rightsholder_agent",
                        ELIX_LANGS_LIST, ELIX_FORMATS_LIST)
ELI_TEXT_PROPERTIES = ("eli:number", "eli:id_local", "eli:responsibility_of",
                       "eli:published_in", "eli:publisher", "eli:rightsholder",
                       "eli:title", "eli:title_short", "eli:title_alternative",
                       "eli:description", "eli:rights",
                       "elix:abstractLegalResourceUriScheme",
                       "elix:legalResourceUriScheme",
                       "elix:legalExpressionUriScheme",
                       "elix:formatUriScheme")

# Reverse properties

ELI_REVERSE_PROPERTIES = {
    "eli:is_member_of": "eli:has_member",
    "eli:has_member": "eli:is_member_of",
    "eli:is_part_of": "eli:has_part",
    "eli:has_part": "eli:is_part_of",
    "eli:realizes": "eli:is_realized_by",
    "eli:is_realized_by": "eli:realizes",
    "eli:embodies": "eli:is_embodied_by",
    "eli:is_embodied_by": "eli:embodies",
    "eli:changes": "eli:changed_by",
    "eli:based_on": "eli:basis_for",
    "eli:cites": "eli:cited_by",
    "eli:consolidates": "eli:consolidated_by",
    "eli:transposes": "eli:transposed_by",
    "eli:applies": "eli:applied_by",
    "eli:commences": "eli:commenced_by",
    "eli:repeals": "eli:repealed_by",
    "eli:corrects": "eli:corrected_by",
    "eli:amends": "eli:amended_by",
    "eli:is_another_publication_of": "eli:has_another_publication",
    "eli:published_in_format": "eli:publishes",
}


# Suffixes used to build the PROV entities from the LegalResource URI
# (PROV is used to indicate which user has created a notice).

PROV_ENTITY_URI_SUFFIX = "/prov/createEntity"
PROV_ACTIVITY_URI_SUFFIX = PROV_ENTITY_URI_SUFFIX + "/activity"
PROV_ASSOCIATION_URI_SUFFIX = PROV_ENTITY_URI_SUFFIX + "/association"


# PROVX Roles (extending PROV)

PROVX_ROLE_CREATOR = "provx:Role-creator"


# Functions for handling namespaces, prefixes and qualified predicates

def ELIGraph():
    graph = rdflib.Graph()
    graph.bind("eli", ELI)
    graph.bind("elix", ELIX)
    graph.bind("skos", SKOS)
    graph.bind("dc", DC)
    graph.bind("dct", DCTERMS)
    graph.bind("prov", PROV)
    graph.bind("provx", PROVX)
    return graph

prefixes = {
    str(RDF): RDF,
    "rdf": RDF,
    str(RDFS): RDFS,
    "rdfs": RDFS,
    str(OWL): OWL,
    "owl": OWL,
    str(SKOS): SKOS,
    "skos": SKOS,
    str(DC): DC,
    "dc": DC,
    str(DCTERMS): DCTERMS,
    "dct": DCTERMS,
    str(ELI): ELI,
    "eli": ELI,
    str(ELIX): ELIX,
    "elix": ELIX,
    str(PROV): PROV,
    "prov": PROV,
    str(PROVX): PROVX,
    "provx": PROVX,
}

inv_prefixes = {
    str(RDF): "rdf",
    str(RDFS): "rdfs",
    str(OWL): "owl",
    str(SKOS): "skos",
    str(DC): "dc",
    str(DCTERMS): "dct",
    str(ELI): "eli",
    str(ELIX): "elix",
    str(PROV): "prov",
    str(PROVX): "provx",
}

def parse_uri(uri, prf=None):
    prefix, fragment = uri.split(":")
    if prefix in prefixes:
        return prefixes[prefix][fragment]
    elif prf and prefix in prf:
        return prf[prefix][fragment]
    else:
        return rdflib.URIRef(uri)

def parse_predicate(uri, prf=None):
    if "@" in uri:
        pred, lang = uri.split("@")
    else:
        pred, lang = uri, None
    return parse_uri(pred, prf), lang

def compact_uri(pred, obj=None):
    lang = ""
    if isinstance(obj, rdflib.term.Literal) and obj.language:
        lang = "@" + obj.language
    for ns, pref in inv_prefixes.items():
        if pred.startswith(ns):
            pred = pred.replace(ns, pref+":")
            break
    return pred+lang

_NSM = rdflib.namespace.NamespaceManager(rdflib.Graph())
_NSM.bind("eli", str(ELI))
_NSM.bind("elix", str(ELIX))
_NSM.bind("prov", str(PROV))
_NSM.bind("provx", str(PROVX))

def parse_compact_uri(uri):
    return rdflib.util.from_n3(uri, nsm=_NSM)

def uri2filename(uri):
    return uri.replace(':','').replace('/','_').replace('#','_')
