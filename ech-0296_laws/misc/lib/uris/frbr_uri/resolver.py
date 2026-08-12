"""
frbr_uri/resolver.py
tags: akn, frbr, resolver

FRBR URI Resolver for AKN documents.

Loads jurisdiction profiles from the `profiles/` directory (bundled or user-supplied)
and resolves Work, Expression, Manifestation, and Item URIs according to
Akoma Ntoso 3.0 naming conventions.

Usage:
    from frbr_uri.resolver import FRBRResolver

    r = FRBRResolver()
    uris = r.resolve(
        jurisdiction="ch-zh",
        doc_type="act",
        date="2024-01-15",
        number="170.4",
        lang="de",
        version="2024-01-15",
        format="xml"
    )
    print(uris.work)
    print(uris.expression)
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

# ── Profile directory ───────────────────────────────────────────────────────
# Bundled profiles live next to this file. Users can supply extra directories.
_BUNDLED_PROFILES = Path(__file__).parent / "profiles"


# ── Data classes ─────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class FRBRUris:
    """Four FRBR levels for a single document."""
    work: str
    expression: str
    manifestation: str
    item: Optional[str]
    jurisdiction: str
    doc_type: str
    akn_doc_type: str
    subtype: str


@dataclass(frozen=True)
class ResolvedProfile:
    """A loaded and parsed jurisdiction profile."""
    jurisdiction: str
    level: str
    name: str
    akn_prefix: str
    language_codes: dict[str, str]
    default_language: str
    document_types: dict[str, dict]
    uri_templates: dict[str, str]
    raw: dict


# ── Resolver ─────────────────────────────────────────────────────────────────

class FRBRResolver:
    """
    Resolves AKN FRBR URIs for Swiss jurisdictions.

    Profiles are loaded from:
      1. The bundled `profiles/` directory (ch.json, ch-zh.json, etc.)
      2. Any additional directories passed as `extra_profile_dirs`

    Later-loaded profiles override earlier ones (user profiles win over bundled).
    """

    def __init__(self, extra_profile_dirs: Optional[list[Path | str]] = None):
        self._profiles: dict[str, ResolvedProfile] = {}
        self._load_dir(_BUNDLED_PROFILES)
        for d in (extra_profile_dirs or []):
            self._load_dir(Path(d))

    # ── Loading ──────────────────────────────────────────────────────────────

    def _load_dir(self, directory: Path) -> None:
        if not directory.is_dir():
            return
        for path in sorted(directory.glob("*.json")):
            if path.name.startswith("profile.schema"):
                continue
            try:
                self._load_profile(path)
            except Exception as exc:
                # Don't crash on a malformed community profile; warn instead.
                print(f"[frbr-uri] Warning: could not load profile {path.name}: {exc}")

    def _load_profile(self, path: Path) -> None:
        with path.open(encoding="utf-8") as f:
            raw = json.load(f)
        jid = raw.get("jurisdiction")
        if not jid:
            raise ValueError("Profile missing 'jurisdiction' field")
        self._profiles[jid] = ResolvedProfile(
            jurisdiction=jid,
            level=raw.get("level", "other"),
            name=raw.get("name", jid),
            akn_prefix=raw["akn_prefix"],
            language_codes=raw.get("language_codes", {}),
            default_language=raw.get("default_language", "de"),
            document_types=raw.get("document_types", {}),
            uri_templates=raw["uri_templates"],
            raw=raw,
        )

    # ── Public API ───────────────────────────────────────────────────────────

    def list_jurisdictions(self) -> list[dict]:
        """Return a summary list of all loaded jurisdictions."""
        return [
            {
                "jurisdiction": p.jurisdiction,
                "level": p.level,
                "name": p.name,
                "languages": list(p.language_codes.keys()),
                "document_types": list(p.document_types.keys()),
            }
            for p in sorted(self._profiles.values(), key=lambda x: x.jurisdiction)
        ]

    def get_profile(self, jurisdiction: str) -> ResolvedProfile:
        """Return the profile for a jurisdiction id, raising KeyError if not found."""
        if jurisdiction not in self._profiles:
            available = ", ".join(sorted(self._profiles.keys()))
            raise KeyError(
                f"Unknown jurisdiction '{jurisdiction}'. "
                f"Available: {available}"
            )
        return self._profiles[jurisdiction]

    def resolve(
        self,
        jurisdiction: str,
        doc_type: str,
        date: str,
        number: str,
        lang: Optional[str] = None,
        version: Optional[str] = None,
        format: str = "xml",
        component: Optional[str] = None,
    ) -> FRBRUris:
        """
        Resolve all four FRBR URIs for a document.

        Args:
            jurisdiction: Profile key, e.g. 'ch', 'ch-zh', 'ch-zg', 'ch-vd-5586'
            doc_type:     Document type key from the profile, e.g. 'act', 'ordinance'
            date:         Date string, YYYY-MM-DD (enactment / entry-into-force date)
            number:       Official document number (e.g. '170.4', '2024-15')
            lang:         2-letter language code; defaults to profile default
            version:      Version date (YYYY-MM-DD) or 'current'; defaults to date
            format:       Manifestation format: 'xml', 'html', 'pdf'
            component:    Item component name (e.g. 'main', 'annex-1')

        Returns:
            FRBRUris with all resolved URI strings
        """
        profile = self.get_profile(jurisdiction)
        doc_def = self._resolve_doc_type(profile, doc_type)

        # Language
        lang_2 = lang or profile.default_language
        lang_3 = profile.language_codes.get(lang_2)
        if not lang_3:
            raise ValueError(
                f"Language '{lang_2}' not supported by jurisdiction '{jurisdiction}'. "
                f"Supported: {list(profile.language_codes.keys())}"
            )

        # Version
        version_str = version or date

        # Sanitize number for URI (spaces → hyphens, keep dots)
        number_uri = re.sub(r"\s+", "-", number.strip())

        # Validate date format loosely
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            raise ValueError(f"Date must be YYYY-MM-DD, got '{date}'")

        ctx = {
            "doc_type": doc_def["subtype"],
            "date": date,
            "number": number_uri,
            "lang": lang_3,
            "version": version_str,
            "format": format,
            "component": component or "main",
        }

        templates = profile.uri_templates
        return FRBRUris(
            work=self._fill(templates["work"], ctx),
            expression=self._fill(templates["expression"], ctx),
            manifestation=self._fill(templates["manifestation"], ctx),
            item=self._fill(templates["item"], ctx) if "item" in templates else None,
            jurisdiction=jurisdiction,
            doc_type=doc_type,
            akn_doc_type=doc_def["akn_type"],
            subtype=doc_def["subtype"],
        )

    def resolve_work(self, jurisdiction: str, doc_type: str, date: str, number: str) -> str:
        """Convenience: return only the Work URI."""
        return self.resolve(jurisdiction, doc_type, date, number).work

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _resolve_doc_type(self, profile: ResolvedProfile, doc_type: str) -> dict:
        if doc_type not in profile.document_types:
            available = ", ".join(profile.document_types.keys())
            raise KeyError(
                f"Document type '{doc_type}' not defined for jurisdiction "
                f"'{profile.jurisdiction}'. Available: {available}"
            )
        return profile.document_types[doc_type]

    @staticmethod
    def _fill(template: str, ctx: dict) -> str:
        """Fill a URI template with context values."""
        result = template
        for key, value in ctx.items():
            result = result.replace(f"{{{key}}}", str(value))
        # Detect unfilled placeholders
        missing = re.findall(r"\{[^}]+\}", result)
        if missing:
            raise ValueError(f"URI template has unfilled placeholders: {missing}")
        return result
