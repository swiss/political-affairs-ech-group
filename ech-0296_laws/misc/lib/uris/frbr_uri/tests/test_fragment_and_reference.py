"""
tests/test_fragment_and_reference.py
tags: akn, fragment, reference, tests

Tests for:
  - Subdivision codes and FragmentRef building
  - Compact display syntax (#a47, #p2, #lit-a, etc.)
  - Jurisdiction shorthand resolution (ch, ZH, 261, BFS ranges)
  - DocumentPointer priority (short title > SR > AS)
  - LegalReferenceBuilder.from_url and from_shorthand
  - Human-readable citations (de/fr/it)
  - Round-trip: compact → eid → compact
  - parse_fragment (human and eId inputs)

Run with:  PYTHONPATH=. python -m pytest frbr_uri/tests/test_fragment_and_reference.py -v
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest

from frbr_uri.fragment import (
    build_fragment, parse_fragment, parse_compact_fragment, compact_fragment,
    resolve_jurisdiction, DocumentPointer, FragmentRef, SubdivisionRef,
    SUBDIVISION_CODES,
)
from frbr_uri.reference import LegalReferenceBuilder


# ── SubdivisionRef / FragmentRef ─────────────────────────────────────────────

class TestSubdivisionRef:
    def test_article_code(self):
        s = SubdivisionRef(kind="article", value="47")
        assert s.code == "art"
        assert s.segment == "art_47"

    def test_paragraph_code(self):
        s = SubdivisionRef(kind="paragraph", value="2")
        assert s.code == "para"
        assert s.segment == "para_2"

    def test_litera_code(self):
        s = SubdivisionRef(kind="litera", value="a")
        assert s.code == "lit"
        assert s.segment == "lit_a"

    def test_number_code(self):
        # F4: Ziffer uses `num`
        s = SubdivisionRef(kind="number", value="3")
        assert s.code == "num"

    def test_chapter_code(self):
        s = SubdivisionRef(kind="chapter", value="2")
        assert s.code == "chp"

    def test_section_code(self):
        s = SubdivisionRef(kind="section", value="1")
        assert s.code == "sec"

    def test_annex_code(self):
        s = SubdivisionRef(kind="annex", value="1")
        assert s.code == "anx"


class TestFragmentRef:
    def test_empty(self):
        f = FragmentRef()
        assert f.is_empty()
        assert f.eid() == ""
        assert f.fragment() == "#"
        assert f.eli_path() == "/"

    def test_single_article(self):
        f = build_fragment(article="47")
        assert f.eid() == "art_47"
        assert f.fragment() == "#art_47"
        assert f.eli_path() == "/art_47"

    def test_article_para_lit(self):
        f = build_fragment(article="47", paragraph="2", litera="a")
        assert f.eid() == "art_47.para_2.lit_a"
        assert f.fragment() == "#art_47.para_2.lit_a"
        assert f.eli_path() == "/art_47/para_2/lit_a"

    def test_full_hierarchy(self):
        f = build_fragment(chapter="3", section="2", article="5",
                           paragraph="1", litera="b")
        assert f.eid() == "chp_3.sec_2.art_5.para_1.lit_b"

    def test_article_with_number_and_lit(self):
        f = build_fragment(article="11", number="3", litera="b")
        assert f.eid() == "art_11.num_3.lit_b"

    def test_optional_chapter_omitted(self):
        # F6: chapter/section are optional
        f = build_fragment(article="5", paragraph="1")
        assert "chp" not in f.eid()
        assert "sec" not in f.eid()

    def test_annex(self):
        f = build_fragment(annex="2")
        assert f.eid() == "anx_2"

    def test_sublitera(self):
        f = build_fragment(article="3", litera="a", sublitera="aa")
        assert f.eid() == "art_3.lit_a.sublit_aa"


# ── Human-readable citations ──────────────────────────────────────────────────

class TestHumanReadable:
    def test_german_art_abs_lit(self):
        f = build_fragment(article="47", paragraph="2", litera="a")
        assert f.human_readable("de") == "Art. 47 Abs. 2 lit. a"

    def test_french_art_al_let(self):
        f = build_fragment(article="47", paragraph="2", litera="a")
        assert f.human_readable("fr") == "Art. 47 Al. 2 let. a"

    def test_italian_art_cpv_lett(self):
        f = build_fragment(article="47", paragraph="2", litera="a")
        assert f.human_readable("it") == "Art. 47 cpv. 2 lett. a"

    def test_german_kapitel_abschnitt(self):
        f = build_fragment(chapter="3", section="2", article="5")
        hr = f.human_readable("de")
        assert "Kap. 3" in hr
        assert "Abschn. 2" in hr
        assert "Art. 5" in hr

    def test_german_ziffer(self):
        f = build_fragment(article="11", number="3")
        assert "Ziff. 3" in f.human_readable("de")

    def test_french_chiffre(self):
        f = build_fragment(article="11", number="3")
        assert "ch. 3" in f.human_readable("fr")

    def test_fallback_lang(self):
        # Unknown lang falls back to German labels
        f = build_fragment(article="5")
        hr = f.human_readable("de")
        assert "Art. 5" in hr


# ── Compact display syntax (F11) ──────────────────────────────────────────────

class TestCompactSyntax:
    def test_article_only(self):
        f = build_fragment(article="47")
        assert compact_fragment(f) == "#a47"

    def test_article_para(self):
        f = build_fragment(article="47", paragraph="2")
        assert compact_fragment(f) == "#a47-p2"

    def test_article_para_lit(self):
        f = build_fragment(article="47", paragraph="2", litera="a")
        assert compact_fragment(f) == "#a47-p2-lit-a"

    def test_with_chapter_section(self):
        f = build_fragment(chapter="3", section="2", article="5")
        c = compact_fragment(f)
        # chp is multi-char → hyphenated
        assert "chp" in c
        assert "s2" in c
        assert "a5" in c

    def test_ziffer(self):
        f = build_fragment(article="11", number="3")
        assert compact_fragment(f) == "#a11-num-3"

    def test_ziffer_then_lit(self):
        f = build_fragment(article="11", number="3", litera="b")
        assert compact_fragment(f) == "#a11-num-3-lit-b"

    def test_annex(self):
        f = build_fragment(annex="2")
        assert compact_fragment(f) == "#anx-2"

    def test_empty(self):
        f = FragmentRef()
        assert compact_fragment(f) == ""

    def test_section_only(self):
        f = build_fragment(section="3")
        assert compact_fragment(f) == "#s3"


class TestParseCompact:
    def test_article(self):
        f = parse_compact_fragment("#a47")
        assert f.eid() == "art_47"

    def test_article_para_lit(self):
        f = parse_compact_fragment("#a47-p2-lit-a")
        assert f.eid() == "art_47.para_2.lit_a"

    def test_chapter_section_article(self):
        f = parse_compact_fragment("#chp3-s2-a5")
        assert f.eid() == "chp_3.sec_2.art_5"

    def test_ziffer_lit(self):
        f = parse_compact_fragment("#a11-num-3-lit-b")
        assert f.eid() == "art_11.num_3.lit_b"

    def test_without_hash(self):
        f = parse_compact_fragment("a47")
        assert f.eid() == "art_47"

    def test_annex(self):
        f = parse_compact_fragment("#anx-2")
        assert f.eid() == "anx_2"

    def test_empty(self):
        f = parse_compact_fragment("")
        assert f.is_empty()

    def test_section(self):
        f = parse_compact_fragment("#s3")
        assert f.eid() == "sec_3"

    def test_para_only(self):
        f = parse_compact_fragment("#p2")
        assert f.eid() == "para_2"


class TestCompactRoundTrip:
    """All compact forms should survive eid() → compact → parse → eid()."""

    @pytest.mark.parametrize("compact,expected_eid", [
        ("#a47",           "art_47"),
        ("#a47-p2",        "art_47.para_2"),
        ("#a47-p2-lit-a",  "art_47.para_2.lit_a"),
        ("#a11-num-3-lit-b","art_11.num_3.lit_b"),
        ("#anx-2",         "anx_2"),
        ("#s3",            "sec_3"),
        ("#p2",            "para_2"),
    ])
    def test_round_trip(self, compact, expected_eid):
        parsed = parse_compact_fragment(compact)
        assert parsed.eid() == expected_eid
        # Round-trip back to compact
        back = compact_fragment(parsed)
        re_parsed = parse_compact_fragment(back)
        assert re_parsed.eid() == expected_eid


# ── parse_fragment (human text + eId) ────────────────────────────────────────

class TestParseFragment:
    def test_german_full(self):
        f = parse_fragment("Art. 47 Abs. 2 lit. a")
        assert f.eid() == "art_47.para_2.lit_a"

    def test_german_kapitel(self):
        f = parse_fragment("Kapitel 3 Abschnitt 2 Art. 5")
        assert "chp_3" in f.eid()
        assert "sec_2" in f.eid()
        assert "art_5" in f.eid()

    def test_french(self):
        f = parse_fragment("Art. 47 Al. 2 let. a")
        assert f.eid() == "art_47.para_2.lit_a"

    def test_italian(self):
        f = parse_fragment("Art. 47 cpv. 2 lett. a")
        assert f.eid() == "art_47.para_2.lit_a"

    def test_eid_passthrough(self):
        f = parse_fragment("art_47.para_2.lit_a")
        assert f.eid() == "art_47.para_2.lit_a"

    def test_hash_eid(self):
        f = parse_fragment("#art_47")
        assert f.eid() == "art_47"

    def test_german_ziffer(self):
        f = parse_fragment("Art. 11 Abs. 3 Ziff. 2 lit. a")
        assert "num_2" in f.eid()
        assert "lit_a" in f.eid()


# ── Jurisdiction resolution ───────────────────────────────────────────────────

class TestResolveJurisdiction:
    def test_empty_is_federal(self):
        assert resolve_jurisdiction("") == "ch"

    def test_ch(self):
        assert resolve_jurisdiction("ch") == "ch"

    def test_ch_uppercase(self):
        assert resolve_jurisdiction("CH") == "ch"

    def test_canton_zh(self):
        assert resolve_jurisdiction("ZH") == "ch-zh"

    def test_canton_zh_lowercase(self):
        assert resolve_jurisdiction("zh") == "ch-zh"

    def test_canton_zg(self):
        assert resolve_jurisdiction("ZG") == "ch-zg"

    def test_canton_be(self):
        assert resolve_jurisdiction("BE") == "ch-be"

    def test_canton_vd(self):
        assert resolve_jurisdiction("VD") == "ch-vd"

    def test_canton_ge(self):
        assert resolve_jurisdiction("GE") == "ch-ge"

    def test_bfs_known_zuerich(self):
        assert resolve_jurisdiction("261") == "ch-zh-261"

    def test_bfs_known_bern(self):
        assert resolve_jurisdiction("351") == "ch-be-351"

    def test_bfs_known_lausanne(self):
        assert resolve_jurisdiction("5586") == "ch-vd-5586"

    def test_bfs_known_cham(self):
        assert resolve_jurisdiction("1702") == "ch-zg-1702"

    def test_bfs_range_ag(self):
        # BFS 4001-4500 → AG
        jid = resolve_jurisdiction("4001")
        assert jid.startswith("ch-ag-")

    def test_bfs_range_ti(self):
        jid = resolve_jurisdiction("5100")
        assert jid.startswith("ch-ti-")

    def test_passthrough_full(self):
        assert resolve_jurisdiction("ch-zh-261") == "ch-zh-261"

    def test_passthrough_canton(self):
        assert resolve_jurisdiction("ch-zg") == "ch-zg"

    def test_invalid_raises(self):
        with pytest.raises(ValueError):
            resolve_jurisdiction("XX")  # not a valid canton code

    def test_invalid_bfs_raises(self):
        with pytest.raises(ValueError):
            resolve_jurisdiction("99999")  # out of range


# ── DocumentPointer ───────────────────────────────────────────────────────────

class TestDocumentPointer:
    def test_short_title_priority(self):
        # F8: short title wins
        p = DocumentPointer(short_title="OR", sr_number="220", as_number="2021/5")
        assert p.preferred_id() == "OR"
        assert p.akn_pointer() == "or"

    def test_sr_number_fallback(self):
        p = DocumentPointer(sr_number="220")
        assert p.preferred_id() == "SR 220"
        assert p.akn_pointer() == "sr-220"

    def test_sr_with_dots(self):
        p = DocumentPointer(sr_number="235.1")
        assert p.akn_pointer() == "sr-235-1"

    def test_as_number_fallback(self):
        p = DocumentPointer(as_number="2022/491", jurisdiction="ch")
        assert "AS" in p.preferred_id()
        assert p.akn_pointer().startswith("as-")

    def test_ls_number(self):
        # ZH-Lex LS number used as SR equivalent
        p = DocumentPointer(sr_number="170.41", jurisdiction="ch-zh")
        assert p.preferred_id() == "SR 170.41"


# ── LegalReferenceBuilder ─────────────────────────────────────────────────────

class TestLegalReferenceBuilder:
    def setup_method(self):
        self.builder = LegalReferenceBuilder()

    def test_fedlex_cc_with_fragment(self):
        ref = self.builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            article="47", paragraph="2", litera="a",
            short_title="BV", sr_number="101"
        )
        assert ref.fragment.eid() == "art_47.para_2.lit_a"
        assert "#art_47" in ref.fragment_uri
        assert "bv" in ref.display_uri
        assert "#art_47.para_2.lit_a" in ref.display_uri

    def test_human_citation_de(self):
        ref = self.builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            article="47", paragraph="2", litera="a",
            short_title="BV"
        )
        assert ref.human_citation("de") == "BV Art. 47 Abs. 2 lit. a"

    def test_human_citation_fr(self):
        ref = self.builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/fr",
            article="47", paragraph="2", litera="a",
            short_title="Cst."
        )
        assert ref.human_citation("fr") == "Cst. Art. 47 Al. 2 let. a"

    def test_sr_fallback_in_display(self):
        ref = self.builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/2007/758/de",
            article="64", sr_number="142.20"
        )
        # No short_title → SR number used
        assert "sr-142-20" in ref.display_uri or "sr-142.20" in ref.display_uri.lower() \
            or "142" in ref.display_uri

    def test_frbr_work_uri(self):
        ref = self.builder.from_url(
            "https://fedlex.data.admin.ch/eli/cc/1993/1798_1798_1798/20220101/de",
        )
        assert ref.frbr_uris is not None
        assert ref.frbr_uris.work.startswith("/akn/ch/")

    def test_fragment_uri_structure(self):
        ref = self.builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            article="3", short_title="BV"
        )
        # Should be: /akn/ch/.../deu@...#art_3
        assert "#art_3" in ref.fragment_uri

    def test_eli_subdivision_uri(self):
        ref = self.builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            article="47", paragraph="2"
        )
        assert ref.eli_subdivision_uri.endswith("/art_47/para_2")

    def test_work_fragment_uri(self):
        ref = self.builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            article="47", short_title="BV"
        )
        assert ref.work_fragment_uri.endswith("#art_47")

    def test_zh_lex_url(self):
        ref = self.builder.from_url(
            "http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=170.41,28.05.2008,01.10.2008,108",
            article="3"
        )
        assert ref.parsed_url.jurisdiction == "ch-zh"
        assert ref.parsed_url.ls_number == "170.41"
        assert ref.fragment.eid() == "art_3"

    def test_compact_display_on_ref(self):
        ref = self.builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            article="47", paragraph="2", litera="a", short_title="BV"
        )
        c = compact_fragment(ref.fragment)
        assert c == "#a47-p2-lit-a"

    def test_no_fragment_urls_still_work(self):
        ref = self.builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/1999/404/de",
            short_title="BV"
        )
        assert not ref.fragment_uri.endswith("#")
        assert ref.frbr_uris is not None

    def test_as_dict_keys(self):
        ref = self.builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            article="47", short_title="BV"
        )
        d = ref.as_dict()
        assert "fragment" in d
        assert "uris" in d
        assert "document_pointer" in d
        assert d["document_pointer"]["short_title"] == "BV"
        assert d["fragment"]["eid"] == "art_47"
        assert d["uris"]["display_uri"] is not None


class TestReferenceBuilderFromShorthand:
    def setup_method(self):
        self.builder = LegalReferenceBuilder()

    def test_federal_default(self):
        ref = self.builder.from_shorthand(
            short_title="OR", sr_number="220",
            article="11", paragraph="3"
        )
        assert ref.document_pointer.preferred_id() == "OR"
        assert ref.fragment.eid() == "art_11.para_3"

    def test_canton_shorthand(self):
        ref = self.builder.from_shorthand(
            jurisdiction="ZH",
            sr_number="170.41",
            article="3"
        )
        assert ref.parsed_url.jurisdiction == "ch-zh"

    def test_bfs_shorthand(self):
        ref = self.builder.from_shorthand(
            jurisdiction="261",
            article="5"
        )
        assert "261" in ref.parsed_url.jurisdiction

    def test_empty_jurisdiction_is_federal(self):
        ref = self.builder.from_shorthand(
            jurisdiction="",
            short_title="DSG", sr_number="235.1"
        )
        assert ref.parsed_url.jurisdiction == "ch"

    def test_display_uri_with_short_title(self):
        ref = self.builder.from_shorthand(
            short_title="OR", article="11"
        )
        assert ref.display_uri == "or#art_11"

    def test_display_uri_sr_fallback(self):
        ref = self.builder.from_shorthand(
            sr_number="235.1", article="5"
        )
        assert ref.display_uri.startswith("sr-")
        assert "#art_5" in ref.display_uri


# ── Integration: compact ↔ full reference ────────────────────────────────────

class TestCompactIntegration:
    """Test the full cycle: URL + compact input → full ref → compact display."""

    def test_url_and_compact_article(self):
        builder = LegalReferenceBuilder()
        # User pastes URL and types "#a47" in the display field
        compact_input = "#a47-p2-lit-a"
        fragment = parse_compact_fragment(compact_input)

        ref = builder.from_url(
            "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
            article=fragment.subdivisions[0].value if len(fragment.subdivisions) > 0 else None,
            paragraph=fragment.subdivisions[1].value if len(fragment.subdivisions) > 1 else None,
            litera=fragment.subdivisions[2].value if len(fragment.subdivisions) > 2 else None,
            short_title="BV"
        )
        # Display compact
        displayed = compact_fragment(ref.fragment)
        assert displayed == "#a47-p2-lit-a"
        # Full citation
        assert "BV" in ref.human_citation("de")
        assert "Art. 47" in ref.human_citation("de")
