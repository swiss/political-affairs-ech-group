"""
tests/test_resolver.py
tags: akn, frbr, tests

Tests for the FRBR URI Resolver.
Run with:  python -m pytest packages/frbr-uri/tests/ -v
"""

import sys
from pathlib import Path

# Make the package importable without installing it
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from frbr_uri.resolver import FRBRResolver


@pytest.fixture(scope="module")
def resolver():
    return FRBRResolver()


# ── Basic resolution ──────────────────────────────────────────────────────────

class TestFederalResolution:
    def test_work_uri(self, resolver):
        uris = resolver.resolve("ch", "act", "2024-01-01", "170.4")
        assert uris.work == "/akn/ch/lei/2024-01-01/170.4"

    def test_expression_uri(self, resolver):
        uris = resolver.resolve("ch", "act", "2024-01-01", "170.4", lang="de", version="2024-03-01")
        assert uris.expression == "/akn/ch/lei/2024-01-01/170.4/deu@2024-03-01"

    def test_manifestation_uri(self, resolver):
        uris = resolver.resolve("ch", "act", "2024-01-01", "170.4", lang="fr", format="pdf")
        assert uris.manifestation == "/akn/ch/lei/2024-01-01/170.4/fra@2024-01-01.pdf"

    def test_french_language(self, resolver):
        uris = resolver.resolve("ch", "ordinance", "2023-06-01", "SR 101", lang="fr")
        assert "/fra@" in uris.expression

    def test_italian_language(self, resolver):
        uris = resolver.resolve("ch", "act", "2023-01-01", "101", lang="it")
        assert "/ita@" in uris.expression

    def test_number_spaces_sanitized(self, resolver):
        uris = resolver.resolve("ch", "act", "2024-01-01", "SR 101")
        assert "SR-101" in uris.work
        assert " " not in uris.work


class TestCantonZH:
    def test_work_uri(self, resolver):
        uris = resolver.resolve("ch-zh", "act", "2023-09-15", "LS 170.1")
        assert uris.work == "/akn/ch-zh/gesetz/2023-09-15/LS-170.1"

    def test_unsupported_language_raises(self, resolver):
        with pytest.raises(ValueError, match="Language 'fr' not supported"):
            resolver.resolve("ch-zh", "act", "2023-01-01", "100", lang="fr")

    def test_decree_type(self, resolver):
        uris = resolver.resolve("ch-zh", "decree", "2024-03-01", "OS 2024-5")
        assert uris.subtype == "erlass"


class TestCantonZG:
    def test_work_uri(self, resolver):
        uris = resolver.resolve("ch-zg", "ordinance", "2022-11-01", "BGS 100.1")
        assert "/akn/ch-zg/" in uris.work

    def test_regulation_type(self, resolver):
        uris = resolver.resolve("ch-zg", "regulation", "2023-01-01", "GS 2023-1")
        assert uris.subtype == "reglement"


class TestMunicipalities:
    def test_bern(self, resolver):
        uris = resolver.resolve("ch-be-351", "regulation", "2023-05-01", "2023-12")
        assert "/akn/ch-be-351/" in uris.work

    def test_lausanne_french_default(self, resolver):
        uris = resolver.resolve("ch-vd-5586", "decision", "2024-02-01", "2024-3")
        assert "/fra@" in uris.expression

    def test_lausanne_explicit_lang(self, resolver):
        uris = resolver.resolve("ch-vd-5586", "ordinance", "2024-01-01", "2024-1", lang="fr")
        assert "/fra@" in uris.expression


# ── Error cases ───────────────────────────────────────────────────────────────

class TestErrors:
    def test_unknown_jurisdiction(self, resolver):
        with pytest.raises(KeyError, match="Unknown jurisdiction"):
            resolver.resolve("ch-xx", "act", "2024-01-01", "1")

    def test_unknown_doc_type(self, resolver):
        with pytest.raises(KeyError, match="not defined"):
            resolver.resolve("ch-zh", "unknown_type", "2024-01-01", "1")

    def test_invalid_date_format(self, resolver):
        with pytest.raises(ValueError, match="YYYY-MM-DD"):
            resolver.resolve("ch", "act", "15.01.2024", "170.4")


# ── Community profile loading ─────────────────────────────────────────────────

class TestCommunityProfiles:
    def test_load_extra_profile_dir(self, tmp_path):
        """A community can drop a JSON profile into any directory and it loads."""
        community_profile = {
            "jurisdiction": "ch-zg-1702",
            "level": "municipality",
            "name": "Gemeinde Cham",
            "country": "CH",
            "subdivision": "ZG",
            "municipality": "Cham",
            "bfs_number": "1702",
            "akn_country": "ch",
            "akn_prefix": "/akn/ch-zg-1702",
            "language_codes": {"de": "deu"},
            "default_language": "de",
            "document_types": {
                "regulation": {
                    "akn_type": "act",
                    "subtype": "reglement",
                    "label_de": "Reglement"
                }
            },
            "uri_templates": {
                "work":          "/akn/ch-zg-1702/{doc_type}/{date}/{number}",
                "expression":    "/akn/ch-zg-1702/{doc_type}/{date}/{number}/{lang}@{version}",
                "manifestation": "/akn/ch-zg-1702/{doc_type}/{date}/{number}/{lang}@{version}.{format}"
            }
        }
        import json
        profile_file = tmp_path / "ch-zg-1702.json"
        profile_file.write_text(json.dumps(community_profile), encoding="utf-8")

        r = FRBRResolver(extra_profile_dirs=[tmp_path])
        uris = r.resolve("ch-zg-1702", "regulation", "2024-01-01", "2024-1")
        assert uris.work == "/akn/ch-zg-1702/reglement/2024-01-01/2024-1"

    def test_list_jurisdictions(self, resolver):
        jds = resolver.list_jurisdictions()
        ids = [j["jurisdiction"] for j in jds]
        assert "ch" in ids
        assert "ch-zh" in ids
        assert "ch-zg" in ids
        assert "ch-be-351" in ids
        assert "ch-vd-5586" in ids
