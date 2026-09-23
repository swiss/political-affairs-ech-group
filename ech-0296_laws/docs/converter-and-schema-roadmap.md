# eCH-0296 — Schema- & Konverter-Fahrplan

Ergebnis der Design-Session. Die grundlegenden Entscheidungen liegen in `docs/adr/`; dieses Dokument leitet daraus die konkrete Arbeit ab.

## Entscheidungen (ADRs)

- **ADR-0001** — LinkML ist Source of Truth; die generierte XSD + Schematron müssen die **reale, unveränderte SR-101** validieren.
- **ADR-0002** — Inline-/Mixed-Content wird als echte Klassen modelliert (`InlineElement`-Basis: `TextRun, Ref, B, I, Sup, Span, AuthorialNote, Inline, Placeholder, Br` + `Mod/Ins/Del`), diskriminiert über einen `designates_type`-Slot (`element_type`).
- **ADR-0003** — Ein publisher-neutrales `schema.yaml`; Aufteilung in Core + Profile erst bei zweitem Profil (Kanton).
- **ADR-0004** — Commons via AKN-native Erweiterungspunkte (`PersonReference`/`GroupReference` → `FRBRauthor`/`TLCOrganization` `@href`-CURIE; `global_uri` in `meta/proprietary`).
- **ADR-0005** — Validierung gesplittet: **XSD 1.0 trägt ~90 %** der Fedlex-Regeln (Contentmodelle, Pflicht-Attribute, Attribut-Enums, `xs:unique`); ein **3-Regel-Schematron** trägt `FLX-HR-003`, `FLX-XF-002b`, `FLX-HR-001-lv` (transparentes level).

## Phasing (Beispiel & Round-trip)

- **Phase 1 (jetzt):** handgeschriebenes `input/data_sr101_excerpt.yaml` → Vorwärts-Generierung → validiert; speist Word/JSON-Doku-Pipeline.
- **Phase 2 (später):** Rückwärts-Konverter (AKN-XML → LinkML), voller SR-101-Round-trip.

## Schema-Anpassungen (`input/schema.yaml`)

> **Status:** Die vom Coverage-Report gefundenen Schema-Lücken sind geschlossen
> (Mapping 37 → **53/53**). Erledigt: FRBR-Wertelemente als `@value`-Halter
> (`ValueType`/`UriValueType`/`LanguageType`/`FormatType`), Inline-Modell nach
> ADR-0002 (`InlineElement` + 10 Subklassen, `MixedText`), fehlende Attribute
> (`fedlex:rs/rs-uri/message`, `border`, `colspan`, `language`), `BlockListItem`
> auf `item → num + p` korrigiert. Das Backlog im Report ist jetzt **rein
> Konverter** (ATTR, CHOICE, MIXED). Offen unten: neutrale Umbenennung (ADR-0003)
> und die Commons-Anbindung (ADR-0004).

1. `FedlexDocument` → publisher-neutraler Name (`LegalText`); Fedlex-Spezifika als markierte Profil-Schicht (Mixins + `slot_usage`).
2. Inline-Modell nach ADR-0002 hinzufügen; `text_content: XmlContent(str)` ersetzen durch `inline_content: [InlineElement]` (geordnet, multivalued, inlined). `AuthorialNote` rekursiv in Block-Content, `Ref` rekursiv in `inline_content`.
3. `Proprietary`-Klasse + Import von `schema_common` (nur `PersonReference`/`GroupReference` genutzt).
4. `fedlex_role` exakt: pro Klasse restringiertes Enum (`Level` → `{marginal}`, `Subheading` → `{reference}`) statt einem gemeinsamen `{marginal,reference}`.
5. Contentmodell-Reihenfolge sicherstellen: `num?, heading?, subheading?` zuerst (deckt `FLX-HD-*`).
6. `schematron_rule:`-Annotationen von Doku → maschinenlesbar für die 3 Rest-Regeln (z. B. `schematron_assert: {id, test, msg}`).

## Konverter-Backlog (`/Users/christian/Bitbucket/linkml`), nach Abhängigkeit

Der Abdeckungsreport (siehe unten) hält den Live-Status; dies ist die geplante Reihenfolge.

> **Status: NORDSTERN ERREICHT.** Phase 0–3 erledigt
> (`linkml/src/linkml_to_xsd/converter.py`). **Die reale, unveränderte SR-101
> validiert gegen die aus LinkML generierte XSD** (ADR-0001) — Coverage
> **53/53**, Backlog leer. 23 Tests grün (inkl. SR-101-Regressionstest), ruff
> sauber. Der Weg dahin fand 4 Schema-Lücken (FRBRdate/@name als Element statt
> Attribut, `td` trägt Block- statt Inline-Inhalt, `preface > p > docNumber`,
> Hierarchie-Kinder `article`/`level` unter title/proviso) und einen Domänen-
> befund: **Fedlex-eIds sind nicht eindeutig** (`docs/adr/0006`).

- **Phase 0 — Fundament. ✅** Annotationen (`xml_element`, `xml_attribute`, `xml_name`, `xml_namespace`) werden gelesen; String-Typen werden jetzt als `simpleType` emittiert (behebt hängende Typ-Referenzen). *(Offen: die zwischen `converter.py` und `xml_generator.py` duplizierte `_class_slots`-Logik in einen gemeinsamen Kern ziehen — sobald `xml_generator.py` in Phase 3 angefasst wird.)*
- **Phase 1 — XML-Grundlagen. ✅** Slot→`xs:attribute` (inkl. `use="required"`, `xml_name`); Element-Name aus `xml_element`/`xml_name`/Range-Klasse; `targetNamespace`=AKN aus Annotation; `anyAttribute namespace="##other"` (AKNs `core`-Muster) absorbiert `fedlex:`/`xml:`/Tooling-Namespaces statt `xml.xsd`-Import.
- **Phase 2 — Strukturregeln (die ~90 %). ✅** `xs:choice`-Contentmodelle über `xsd_content_model: choice` (Überschriften-Präfix `num?/heading?/subheading?` als Sequenz, dann `xs:choice maxOccurs=unbounded`) auf 15 Container-Klassen; `xs:unique` für eId-Eindeutigkeit auf der tree_root. *(Offen/verschoben: pro-Klasse restringierte `fedlex:role`-Enums — als Fremd-Attribut läuft `fedlex:role` über die `anyAttribute`-Wildcard, daher bleibt die Werteinschränkung FLX-XF-003/004/005 vorerst beim 3-Regel-Schematron aus ADR-0005.)*
- **Phase 3 — Mixed Content. ✅** `xsd_mixed`/polymorphe `inline_content` → `mixed="true"` + `xs:choice` über die konkreten `InlineElement`-Subklassen; `designates_type` (`element_type`) und `TextRun` werden in XSD übersprungen (Text deckt `mixed` ab); abstrakte Basis wird nicht als Extension-Basis genutzt; globale Element-Namen dedupliziert (`akn:p` als Mixed-Absatz *und* Preface-Wrapper). **→ reale SR-101 validiert.**
- **Phase 4a — Rest-Schematron. ✅** Die 3 Regeln (`FLX-HR-003`, `FLX-XF-002`, transparentes `FLX-HR-001-lv`) werden aus LinkML generiert — über den neuen Profil-Hook `schematron_patterns` (`profile/akn.py`) + `schematron/spec.py`, gerendert als **XPath 1.0**, sodass lxmls ISO-Schematron sie ausführt. Befund: SR-101 erfüllt 2 der 3; **FLX-HR-003 wird von SR-101s eigenem Sachregister (`disp_u2`, A–Z) verletzt** — die Fedlex-Referenzdatei bricht ihre eigene Regel (`docs/adr/0007`). Nordstern-Schematron-Test grün, 171 Tests grün.
- **Phase 4b — Beispiel + Doku. ← als Nächstes.** `input/data_sr101_excerpt.yaml` schreiben (der Beispielgenerator `xml_generator.py` hat noch das `depth < 2`-Limit); Doku-Pipeline (`extract_examples`/`gen-doc`/`pandoc`) für ech-0296 verdrahten; `schematron`-CLI-Subcommand ergänzen.
- **Phase 5 — Commons & Reverse (später).** `meta/proprietary` + `@href`-CURIE-Serialisierung; Rückwärts-Konverter; optional XSD-1.1-Umstieg (`lxml`→`xmlschema`), falls die `xs:assert`-Regeln in die XSD sollen.

## Abdeckungsreport (lebendes Artefakt)

Skript im Konverter-Repo (`tools/coverage_report.py`): Eingabe `schema.yaml` + generierte XSD + SR-101; Ausgabe `coverage.md`. Zeilen = jedes AKN-Element/Attribut aus SR-101; Spalten = XML-Vorkommen | XSD-Anforderung | Schematron-Regel | LinkML-Klasse/Slot | benötigtes Konverter-Feature | Status (✅/Lücke). Die Status-Spalte ist das Live-Backlog; läuft in CI.

## Nordstern-Regressionstest

`SR-101-01012029-DE.xml` wird permanente Fixture: jede Schema-/Konverter-Änderung wird geprüft, indem die Datei erneut gegen die generierte XSD + das 3-Regel-Schematron validiert wird.
