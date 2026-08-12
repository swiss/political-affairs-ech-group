# Fedlex SKOS controlled vocabularies (SPARQL pull)

Live pull from `https://fedlex.data.admin.ch/sparqlendpoint` against the 10 SKOS
`ConceptScheme`s named by title. Generated 2026-07-30. Queries used:

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
# 1. find the scheme URI for a known German dct:title (or skos:prefLabel):
SELECT ?scheme ?p ?label WHERE {
  ?scheme a skos:ConceptScheme .
  { ?scheme skos:prefLabel ?label } UNION { ?scheme <http://purl.org/dc/terms/title> ?label }
  FILTER(lang(?label) = "de" || lang(?label) = "")
}

# 2. list members of a scheme (the endpoint stores many duplicate triples across
#    internal graphs, so joining `?concept a skos:Concept` as a BGP pattern
#    multiplies rows -- use FILTER EXISTS/NOT EXISTS instead, and SELECT DISTINCT):
SELECT DISTINCT ?concept ?notation ?label WHERE {
  ?concept skos:inScheme <SCHEME_URI> .
  FILTER EXISTS   { ?concept a skos:Concept }
  FILTER NOT EXISTS { ?concept a skos:Collection }   # excludes admin grouping nodes
  OPTIONAL { ?concept skos:notation ?notation }
  OPTIONAL { ?concept skos:prefLabel ?label . FILTER(lang(?label)="de") }
}
```

## Summary

| # | German title (as given) | Scheme URI | Expected count | Live count | Match |
|---|---|---|---|---|---|
| 1 | Erlassarten | `legal-resource-genre` | 4 | 4 | ✓ |
| 2 | Gliederungseinheiten des Textes | `subdivision-type` | 19 | 20 | ⚠ (+1) |
| 3 | Arten des Entscheides des Bundesrates bezüglich eines zu publizierenden Textes | `task-result-type` | 3 | 3 | ✓ |
| 4 | Projekttypen und Ereignisse der Rechtsetzung | `type-projet` | 26 | 26 | ✓ |
| 5 | Publikationsformate | `user-format` | 19 | 19 | ✓ |
| 6 | Rechtsnatur des Vertragsakts | `notification-type` | 9 | 9 | ✓ |
| 7 | Status der Verträge | `treaty-status` | 6 | 6 | ✓ |
| 8 | Dokumententypen des Vernehmlassungsverfahrens | `draft-document-type` | 13 | 13 | ✓ |
| 9 | Klassifizierung der sektoriellen Abkommen mit der Europäischen Union | `eutext-subject-theme` | 24 | 24 | ✓ |
| 10 | Texttypen | `resource-type` | 85 | 83 | ⚠ (-2) |

**Two discrepancies, investigated live (not guessed):**

- **`subdivision-type`** (Gliederungseinheiten des Textes): live has 20, not 19. The extra
  concept is `subdivision-type/scope` ("Geltungsbereich" / scope-of-application marker),
  `euvoc:status = CURRENT`, `owl:deprecated = false`, `jolux:order = 165` — the highest order
  value in the scheme, i.e. it looks like the most recently appended member. Everything else
  in the scheme is a genuine AKN-style structural subdivision (article, chapter, part, ...).
  Most likely explanation: the vocabulary grew by one entry after whatever count you're
  comparing against was fixed — not a query artefact. 4 further `skos:Collection` grouping
  nodes (`collection/article`, `collection/migration`, `collection/part-of-text`,
  `collection/titre`) are correctly excluded already (they're administrative groupers, not
  concepts).

- **`resource-type`** (Texttypen): live has 83 real `skos:Concept`s (52 `CURRENT`, 29
  `DEPRECATED`, 2 with no status) plus 3 `skos:Collection` grouping nodes (`act-category`,
  `text-type`, `treaty`) = 86 total entries either way. **No combination of these lands on
  85** (83, 86, and 84 if exactly one collection is included are all I can construct) —
  flagging this honestly as unresolved rather than forcing a match. If you have the eCH-0296
  source document that quotes 85, a byte-level diff against this list would settle it.

The other 8 schemes match the given counts exactly once `skos:Collection` grouping nodes are
excluded from the concept count (this alone explains the apparent mismatches for
`user-format` 22→19, `notification-type` 10→9, `draft-document-type` 16→13 seen in a first,
naive pull).

## 1. Erlassarten

Scheme: `https://fedlex.data.admin.ch/vocabulary/legal-resource-genre` — 4 concepts

| Notation | Concept URI | German label |
|---|---|---|
| A | `legal-resource-genre/200` | Änderungserlass |
| G | `legal-resource-genre/100` | Grunderlass |
| M | `legal-resource-genre/300` | Mantelerlass |
| X | `legal-resource-genre/900` | Andere |

## 2. Gliederungseinheiten des Textes

Scheme: `https://fedlex.data.admin.ch/vocabulary/subdivision-type` — 20 concepts

| Notation | Concept URI | German label |
|---|---|---|
| a, art | `subdivision-type/art` | Artikel |
| annex | `subdivision-type/annex` | Anhang |
| book | `subdivision-type/book` | Abteilung |
| chap | `subdivision-type/chap` | Kapitel |
| dfin | `subdivision-type/dfin` | Schlussbestimmungen |
| dtrans | `subdivision-type/dtrans` | Übergangsbestimmungen |
| index, text | `subdivision-type/text` | Erlass |
| lvl | `subdivision-type/lvl` | Stufe |
| maintext | `subdivision-type/maintext` | Textkörper |
| para | `subdivision-type/para` | Absatz |
| part | `subdivision-type/part` | Teil |
| preamb | `subdivision-type/preamb` | Ingress |
| preface | `subdivision-type/preface` | Vorspann |
| sec | `subdivision-type/sec` | Abschnitt |
| subch | `subdivision-type/subch` | Unterkapitel |
| subsec | `subdivision-type/subsec` | Unterabschnitt |
| tfin | `subdivision-type/tfin` | Schlusstitel |
| tit | `subdivision-type/tit` | Titel |
| — | `subdivision-type/expr` | Ausdruck |
| — | `subdivision-type/scope` | Geltungsbereich |

## 3. Arten des Entscheides des Bundesrates bezüglich eines zu publizierenden Textes

Scheme: `https://fedlex.data.admin.ch/vocabulary/task-result-type` — 3 concepts

| Notation | Concept URI | German label |
|---|---|---|
| 1 | `task-result-type/1` | gem. Antrag |
| 2 | `task-result-type/2` | gem. Mitberichtsverfahren |
| 3 | `task-result-type/3` | gem. Mitberichtsverfahren und Beratung |

## 4. Projekttypen und Ereignisse der Rechtsetzung

Scheme: `https://fedlex.data.admin.ch/vocabulary/type-projet` — 26 concepts

| Notation | Concept URI | German label |
|---|---|---|
| 1, cons | `type-projet/1` | Vernehmlassung |
| 2 | `type-projet/2` | Erlassentwurf |
| 3, cons-planif | `type-projet/3` | Geplante Vernehmlassungen |
| 4, cons-open | `type-projet/4` | Eröffnung der Vernehmlassung |
| 5, cons-pos | `type-projet/5` | Veröffentlichung der Stellungnahmen |
| 6, cons-result | `type-projet/6` | Veröffentlichung des Ergebnisberichts |
| 200, mess | `type-projet/200` | Botschaft des Bundesrats |
| 201 | `type-projet/201` | Stellungnahme des Bundesrates |
| 300, final-vote | `type-projet/300` | Beschluss des Parlaments |
| 301 | `type-projet/301` | Bericht Kommission |
| 400 | `type-projet/400` | Ablauf der Referendumsfrist am |
| 450 | `type-projet/450` | Referendum eingereicht am |
| 480 | `type-projet/480` | Ref. Zustandegekommen |
| 490 | `type-projet/490` | Ref. nicht zustandegekommen |
| 630, date-votation | `type-projet/630` | Festlegung Abstimmungsgegenstände BR |
| 650 | `type-projet/650` | Abgestimmt am |
| 700 | `type-projet/700` | Inkrafttreten am |
| 701 | `type-projet/701` | Teilinkraftsetzung |
| 710 | `type-projet/710` | Geändert in anderem Erlass |
| 715 | `type-projet/715` | Berichtigung |
| 716 | `type-projet/716` | Mitteilung |
| 720 | `type-projet/720` | Aufgehoben in anderem Erlass |
| 900 | `type-projet/900` | Anderweitig erledigt |
| publ | `type-projet/9` | — |
| — | `type-projet/7` | Publikation der Eröffnung der Vernehmlassung |
| — | `type-projet/8` | Publikation der Eröffnung im BBl |

## 5. Publikationsformate

Scheme: `https://fedlex.data.admin.ch/vocabulary/user-format` — 19 concepts

| Notation | Concept URI | German label |
|---|---|---|
| doc | `user-format/doc` | Dokument doc |
| doc, doc-an | `user-format/doc-an` | anonymisiertes Dokument doc |
| docx | `user-format/docx` | Dokument docx |
| docx, docx-an | `user-format/docx-an` | anonymisiertes Dokument doc |
| html | `user-format/html` | html |
| html, html-an | `user-format/html-an` | anonymisiertes HTML |
| jpg | `user-format/jpeg` | JPEG Bild |
| link | `user-format/url` | url |
| pdf | `user-format/pdf` | pdf |
| pdf, pdf-a | `user-format/pdf-a` | authentifiziertes pdf |
| pdf, pdf-a-an | `user-format/pdf-a-an` | authentifiziertes anonymisiertes pdf |
| pdf, pdf-sig | `user-format/pdf-sig` | signiertes pdf |
| pdf, pdf-x | `user-format/pdf-x` | pdf x |
| print | `user-format/print` | Papier |
| xls | `user-format/xls` | Dokument xls |
| xlsx | `user-format/xlsx` | Dokument xlsx |
| xml | `user-format/xml` | xml AkomaNtoso |
| xml, xml-an | `user-format/xml-an` | anonymisiertes xml AkomaNtoso |
| zip | `user-format/zip` | zip file |

## 6. Rechtsnatur des Vertragsakts

Scheme: `https://fedlex.data.admin.ch/vocabulary/notification-type` — 9 concepts

| Notation | Concept URI | German label |
|---|---|---|
| AP | `notification-type/2` | Provisorische Anwendung |
| SI | `notification-type/1` | Unterzeichnung |
| — | `notification-type/0` | Diverse Informationen |
| — | `notification-type/3` | Ratifikation |
| — | `notification-type/4` | Inkrafttreten |
| — | `notification-type/5` | Kündigung |
| — | `notification-type/6` | Unterzeichnung ohne Ratifikationsvorbehalt |
| — | `notification-type/7` | Vorbehalte und Erklärungen |
| — | `notification-type/8` | Einwendungen |

## 7. Status der Verträge

Scheme: `https://fedlex.data.admin.ch/vocabulary/treaty-status` — 6 concepts

| Notation | Concept URI | German label |
|---|---|---|
| — | `treaty-status/1` | abgeschlossen (drafts) |
| — | `treaty-status/2` | in Kraft |
| — | `treaty-status/3` | unterzeichnet |
| — | `treaty-status/4` | provisorische Anwendung |
| — | `treaty-status/5` | abgelaufen |
| — | `treaty-status/6` | ratifiziert |

## 8. Dokumententypen des Vernehmlassungsverfahrens

Scheme: `https://fedlex.data.admin.ch/vocabulary/draft-document-type` — 13 concepts

| Notation | Concept URI | German label |
|---|---|---|
| 1, doc-broader | `draft-document-type/10` | Unterlagen |
| 2, avis-broader | `draft-document-type/20` | Stellungnahmen |
| 3, result-broader | `draft-document-type/30` | Ergebnis |
| 4, draft | `draft-document-type/11` | Vernehmlassungsvorlage |
| 5, report | `draft-document-type/12` | Erläuternder Bericht |
| 6, letter | `draft-document-type/13` | Begleitschreiben |
| 7, recipient-list | `draft-document-type/14` | Adressatenliste |
| 8, various-text | `draft-document-type/15` | Diverses |
| 9, opinion | `draft-document-type/21` | Stellungnahmen |
| 10, final-report | `draft-document-type/31` | Ergebnisbericht |
| 11, response-form | `draft-document-type/22` | Antwortformular |
| 12, survey | `draft-document-type/23` | Fragebogen |
| synoptic-table | `draft-document-type/16` | Synoptische Tabelle |

## 9. Klassifizierung der sektoriellen Abkommen mit der Europäischen Union

Scheme: `https://fedlex.data.admin.ch/vocabulary/eutext-subject-theme` — 24 concepts

| Notation | Concept URI | German label |
|---|---|---|
| 1 | `eutext-subject-theme/1` | Forschung |
| 2 | `eutext-subject-theme/2` | Öffentliches Beschaffungswesen |
| 3 | `eutext-subject-theme/3` | Technische Handelshemmnisse |
| 4 | `eutext-subject-theme/4` | Landwirtschaft |
| 5 | `eutext-subject-theme/5` | Luftverkehr |
| 6 | `eutext-subject-theme/6` | Landverkehr |
| 7 | `eutext-subject-theme/7` | Personenverkehr |
| 8 | `eutext-subject-theme/8` | Schengen |
| 9 | `eutext-subject-theme/9` | Dublin |
| 10 | `eutext-subject-theme/10` | Zinsbesteuerung |
| 11 | `eutext-subject-theme/11` | Betrugsbekämpfung |
| 12 | `eutext-subject-theme/12` | Verarbeitete Landwirtschaftsprodukte |
| 13 | `eutext-subject-theme/13` | Umwelt |
| 14 | `eutext-subject-theme/14` | Statistik |
| 15 | `eutext-subject-theme/15` | MEDIA |
| 16 | `eutext-subject-theme/16` | Ruhegehälter |
| 17 | `eutext-subject-theme/17` | Freihandel |
| 18 | `eutext-subject-theme/18` | Versicherung |
| 19 | `eutext-subject-theme/19` | Güterverkehr |
| 20 | `eutext-subject-theme/20` | Jugend in Aktion und lebenslanges Lernen |
| 21 | `eutext-subject-theme/21` | Europäische Satellitennavigationsprogramme |
| 22 | `eutext-subject-theme/22` | Wettbewerbsrecht |
| 23 | `eutext-subject-theme/23` | Emissionshandel |
| 24 | `eutext-subject-theme/24` | Prümer Zusammenarbeit |

## 10. Texttypen

Scheme: `https://fedlex.data.admin.ch/vocabulary/resource-type` — 83 concepts

| Notation | Concept URI | German label |
|---|---|---|
| 101 | `resource-type/55` | Obligatorisches Referendum |
| 102, 110, 120 | `resource-type/10` | Bundesbeschluss der dem obligatorschen Referendum untersteht |
| 130 | `resource-type/65` | Dringlicher BB ohne Verfassungsgrundlage, Laufzeit >1 Jahr |
| 140 | `resource-type/66` | Dringlicher BB ohne Verfassungsgrundlage, Laufzeit <1 Jahr |
| 150 | `resource-type/67` | Plebiszit |
| 160 | `resource-type/68` | Verfahrensleitender Entscheid |
| 201 | `resource-type/54` | Fakultatives Referendum |
| 211, 212, 213 | `resource-type/36` | Bundesbeschluss der dem fakultativen Referendum untersteht (Verträge) |
| 214 | `resource-type/69` | Staatsvertragsreferendum Art. 141 Abs. 2 |
| 220 | `resource-type/22` | Dringliches Bundesgesetz |
| 281 | `resource-type/70` | Staatsvertragsreferendum Art. 89 Abs. 3 Bst a |
| 282 | `resource-type/71` | Staatsvertragsreferendum Art. 89 Abs. 3 Bst b |
| 283 | `resource-type/72` | Staatsvertragsreferendum Art. 89 Abs. 3 Bst c |
| 284 | `resource-type/73` | Staatsvertragsreferendum Art. 89 Abs. 4 |
| 291 | `resource-type/74` | Dringlicher BB mit Verfassungsgrundlage, Laufzeit >1 Jahr |
| 292 | `resource-type/75` | Dringlicher BB mit Verfassungsgrundlage, Laufzeit <1 Jahr |
| 300 | `resource-type/19` | Gewährleistungen Kantonsverfassung |
| 310 | `resource-type/76` | Allgemeinverbindlicher Bundesbeschluss |
| 311, 510 | `resource-type/28` | Verordnung der Bundesversammlung |
| 320 | `resource-type/62` | Einfacher Bundesbeschluss |
| 330 | `resource-type/29` | Verordnung des Bundesrates |
| 340 | `resource-type/26` | Departementsverordnung |
| 350 | `resource-type/27` | Amtsverordnung |
| 360 | `resource-type/15` | Verträge zwischen Bund und Kantonen |
| 370 | `resource-type/81` | Vom Bundesrat genehmigter Erlass |
| 380 | `resource-type/14` | Mitteilung über Aufhebungen (Text gegenstandslos) oder Änderungen |
| 390 | `resource-type/16` | Kantonsverfassung |
| 400 | `resource-type/77` | Referendumspflichtiger Erlass in anderem BG |
| 410 | `resource-type/78` | Referendumspflichtiger Erlass in Verordnung |
| 520 | `resource-type/5` | Erlass des Nationalrates |
| 530 | `resource-type/4` | Erlass des Ständerates |
| 540 | `resource-type/2` | Erlass von Kommissionen |
| 600 | `resource-type/3` | Erlass der eidg. Gerichte |
| 700 | `resource-type/1` | Erlass selbständiger Betriebe und Anstalten |
| 900 | `resource-type/80` | Redundanter Titel |
| 901 | `resource-type/31` | Internationaler Rechtstext bilateral |
| 902 | `resource-type/32` | Internationaler Rechtstext multilateral |
| 903 | `resource-type/11` | Geltungsbereich eines Vertrags |
| 1001 | `resource-type/23` | Botschaft des Bundesrates |
| 1002 | `resource-type/63` | Bericht (oder Stellungnahme) des Bundesrates |
| 1003 | `resource-type/30` | Bericht parlamentarische Kommission |
| 1004 | `resource-type/17` | Berichtigung AS |
| 1005 | `resource-type/53` | Behördliche Beschlüsse und Bekanntmachungen, Anzeigen |
| 1006 | `resource-type/79` | Mitteilung AS |
| 1007 | `resource-type/64` | Bundesratsbeschlüsse, Weisungen, Vereinbarungen, Konzessionen |
| — | `resource-type/12` | Kreisschreiben des Bundesrates an die Kantonsregierungen |
| — | `resource-type/13` | Mitteilung |
| — | `resource-type/18` | Weisungen des Bundesrates |
| — | `resource-type/20` | Hinweis auf Erlasse der Bundesversammlung die erst später veröffentlicht werden |
| — | `resource-type/21` | Bundesgesetz |
| — | `resource-type/24` | Bericht des Bundesrates |
| — | `resource-type/25` | Stellungnahme des Bundesrates |
| — | `resource-type/33` | Beschlüsse der Behörde |
| — | `resource-type/34` | Vereinbarungen des Bundesrats |
| — | `resource-type/35` | Dringliches Bundesgesetz das dem obligatorschen Referendum untersteht |
| — | `resource-type/37` | Berichtigung BBl |
| — | `resource-type/38` | Erlassentwurf |
| — | `resource-type/39` | Vorentwurf Erlass |
| — | `resource-type/40` | Eröffnung des Vernehmlassungsverfahrens |
| — | `resource-type/46` | Bundesverfassung, Bundesgesetze und Bundesbeschlüsse |
| — | `resource-type/47` | Verordnungen |
| — | `resource-type/48` | Andere Erlassformen |
| — | `resource-type/49` | Internationale Rechtstexte |
| — | `resource-type/50` | Botschaften und Berichte |
| — | `resource-type/51` | Diverse Texte (BBl, AS) |
| — | `resource-type/52` | Entwürfe |
| — | `resource-type/56` | Obligatorisches Staatsvertragsreferendum |
| — | `resource-type/57` | Eidg. Volksinitiative (Ausgearbeiteter Entwurf) |
| — | `resource-type/58` | Eidg. Volksinitiative (Allgemeine Anregung) |
| — | `resource-type/59` | Staatsvertragsreferendum Art. 141 Abs. 1 Bst. d Ziff. 1 |
| — | `resource-type/6` | Bundesratsbeschluss |
| — | `resource-type/60` | Staatsvertragsreferendum Art. 141 Abs. 1 Bst. d Ziff. 2 |
| — | `resource-type/61` | Staatsvertragsreferendum Art. 141 Abs. 1 Bst. d Ziff. 3 |
| — | `resource-type/7` | Einfacher Bundesbeschluss (Genehmigung Verträge) |
| — | `resource-type/8` | Einfacher Bundesbeschluss (andere) |
| — | `resource-type/82` | Notifikationen |
| — | `resource-type/83` | Diverse Texte (Internationales Recht) |
| — | `resource-type/84` | Schlussabstimmungstext |
| — | `resource-type/85` | Zu genehmigender internationaler Rechtstext |
| — | `resource-type/86` | Vereinbarungen selbständiger Betriebe und Anstalten |
| — | `resource-type/87` | Strategie und Ziele |
| — | `resource-type/88` | Konzessionen |
| — | `resource-type/9` | Bundesbeschluss der dem fakultativen Referendum untersteht (Andere) |
