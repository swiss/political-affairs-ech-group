# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import os, json, logging, glob, shutil
import os.path as osp


STANDARD_LOCALIZ_DIR = osp.join(osp.abspath(osp.dirname(__file__)),
                                "standard_files")
ABOUT = "about"
EXCEL_VOCAB_DOC = "excel_vocab_doc"


def check_localization(data):
    """
    Checks a localization data contains all the
    required keys (compares it to the default localization file)
    """
    errors = []
    if not isinstance(data, dict):
        errors.append("The data in the JSON file should be an object")
        return False, errors
    with open(osp.join(STANDARD_LOCALIZ_DIR,
                       "default-localization.json")) as inp:
        ref = json.load(inp)
    errors = _find_missing_keys(ref, data)
    return (len(errors) == 0), errors


def _find_missing_keys(reference, data, context=None):
    if context is None:
        context = []
    errors = []
    for key,ref_val in reference.items():
        local_context = context[:]
        local_context.append(key)
        if key not in data and key != "help":
            errors.append(
                "Missing key: {}".format(" / ".join(local_context[:])))
        elif isinstance(ref_val, dict):
            data_val = data[key]
            if not isinstance(data_val, dict):
                errors.append(
                    "Missing sub-object for key: {}"
                    "".format(" / ".join(local_context[:])))
            else:
                errors.extend(
                    _find_missing_keys(ref_val, data_val, local_context))
    return errors


def list_installed_localizations(localizations_dirname):
    return sorted(
        [osp.splitext(entry.name)[0]
         for entry in os.scandir(localizations_dirname)
         if entry.is_file() and osp.splitext(entry.name)[1] == ".json"])


def get_localization(localizations_dirname, lang_code):
    fpath = osp.join(localizations_dirname, lang_code.strip()+".json")
    if osp.exists(fpath) and osp.isfile(fpath):
        try:
            with open(fpath, encoding="utf-8") as inp:
                return json.load(inp)
        except Exception as exc:
            from traceback import format_exc
            logging.error("Can't read localization JSON file {0} because "
                          "of:\n{1}".format(fpath, format_exc()))
            return None
    return None


def get_default_localization():
    with open(osp.join(STANDARD_LOCALIZ_DIR,
                       "default-localization.json")) as inp:
        default = json.load(inp)
    return default


def store_localization(localizations_dirname, lang_code, local_data):
    fpath = osp.join(localizations_dirname, lang_code.strip()+".json")
    local_data["langCode"] = lang_code.strip()
    try:
        with open(fpath, "w", encoding="utf-8") as out:
            json.dump(local_data, out)
    except Exception as exc:
        from traceback import format_exc
        logging.error("Can't write localization JSON file {0} because "
                      "of:\n{1}".format(fpath, format_exc()))


def deploy_standard_localizations(localizations_dirname):
    fnames = [entry.name for entry in os.scandir(STANDARD_LOCALIZ_DIR)
              if entry.is_file() and osp.splitext(entry.name)[1] == ".json"
                 and entry.name != "default-localization.json"]
    for fname in fnames:
        inp_fname = osp.join(STANDARD_LOCALIZ_DIR, fname)
        out_fname = osp.join(localizations_dirname, fname)
        try:
            shutil.copyfile(inp_fname, out_fname)
        except Exception as exc:
            from traceback import format_exc
            logging.error(
                "The following exception occurred while trying to deploy the "
                "{0} localization file:\n{1}".format(fname, format_exc()))


def get_localized_resource(localizations_dirname, resource_name, lang_code):
    if resource_name not in (ABOUT, EXCEL_VOCAB_DOC):
        return None
    fpath = osp.join(localizations_dirname,
                     resource_name+".{}.html".format(lang_code.strip()))
    if osp.exists(fpath) and osp.isfile(fpath):
        try:
            with open(fpath, mode="rb") as inp:
                data = inp.readlines()
                return b"".join(data)
        except Exception as exc:
            from traceback import format_exc
            logging.error("Can't read localized resource file {0} because "
                          "of:\n{1}".format(fpath, format_exc()))
            return None
    return None


def store_localized_resource(localizations_dirname, resource_name, lang_code,
                             resource_data):
    assert resource_name in (ABOUT, EXCEL_VOCAB_DOC)
    assert isinstance(resource_data, bytes)
    fpath = osp.join(localizations_dirname,
                     resource_name+".{}.html".format(lang_code.strip()))
    try:
        with open(fpath, "wb") as out:
            out.write(resource_data)
    except Exception as exc:
        from traceback import format_exc
        logging.error("Can't write localized resource file {0} because "
                      "of:\n{1}".format(fpath, format_exc()))


def deploy_standard_localized_resources(localizations_dirname, resource_name):
    assert resource_name in (ABOUT, EXCEL_VOCAB_DOC)
    fnames = [osp.split(name)[1]
              for name in glob.glob(
                      osp.join(STANDARD_LOCALIZ_DIR, resource_name+'.*.html'))
              if osp.isfile(name)]
    for fname in fnames:
        inp_fname = osp.join(STANDARD_LOCALIZ_DIR, fname)
        out_fname = osp.join(localizations_dirname, fname)
        try:
            shutil.copyfile(inp_fname, out_fname)
        except Exception as exc:
            from traceback import format_exc
            logging.error(
                "The following exception occurred while trying to deploy the "
                "{0} resource file:\n{1}".format(fname, format_exc()))
