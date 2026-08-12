# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import os, shutil
import os.path as osp
import datetime as dtm
import functools
import logging
from traceback import format_exc
from lxml import etree
from lxml.html import builder as H
from rdflib import URIRef, Literal
from rdflib.namespace import RDF, SKOS, XSD, FOAF

from .errors import ConversionError, IncorrectResource, ELIError
from .xslt_transform import eli_to_html, WHOLE_PAGE
from .eligraph import (
    ELIX_ABSTRACT_RESOURCE, ELI_RESOURCE, ELI_EXPRESSION, ELI_FORMAT,
    ELI_PARENT_PROPERTY, ELI_LANG_PROPERTY, ELI_FORMAT_PROPERTY,
    ELIX_RES_TYPE_PROPERTY, ELI_CHILD_PROPERTY, ELI_REVERSE_PROPERTIES,
    ELIX_LANGS_LIST, ELIX_FORMATS_LIST, PROVX_ROLE_CREATOR, ELIX_URI_PROPERTIES)
from .eligraph import (parse_uri, ELIGraph, compact_uri, PROV,
                       PROV_ENTITY_URI_SUFFIX, PROV_ACTIVITY_URI_SUFFIX,
                       PROV_ASSOCIATION_URI_SUFFIX)
from .form_values import ELIFormValues
from .form_configs import FormConfigIndex, URIValue, ELIFormConfig
from .vocabs import VocabularyIndex, VocabValue

TYPE_PROPERTY = "rdf:type"
EXPRESSIONS_SUBDIR = "legal-expressions"
FORMATS_SUBDIR = "formats"


# form2eli #####################################################################

def form2eli(form_data, fconfig_index, vocab_index, user_uri, now=None):
    """
    Transforms the data read from the JSON form into an ELI RDF graph.
    """
    assert isinstance(fconfig_index, FormConfigIndex), type(fconfig_index)
    assert isinstance(vocab_index, VocabularyIndex), type(vocab_index)
    # Loads values from form
    raw_values = ELIFormValues.load_from_json(form_data)
    # Gets form config corresponding to the resource type
    obj_types = raw_values.get((ELIX_RES_TYPE_PROPERTY,))
    if obj_types is None or len(obj_types) == 0:
        msg = "No legal resource type defined in form data"
        raise IncorrectResource("incorrectFormValues", msg)
    else:
        obj_type = obj_types[0]
    form_config = fconfig_index.load(obj_type, vocab_index, raw_values)
    # Reads form values thanks to the config
    values = form_config.read_form_values(raw_values)
    # Inferes ELI entities from the values
    inf_entities = values.extract_eli_entities()
    # Builds URIs for each entity
    uris = build_uris_for_entities(inf_entities, form_config, values)
    # Gets the properties associated to each entity URI
    eli_entities = collect_entities_properties(uris, values)
    # Builds the RDF graph for all the entities (URIs and properties)
    graph = entities2eli_graph(eli_entities)
    # Finally adds the creator (user) to the graph
    add_creator_to_eli_graph(graph, user_uri, now)
    root_uri = ensure_single_legal_resource(graph)
    return root_uri, graph


def build_uris_for_entities(entities_desc, form_config, values):
    """
    Builds the URIs of the entities described in ``entities_desc``
    thanks to the data in ``values``

    ``entities_desc`` is a dictionary of entity types (legal resource,
    legal expression, etc.) giving the URIs of the language and format
    associated to the entity (both can be ``None`` if they are not relevant
    for this entity type). This corresponds to the output of
    ``ELIFormValues.extract_eli_entities`` method.

    Example: ``{ELI_RESOURCE: {(None, None)}, ELI_EXPRESSION: {(ENG, None),
    (FRA, None)}, ELI_FORMAT: {(ENG, PDF), (ENG, PRINT), (FRA, PDF)}}``

    ``form_config`` is an ELIFormConfig object.

    ``values`` is an ELIFormValues object containing values read thanks to
    the form configuration.

    Returns a dictionary giving for each entity type (legal resource,
    legal expression, etc.) a dictionary whose keys are the the URIs of the
    language and format and whose values are the associated entity URI.

    Example: ``{ELI_RESOURCE: {(None, None): "http//example/2017"},
    ELI_EXPRESSION: {(ENG, None): "http://example/2017/EN",
    (FRA, None): "http://example/2017/FR"}, ELI_FORMAT: {(ENG, PDF):
    "http://example/2017/EN/pdf", (ENG, PRINT): "http://example/2017/EN/print",
    (FRA, PDF): "http://example/FR/pdf}}``

    """
    assert isinstance(values, ELIFormValues), type(values)
    uris = {}
    for entity_type, lang_frmt_uris in entities_desc.items():
        uri_sch = form_config.uri_schemes.get(entity_type)
        if uri_sch is None:
            msg = ("No URI scheme defined for ELI entity:\n{0}"
                   "").format(entity_type)
            raise IncorrectResource("incorrectFormValues", msg)
        if entity_type not in uris:
            uris[entity_type] = {}
        for lang_uri, frmt_uri in lang_frmt_uris:
            uris[entity_type][(lang_uri, frmt_uri)] = \
                                uri_sch.build_uri(values, lang_uri, frmt_uri)
    return uris


def collect_entities_properties(uris, values):
    """
    For each entity whose URI is given in ``uris``, collects the ELI properties
    that describes it from the data in ``values``.

    ``uris`` is a dictionary giving for each entity type (legal resource,
    legal expression, etc.) a dictionary whose keys are the the URIs of the
    language and format and whose values are the associated entity URI. This
    corresponds to the output of ``build_uris_for_entities`` function.

    Example: ``{ELI_RESOURCE: {(None, None): "http//example/2017"},
    ELI_EXPRESSION: {(ENG, None): "http://example/2017/EN",
    (FRA, None): "http://example/2017/FR"}, ELI_FORMAT: {(ENG, PDF):
    "http://example/2017/EN/pdf", (ENG, PRINT): "http://example/2017/EN/print",
    (FRA, PDF): "http://example/FR/pdf}}``

    ``values`` is an ELIFormValues object containing values read thanks to
    the form configuration.
    """
    assert isinstance(values, ELIFormValues), type(values)
    props = {}
    for entity_type, type_uris in uris.items():
        if entity_type == ELIX_ABSTRACT_RESOURCE:
            continue
        for (lang_uri, frmt_uri), entity_uri in type_uris.items():
            # Collects properties for this entity from form values
            props[entity_uri] = \
                    values.get_context_properties(lang_uri, frmt_uri)
            # Adds type property
            props[entity_uri][TYPE_PROPERTY] = [parse_uri(entity_type)]
            # Adds parent property
            if entity_type == ELI_FORMAT:
                parent_uri = URIValue(uris[ELI_EXPRESSION][(lang_uri, None)])
            elif entity_type == ELI_EXPRESSION:
                parent_uri = URIValue(uris[ELI_RESOURCE][(None, None)])
            elif entity_type == ELI_RESOURCE:
                parent_uri = URIValue(uris[ELIX_ABSTRACT_RESOURCE][(None,None)])
            props[entity_uri][ELI_PARENT_PROPERTY[entity_type]] = [parent_uri]
    return props


def entities2eli_graph(entities):
    """
    Builds a RDF graph from the given entities (URIs and properties).

    ``entities`` is a dictionary associating to each entity URI a dictionary
    of its properties (name of property / list of property values). It
    corresponds to the output of ``collect_entities_properties`` function.

    Returns the RDF graph fully describing the ELI entities.
    """
    graph = ELIGraph()
    values_to_desc = set()
    used_lang_codes = set()
    for entity_uri, entity_props in entities.items():
        # Gets current entity language code (if any)
        if ELI_LANG_PROPERTY in entity_props \
           and entity_props[ELI_LANG_PROPERTY][0].notation is not None:
            lang_code = entity_props[ELI_LANG_PROPERTY][0].notation.lower()
            used_lang_codes.add(lang_code)
        # Builds the URI of the current entity
        rdf_uri = URIRef(entity_uri)
        # Adds in the graph the various predicates corresponding to the
        # properties
        for name, values in entity_props.items():
            if name in (*ELIX_URI_PROPERTIES, ELIX_LANGS_LIST,
                        ELIX_FORMATS_LIST):
                continue
            if name == ELIX_RES_TYPE_PROPERTY:
                res_type = values[0]
                if not isinstance(res_type, URIRef):
                    values = [parse_uri(res_type)]
            rdf_pred = parse_uri(name)
            for val in values:
                if isinstance(val, dtm.date):
                    rdf_val = Literal(val.strftime("%Y-%m-%d"),
                                      datatype=XSD.date)
                elif isinstance(val, URIValue):
                    rdf_val = URIRef(val)
                elif isinstance(val, VocabValue):
                    values_to_desc.add(val)
                    rdf_val = URIRef(val.uri)
                elif isinstance(val, URIRef):
                    rdf_val = val
                else:
                    rdf_val = Literal(val, datatype=XSD.string)
                graph.add((rdf_uri, rdf_pred, rdf_val))
    # Adds in the graph the description of the used vocabulary values
    for vocab_val in values_to_desc:
        rdf_uri = URIRef(vocab_val.uri)
        graph.add(
            (rdf_uri, RDF.type, SKOS.Concept))
        graph.add(
            (rdf_uri, SKOS.inScheme, URIRef(vocab_val.vocabulary.uri)))
        for lang_code, label in vocab_val.labels.items():
            if lang_code is not None and lang_code not in used_lang_codes:
                continue
            graph.add(
                (rdf_uri, SKOS.prefLabel, Literal(label, lang=lang_code)))
        if vocab_val.notation is not None:
            graph.add(
                (rdf_uri, SKOS.notation, Literal(vocab_val.notation,
                                                 datatype=XSD.string)))
    return graph


def add_creator_to_eli_graph(rdf_graph, user_uri, now=None):
    """
    Adds to the ELI RDF graph the user that edited and saved the form (ie the
    user logged in the application).

    The creator is described thanks to PROV properties.
    """
    if user_uri is None:
        # Nothing to do
        return rdf_graph
    if now is None:
        now = dtm.datetime.utcnow()
    res_uri = ensure_single_legal_resource(rdf_graph)
    # Removes existing prov properties
    for rdf_typ in (PROV.Entity, PROV.Activity, PROV.Association, PROV.Agent):
        for subj in set(rdf_graph.subjects(RDF.type, rdf_typ)):
            rdf_graph.remove( (subj, None, None) )
    # Adds creator with prov properties
    base_uri = res_uri
    while len(base_uri) > 0 and base_uri[-1] in ("/", "#"):
        base_uri = base_uri[:-1]
    ent_uri = URIRef(base_uri + PROV_ENTITY_URI_SUFFIX)
    act_uri = URIRef(base_uri + PROV_ACTIVITY_URI_SUFFIX)
    asso_uri = URIRef(base_uri + PROV_ASSOCIATION_URI_SUFFIX)
    user_uri = URIRef(user_uri)
    # PROV entity
    rdf_graph.add( (ent_uri, RDF.type, PROV.Entity) )
    rdf_graph.add( (ent_uri, FOAF.primaryTopic, URIRef(res_uri)) )
    tim = now.isoformat() + "Z"
    rdf_graph.add( (ent_uri, PROV.generatedAtTime,
                    Literal(tim, datatype=XSD.dateTime)) )
    rdf_graph.add( (ent_uri, PROV.wasGeneratedBy, act_uri) )
    rdf_graph.add( (ent_uri, PROV.wasAttributedTo, user_uri) )
    # PROV Activity
    rdf_graph.add( (act_uri, RDF.type, PROV.Activity) )
    rdf_graph.add( (act_uri, RDF.type, PROV.Create) )
    rdf_graph.add( (act_uri, PROV.wasAssociatedWith, user_uri) )
    rdf_graph.add( (act_uri, PROV.qualifiedAssociation, asso_uri) )
    # PROV Association
    rdf_graph.add( (asso_uri, RDF.type, PROV.Association) )
    rdf_graph.add( (asso_uri, PROV.hadRole, parse_uri(PROVX_ROLE_CREATOR)) )
    rdf_graph.add( (asso_uri, PROV.agent, user_uri) )
    # PROV Agent
    rdf_graph.add( (user_uri, RDF.type, PROV.Agent) )
    # returns graph after properties insertion
    return rdf_graph


# eli2form #####################################################################

def eli2form(rdf_graph, resource_type, fconfig_index, vocab_index):
    """
    Extracts the JSON form data from the ``rdf_graph`` and builds an
    ELIFormValues object.

    ``resource_type`` is the type of legal resource (act, journal,
    consolidation) and is necessary to read the correct form configuration
    in ``fconfig_index``. If the ``rdf_graph`` contains the type of legal
    resource, it is ignored.
    """
    assert isinstance(fconfig_index, FormConfigIndex), type(fconfig_index)
    assert isinstance(vocab_index, VocabularyIndex), type(vocab_index)
    # Loads the form configuration and the default values for the given resource
    # type.
    form_config = fconfig_index.load(resource_type, vocab_index)
    raw_form_values = fconfig_index.load_default_values(
        resource_type, recover_from_exceptions=True)
    form_values = form_config.read_form_values(raw_form_values,
                                               check_mandatory=False)
    # Finds URI of LegalResource (raises exception if there is none or several)
    res_uri = ensure_single_legal_resource(rdf_graph)
    # Reads the properties of LegalResource and stores them in form_values
    collect_graph_properties(rdf_graph, res_uri, form_config, form_values)
    # Loops on the URIs of LegalExpressions
    for expr_uri in set(get_rdf_property_values(rdf_graph, res_uri,
                                             ELI_CHILD_PROPERTY[ELI_RESOURCE])):
        # Reads the lang URI
        try:
            lang_uri = get_rdf_property_values(rdf_graph, expr_uri,
                                               ELI_LANG_PROPERTY)[0]
        except IndexError as exc:
            msg = ("The language of {0} Legal Expression is not specified with "
                   "the eli:language property").format(expr_uri)
            raise ConversionError("incorrectEliGraph", msg)
        # Reads the properties of LegalExpression and stores them in form_values
        collect_graph_properties(rdf_graph, expr_uri, form_config, form_values,
                                 lang=lang_uri)
        # Loops on the URIs of Formats
        for frm_uri in set(get_rdf_property_values(rdf_graph, expr_uri,
                                        ELI_CHILD_PROPERTY[ELI_EXPRESSION])):
            # Reads the format URI
            try:
                format_uri = get_rdf_property_values(rdf_graph, frm_uri,
                                                     ELI_FORMAT_PROPERTY)[0]
            except IndexError as exc:
                msg = ("The format of {0} Format is not specified with "
                       "the eli:format property").format(frm_uri)
                raise ConversionError("incorrectEliGraph", msg)
            # Reads the properties of Format and stores them in form_values
            collect_graph_properties(rdf_graph, frm_uri,
                                     form_config, form_values,
                                     lang=lang_uri, frmt=format_uri)
    return res_uri, form_values


def define_resource_type(graph, res_type):
    """
    Adds a property in RDF graph to define the legal resource type of the
    LegalResource thanks to elix:resource_type property.
    """
    res_uri = URIRef(ensure_single_legal_resource(graph))
    legal_type_prop = parse_uri(ELIX_RES_TYPE_PROPERTY)
    # Removes previous legal resource type from the graph
    graph.remove( (res_uri, legal_type_prop, None) )
    # Adds new legal resource type in the graph
    graph.add( (res_uri, legal_type_prop, parse_uri(res_type)) )


def ensure_single_legal_resource(graph):
    """
    Extracts from an RDF graph the URIs of the ELI Legal Resources
    (``eli:LegalResource``) that are not abstract (i.e. that don't
    have any member).

    Raises an exception if there are more than one URI of ELI Legal
    Resource or if there is none.

    Returns the URI as a string.
    """
    legal_resources = []
    for subj in graph.subjects(RDF.type, parse_uri(ELI_RESOURCE)):
        derived_resources = get_rdf_property_values(
            graph, subj, ELI_CHILD_PROPERTY[ELIX_ABSTRACT_RESOURCE])
        if len(derived_resources) == 0:
            legal_resources.append(str(subj))
    if len(legal_resources) != 1:
        msg = ("RDF graph should only contain one single eli:LegalResource "
               "that is not abstract, but {0} were found"
               "").format(len(legal_resources))
        raise ConversionError("incorrectEliGraph", msg)
    return legal_resources[0]


def get_rdf_property_values(rdf_graph, entity_uri, prop_name):
    """
    Inside the ``rdf_graph``, gets the values of the property
    ``prop_name`` of the entity whose URI is ``entity_uri``.

    If the property admits a reverse one, also uses this reverse
    property to collect the values.

    All the values are returned as strings.
    """
    predicate = parse_uri(prop_name)
    if not isinstance(entity_uri, URIRef):
        entity_uri = URIRef(entity_uri)
    vals = [str(val) for val in rdf_graph.objects(entity_uri, predicate)]
    reverse_prop_name = ELI_REVERSE_PROPERTIES.get(prop_name)
    if reverse_prop_name is not None:
        rev_predicate = parse_uri(reverse_prop_name)
        vals.extend([str(val)
                     for val in rdf_graph.subjects(rev_predicate, entity_uri)])
    return vals


def collect_graph_properties(rdf_graph, entity_uri, form_config,
                             form_values=None, lang=None, frmt=None):
    """
    Collects in the ``rdf_graph`` the properties of the entity whose URI is
    ``entity_uri``, and that are described and enabled in ``form_config``
    configuration. The properties values are stored into ``form_values`` (a
    new object is built if not provided).

   ``fconfig_index`` is the form configuration of the entity whose properties
    must be read. It contains the description of the properties and if they are
    enabled or not. Only the enabled properties will be read. If the property
    values are taken from a vocabulary, the values read in the graph that are
    not in the vocabulary specified in the configuration are ignored.

    ``form_values`` is an ELIFormValues object where the properties values are
    stored. If not provided, a new object is built and returned.
    Please be aware that this object must contain values read thanks to the
    configuration and not raw (string) values. cf. ``read_form_values`` method
    of ELIFormConfig.

    ``lang`` is the URI of the language associated with the entity whose
    properties must be read (``LegalExpression`` or ``Format``). Will be
    ``None`` for the  entities not associated with a given language
    (``LegalResource``).

    ``format`` is the URI of the format associated with the entity whose
    properties must be read (``Format``). Will be ``None`` for the entities
    not associated with a given format (``LegalResource`` or
    ``LegalExpression``).
    """
    assert isinstance(form_config, ELIFormConfig), type(form_config)
    assert form_values is None or isinstance(form_values, ELIFormValues), \
        type(form_values)
    if form_values is None:
        form_values = ELIFormValues()
    # Loops on the property configs corresponding to the context of the chosen
    # entity.
    sel_props = form_config.get_context_configs(lang=lang, frmt=frmt)
    for local_name, prop_config in sel_props.items():
        # Builds the property full name.
        if lang is None and frmt is None:
            prop_name = (local_name,)
        elif frmt is None:
            prop_name = (lang, local_name)
        else:
            prop_name = (lang, frmt, local_name)
        # If the property is not enabled, erases values in form_values and goes
        # to next property.
        if not prop_config.enabled:
            if prop_name in form_values:
                form_values.pop(prop_name)
            continue
        # Gets the values in form_values corresponding to the property (adds
        # entry if it doesn't exist).
        vals = form_values.get(prop_name)
        if vals is None:
            vals = []
            form_values[prop_name] = vals
        # Reads values of the property from the RDF graph.
        graph_vals = get_rdf_property_values(rdf_graph, entity_uri, local_name)
        read_vals = []
        for raw_val in graph_vals:
            try:
                read_vals.append(prop_config.read_value(raw_val))
            except ELIError as exc:
                logging.warning(
                    "Found in RDF graph a value that is not compatible with "
                    "the configuration of {0} property. Skipping it:\n{1}\n"
                    "Exception:\n{2}".format(" / ".join(prop_name), raw_val,
                                             format_exc()))
        # Stores read values in form_values and ensures constraints are met.
        if not prop_config.multiple and len(vals) > 0 and len(read_vals) > 0:
            vals.clear() # Erases previous (default) value
        for val in read_vals:
            if val not in vals:
                vals.append(val)
        if not prop_config.multiple and len(vals) > 1:
            deleted = []
            while len(vals) > 1:
                deleted.append(vals.pop())
            logging.warning(
                "Read in RDF graph multiple values for {0} property whose "
                "configuration only admits one. Only keeping first value and "
                "erasing following values:\n{1}."
                "".format(" / ".join(prop_name), "\n".join(deleted)))
    return form_values


# eli2html #####################################################################

def eli2html(filepath, output_dirname, localizations_dirname, index_lang="en",
             html_rendering=WHOLE_PAGE):
    expr_pages = {}
    frmt_pages = {}
    # Deletes previous results
    try:
        shutil.rmtree(osp.join(output_dirname))
    except FileNotFoundError as exc:
        pass
    os.makedirs(osp.join(output_dirname), exist_ok=True)
    # Transforms at expression level
    index, results, log = eli_to_html(
        filepath, localizations_dirname, output_level="expression",
        index_lang=index_lang, html_rendering=html_rendering)
    if log:
        logging.warning(log)
    if len(results) == 0:
        logging.warning(
            "ELI notice doesn't contain the description of any "
            "LegalExpression. Can't produce the HTML files describing the "
            "expressions.")
    else:
        # Saves the expression files in a subdir of output_dirname
        os.makedirs(osp.join(output_dirname, EXPRESSIONS_SUBDIR), exist_ok=True)
        filenames = build_filenames_from_uris(list(results.keys()))
        for expr_uri, result in results.items():
            if expr_uri == "index":
                continue
            fname = osp.join(EXPRESSIONS_SUBDIR, filenames[expr_uri])
            with open(osp.join(output_dirname, fname), "wb") as out:
                out.write(etree.tostring(result, method="html",
                                         encoding="utf-8"))
            expr_pages[expr_uri] = fname
    # Transforms at format level
    index, results, log = eli_to_html(filepath, localizations_dirname,
                                      output_level="format",
                                      index_lang=index_lang)
    if log:
        logging.warn(log)
    if len(results) == 0:
        logging.warning(
            "ELI notice doesn't contain the description of any Format. "
            "Can't produce the HTML files describing the formats.")
    else:
        # Saves the format files in a subdir of output_dirname
        os.makedirs(osp.join(output_dirname, FORMATS_SUBDIR), exist_ok=True)
        filenames = build_filenames_from_uris(list(results.keys()))
        for frmt_uri, result in results.items():
            if frmt_uri == "index":
                continue
            fname = osp.join(FORMATS_SUBDIR, filenames[frmt_uri])
            with open(osp.join(output_dirname, fname), "wb") as out:
                out.write(etree.tostring(result, method="html",
                                         encoding="utf-8"))
            frmt_pages[frmt_uri] = fname
    # Builds a unique index page with links towards all the expressions and
    # formats HTML pages
    if index is None:
        index = H.HTML(H.BODY(H.UL(id="legal-expressions"),
                              H.UL(id="formats")))
    for expr_ul in index.xpath(".//ul[@id='legal-expressions']"):
        for uri,fname in sorted(expr_pages.items()):
            expr_ul.append(H.LI(H.A(uri, href=fname)))
    for frmt_ul in sorted(index.xpath(".//ul[@id='formats']")):
        for uri,fname in frmt_pages.items():
            frmt_ul.append(H.LI(H.A(uri, href=fname)))
    with open(osp.join(output_dirname, "index.html"), "wb") as out:
        out.write(etree.tostring(index, method="html", encoding="utf-8"))


def build_filenames_from_uris(uris_list, extension=".html"):
    base_uri = _get_base_uri(uris_list)
    name = lambda uri: uri[len(base_uri):].replace("/", "_").replace("#", "_")
    return {uri: "{0}{1}".format(name(uri), extension) for uri in uris_list}

def _get_base_uri(uris_list):
    common_str = functools.reduce(_get_common_part, uris_list)
    return common_str[:max(common_str.rfind("/"), common_str.rfind("#"))+1]

def _get_common_part(string1, string2):
    commons = []
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            break
        commons.append(char1)
    return "".join(commons)


# main #########################################################################

if __name__ == '__main__':
    import sys, json
    def usage():
        print('usage: {} form2eli <inputfile> <outputfile> <formconfig_dir> <vocab_dir>'.
              format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    if len(sys.argv) == 6 and sys.argv[1] == 'form2eli':
        inp, out, form, vocab = sys.argv[2:]
        with open(inp, encoding='utf-8') as fp:
            data = json.load(fp)
        rooturi, graph = form2eli(data, FormConfigIndex(form), VocabularyIndex(vocab))
        ext = os.path.splitext(out)[1][1:]
        fmt = {'rdf':'xml', 'xml':'xml', 'ttl': 'turtle'}[ext]
        with open(out, 'wb') as fp:
            fp.write(graph.serialize(format=fmt).encode('utf-8'))
    else:
        usage()

