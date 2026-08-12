"""
tests/test_url_parser.py
tags: akn, url-parser, tests

Tests for URL parsing of Fedlex and ZH-Lex URLs.
Run with:  PYTHONPATH=. python -m pytest frbr_uri/tests/test_url_parser.py -v
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from frbr_uri.parsers.url_parser import parse_legal_url, UnsupportedUrlError


# ── Fedlex Classified Compilation ─────────────────────────────────────────────

class TestFedlexCC:
    def test_work_level(self):
        r = parse_legal_url("https://www.fedlex.admin.ch/eli/cc/1999/404")
        assert r.jurisdiction == "ch"
        assert r.doc_type == "act"
        assert r.date == "1999-01-01"
        assert r.number == "404"
        assert r.lang is None
        assert r.version is None
        assert r.platform == "fedlex-cc"
        assert r.collection == "cc"

    def test_work_level_with_lang(self):
        r = parse_legal_url("https://www.fedlex.admin.ch/eli/cc/1999/404/de")
        assert r.lang == "de"
        assert r.version is None

    def test_expression_level(self):
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/cc/1999/404/20210307/de")
        assert r.jurisdiction == "ch"
        assert r.lang == "de"
        assert r.version == "2021-03-07"   # YYYYMMDD → ISO 8601
        assert r.number == "404"

    def test_expression_french(self):
        r = parse_legal_url("https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/fr")
        assert r.lang == "fr"
        assert r.version == "2021-03-07"

    def test_expression_italian(self):
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/cc/2013/642/20220526/it")
        assert r.lang == "it"
        assert r.version == "2022-05-26"
        assert r.number == "642"
        assert r.date == "2013-01-01"

    def test_data_subdomain_works(self):
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/cc/1999/404/20210307/de")
        assert r.jurisdiction == "ch"

    def test_note_contains_as_number_warning(self):
        r = parse_legal_url("https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de")
        assert any("AS publication sequence" in n for n in r.notes)

    def test_old_number_format(self):
        # 1948-1999 era (year + 3 per-language page numbers, no separate volume — see
        # spec/URI_fedlex_template.md "Zwischen 1948 und 1999"), here re-consolidated with a
        # modern point-in-time + language: both the historical identity and the modern
        # expression info must survive.
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/cc/1966/57_57_57/20210101/de")
        assert r.number == "57_57_57"
        assert r.page_de == "57" and r.page_fr == "57" and r.page_it == "57"
        assert r.volume is None  # 1948-1999 has no separate volume field, unlike 1848-1947
        assert r.version == "2021-01-01"
        assert r.lang == "de"

    def test_resolver_kwargs(self):
        r = parse_legal_url("https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de")
        kwargs = r.to_resolver_kwargs()
        assert kwargs["jurisdiction"] == "ch"
        assert kwargs["doc_type"] == "act"
        assert kwargs["lang"] == "de"
        assert kwargs["version"] == "2021-03-07"


# ── Fedlex Official Compilation ───────────────────────────────────────────────

class TestFedlexOC:
    def test_oc_with_lang(self):
        r = parse_legal_url("https://www.fedlex.admin.ch/eli/oc/2022/491/de")
        assert r.platform == "fedlex-oc"
        assert r.collection == "oc"
        assert r.date == "2022-01-01"
        assert r.number == "491"
        assert r.lang == "de"

    def test_oc_work_level(self):
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/oc/2022/491")
        assert r.platform == "fedlex-oc"
        assert r.lang is None


# ── Fedlex Federal Gazette ────────────────────────────────────────────────────

class TestFedlexFGA:
    def test_fga_with_lang(self):
        r = parse_legal_url("https://www.fedlex.admin.ch/eli/fga/2009/876/de")
        assert r.platform == "fedlex-fga"
        assert r.collection == "fga"
        assert r.number == "876"
        assert r.lang == "de"
        assert r.date == "2009-01-01"

    def test_fga_warning_language(self):
        r = parse_legal_url("https://www.fedlex.admin.ch/eli/fga/2009/876/de")
        assert any("language-specific" in w for w in r.warnings)


# ── Fedlex historical (pre-1999) patterns ──────────────────────────────────────
# Real examples taken from spec/URI_fedlex_template.md — three genuinely distinct eras, not
# formatting variants of one scheme. See DECISIONS.md for the finding that these were previously
# unhandled (silently mis-parsed as one opaque "number" by the modern-era regexes).

class TestFedlex1848to1947:
    """1848-1947: {collection}/{volume}_{page-de}_{page-fr}_{page-it}, no year in the URI."""

    def test_roman_numeral_volume_1848_1874(self):
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/oc/VII/342_337_325")
        assert r.volume == "VII"
        assert r.page_de == "342" and r.page_fr == "337" and r.page_it == "325"
        assert r.number == "VII_342_337_325"
        assert r.date == "0000-01-01"
        assert any("Work date is unknown" in w for w in r.warnings)

    def test_arabic_volume_1874_1947(self):
        # NOTE: this example's volume ("III") is roman, even though URI_fedlex_template.md labels
        # the 1874-1947 range as using arabic numbers. Per the user (2026-07-29): the roman-numeral
        # volume was the original numbering convention and was later revised to arabic within this
        # window — not a documentation typo, an actual scheme change mid-era. Source not yet
        # pinned down to an exact revision date; flagged here rather than guessed at. The regex
        # accepts both roman and 1-3 digit arabic volumes, so both sub-periods parse correctly
        # regardless of the exact cutover point.
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/oc/III/183_182_182")
        assert r.volume == "III"
        assert r.page_de == "183"


class TestFedlex1948to1999:
    """1948-1999 (oc/cc): {year}/{page-de}_{page-fr}_{page-it} — no separate volume field."""

    def test_year_and_three_pages(self):
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/oc/1996/1506_1506_1506")
        assert r.pub_year == "1996"
        assert r.page_de == r.page_fr == r.page_it == "1506"
        assert r.volume is None
        assert r.date == "1996-01-01"


class TestFedlexFGAPre2000:
    """Pre-2000 FGA: {year}/{volume}_{page-de}_{page-fr}_{page-it} — pages may be empty when
    only one language was scanned/aligned."""

    def test_aligned_all_three_languages(self):
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/fga/1994/2_1_1_1")
        assert r.pub_year == "1994"
        assert r.volume == "2"
        assert r.page_de == r.page_fr == r.page_it == "1"

    def test_only_german_page_known(self):
        # BBl 1994 I 569 — only the German page is scanned/aligned; fr/it are empty, not zero.
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/fga/1994/1_569__")
        assert r.volume == "1"
        assert r.page_de == "569"
        assert r.page_fr is None
        assert r.page_it is None

    def test_only_french_page_known(self):
        # BBl vom 3. Oktober 1940, S. 1083 (auf Französisch)
        r = parse_legal_url("https://fedlex.data.admin.ch/eli/fga/1940/1__1083_")
        assert r.volume == "1"
        assert r.page_de is None
        assert r.page_fr == "1083"
        assert r.page_it is None


# ── ZH-Lex Legacy ─────────────────────────────────────────────────────────────

class TestZHLexLegacy:
    def test_current_version_only(self):
        r = parse_legal_url("http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=170.41")
        assert r.jurisdiction == "ch-zh"
        assert r.ls_number == "170.41"
        assert r.number == "170.41"
        assert r.lang == "de"
        assert r.erlass_date is None
        assert r.band_number is None

    def test_versioned_link(self):
        r = parse_legal_url(
            "http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=170.41,28.05.2008,01.10.2008,108"
        )
        assert r.ls_number == "170.41"
        assert r.erlass_date == "2008-05-28"   # DD.MM.YYYY → ISO
        assert r.inkraft_date == "2008-10-01"
        assert r.band_number == "108"
        assert r.date == "2008-05-28"
        assert r.version == "2008-10-01"

    def test_kantonsverfassung(self):
        r = parse_legal_url(
            "http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=101,27.02.2005,01.01.2006,103"
        )
        assert r.ls_number == "101"
        assert r.date == "2005-02-27"

    def test_missing_date_warning(self):
        r = parse_legal_url("http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=551.1")
        assert any("Work date is unknown" in w for w in r.warnings)

    def test_note_contains_eli_warning(self):
        r = parse_legal_url("http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=101")
        assert any("ELI" in n for n in r.notes)

    def test_resolver_kwargs_zh(self):
        r = parse_legal_url(
            "http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=170.41,28.05.2008,01.10.2008,108"
        )
        kwargs = r.to_resolver_kwargs()
        assert kwargs["jurisdiction"] == "ch-zh"
        assert kwargs["number"] == "170.41"
        assert kwargs["lang"] == "de"


# ── ZH.ch Portal ──────────────────────────────────────────────────────────────

class TestZHChPortal:
    def test_portal_url(self):
        r = parse_legal_url(
            "https://www.zh.ch/de/politik-staat/gesetze-beschluesse/"
            "gesetzessammlung/zhlex-ls/erlass-170_41-2008_05_28-2008_10_01-108.html"
        )
        assert r.ls_number == "170.41"
        assert r.erlass_date == "2008-05-28"
        assert r.inkraft_date == "2008-10-01"
        assert r.band_number == "108"
        assert r.jurisdiction == "ch-zh"

    def test_portal_note(self):
        r = parse_legal_url(
            "https://www.zh.ch/de/politik-staat/gesetze-beschluesse/"
            "gesetzessammlung/zhlex-ls/erlass-101-2005_02_27-2006_01_01-103.html"
        )
        assert any("zhlex.zh.ch" in n for n in r.notes)

    def test_portal_number_dot_restoration(self):
        r = parse_legal_url(
            "https://www.zh.ch/de/politik-staat/gesetze-beschluesse/"
            "gesetzessammlung/zhlex-ls/erlass-415_11-1998_03_15-1998_10_01-129.html"
        )
        assert r.ls_number == "415.11"


# ── Error cases ───────────────────────────────────────────────────────────────

class TestErrors:
    def test_unsupported_domain(self):
        with pytest.raises(UnsupportedUrlError):
            parse_legal_url("https://www.example.com/some/law")

    def test_fedlex_unknown_path(self):
        with pytest.raises(UnsupportedUrlError):
            parse_legal_url("https://fedlex.data.admin.ch/unknown/path/structure")

    def test_zhlex_missing_ordnr(self):
        with pytest.raises(UnsupportedUrlError):
            parse_legal_url("http://www.zhlex.zh.ch/Erlass.html?Open")
