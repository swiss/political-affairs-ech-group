"""
api/tests/test_api.py
tags: fastapi, api, tests

Endpoint tests for the AKN Pipeline API.

Run:  cd akn-pipeline && PYTHONPATH=packages pytest api/tests/ -v
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "packages"))

import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


# ── /health ───────────────────────────────────────────────────────────────────

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


# ── GET /resolve ──────────────────────────────────────────────────────────────

class TestResolveGet:
    BASE_URL = "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de"

    def test_minimal(self):
        r = client.get("/resolve", params={"url": self.BASE_URL})
        assert r.status_code == 200
        d = r.json()
        assert d["parsed_url"]["jurisdiction"] == "ch"
        assert d["uris"]["work"] is not None

    def test_with_article(self):
        r = client.get("/resolve", params={
            "url": self.BASE_URL, "article": "47", "short_title": "BV"
        })
        d = r.json()
        assert d["fragment"]["eid"] == "art_47"
        assert d["fragment"]["compact"] == "#a47"
        assert d["uris"]["display_uri"] == "bv#art_47"

    def test_full_subdivision(self):
        r = client.get("/resolve", params={
            "url": self.BASE_URL,
            "article": "47", "paragraph": "2", "litera": "a",
            "short_title": "BV", "lang": "de"
        })
        d = r.json()
        assert d["fragment"]["eid"] == "art_47.para_2.lit_a"
        assert d["fragment"]["compact"] == "#a47-p2-lit-a"
        assert d["human_citation"] == "BV Art. 47 Abs. 2 lit. a"
        assert "#art_47.para_2.lit_a" in d["uris"]["fragment_uri"]

    def test_french_citation(self):
        r = client.get("/resolve", params={
            "url": self.BASE_URL,
            "article": "47", "paragraph": "2", "litera": "a",
            "short_title": "Cst.", "lang": "fr"
        })
        d = r.json()
        assert d["human_citation"] == "Cst. Art. 47 Al. 2 let. a"

    def test_sr_fallback(self):
        r = client.get("/resolve", params={
            "url": self.BASE_URL, "article": "5", "sr_number": "101"
        })
        d = r.json()
        assert "sr-101" in d["uris"]["display_uri"]

    def test_no_fragment(self):
        r = client.get("/resolve", params={"url": self.BASE_URL, "short_title": "BV"})
        d = r.json()
        assert d["fragment"] is None
        assert d["uris"]["display_uri"] == "bv"

    def test_eli_subdivision_uri(self):
        r = client.get("/resolve", params={
            "url": self.BASE_URL, "article": "47", "paragraph": "2"
        })
        d = r.json()
        assert d["uris"]["eli_subdivision_uri"].endswith("/art_47/para_2")

    def test_work_fragment_uri(self):
        r = client.get("/resolve", params={
            "url": self.BASE_URL, "article": "3", "short_title": "BV"
        })
        d = r.json()
        assert d["uris"]["work_fragment_uri"].endswith("#art_3")


# ── POST /resolve ─────────────────────────────────────────────────────────────

class TestResolvePost:
    def test_basic(self):
        r = client.post("/resolve", json={
            "url": "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            "subdivision": {"article": "47", "paragraph": "2"},
            "short_title": "BV",
            "lang": "de"
        })
        assert r.status_code == 200
        d = r.json()
        assert d["fragment"]["eid"] == "art_47.para_2"
        assert d["human_citation"] == "BV Art. 47 Abs. 2"

    def test_zh_lex(self):
        r = client.post("/resolve", json={
            "url": "http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=170.41,28.05.2008,01.10.2008,108",
            "subdivision": {"article": "3"},
        })
        assert r.status_code == 200
        d = r.json()
        assert d["parsed_url"]["jurisdiction"] == "ch-zh"
        assert d["fragment"]["eid"] == "art_3"

    def test_with_chapter_section(self):
        r = client.post("/resolve", json={
            "url": "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            "subdivision": {"chapter": "3", "section": "2", "article": "5"},
        })
        assert r.status_code == 200
        d = r.json()
        assert d["fragment"]["eid"] == "chp_3.sec_2.art_5"

    def test_with_number_and_litera(self):
        r = client.post("/resolve", json={
            "url": "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            "subdivision": {"article": "11", "number": "3", "litera": "b"},
        })
        assert r.status_code == 200
        d = r.json()
        assert d["fragment"]["eid"] == "art_11.num_3.lit_b"
        assert d["fragment"]["compact"] == "#a11-num-3-lit-b"
        assert d["fragment"]["human_de"] == "Art. 11 Ziff. 3 lit. b"

    def test_all_fields_present(self):
        r = client.post("/resolve", json={
            "url": "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            "subdivision": {"article": "1"},
        })
        d = r.json()
        assert "parsed_url" in d
        assert "document_pointer" in d
        assert "fragment" in d
        assert "uris" in d
        assert "human_citation" in d
        assert "warnings" in d
        assert "notes" in d


# ── POST /fragment ────────────────────────────────────────────────────────────

class TestFragmentPost:
    def test_article_only(self):
        r = client.post("/fragment", json={"subdivision": {"article": "47"}})
        assert r.status_code == 200
        d = r.json()
        assert d["eid"] == "art_47"
        assert d["compact"] == "#a47"
        assert d["fragment"] == "#art_47"
        assert d["eli_path"] == "/art_47"

    def test_full(self):
        r = client.post("/fragment", json={
            "subdivision": {"article": "47", "paragraph": "2", "litera": "a"}
        })
        d = r.json()
        assert d["eid"] == "art_47.para_2.lit_a"
        assert d["compact"] == "#a47-p2-lit-a"
        assert d["human_de"] == "Art. 47 Abs. 2 lit. a"
        assert d["human_fr"] == "Art. 47 Al. 2 let. a"
        assert d["human_it"] == "Art. 47 cpv. 2 lett. a"

    def test_annex(self):
        r = client.post("/fragment", json={"subdivision": {"annex": "2"}})
        assert r.status_code == 200
        assert r.json()["eid"] == "anx_2"

    def test_empty_returns_422(self):
        r = client.post("/fragment", json={"subdivision": {}})
        assert r.status_code == 422

    def test_number_litera(self):
        r = client.post("/fragment", json={
            "subdivision": {"article": "11", "number": "3", "litera": "b"}
        })
        d = r.json()
        assert d["eid"] == "art_11.num_3.lit_b"
        assert d["compact"] == "#a11-num-3-lit-b"


# ── GET /fragment/parse ───────────────────────────────────────────────────────

class TestFragmentParse:
    @pytest.mark.parametrize("q,expected_eid", [
        ("#a47",                "art_47"),
        ("#a47-p2-lit-a",       "art_47.para_2.lit_a"),
        ("#a11-num-3-lit-b",    "art_11.num_3.lit_b"),
        ("art_47.para_2.lit_a", "art_47.para_2.lit_a"),
        ("Art. 47 Abs. 2 lit. a", "art_47.para_2.lit_a"),
        ("Art. 47 Al. 2 let. a",  "art_47.para_2.lit_a"),
        ("#anx-2",              "anx_2"),
        ("#s3",                 "sec_3"),
    ])
    def test_parse_formats(self, q, expected_eid):
        r = client.get("/fragment/parse", params={"q": q})
        assert r.status_code == 200, r.text
        assert r.json()["eid"] == expected_eid

    def test_all_output_fields_present(self):
        r = client.get("/fragment/parse", params={"q": "#a47-p2-lit-a"})
        d = r.json()
        for key in ("eid", "fragment", "compact", "human_de", "human_fr", "human_it", "eli_path"):
            assert key in d

    def test_invalid_returns_422(self):
        r = client.get("/fragment/parse", params={"q": "---invalid---"})
        assert r.status_code == 422


# ── GET /jurisdiction ─────────────────────────────────────────────────────────

class TestJurisdiction:
    @pytest.mark.parametrize("q,expected", [
        ("ch",       "ch"),
        ("CH",       "ch"),
        ("ZH",       "ch-zh"),
        ("zh",       "ch-zh"),
        ("ZG",       "ch-zg"),
        ("BE",       "ch-be"),
        ("VD",       "ch-vd"),
        ("261",      "ch-zh-261"),
        ("351",      "ch-be-351"),
        ("ch-zh-261","ch-zh-261"),
        ("ch-zh",    "ch-zh"),
    ])
    def test_resolve(self, q, expected):
        r = client.get("/jurisdiction", params={"q": q})
        assert r.status_code == 200
        assert r.json()["jurisdiction"] == expected

    def test_invalid_raises_422(self):
        r = client.get("/jurisdiction", params={"q": "XX"})
        assert r.status_code == 422


# ── GET /parse-url ────────────────────────────────────────────────────────────

class TestParseURL:
    def test_fedlex_cc(self):
        r = client.get("/parse-url", params={
            "url": "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de"
        })
        assert r.status_code == 200
        d = r.json()
        assert d["jurisdiction"] == "ch"
        assert d["lang"] == "de"
        assert d["platform"] == "fedlex-cc"

    def test_zh_lex(self):
        r = client.get("/parse-url", params={
            "url": "http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=170.41"
        })
        assert r.status_code == 200
        d = r.json()
        assert d["jurisdiction"] == "ch-zh"
        assert d["ls_number"] == "170.41"

    def test_invalid_url_422(self):
        r = client.get("/parse-url", params={"url": "https://example.com/not-a-law"})
        assert r.status_code == 422
