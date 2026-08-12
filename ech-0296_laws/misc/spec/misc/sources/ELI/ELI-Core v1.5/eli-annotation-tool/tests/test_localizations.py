# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

import unittest
import os, tempfile, json

from eli_annotation import localizations


class LocalsTC(unittest.TestCase):

    def test_deploy_standard_localizations(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            fnames = os.listdir(tmpdir)
            self.assertEqual(len(fnames), 0)
            localizations.deploy_standard_localizations(tmpdir)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, ["en.json", "fr.json"])

    def test_check_localization_valid(self):
        with open(os.path.join(localizations.STANDARD_LOCALIZ_DIR,
                               "en.json")) as inp:
            data = json.load(inp)
        res, errs = localizations.check_localization(data)
        self.assertTrue(res)
        self.assertEqual(errs, [])

    def test_check_localization_missing_keys(self):
        with open(os.path.join(localizations.STANDARD_LOCALIZ_DIR,
                               "en.json")) as inp:
            data = json.load(inp)
        data["uiMessages"].pop("missingVocabulary")
        data["eliOntology"]["eli:number"].pop("label")
        data["eliOntology"]["eli:id_local"].pop("help")
        res, errs = localizations.check_localization(data)
        self.assertFalse(res)
        self.assertEqual(sorted(errs),
                         ['Missing key: eliOntology / eli:number / label',
                          'Missing key: uiMessages / missingVocabulary'])

    def test_check_localization_wrong_object(self):
        res, errs = localizations.check_localization("wrong object")
        self.assertFalse(res)
        self.assertEqual(sorted(errs),
                         ['The data in the JSON file should be an object'])

    def test_list_localizations(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            localizations.deploy_standard_localizations(tmpdir)
            for fname in ["de.json", "glossary.xml"]:
                with open(os.path.join(tmpdir, fname), "w") as out:
                    out.write("Nothing")
            langs = localizations.list_installed_localizations(tmpdir)
            self.assertEqual(langs, ["de", "en", "fr"])

    def test_get_localization(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            localizations.deploy_standard_localizations(tmpdir)
            data = localizations.get_localization(tmpdir, "fr")
            self.assertEqual(data["langCode"], "fr")
            self.assertEqual(data["uiMessages"]["processing"], "Traitement en cours...")

    def test_get_missing_localization(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            localizations.deploy_standard_localizations(tmpdir)
            data = localizations.get_localization(tmpdir, "de")
            self.assertEqual(data, None)

    def test_get_default_localization(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            localizations.deploy_standard_localizations(tmpdir)
            data = localizations.get_default_localization()
            self.assertEqual(data["langCode"], "en")
            self.assertEqual(data["uiMessages"]["processing"], "Processing...")

    def test_store_new_localization(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            localizations.deploy_standard_localizations(tmpdir)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, ["en.json", "fr.json"])
            data = localizations.get_default_localization()
            data["langCode"] = "de"
            data["uiMessages"]["processing"] = "XXX XXX"
            localizations.store_localization(tmpdir, "de", data)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, ["de.json", "en.json", "fr.json"])
            with open(os.path.join(tmpdir, "de.json")) as inp:
                check = json.load(inp)
            self.assertEqual(data, check)

    def test_store_existing_localization(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            localizations.deploy_standard_localizations(tmpdir)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, ["en.json", "fr.json"])
            data = localizations.get_default_localization()
            data["langCode"] = "en"
            data["uiMessages"]["processing"] = "XXX XXX"
            localizations.store_localization(tmpdir, "en", data)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, ["en.json", "fr.json"])
            with open(os.path.join(tmpdir, "en.json")) as inp:
                check = json.load(inp)
            self.assertEqual(data, check)

    def test_deploy_standard_about_resources(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            fnames = os.listdir(tmpdir)
            self.assertEqual(len(fnames), 0)
            localizations.deploy_standard_localized_resources(
                tmpdir, localizations.ABOUT)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, ["about.en.html", "about.fr.html"])

    def test_deploy_standard_excel_vocab_doc_resources(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            fnames = os.listdir(tmpdir)
            self.assertEqual(len(fnames), 0)
            localizations.deploy_standard_localized_resources(
                tmpdir, localizations.EXCEL_VOCAB_DOC)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, ["excel_vocab_doc.en.html",
                                      "excel_vocab_doc.fr.html"])

    def test_get_localized_about(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            for name in (localizations.ABOUT, localizations.EXCEL_VOCAB_DOC):
                localizations.deploy_standard_localized_resources(tmpdir, name)
            data = localizations.get_localized_resource(
                tmpdir, localizations.ABOUT, "fr")
            start = b'<div>\n  <p>L\'outil d\'annotation ELI a \xc3\xa9t\xc3\xa9'
            self.assertEqual(data[:len(start)], start)

    def test_get_localized_excel_vocab_doc(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            for name in (localizations.ABOUT, localizations.EXCEL_VOCAB_DOC):
                localizations.deploy_standard_localized_resources(tmpdir, name)
            data = localizations.get_localized_resource(
                tmpdir, localizations.EXCEL_VOCAB_DOC, "fr")
            start = (b'<!DOCTYPE html >\n<html>\n<head>\n<meta http-equiv='
                     b'"Content-Type" content="text/html; charset=utf-8" />\n'
                     b'<title>Sp\xc3\xa9cifications du fichier Excel')
            self.assertEqual(data[:len(start)], start)

    def test_get_unknown_localized_resource(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            for name in (localizations.ABOUT, localizations.EXCEL_VOCAB_DOC):
                localizations.deploy_standard_localized_resources(tmpdir, name)
            data = localizations.get_localized_resource(tmpdir, "unknown", "fr")
            self.assertEqual(data, None)

    def test_get_missing_localized_resource(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            for name in (localizations.ABOUT, localizations.EXCEL_VOCAB_DOC):
                localizations.deploy_standard_localized_resources(tmpdir, name)
            data = localizations.get_localized_resource(
                tmpdir, localizations.ABOUT, "sq")
            self.assertEqual(data, None)

    def test_store_new_localized_resource(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            for name in (localizations.ABOUT, localizations.EXCEL_VOCAB_DOC):
                localizations.deploy_standard_localized_resources(tmpdir, name)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, ["about.en.html", "about.fr.html",
                                      "excel_vocab_doc.en.html",
                                      "excel_vocab_doc.fr.html"])
            data = b"<div>Etwas in deutsch</div>\n"
            localizations.store_localized_resource(
                tmpdir, localizations.ABOUT, "de", data)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, [
                "about.de.html", "about.en.html", "about.fr.html",
                "excel_vocab_doc.en.html", "excel_vocab_doc.fr.html"])
            with open(os.path.join(tmpdir, "about.de.html"), "rb") as inp:
                check = inp.readlines()
            self.assertEqual(data, b"".join(check))

    def test_store_existing_localized_resource(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            for name in (localizations.ABOUT, localizations.EXCEL_VOCAB_DOC):
                localizations.deploy_standard_localized_resources(tmpdir, name)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, ["about.en.html", "about.fr.html",
                                      "excel_vocab_doc.en.html",
                                      "excel_vocab_doc.fr.html"])
            data = b"<div>Quelque chose en fran\xc3\xa7ais</div>\n"
            localizations.store_localized_resource(
                tmpdir, localizations.ABOUT, "fr", data)
            fnames = sorted(os.listdir(tmpdir))
            self.assertEqual(fnames, ["about.en.html", "about.fr.html",
                                      "excel_vocab_doc.en.html",
                                      "excel_vocab_doc.fr.html"])
            with open(os.path.join(tmpdir, "about.fr.html"), "rb") as inp:
                check = inp.readlines()
            self.assertEqual(data, b"".join(check))


if __name__ == '__main__':
    unittest.main()
