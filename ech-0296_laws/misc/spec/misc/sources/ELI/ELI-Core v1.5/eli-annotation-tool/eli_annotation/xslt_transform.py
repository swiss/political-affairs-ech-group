# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import os
from os import path as osp
import json, glob, logging
from lxml import etree


XSLT_DIRNAME =  osp.join(osp.abspath(osp.dirname(__file__)), "xslt")
XML_GLOSSARY_FILENAME = "glossary.xml"
ELID_NS = "urn:eli:annotation-tool:data:"
ONLY_METADATA = "metadata"
WHOLE_PAGE = "whole"


def build_xml_glossary(localizations_dirname):
    """
    Builds and saves an XML glossary containing the localizations of
    all the terms that can be encountered in the XSLT (ELI properties,
    SKOS properties, etc.)

    The localizations are read from the JSON localizations files found
    inside ``localizations_dirname``.

    The XML glossary is saved inside the same ``localizations_dirname``.
    """
    # Reads JSON localization files
    l10n_data = {}
    for fname in glob.glob(osp.join(localizations_dirname,'*.json')):
        if not osp.isfile(fname):
            continue
        try:
            with open(fname, encoding='utf-8') as inp:
                data = json.load(inp)
                lang_code = data["langCode"]
        except Exception as exc:
            from traceback import format_exc
            logging.error("Can't read localization file: {0}\n"
                          "The following exception occurred:\n{1}"
                          "".format(fname, format_exc()))
            continue
        decl_prefixes = data.get("prefixes", {})
        for domain,dom_data in data.items():
            if domain in ("langCode", "uiMessages", "prefixes"):
                continue
            for term,transl in dom_data.items():
                if not isinstance(transl, dict):
                    continue
                label = transl.get("label")
                if label is None:
                    continue
                if ":" in term:
                    prefix = term.split(":")[0]
                    local_name = ":".join(term.split(":")[1:])
                    if prefix in decl_prefixes:
                        term = decl_prefixes[prefix] + local_name
                if term not in l10n_data:
                    l10n_data[term] = {}
                l10n_data[term][lang_code] = label
    # Builds xml localization file (with all languages)
    root_elt = etree.Element("glossary")
    for term,transl in sorted(l10n_data.items()):
        term_elt = etree.SubElement(root_elt, "term")
        term_elt.set("name", term)
        for lang,label in transl.items():
            label_elt = etree.SubElement(term_elt, "label")
            label_elt.set("lang", lang)
            label_elt.text = label
    # Saves xml localization file
    gloss_fname = osp.join(localizations_dirname, XML_GLOSSARY_FILENAME)
    with open(gloss_fname, "wb") as out:
        out.write(etree.tostring(root_elt, encoding="utf-8",
                                 xml_declaration=True))

def skos_to_html(skos_fname, localizations_dirname, lang="en",
                 html_rendering=WHOLE_PAGE):
    gloss_fname = osp.join(localizations_dirname, XML_GLOSSARY_FILENAME)
    trf = etree.parse(osp.join(XSLT_DIRNAME, "skos2html.xsl"))
    transform = etree.XSLT(trf)
    vocab = etree.parse(skos_fname)
    whole_result = transform(
        vocab,
        glossaryFile='"{0}"'.format(gloss_fname),
        lang='"{0}"'.format(lang.lower()),
        saveHtmlFiles='"no"',
        htmlContent=('"none"' if html_rendering == ONLY_METADATA
                     else '"whole-page"')
    )
    results = {}
    for fcontent in whole_result.xpath("elid:file",
                                       namespaces={"elid": ELID_NS}):
        results[fcontent.get("node-id")] = fcontent.find("html")
    return results, transform.error_log


def eli_to_html(eli_fname, localizations_dirname, output_level="expression",
                index_lang="en", html_rendering=WHOLE_PAGE):
    gloss_fname = osp.join(localizations_dirname, XML_GLOSSARY_FILENAME)
    trf = etree.parse(osp.join(XSLT_DIRNAME, "eli2html.xsl"))
    transform = etree.XSLT(trf)
    notice = etree.parse(eli_fname)
    whole_result = transform(
        notice,
        glossaryFile='"{0}"'.format(gloss_fname),
        htmlFilesLevel='"{0}"'.format(output_level.lower()),
        saveHtmlFiles='"no"',
        indexLangCode='"{0}"'.format(index_lang),
        htmlContent=('"none"' if html_rendering == ONLY_METADATA
                     else '"whole-page"')
    )
    results = {}
    index = None
    for fcontent in whole_result.xpath("elid:file",
                                       namespaces={"elid": ELID_NS}):
        if fcontent.get("filename") == "index.html":
            index = fcontent.find("html")
        else:
            results[fcontent.get("node-id")] = fcontent.find("html")
    return index, results, transform.error_log


def skos_index(skos_fname, localizations_dirname, index_lang="en",
               html_rendering=WHOLE_PAGE):
    gloss_fname = osp.join(localizations_dirname, XML_GLOSSARY_FILENAME)
    trf = etree.parse(osp.join(XSLT_DIRNAME, "skos-index.xsl"))
    transform = etree.XSLT(trf)
    vocab = etree.parse(skos_fname)
    whole_result = transform(
        vocab,
        glossaryFile='"{0}"'.format(gloss_fname),
        saveHtmlFiles='"no"',
        indexLangCode='"{0}"'.format(index_lang),
        htmlContent=('"none"' if html_rendering == ONLY_METADATA
                     else '"whole-page"')
    )
    indexes = {}
    for fcontent in whole_result.xpath("elid:file",
                                       namespaces={"elid": ELID_NS}):
        indexes[fcontent.get("node-id")] = fcontent.find("html")
    return indexes, transform.error_log
