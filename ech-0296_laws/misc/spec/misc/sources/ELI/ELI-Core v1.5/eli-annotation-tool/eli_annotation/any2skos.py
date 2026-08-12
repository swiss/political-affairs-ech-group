# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import os, string
import os.path as osp
import datetime, csv, logging, shutil
import logging
from lxml import etree
from lxml.html import builder as H
from collections import defaultdict

import rdflib
from rdflib.namespace import RDF, SKOS, DCTERMS
from rdflib.term import URIRef, Literal
import openpyxl as pxl

from .eligraph import parse_uri, parse_predicate, compact_uri
from .xslt_transform import (skos_to_html, build_xml_glossary, skos_index,
                             WHOLE_PAGE)
from .errors import ConversionError, ConversionWarnings


STANDARD_VOCABS_DIR = osp.join(osp.abspath(osp.dirname(__file__)),
                               "standard_files")

def read_excel_cells(cells):
    values = []
    for cell in cells:
        if cell.value is None:
            value = ""
        elif isinstance(cell.value, datetime.datetime):
            value = cell.value.strftime("%Y-%m-%d")
        else:
            value = str(cell.value)
        value = value.strip()
        if value.startswith('=HYPERLINK'):
            value = value.split('"')[-2]
            value = value.strip()
        values.append(value)
    return values


def is_conceptscheme(txt):
    return set(txt.lower().split()).issuperset({'uri', 'conceptscheme'})
def is_concept(txt):
    return set(txt.lower().split()).issuperset({'uri', 'concept'})

def xl2skos(excelfile, valid_properties):
    result = {}
    warnings = []
    book = pxl.load_workbook(excelfile)
    for sheet in book.worksheets:
        a1_val = read_excel_cells( (sheet['A1'],) )[0]
        if is_conceptscheme(a1_val):
            try:
                uri, (graph, wrn) = xlworksheet2skos(sheet, valid_properties)
                result[uri] = graph
                if len(wrn) > 0:
                    warnings.append(wrn)
            except ConversionError as exc:
                exc.context = sheet.title
                warnings.append(exc)
        else:
            wrn = ConversionWarnings("ignoredWorksheet", sheet.title)
            wrn.log("Could not find the header describing the ConceptScheme. "
                    "The first cell (cell A1) doesn't contain the words "
                    "\"ConceptScheme URI\". Read the specification for "
                    "details.")
            warnings.append(wrn)
    return result, warnings

def xlworksheet2skos(worksheet, valid_properties):
    warnings = ConversionWarnings("errorsInWorksheet", worksheet.title)
    # detect separation header / data
    for idx, value in enumerate(read_excel_cells(list(worksheet.columns)[0])):
        if value and is_concept(value):
            body_line_idx = idx
            break
    else:
        msg = ("Could not find the body describing the concepts. Do you have a "
               "cell containing the words \"URI Concept\" is the first column "
               "(column A)? Please read the specification for details.")
        raise ConversionError("malformedExcelWorksheet", msg)
    # Reads Concept Scheme URI
    rows = list(worksheet.iter_rows())
    first_row = read_excel_cells(rows[0])
    if not is_conceptscheme(first_row[0]):
        msg = ("Could not find the header describing the ConceptScheme. Does "
               "the first cell (cell A1) contain the words "
               "\"ConceptScheme URI\"? Please read the specification for "
               "details.")
        raise ConversionError("malformedExcelWorksheet", msg)
    try:
        cs_uri = _build_rdf_uri(first_row[1])
    except ValueError:
        msg = ("The URI of the ConceptScheme is not a valid URI: {}"
               "".format(first_row[1]))
        raise ConversionError("malformedExcelWorksheet", msg)
    # Reads header (properties of Concept Scheme)
    prefixes = {}
    raw_header = defaultdict(list)
    for row in rows[1:body_line_idx]:
        items = read_excel_cells(row)
        if items[0] == "":
            continue
        if items[0].startswith('prefix:'):
            prefixes[items[0][7:].strip()] = rdflib.Namespace(items[1])
        elif items[1] != "":
            raw_header[items[0]].append(items[1])
    # Converts property names in header to URIs
    header = defaultdict(list)
    for line_name, vals in raw_header.items():
        try:
            key = _parse_prop_name(line_name, prefixes, valid_properties)
            sep = key[2]
            values = []
            if sep is not None:
                for val in vals:
                    values.extend(val.split(sep))
            else:
                values = vals
            header[key].extend(values)
        except Exception as exc:
            warnings.log("Inside the header (properties of ConceptScheme), "
                         "ignoring the line \"{0}\" because of: {1}"
                         "".format(line_name, str(exc)))
    # Reads first line of body (name of properties of Concepts)
    col_names = []
    for col_name in read_excel_cells(rows[body_line_idx]):
        if col_name == "":
            key = None
        elif is_concept(col_name):
            key = ('URI', None, None)
        else:
            try:
                key = _parse_prop_name(col_name, prefixes, valid_properties)
            except Exception as exc:
                warnings.log("Inside the body (table of Concepts), ignoring "
                             "the column \"{0}\" because of: {1}"
                             "".format(col_name, str(exc)))
                key = None
        col_names.append(key)
    # Reads data (Concepts and their properties)
    data = []
    for row in rows[body_line_idx+1:]:
        values = read_excel_cells(row)
        # Skips empty lines or lines without a Concept URI
        if len(values) == 0 or values[0] == "":
            continue
        row_data = defaultdict(list)
        for (key, val) in zip(col_names, values):
            if key is None or val == "":
                continue
            sep = key[2]
            if sep is not None:
                values = val.split(sep)
            else:
                values = [val]
            row_data[key].extend(values)
        data.append(row_data)
    # Converts header to rdf graph
    g = rdflib.Graph()
    g.bind('skos', SKOS)
    g.bind('dct', DCTERMS)
    g.add( (cs_uri, RDF.type, SKOS.ConceptScheme) )
    for (prop_uri, lang, separator), vals in header.items():
        for val in vals:
            obj = _build_rdf_value(val, lang)
            g.add( (cs_uri, prop_uri, obj) )
    # Converts data to rdf graph
    for row_data in data:
        uris = row_data.pop( ("URI", None, None) )
        if len(uris) == 0:
            continue
        try:
            uri = _build_rdf_uri(uris[0])
        except ValueError:
            warnings.log(
                "The URI of a Concept doesn't seem to be a valid URI; this "
                "Concept will be skipped: {}".format(uris[0]))
        g.add( (uri, RDF.type, SKOS.Concept) )
        g.add( (uri, SKOS.inScheme, cs_uri) )
        for (prop_uri, lang, _), vals in row_data.items():
            for val in vals:
                obj = _build_rdf_value(val, lang)
                g.add( (uri, prop_uri, obj) )
    return str(cs_uri), (g, warnings)

def _parse_prop_name(name, prefixes, valid_props):
    raw_name = name
    if ":" not in name:
        raise ValueError(
            "Property name doesn't follow the expected form "
            "<prefix>:<name>@<lang>[<option>=<value>]: {}".format(raw_name))
    separator = None
    if "[" in name:
        name, *option = name.split("[")
        option = "[".join(option)
        if "]" not in option:
            raise ValueError(
                "Property name doesn't follow the expected form "
                "<prefix>:<name>@<lang>[<option>=<value>]: {}".format(raw_name))
        option = option[:option.rfind("]")]
        try:
            opt_name, opt_value = option.split("=")
            opt_name = opt_name.strip()
            opt_value = opt_value.strip()
        except ValueError:
            raise ValueError(
                "Property name doesn't follow the expected form "
                "<prefix>:<name>@<lang>[<option>=<value>]: {}".format(raw_name))
        if opt_name != "separator":
            raise ValueError(
                "Property name follows the expected form "
                "<prefix>:<name>@<lang>[<option>=<value>] but the only "
                "existing option is separator: {}".format(raw_name))
        if opt_value in ('""', "''"):
            separator = None
        else:
            if len(opt_value) < 3 \
               or ((opt_value[0] != "'" or opt_value[-1] != "'") \
                   and (opt_value[0] != '"' or opt_value[-1] != '"')):
                raise ValueError(
                    "Property name follows the expected form "
                    "<prefix>:<name>@<lang>[<option>=<value>] but the value "
                    "should be between simple or double quotes (e.g. "
                    "\";\"): {}".format(raw_name))
            separator = opt_value[1:-1]
    name = name.strip()
    prefix = name.split(":")[0]
    pred, lang = parse_predicate(name, prefixes)
    if prefix not in prefixes and pred not in valid_props:
        raise ValueError(
            "Invalid property not in SKOS or DCT standards and not "
            "in the declared prefixes: {}".format(str(pred)))
    if lang is not None:
        lang = lang.strip()
        if len(lang) != 2 \
           or (lang[0] not in string.ascii_letters \
               and lang[1] not in  string.ascii_letters):
            raise ValueError(
                "Property name follows the expected form "
                "<prefix>:<name>@<lang>[<option>=<value>] but the lang "
                "value is not a two-letters code")
    try:
        pred.n3()
    except Exception:
        raise ValueError(
            "URI of property built from {0} is not a valid URI: {1}"
            "".format(name, str(pred)))
    return pred, lang, separator

def _build_rdf_uri(str_uri):
    uri = URIRef(str_uri)
    try:
        uri.n3()
    except Exception:
        raise ValueError("URI built from {0} is not a valid URI: {1}"
                         "".format(str_uri, str(uri)))
    return uri

def _build_rdf_value(str_value, lang):
    if str_value.startswith('http://') or str_value.startswith("urn:"):
        try:
            val = _build_rdf_uri(str_value)
        except ValueError:
            val = Literal(str_value, lang=lang)
    else:
        val = Literal(str_value, lang=lang)
    return val

# in/out

def get_skos_properties():
    skos = rdflib.Graph()
    with open(osp.join(STANDARD_VOCABS_DIR, "skos.owl")) as fp:
        skos.parse(fp, format='xml')
    skos_properties = set(skos.subjects(RDF.type, RDF.Property))
    return skos_properties

def get_dcmi_properties():
    dcmi = rdflib.Graph()
    with open(osp.join(STANDARD_VOCABS_DIR, "dcmi.ttl")) as fp:
        dcmi.parse(fp, format='turtle')
    dcmi_properties = set(dcmi.subjects(RDF.type, RDF.Property))
    return dcmi_properties

FORMATS = {'.rdf': 'xml', '.ttl': 'turtle'}

def xl2rdf(filepath, outpath):
    skos_properties = get_skos_properties()
    dcmi_properties = get_dcmi_properties()
    fmt = FORMATS.get(osp.splitext(outpath)[1], 'xml')
    with open(filepath,'rb') as workbook:
        result, warns = xl2skos(workbook, skos_properties | dcmi_properties)
    for wrn in warns:
        print(str(wrn))
    for title, graph in result.items():
        title = title.replace(':','').replace('/','_').replace('#','_')
        outfile, ext = osp.splitext(outpath)
        outfile = outfile+'-'+title+ext
        with open(outfile,'wb') as out:
            out.write(graph.serialize(format=fmt).encode('utf-8'))

def skos2csv(filepath, outpath):
    skos = rdflib.Graph()
    skos.parse(filepath)
    rows = graph2table(skos)
    with open(outpath, 'w', encoding='utf-8') as out:
        writer = csv.writer(out)
        writer.writerows(rows)

def graph2table(skos):
    rows = []
    # concept scheme
    csuri = skos.value(None, RDF.type, SKOS.ConceptScheme)
    rows.append(('uri of conceptscheme',csuri))
    for pred, obj in skos.predicate_objects(csuri):
        if pred == RDF.type: continue
        rows.append((compact_uri(pred, obj),obj))
    # concepts
    keys = []
    for curi in skos.subjects(RDF.type, SKOS.Concept):
        for pred, obj in skos.predicate_objects(curi):
            if pred == RDF.type: continue
            if pred == SKOS.inScheme: continue
            pred = compact_uri(pred, obj)
            if pred not in keys:
                keys.append(pred)
    rows.append(['uri of concept']+keys)
    datarows = []
    for curi in skos.subjects(RDF.type, SKOS.Concept):
        row = [curi]
        for key in keys:
            pred, lang = parse_predicate(key)
            if lang:
                row.append(', '.join(obj for obj in skos.objects(curi, pred) if obj.language == lang))
            else:
                row.append(', '.join(skos.objects(curi, pred)))
        datarows.append(row)
    datarows.sort()
    rows.extend(datarows)
    return rows

def skos2html(filepath, output_dirname, output_basename,
              localizations_dirname, langs, index_lang="en",
              html_rendering=WHOLE_PAGE):
    # Deletes previous results
    try:
        shutil.rmtree(osp.join(output_dirname))
    except FileNotFoundError as exc:
        pass
    os.makedirs(osp.join(output_dirname), exist_ok=True)
    # Creates HTML rendering for each language
    lang_files = {}
    for lang in langs:
        results, log = skos_to_html(filepath, localizations_dirname, lang,
                                    html_rendering)
        if log:
            logging.warning(log)
        if len(results) == 0:
            msg = ("SKOS vocabulary doesn't contain the description of any "
                   "ConceptScheme. Can't produce the HTML file describing "
                   "the  ConceptScheme and its Concepts for language {0}."
                   "").format(lang)
            raise ConversionError("incorrectVocabularyFile", msg)
        if len(results) > 1:
            msg = ("SKOS vocabulary contains the description of multiple "
                   "ConceptScheme ({0:d}). Can't produce a single HTML "
                   "file, for language {1}, describing all the "
                   "ConceptScheme (there is one file per ConceptScheme for "
                   "each language).").format(len(results), lang)
            raise ConversionError("incorrectVocabularyFile", msg)
        result = list(results.values())[0]
        out_filename = "{0}.{1}.html".format(output_basename, lang)
        with open(osp.join(output_dirname, out_filename), "wb") as out:
            out.write(etree.tostring(result, method="html",
                                     encoding="utf-8"))
        lang_files[lang] = out_filename
    # Creates HTML index file for previewing
    indexes, log = skos_index(filepath, localizations_dirname, index_lang,
                              WHOLE_PAGE)
    if log:
        logging.warning(log)
    if len(indexes) == 0:
        msg = ("SKOS vocabulary doesn't contain the description of any "
               "ConceptScheme. Can't produce the HTML file containing the "
               "languages index.")
        raise ConversionError("incorrectVocabularyFile", msg)
    if len(indexes) > 1:
        msg = ("SKOS vocabulary contains the description of multiple "
               "ConceptScheme ({0:d}). Can't produce a single HTML containing "
               "the langauges index.").format(len(results))
        raise ConversionError("incorrectVocabularyFile", msg)
    index = list(indexes.values())[0]
    if index is None:
        index = H.HTML(H.BODY(UL(id="concept-scheme")))
    for ul_elt in index.xpath(".//ul[@id='concept-scheme']"):
        for lang, fname in lang_files.items():
            ul_elt.append(H.LI(H.A(lang.upper(), href=fname)))
    with open(osp.join(output_dirname, "index.html"), "wb") as out:
        out.write(etree.tostring(index, method="html",
                                 encoding="utf-8"))


if __name__ == '__main__':
    import sys
    try:
        action = sys.argv[1]
        inputfile = sys.argv[2]
        outfile = sys.argv[3]
        assert action in ('convert','csv')
    except IndexError:
        print('any2skos.py [convert|csv] <inputfile.[xlsx,rdf]> <output.[rdf,ttl]>')
        sys.exit(1)
    if action == 'convert':
        xl2rdf(inputfile, outfile)
    elif action == 'csv':
        skos2csv(inputfile, outfile)
