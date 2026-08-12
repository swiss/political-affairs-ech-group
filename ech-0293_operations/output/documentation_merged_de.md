---
title: "eCH-0293 Öffentlicher Ratsbetrieb"
lang: de
toc: false
---

|**Name**|**Öffentlicher Ratsbetrieb**|
|---|---|
|**eCH-Nummer**|eCH-0293|
|**Kategorie**|Standard|
|**Reifegrad**|Definiert|
|**Version**|0.1.0|
|**Status**|In Arbeit|
|**Beschluss am**||
|**Ausgabedatum**||
|**Ersetzt Version**||
|**Voraussetzungen**||
|**Beilagen**|-|
|**Sprachen**|Deutsch (Original) - English (Datamodel)|
|**Autoren**|Fachgruppe Politische Geschäfte: Nicole Aeby, David Imseng, Jonas Schärer, Lena Mina Friedrich, Manuel Weingartner, Orhan Saeedi, Michel Moret, Laurens Abu-Talib|
|**Herausgeber / Vertrieb**|Verein eCH, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)|

\newpage

# Abstrakt

Der Standard eCH-0293 definiert ein gemeinsames Datenmodell für die Erfassung und Publikation von Informationen zum öffentlichen Ratsbetrieb in der Schweiz. Er deckt die zeitliche Organisation parlamentarischer Arbeit (Legislaturperioden, Sessionen), die Strukturierung von Sitzungen und Traktanden, Abstimmungen und Wahlen, Einzelstimmen, Anwesenheitslisten sowie Wortmeldungen und Resolutionen ab.

Dieser Standard richtet sich an Parlamentsdienste, Softwareanbieterinnen und Softwareanbieter von Parlamentsverwaltungssystemen, Datennutzerinnen und Datennutzer für Analysen und Visualisierungen sowie an Open-Data-Plattformen.

eCH-0293 ist Teil einer Familie von Standards für politische Daten und arbeitet eng mit eCH-0294 (Politische Akteure), eCH-0295 (Parlamentarische Geschäfte), eCH-0296 (Erlasse und Gesetzestexte) und eCH-0297 (Öffentliche Konsultationen) zusammen.

\newpage

# Inhaltsverzeichnis

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \o "1-2" \h \z \u </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Rechtsklick &gt; „Felder aktualisieren“, um das Inhaltsverzeichnis zu erzeugen.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```

\newpage

# Einleitung

## Die Standardfamilie „Politische Geschäfte"

Das politische Geschehen der Schweiz findet auf Bundes-, Kantons- und Gemeindeebene statt – in Parlamenten und Gemeindeversammlungen, in Exekutiven und Verwaltungen, in Vernehmlassungen und Konsultationen sowie über die direktdemokratische Mitwirkung der Stimmberechtigten. Die Fachgruppe „Politische Geschäfte" des Vereins eCH entwickelt dafür eine Familie aufeinander abgestimmter Standards, welche diese Daten föderal übergreifend strukturieren. Die Standards nutzen gemeinsame Datenelemente (eCH-0292) und referenzieren sich gegenseitig über eindeutige Identifikatoren.

Die Familie umfasst:

- **eCH-0292 – Gemeinsame Datenelemente (Meta):** Definiert die übergreifend genutzten Datenelemente und Metaprozesse, auf denen die übrigen Standards aufbauen. eCH-0293 übernimmt daraus unter anderem die Identifikations- und Datumselemente sowie die FRBR-Struktur für verknüpfte Dokumente.
- **eCH-0293 – Öffentlicher Ratsbetrieb (Operations) – dieser Standard:** Beschreibt den öffentlichen Ratsbetrieb – Legislaturperioden und Sessionen, Sitzungen und Traktanden, Protokolle und Beschlüsse, Abstimmungen und Wahlen, Anwesenheiten sowie Wortmeldungen.
- **eCH-0294 – Politische Akteure (Actors):** Definiert Personen, Gruppen und Organe im politischen Kontext sowie deren Mitgliedschaften und Interessenbindungen. eCH-0293 referenziert diese Akteure über `actor_id` – etwa welches Parlament getagt und welche Person abgestimmt hat.
- **eCH-0295 – Parlamentarische Geschäfte (Affairs):** Beschreibt den Lebenszyklus politischer Geschäfte. Traktanden in eCH-0293 verweisen über `affair_id` auf das zugehörige Geschäft.
- **eCH-0296 – Erlasse und Gesetzestexte (Laws):** Erfasst die Resultate des parlamentarischen Prozesses – die verabschiedeten Gesetze und Erlasse.
- **eCH-0297 – Öffentliche Konsultationen (Consultations):** Strukturiert Vernehmlassungsverfahren, die oft Ausgangspunkt für parlamentarische Geschäfte sind.

Ziel dieser Standardfamilie ist es, eine gemeinsam nutzbare Struktur für politische Daten zu schaffen und Organisationen, die Informationen zu politischen Geschäften veröffentlichen, ein tragfähiges Datenmodell an die Hand zu geben.

## Aufbau einer Lieferung

Eine Lieferung ist ein `Container`: ein Umschlag mit einer eigenen `global_uri` und je einer Sammlung pro Klasse — `legislatures`, `sessions`, `meetings`, `agenda_items`, `protocols`, `votings`, `elections`, `individual_votes`, `attendances`, `individual_attendances`, `speeches` und `resolutions`. Alle Sammlungen sind optional: Wer nur Sitzungen veröffentlicht, liefert nur `meetings`.

Die Entitäten liegen darin flach nebeneinander und sind über Referenzen verbunden — `parent_meeting`, `parent_voting`, `parent_attendance` und so fort —, statt ineinander verschachtelt zu sein. So lässt sich eine einzelne Sitzung nachliefern, ohne die ganze Legislaturperiode erneut zu senden, und dieselbe Entität von mehreren Stellen referenzieren. Wo die Verschachtelung den Zusammenhang besser abbildet, ist sie zusätzlich möglich: Die Session nimmt ihre Sitzungen als Liste auf, das Protokoll seine Traktanden, Abstimmungen und Wortmeldungen.



### Klasse: Container []{#Container}


_Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Sessionen, Sitzungen, Traktanden, Protokolle, Abstimmungen, Wahlen, Anwesenheiten, Wortmeldungen und Resolutionen._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| legislatures | * <br/> [Legislature](#Legislature) | Sammlung der Legislaturperioden.  |
| sessions | * <br/> [Session](#Session) | Sammlung der Sessionen.  |
| meetings | * <br/> [Meeting](#Meeting) | Sammlung der Sitzungen.  |
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | Sammlung der Traktanden.  |
| protocols | * <br/> [Protocol](#Protocol) | Sammlung der Protokolle.  |
| votings | * <br/> [Voting](#Voting) | Sammlung der Abstimmungen.  |
| elections | * <br/> [Election](#Election) | Sammlung der Wahlen.  |
| individual_votes | * <br/> [IndividualVote](#IndividualVote) | Sammlung der Einzelstimmen.  |
| attendances | * <br/> [Attendance](#Attendance) | Sammlung der Anwesenheitslisten.  |
| individual_attendances | * <br/> [IndividualAttendance](#IndividualAttendance) | Sammlung der einzelnen Anwesenheitsfeststellungen.  |
| speeches | * <br/> [Speech](#Speech) | Sammlung der Wortmeldungen.  |
| resolutions | * <br/> [Resolution](#Resolution) | Sammlung der Resolutionen.  |

















#### Beispiele
##### Beispiel Container: meeting

```yaml
global_uri: ops:meetings_1
meetings:
  - spatial: "https://ld.admin.ch/canton/2"
    global_uri: ops:340dcf932fb044dd8f8c5c943267fbcc
    meeting_type: "session"
    name:
      - text: "Regierungssitzung vom 31. März 2021"
        language: "de"
      - text: "Séance du gouvernement du 31 mars 2021"
        language: "fr"
    url:
      - text: "https://www.rr.be.ch/de/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc"
        language: "de"
      - text: "https://www.rr.be.ch/fr/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc"
        language: "fr"
    actor_id:
      global_uri: "actors:rr_be"
      label: "Regierungsrat Bern"
      abbreviation:
        - value: "RR"
          language: de
    actor_name: "Regierungsrat Bern"
    date_begin_planned: "2021-03-31"
    date_end_planned: "2021-03-31"
    datetime_created: "2024-10-28T01:22:26Z"
    datetime_modified: "2024-11-27T20:40:57Z"

  - spatial: "https://ld.admin.ch/canton/2"
    global_uri: ops:e7c5d453-848a-430a-b024-1dd2f6873aa6
    meeting_type: "session"
    name:
      - text: "Donnerstag (Nachmittag)"
        language: "de"
    url:
      - text: "https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
        language: "de"
      - text: "https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
        language: "fr"
    actor_id:
      global_uri: "https://api.openparldata.ch/v1/bodies/253"
      label: "Grosser Rat Bern"
      abbreviation:
        - value: "GR"
          language: de
    actor_name: "Grosser Rat Bern"
    date_begin_planned: "2025-06-05"
    date_end_planned: "2025-06-05"
    datetime_created: "2025-04-25T11:10:25Z"
    datetime_modified: "2025-05-19T01:06:45Z"

```
##### Beispiel Container: meeting sr winter25 Sitzung6

```yaml
global_uri: ops:data_meeting_sr_winter25_Sitzung6

meetings:
  - global_uri: "parl:sr_winter25_sitzung_6"
    spatial: "https://ld.admin.ch/country/CHE"
    meeting_type: "session"
    name:
      - text: "Sechste Sitzung"
        language: "de"
      - text: "Sixième séance"
        language: "fr"
    url:
      - text: "https://www.parlament.ch/de/ratsbetrieb/suche-Amtliches-bulletin"
        language: "de"
    actor_id:
      global_uri: "https://api.openparldata.ch/v1/bodies/42"
      label: "Ständerat"
      abbreviation:
        - value: "SR"
          language: de
    actor_name: "Ständerat"
    datetime_begin_planned: "2025-12-19T08:15:00+01:00"
    datetime_created: "2026-01-12T00:00:00+01:00"
    datetime_modified: "2026-01-12T00:00:00+01:00"

agenda_items:
  - global_uri: ops:69905
    parent_meeting: "parl:sr_winter25_sitzung_6"
    agenda_item_type: "item"
    datetime_begin_planned: "2025-12-19T09:15:00+01:00"
    datetime_begin_actual: "2025-12-19T09:20:00+01:00"
    agenda_item_number: "6"
    agenda_item_position: 4
    agenda_item_title:
      - text: "Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich durchführen, um die Verzögerungen zu verstehen"
        language: "de"
    affair_id: "affairs:24.4471"
    landing_page: "https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3"
    agenda_item_category: "agenda_item"
    datetime_created: "2026-01-12T00:00:00+01:00"
    datetime_modified: "2026-01-12T00:00:00+01:00"

speeches:
  - global_uri: ops:366631
    language: "fr"
    datetime_begin: "2025-12-19T09:20:00+01:00"
    datetime_end: "2025-12-19T09:25:00+01:00"
    actor_fullname: "Pascal Broulis"
    actor_id:
      global_uri: "https://api.openparldata.ch/v1/persons/18682"
      wikidata_uri: "http://www.wikidata.org/entity/Q116407"
      label: "Pascal Broulis"
    role: "speaker"
    text: >-
      Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec attention
      les différents commentaires qui ont été effectués sur mon postulat. Cela reste un postulat,
      ce n'est pas une motion. D'abord, je ne partage pas l'avis selon lequel ce postulat
      n'apporterait pas une valeur ajoutée. En effet, un "benchmark", à savoir un modèle chiffré
      de performance, permettrait de mieux comprendre les raisons des retards que notre pays
      rencontre en comparaison avec les principaux pays européens.
    text_format: "html"
    text_type: "final"
    landing_page: "https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631"
    media_url: "https://par-pcache.simplex.tv/content?externalid=366631"
    media_type: "video"
    media_format: "video/mp4"

```
##### Beispiel Container: meeting complete

```yaml
global_uri: ops:meeting_examples_2025

meetings:

- global_uri: ops:meeting_sg_2025_03_15
  spatial: "https://ld.admin.ch/canton/17"
  meeting_type: "session"
  name:
    - text: "Kantonsratssitzung vom 15. März 2025"
      language: "de"
  url:
    - text: "https://www.ratsinfo.sg.ch/sessions/2025-03-15"
      language: "de"
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/265"
    label: "Kantonsrat St. Gallen"
    abbreviation:
      - value: "KR"
        language: de
  actor_name: "Kantonsrat St. Gallen"
  datetime_begin_planned: "2025-03-15T08:00:00Z"
  datetime_end_planned: "2025-03-15T18:00:00Z"
  datetime_begin_actual: "2025-03-15T08:15:00Z"
  datetime_end_actual: "2025-03-15T17:30:00Z"
  state: "planned"
  location: "Kantonsratssaal, Regierungsgebäude St. Gallen"
  parent_legislature: ops:legislature_sg_2024_2028
  datetime_created: "2025-02-01T10:00:00Z"
  datetime_modified: "2025-03-15T17:30:00Z"

- global_uri: ops:meeting_be_committee_wak_2025_05_12
  spatial: "https://ld.admin.ch/canton/2"
  meeting_type: "committee"
  name:
    - text: "Sitzung Kommission für Wirtschaft und Abgaben"
      language: "de"
    - text: "Séance Commission de l'économie et des redevances"
      language: "fr"
  url:
    - text: "https://www.gr.be.ch/kommissionen/wak/2025-05-12"
      language: "de"
  actor_id:
    global_uri: "actors:committee_wak_be"
    label: "Kommission für Wirtschaft und Abgaben (WAK)"
    abbreviation:
      - value: "WAK"
        language: de
  actor_name: "Kommission für Wirtschaft und Abgaben (WAK)"
  datetime_begin_planned: "2025-05-12T14:00:00Z"
  datetime_end_planned: "2025-05-12T17:00:00Z"
  datetime_begin_actual: "2025-05-12T14:10:00Z"
  datetime_end_actual: "2025-05-12T16:45:00Z"
  state: "planned"
  location: "Kommissionszimmer 301, Rathaus Bern"
  parent_legislature: ops:legislature_be_2022_2026
  datetime_created: "2025-04-15T09:00:00Z"
  datetime_modified: "2025-05-12T16:45:00Z"

- global_uri: ops:meeting_gl_landsgemeinde_2025
  spatial: "https://ld.admin.ch/canton/8"
  meeting_type: "sitting"
  name:
    - text: "Landsgemeinde 2025"
      language: "de"
  url:
    - text: "https://www.landsgemeinde.gl.ch/2025"
      language: "de"
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/258"
    label: "Landsgemeinde Glarus"
    abbreviation:
      - value: "LG"
        language: de
  actor_name: "Landsgemeinde Glarus"
  datetime_begin_planned: "2025-05-04T09:30:00Z"
  datetime_end_planned: "2025-05-04T14:00:00Z"
  datetime_begin_actual: "2025-05-04T09:30:00Z"
  datetime_end_actual: "2025-05-04T13:45:00Z"
  state: "planned"
  location: "Zaunplatz, Glarus"
  parent_legislature: ops:legislature_gl_2024_2028
  datetime_created: "2025-01-10T12:00:00Z"
  datetime_modified: "2025-05-04T13:45:00Z"

agenda_items:

- global_uri: ops:agenda_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  agenda_item_type: "item"
  agenda_item_number: "15"
  agenda_item_position: 15
  agenda_item_title:
    - text: "Energiegesetz - Schlussabstimmung"
      language: "de"
  agenda_item_description:
    - text: "Schlussabstimmung über das revidierte Energiegesetz des Kantons St. Gallen"
      language: "de"
  agenda_item_category: "Gesetzgebung"
  state_id: "completed"
  datetime_begin_planned: "2025-03-15T14:00:00Z"
  datetime_begin_actual: "2025-03-15T14:30:00Z"
  affair_id: "affairs:sg_2024_123_energiegesetz"
  datetime_created: "2025-02-01T10:00:00Z"
  datetime_modified: "2025-03-15T14:35:00Z"

- global_uri: ops:agenda_item_be_2025_042
  parent_meeting: ops:meeting_be_committee_wak_2025_05_12
  agenda_item_type: "item"
  agenda_item_number: "4.2"
  agenda_item_position: 42
  agenda_item_title:
    - text: "Steuergesetz - Detailberatung Art. 5"
      language: "de"
    - text: "Loi fiscale - Délibération détaillée art. 5"
      language: "fr"
  agenda_item_description:
    - text: "Beratung von Änderungsanträgen zu Artikel 5 des Steuergesetzes"
      language: "de"
    - text: "Délibération sur les propositions de modification de l'article 5 de la loi fiscale"
      language: "fr"
  agenda_item_category: "Gesetzgebung"
  state_id: "completed"
  datetime_begin_planned: "2025-05-12T15:00:00Z"
  datetime_begin_actual: "2025-05-12T15:15:00Z"
  affair_id: "affairs:be_2024_089_steuergesetz"
  datetime_created: "2025-04-15T09:00:00Z"
  datetime_modified: "2025-05-12T15:20:00Z"

- global_uri: ops:agenda_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  agenda_item_type: "item"
  agenda_item_number: "8"
  agenda_item_position: 8
  agenda_item_title:
    - text: "Budget 2026"
      language: "de"
  agenda_item_description:
    - text: "Beratung und Beschlussfassung über das Kantonsbudget für das Jahr 2026"
      language: "de"
  agenda_item_category: "Budget und Finanzen"
  state_id: "completed"
  datetime_begin_planned: "2025-11-20T16:00:00Z"
  datetime_begin_actual: "2025-11-20T16:45:00Z"
  affair_id: "affairs:zh_2025_budget_2026"
  datetime_created: "2025-10-01T08:00:00Z"
  datetime_modified: "2025-11-20T16:50:00Z"

```
##### Beispiel Container: legislature

```yaml
global_uri: ops:legislature_examples
legislatures:

# Bund: abgeschlossene Legislaturperiode, vier Jahre, dreisprachige Bezeichnung.
- global_uri: ops:legislature_51
  wikidata_uri: http://www.wikidata.org/entity/Q71712404
  spatial: "https://ld.admin.ch/country/CHE"
  name:
    - text: "51. Legislaturperiode"
      language: "de"
    - text: "51e législature"
      language: "fr"
    - text: "51ª legislatura"
      language: "it"
  description: "Amtsdauer der am 20. Oktober 2019 gewählten Bundesversammlung; sie endete am Vortag der konstituierenden Sitzung der 52. Legislaturperiode vom 4. Dezember 2023."
  landing_page: "https://www.parlament.ch/de/ratsbetrieb/sessionen"
  actor_id:
    global_uri: "actors:bundesversammlung"
    label: "Bundesversammlung"
    abbreviation:
      - value: "BV"
        language: de
  date_begin_actual: "2019-12-02"
  date_end_actual: "2023-12-03"
  datetime_created: "2019-12-02T09:00:00+01:00"
  datetime_modified: "2023-12-04T08:30:00+01:00"

# Kanton mit vierjähriger Amtsdauer; Beginn und Ende sind hier von Gesetzes
# wegen auf den Tag festgelegt und deshalb schon bei der Planung bekannt.
- global_uri: ops:legislature_be_2022_2026
  local_id: "GR-BE-2022-2026"
  spatial: "https://ld.admin.ch/canton/2"
  name:
    - text: "Legislatur 2022–2026"
      language: "de"
    - text: "Législature 2022-2026"
      language: "fr"
  landing_page: "https://www.gr.be.ch/de/start/grosser-rat.html"
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/253"
    label: "Grosser Rat Bern"
    abbreviation:
      - value: "GR"
        language: de
  date_begin_planned: "2022-06-01"
  date_end_planned: "2026-05-31"
  date_begin_actual: "2022-06-01"
  date_end_actual: "2026-05-31"
  datetime_created: "2022-04-01T10:15:00+02:00"
  datetime_modified: "2026-06-01T07:00:00+02:00"

# Kanton mit fünfjähriger Amtsdauer: laufende Legislatur, deren Ende erst
# geplant ist -- date_end_actual bleibt deshalb leer.
- global_uri: ops:legislature_vd_2022_2027
  wikidata_uri: http://www.wikidata.org/entity/Q131627357
  spatial: "https://ld.admin.ch/canton/22"
  name:
    - text: "Législature 2022-2027"
      language: "fr"
  description: "Le Grand Conseil vaudois est élu pour cinq ans."
  landing_page: "https://www.vd.ch/gc"
  actor_id:
    global_uri: "actors:gc_vd"
    label: "Grand Conseil du canton de Vaud"
    abbreviation:
      - value: "GC"
        language: fr
  date_begin_actual: "2022-07-01"
  date_end_planned: "2027-06-30"
  datetime_created: "2022-05-10T14:00:00+02:00"
  datetime_modified: "2025-01-08T11:20:00+01:00"

```
##### Beispiel Container: meeting item

```yaml
global_uri: ops:agenda_items_1
agenda_items:
  - global_uri: ops:cea750a5bd7b420fa4da1c914f801384
    parent_meeting: ops:meeting_bern_2022_03_17
    agenda_item_type: item
    datetime_begin_planned: '2022-03-17T17:00:00Z'
    agenda_item_position: 29
    agenda_item_number: '8'
    agenda_item_title:
      - text: >-
          Interpellation Fraktion GB/JA! (Katharina Gallizzi, GB): Welche
          Konsequenzen haben die Klimaziele für das Gasnetz in Bern?
        language: de
    affair_id: affairs:2020.SR.000007
    url:
      - text: >-
          https://stadtrat.bern.ch/de/sitzungen/detail.php?gid=000d6cf5f0bc4d89a5171e0123cfbff5#cea750a5bd7b420fa4da1c914f801384
        language: de
    datetime_created: '2025-01-17T21:25:52Z'
    datetime_modified: '2025-01-17T21:25:52Z'
  - global_uri: ops:2023_10_03-52
    parent_meeting: ops:meeting_lausanne_2023_10_03
    agenda_item_type: item
    datetime_begin_planned: '2023-10-03T00:00:00Z'
    agenda_item_position: 52
    agenda_item_number: '52'
    agenda_item_title:
      - text: >-
          Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité
          commerciale » (FIM)
        language: fr
    state_id: postponed
    agenda_item_category: RAPPORTS
    affair_id: affairs:POS22/029
    url:
      - text: >-
          https://www.lausanne.ch/apps/agir/affaire/81/b7157ea2a4994086b65cf176768c6381.htm
        language: fr
    datetime_created: '2025-02-08T12:33:10Z'
    datetime_modified: '2025-02-08T12:33:10Z'
  - global_uri: ops:2025_05_20-23
    parent_meeting: ops:meeting_lausanne_2025_05_20
    agenda_item_type: item
    datetime_begin_planned: '2025-05-20T00:00:00Z'
    agenda_item_position: 23
    agenda_item_number: '23'
    agenda_item_title:
      - text: >-
          Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : «
          Interpellation urgente de Kulmiye Yusuf et crts – Solidarité sans
          frontières, Lausanne en faveur du respect du droit international et de
          la protection des populations civiles à Gaza »
        language: fr
    state_id: not_treated
    agenda_item_category: ANNONCES ET INTERPELLATIONS
    affair_id: affairs:INT25/027
    url:
      - text: >-
          https://www.lausanne.ch/apps/agir/affaire/6c/049b6c612fe2428f9be66ea39522ac6c.htm
        language: fr
    datetime_created: '2025-06-07T23:50:18Z'
    datetime_modified: '2025-06-07T23:50:18Z'
  - global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
    parent_meeting: ops:meeting_vaud_2008_04_30
    agenda_item_type: item
    datetime_begin_planned: '2008-04-30T00:00:00Z'
    agenda_item_position: 7
    agenda_item_number: '7'
    agenda_item_title:
      - text: >-
          Révision partielle de sept ordonnances fédérales relatives aux
          produits chimiques
        language: fr
    agenda_item_description:
      - text: >
          Le Conseil d'Etat approuve le projet de révision partielle de sept
          ordonnances fédérales relatives aux produits chimiques. Il salue la
          volonté des autorités fédérales d'introduire dans la législation
          fédérale les modifications nécessaires découlant des nouveaux
          règlements européens, afin d'éliminer des entraves au commerce et
          d'augmenter la sécurité d'évaluation des produits chimiques.
        language: fr
    url:
      - text: >-
          https://www.vd.ch/actualites/decisions-du-conseil-detat/seance-du-conseil-detat/seance/265632#7b3545e4-57dc-3901-aaa8-4020da6ab0c6
        language: fr
    datetime_created: '2024-12-06T10:50:04Z'
    datetime_modified: '2024-12-06T10:50:04Z'
  - global_uri: ops:06fb582b753c416d8fdb05fa13873545
    parent_meeting: ops:meeting_2011_11_23
    agenda_item_type: item
    datetime_begin_planned: '2011-11-23T00:00:00Z'
    agenda_item_position: 2
    agenda_item_title:
      - text: >-
          Interpellation Peter Mark betr. elektronische Datenerfassung durch
          Mitarbeiter im Werkhof – Versuchsphase
        language: de
    datetime_created: '2025-03-21T23:15:19Z'
    datetime_modified: '2025-03-21T23:15:19Z'
  - global_uri: ops:16155798_3
    parent_meeting: ops:meeting_schaffhausen_2025_03_31
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 2
    agenda_item_number: '2'
    agenda_item_title:
      - text: >-
          Motion Nr. 2023/9 von Rainer Schmidig vom 18. Dezember 2023 betreffend
          zeitgemässe Abzüge in den Art. 35 und 37 des Gesetzes über die
          direkten Steuern
        language: de
    agenda_item_category: Traktanden
    affair_id: affairs:MOT_2023_9
    datetime_created: '2025-05-02T11:23:49Z'
    datetime_modified: '2025-05-02T11:23:49Z'
  - global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
    parent_meeting: ops:meeting_bern_rr_2025_04_02
    agenda_item_type: item
    datetime_begin_planned: '2025-04-02T00:00:00Z'
    agenda_item_title:
      - text: >-
          Petition «Gleichberechtigung für Tagesfamilien: Gleich hohe
          Betreuungsgutscheine für alle Anbieter im Kanton Bern».
          Regierungsrätliches Antwortschreiben
        language: de
    affair_id: affairs:2025.STA.622
    url:
      - text: >-
          https://www.rr.be.ch/de/start/beschluesse/suche/geschaeftsdetail.html?guid=21c50b86d21b4b4baeb1a76738ff82a3
        language: de
    datetime_created: '2025-04-25T11:11:40Z'
    datetime_modified: '2025-04-25T11:11:40Z'
  - global_uri: ops:49_253
    parent_meeting: ops:meeting_2025_03_31
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 2
    agenda_item_number: '2'
    agenda_item_title:
      - text: Programmvereinbarungen 2024
        language: de
    datetime_created: '2025-03-29T01:07:14Z'
    datetime_modified: '2025-03-29T01:07:14Z'
  - global_uri: ops:16155798_4
    parent_meeting: ops:meeting_schaffhausen_2025_03_31_b
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 3
    agenda_item_number: '3'
    agenda_item_title:
      - text: >-
          Volksmotion Nr. 2024/1 von Sandro Mamedow und Livia Schraff
          (Erstunterzeichnende) sowie weitere 150 Mitunterzeichnende vom 22.
          März 2024 mit dem Titel: «Für eine Stimme der Studierenden im
          Hochschulrat der Pädagogischen Hochschule Schaffhausen (PHSH)»
        language: de
    agenda_item_category: Traktanden
    affair_id: affairs:MOT_2024_1
    datetime_created: '2025-05-02T11:23:49Z'
    datetime_modified: '2025-05-02T11:23:49Z'
  - global_uri: ops:87b69a72919445a493a061d9b0daeba3
    parent_meeting: ops:meeting_be_2025_06_02
    agenda_item_type: item
    datetime_begin_planned: '2025-06-02T00:00:00Z'
    agenda_item_title:
      - text: Differenzierte Anpassung des Gehalts von Lehrpersonen ohne Lehrdiplom
        language: de
    affair_id: affairs:2025.GRPARL.81
    datetime_created: '2025-04-25T11:10:35Z'
    datetime_modified: '2025-04-25T11:10:35Z'
  - global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
    parent_meeting: ops:meeting_luzern_2025_01_28
    agenda_item_type: item
    datetime_begin_planned: '2025-01-28T00:00:00Z'
    agenda_item_position: 29
    agenda_item_number: '29'
    agenda_item_title:
      - text: >-
          Postulat Widmer Reichlin Gisela und Mit. über Massnahmen zur Erfüllung
          des Sonderschulkonkordats und zur gezielten Behebung des
          Fachkräftemangels im Bereich schulische Heilpädagogik / Bildungs- und
          Kulturdepartement
        language: de
    agenda_item_category: voting
    url:
      - text: >-
          https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
        language: de
    affair_id: affairs:2024P_125
    datetime_created: '2025-01-29T06:59:41Z'
    datetime_modified: '2025-01-29T06:59:41Z'
  - global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
    parent_meeting: ops:meeting_luzern_2025_01_28_b
    agenda_item_type: item
    datetime_begin_planned: '2025-01-28T00:00:00Z'
    agenda_item_position: 14
    agenda_item_number: '14'
    agenda_item_title:
      - text: >-
          Postulat Stadelmann Karin Andrea und Mit. über die Überprüfung und
          Anpassung der Kriterien zum früheren Eintritt von Kindern in die
          Basisstufe (den freiwilligen Kindergarten) / Bildungs- und
          Kulturdepartement
        language: de
    agenda_item_category: voting
    url:
      - text: >-
          https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=fa732e0e-7e5f-4d45-994a-fc74720c0781
        language: de
    affair_id: affairs:2023P_102
    datetime_created: '2025-01-29T06:59:41Z'
    datetime_modified: '2025-01-29T06:59:41Z'

```
##### Beispiel Container: voting

```yaml
global_uri: ops:voting_examples_2025

votings:

- global_uri: ops:voting_sg_2025_001
  voting_title:
    - text: "Schlussabstimmung Energiegesetz"
      language: "de"
  voting_type: "final_vote"
  datetime_begin: "2025-03-15T14:30:00Z"
  datetime_end: "2025-03-15T14:35:00Z"
  total_count_yes: 78
  total_count_no: 42
  total_count_abstention: 5
  total_absent: 3
  total: 128
  majority_type: "absolute"
  majority_count: 65
  result_text: "Mit 78 zu 42 Stimmen bei 5 Enthaltungen angenommen"
  parent_agenda_item: ops:agenda_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/265"
    label: "Kantonsrat St. Gallen"
    abbreviation:
      - value: "KR"
        language: de
  datetime_created: "2025-03-15T14:30:00Z"
  datetime_modified: "2025-03-15T14:35:00Z"

- global_uri: ops:voting_be_2025_042
  voting_title:
    - text: "Änderungsantrag Art. 5 Abs. 2"
      language: "de"
    - text: "Proposition de modification art. 5 al. 2"
      language: "fr"
  voting_type: "preliminary_vote"
  datetime_begin: "2025-06-05T10:15:00Z"
  datetime_end: "2025-06-05T10:17:00Z"
  total_count_yes: 45
  total_count_no: 87
  total_count_abstention: 8
  total_absent: 10
  total: 150
  majority_type: "absolute"
  majority_count: 76
  result_text: "Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt"
  parent_agenda_item: ops:agenda_item_be_2025_042
  parent_meeting: ops:meeting_be_2025_06_05
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/253"
    label: "Grosser Rat Bern"
    abbreviation:
      - value: "GR"
        language: de
  datetime_created: "2025-06-05T10:15:00Z"
  datetime_modified: "2025-06-05T10:15:00Z"

- global_uri: ops:voting_zh_budget_2026
  voting_title:
    - text: "Budgetbeschluss 2026"
      language: "de"
  voting_type: "final_vote"
  datetime_begin: "2025-11-20T16:45:00Z"
  datetime_end: "2025-11-20T16:50:00Z"
  total_count_yes: 105
  total_count_no: 70
  total_count_abstention: 5
  total_absent: 0
  total: 180
  majority_type: "absolute"
  majority_count: 91
  result_text: "Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen"
  parent_agenda_item: ops:agenda_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/275"
    label: "Kantonsrat Zürich"
    abbreviation:
      - value: "KR"
        language: de
  datetime_created: "2025-11-20T16:45:00Z"
  datetime_modified: "2025-11-20T16:50:00Z"

# Realbeispiel Gemeinderat der Stadt Zürich (28.02.2024, 86. Sitzung):
# "Gleichgerichtete Anträge" mit mehreren Auswahloptionen (Zürich: mehrere Knöpfe).
# Die Optionen sind nicht Ja/Nein/Enthaltung, sondern Auswahl A–D und werden
# deshalb über total_other (Liste von TotalOther {count, label}) abgebildet.
# Quelle: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
- global_uri: ops:voting_zh_gr_2024_2023_361
  voting_title:
    - text: "Liegenschaften Stadt Zürich, Wohnhaus Magnusstrasse 27, Gesamtinstandsetzung, Grundrissanpassung, Netto-Zusatzkredit (Geschäft 2023/361)"
      language: "de"
  voting_type: "other"
  type_label: "Gleichgerichtete Anträge (Mehrfachauswahl)"
  datetime_begin: "2024-02-28T00:00:00Z"
  datetime_end: "2024-02-28T00:00:00Z"
  landing_page: "https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89"
  # Bei reinen Auswahlabstimmungen bleiben Ja/Nein/Enthaltung leer; jede Option
  # erhält einen eigenen TotalOther-Eintrag mit Stimmenzahl und Bezeichnung.
  total_other:
    - count: 75
      label: "Auswahl A (siegreich)"
    - count: 25
      label: "Auswahl B"
    - count: 12
      label: "Auswahl C"
    - count: 0
      label: "Auswahl D"
  total_absent: 13
  total: 112
  majority_type: "other"
  result_text: "Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25, Auswahl C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern)."
  parent_agenda_item: ops:agenda_item_zh_gr_2024_2023_361
  parent_meeting: ops:meeting_zh_gr_2024_02_28
  affair_id: "2023/361"
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/"
    label: "Gemeinderat der Stadt Zürich"
    abbreviation:
      - value: "GR"
        language: de
  datetime_created: "2024-02-28T00:00:00Z"
  datetime_modified: "2024-02-28T00:00:00Z"

individual_votes:

# Einzelstimmen zum Zürcher Mehrfachoptionen-Beispiel: Da die Auswahloptionen
# nicht Ja/Nein/Enthaltung sind, wird individual_vote_type "other" mit type_label
# je gewählter Option verwendet; abwesende Mitglieder erhalten "not_voted".
- global_uri: ops:vote_zh_gr_2024_2023_361_a1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/1"
    label: "Mitglied Auswahl A"
  seat_nr: "12"
  individual_vote_type: "other"
  type_label: "Auswahl A"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_b1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/2"
    label: "Mitglied Auswahl B"
  seat_nr: "47"
  individual_vote_type: "other"
  type_label: "Auswahl B"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_c1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/3"
    label: "Mitglied Auswahl C"
  seat_nr: "88"
  individual_vote_type: "other"
  type_label: "Auswahl C"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_abs1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/4"
    label: "Abwesendes Mitglied"
  seat_nr: "103"
  individual_vote_type: "not_voted"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_sg_2025_001_person_123
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27235"
    label: "Paul Schlegel"
  seat_nr: "1"
  individual_vote_type: "yes"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_456
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27234"
    label: "Andreas Eggenberger"
  seat_nr: "2"
  individual_vote_type: "no"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_789
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27233"
    label: "Thomas Ammann"
  seat_nr: "3"
  individual_vote_type: "abstention"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_321
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/25177"
    label: "Ruedi Thomann"
  seat_nr: "4"
  individual_vote_type: "not_voted"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_zh_budget_2026_person_101
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27237"
    label: "Thomas Wolf"
  seat_nr: "1"
  individual_vote_type: "yes"
  datetime_created: "2025-11-20T16:45:00Z"

- global_uri: ops:vote_zh_budget_2026_person_102
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/25208"
    label: "Jean-Daniel Strub"
  seat_nr: "2"
  individual_vote_type: "no"
  datetime_created: "2025-11-20T16:45:00Z"

```
##### Beispiel Container: session

```yaml
global_uri: ops:sessions_example_2025
sessions:

- global_uri: ops:session_5207
  spatial: "https://ld.admin.ch/country/CHE"
  name:
    - text: "Frühjahrssession 2025"
      language: "de"
    - text: "Session de printemps 2025"
      language: "fr"
    - text: "Sessione primaverile 2025"
      language: "it"
  url:
    - text: "https://www.parlament.ch/de/ratsbetrieb/sessionen/fruehjahr-2025"
      language: "de"
    - text: "https://www.parlament.ch/fr/ratsbetrieb/sessionen/fruehjahr-2025"
      language: "fr"
    - text: "https://www.parlament.ch/it/ratsbetrieb/sessionen/fruehjahr-2025"
      language: "it"
  date_begin_planned: "2025-03-03"
  date_end_planned: "2025-03-21"
  parent_legislature: ops:legislature_51
  datetime_modified: "2025-04-24T00:19:37Z"
  datetime_created: "2025-03-20T14:27:09Z"

- global_uri: ops:session_be_summer_2025
  spatial: "https://ld.admin.ch/canton/2"
  name:
    - text: "Sommersession 2025"
      language: "de"
    - text: "Session d'été 2025"
      language: "fr"
  url:
    - text: "https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
      language: "de"
    - text: "https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
      language: "fr"
  date_begin_planned: "2025-06-02"
  date_end_planned: "2025-06-12"
  datetime_modified: "2025-05-19T01:06:44Z"
  datetime_created: "2025-04-25T11:10:24Z"

- global_uri: ops:session_gl_landrat_2025_02_26
  spatial: "https://ld.admin.ch/canton/8"
  name:
    - text: "Sitzung des Landrates vom 26.02.2025"
      language: "de"
  url:
    - text: "https://www.gl.ch/parlament/landrat/landratsprotokolle-ab-30-juni-2010.html/239"
      language: "de"
  date_begin_planned: "2025-02-26"
  date_end_planned: "2025-02-26"
  datetime_modified: "2025-04-25T13:40:34Z"
  datetime_created: "2025-04-23T22:58:39Z"

- global_uri: ops:session_gl_landsgemeinde_2025_05_04
  spatial: "https://ld.admin.ch/canton/8"
  name:
    - text: "Landsgemeinde vom 04. Mai 2025"
      language: "de"
  url:
    - text: "https://www.landsgemeinde.gl.ch/landsgemeinde/2025-05-04"
      language: "de"
  date_begin_planned: "2025-05-04"
  date_end_planned: "2025-05-04"
  datetime_modified: "2025-04-25T13:40:34Z"
  datetime_created: "2025-04-23T22:58:39Z"

```






</div>

\newpage

<!-- ToDo: Christian -->

# Zeitliche Organisation des Ratsbetriebs

Der Ratsbetrieb ist zeitlich in vier Klassen gegliedert:

```
Legislature (Legislaturperiode)
  └─ Session (z.B. Frühjahrssession)
      └─ Meeting (einzelne Sitzung)
          └─ AgendaItem (Traktandum)
```

Die Legislaturperiode bildet den langfristigen Rahmen, die Session strukturiert die Arbeit innerhalb einer Legislaturperiode, das Meeting ist die konkrete Sitzung, in der Geschäfte beraten werden, und das Traktandum gliedert die einzelne Sitzung. Die Ebenen greifen auf zwei Arten ineinander: Die Session nimmt ihre Sitzungen als Liste auf (`meetings`), während Sitzung und Traktandum über Referenzen nach oben zeigen (`parent_legislature`, `parent_meeting`, `parent_agenda_item`). Wer keine Sessionen führt, liefert seine Sitzungen einzeln und hängt sie über `parent_legislature` an die Legislaturperiode.

Die ersten drei Klassen sind nachfolgend beschrieben, das Traktandum im nächsten Kapitel.

## Gemeinsame Elemente

Die drei Klassen sind bewusst gleich gebaut. Die folgenden Felder haben auf allen Ebenen dieselbe Bedeutung.

**Identifikation.** `global_uri` ist der Identifikator und obligatorisch. `local_id` nimmt die Id des liefernden Systems auf, `wikidata_uri` verweist auf den Wikidata-Eintrag, sofern es einen gibt.

**Beginn und Ende.** Die Zeitangaben werden doppelt geführt: `date_begin_planned` und `date_end_planned` halten fest, was angesetzt war, `date_begin_actual` und `date_end_actual`, was tatsächlich geschah. Wo die Uhrzeit relevant ist, stehen die Varianten `datetime_*` zur Verfügung.

**Raum und Organ.** `spatial` verweist auf die Raumeinheit gemäss LINDAS — Land, Kanton, Bezirk oder Gemeinde, also `https://ld.admin.ch/canton/2` statt „BE". Es ist dasselbe Feld, mit dem eCH-0294 seine Gruppen verortet, sodass ein Ratsbetrieb und die Akteure, die ihn tragen, auf dieselbe Ressource zeigen. Wer innerhalb dieser Raumeinheit tagt, sagt `actor_id` als Kurzreferenz auf das Organ gemäss eCH-0294.

**Verlinkte Dokumente.** `documents` verknüpft Dokumente als FRBR-Works gemäss eCH-0292 — bei der Legislaturperiode etwa Mitglieder- und Geschäftsverzeichnisse, bei der Session das Sessionsprogramm, beim Meeting das Protokoll.

## Legislature (Legislaturperiode)

Eine Legislaturperiode bezeichnet den Zeitraum, für den ein Parlament gewählt wird und in seiner aktuellen Zusammensetzung tätig ist.

### Dauer und Verlauf

Die Dauer ist nicht vorgegeben — die Beispiele zeigen eine vier- und eine fünfjährige Amtsdauer. Anders als bei der Sitzung fallen Planung und Verlauf hier kaum auseinander; wo eine Legislaturperiode gesetzlich auf den Tag festgelegt ist, tragen `*_planned` und `*_actual` dieselben Daten.



### Klasse: Legislature []{#Legislature}


_Amtsdauer eines Parlaments als gesetzgebender Versammlung. Dauert in der Regel vier Jahre._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| spatial | 0..1 <br/> String | Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer, Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234, Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23, Bund: https://ld.admin.ch/country/CHE.  |
| administrative_id | 0..1 <br/> String | Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Mehrsprachige vollständige Bezeichnung.  |
| description | 0..1 <br/> String | Beschreibender Text zum Element.  |
| landing_page | 0..1 <br/> String | URL mit weiteren Informationen.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Referenz auf das handelnde Organ/Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_begin_actual | 0..1 <br/> Date | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | legislatures | range | [Legislature](#Legislature) |














#### Beispiele
##### Beispiel Legislature: Laufende kantonale Legislatur mit fünfjähriger Amtsdauer

```yaml
legislatures:
- global_uri: ops:legislature_vd_2022_2027
  wikidata_uri: http://www.wikidata.org/entity/Q131627357
  spatial: https://ld.admin.ch/canton/22
  name:
  - text: Législature 2022-2027
    language: fr
  description: Le Grand Conseil vaudois est élu pour cinq ans.
  landing_page: https://www.vd.ch/gc
  actor_id:
    global_uri: actors:gc_vd
    label: Grand Conseil du canton de Vaud
    abbreviation:
    - value: GC
      language: fr
  date_begin_actual: '2022-07-01'
  date_end_planned: '2027-06-30'
  datetime_created: '2022-05-10T14:00:00+02:00'
  datetime_modified: '2025-01-08T11:20:00+01:00'

```
##### Beispiel Legislature: Cantonal legislature with a four-year term

```yaml
legislatures:
- global_uri: ops:legislature_be_2022_2026
  local_id: GR-BE-2022-2026
  spatial: https://ld.admin.ch/canton/2
  name:
  - text: Legislatur 2022–2026
    language: de
  - text: Législature 2022-2026
    language: fr
  landing_page: https://www.gr.be.ch/de/start/grosser-rat.html
  actor_id:
    global_uri: https://api.openparldata.ch/v1/bodies/253
    label: Grosser Rat Bern
    abbreviation:
    - value: GR
      language: de
  date_begin_planned: '2022-06-01'
  date_end_planned: '2026-05-31'
  date_begin_actual: '2022-06-01'
  date_end_actual: '2026-05-31'
  datetime_created: '2022-04-01T10:15:00+02:00'
  datetime_modified: '2026-06-01T07:00:00+02:00'

```
##### Beispiel Legislature: Completed federal legislature

```yaml
legislatures:
- global_uri: ops:legislature_51
  wikidata_uri: http://www.wikidata.org/entity/Q71712404
  spatial: https://ld.admin.ch/country/CHE
  name:
  - text: 51. Legislaturperiode
    language: de
  - text: 51e législature
    language: fr
  - text: 51ª legislatura
    language: it
  description: >-
    Amtsdauer der am 20. Oktober 2019 gewählten Bundesversammlung; sie endete am Vortag
    der konstituierenden Sitzung der 52. Legislaturperiode vom 4. Dezember 2023.
  landing_page: https://www.parlament.ch/de/ratsbetrieb/sessionen
  actor_id:
    global_uri: actors:bundesversammlung
    label: Bundesversammlung
    abbreviation:
    - value: BV
      language: de
  date_begin_actual: '2019-12-02'
  date_end_actual: '2023-12-03'
  datetime_created: '2019-12-02T09:00:00+01:00'
  datetime_modified: '2023-12-04T08:30:00+01:00'

```






</div>

## Session (Sitzungsperiode)

Eine Session ist eine zusammenhängende Sitzungsperiode, in der mehrere Meetings stattfinden.

### Optionale Ebene

Die Session ist die einzige der drei Ebenen, auf die verzichtet werden kann: Föderaleinheiten ohne formale Sessionen lassen sie weg und führen ihre Sitzungen direkt. Session und Meeting können auch zusammenfallen — eine eintägige Sitzung des Landrats oder eine Landsgemeinde wird als Sitzungsperiode mit einer einzigen Sitzung geführt.

### Nummerierung

Nummeriert wird sehr unterschiedlich, weshalb vier Felder zur Verfügung stehen: `number` hält die laufende Nummer als Zahl fest, `sequential_number` dieselbe Angabe als Zeichenkette (und damit auch römische Ziffern), `position` die Position innerhalb der Legislaturperiode und `meeting_abbreviation` eine Kurzbezeichnung wie „FS24“. Das Meeting kennt dieselben vier Felder.



### Klasse: Session []{#Session}


_Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen bestimmten Zeitraum erstreckt._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| spatial | 0..1 <br/> String | Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer, Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234, Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23, Bund: https://ld.admin.ch/country/CHE.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Mehrsprachige vollständige Bezeichnung.  |
| number | 0..1 <br/> String | Laufende Nummer, z.B. innerhalb der Legislatur, der Session oder des Jahres.  |
| sequential_number | 0..1 <br/> Integer | Laufende Nummer der Sitzung, die zur Sortierung verwendet wird.  |
| position | 0..1 <br/> String | Ganzzahlige Position innerhalb der übergeordneten Reihenfolge.  |
| meeting_abbreviation | 0..1 <br/> String | Kurzbezeichnung der Session oder Sitzung (z.B. „FS24“ für die Frühjahrssession 2024).  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing Page oder weiterführende Webadresse, mehrsprachig.  |
| parent_legislature | 0..1 <br/> String | Der gesetzgebende Körper, auf dem die Sitzung basiert.  |
| meetings | * <br/> [Meeting](#Meeting) | Sammlung der Sitzungen.  |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_begin_actual | 0..1 <br/> Date | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | sessions | range | [Session](#Session) |














#### Beispiele
##### Beispiel Session: Eidgenössische Session mit dreisprachiger Bezeichnung

```yaml
sessions:
- global_uri: ops:session_5207
  spatial: https://ld.admin.ch/country/CHE
  name:
  - text: Frühjahrssession 2025
    language: de
  - text: Session de printemps 2025
    language: fr
  - text: Sessione primaverile 2025
    language: it
  url:
  - text: https://www.parlament.ch/de/ratsbetrieb/sessionen/fruehjahr-2025
    language: de
  - text: https://www.parlament.ch/fr/ratsbetrieb/sessionen/fruehjahr-2025
    language: fr
  - text: https://www.parlament.ch/it/ratsbetrieb/sessionen/fruehjahr-2025
    language: it
  date_begin_planned: '2025-03-03'
  date_end_planned: '2025-03-21'
  parent_legislature: ops:legislature_51
  datetime_modified: '2025-04-24T00:19:37Z'
  datetime_created: '2025-03-20T14:27:09Z'

```
##### Beispiel Session: Landsgemeinde as a sitting period

```yaml
sessions:
- global_uri: ops:session_gl_landsgemeinde_2025_05_04
  spatial: https://ld.admin.ch/canton/8
  name:
  - text: Landsgemeinde vom 04. Mai 2025
    language: de
  url:
  - text: https://www.landsgemeinde.gl.ch/landsgemeinde/2025-05-04
    language: de
  date_begin_planned: '2025-05-04'
  date_end_planned: '2025-05-04'
  datetime_modified: '2025-04-25T13:40:34Z'
  datetime_created: '2025-04-23T22:58:39Z'

```
##### Beispiel Session: Cantonal session with a bilingual designation

```yaml
sessions:
- global_uri: ops:session_be_summer_2025
  spatial: https://ld.admin.ch/canton/2
  name:
  - text: Sommersession 2025
    language: de
  - text: Session d'été 2025
    language: fr
  url:
  - text: >-
      https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
    language: de
  - text: >-
      https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
    language: fr
  date_begin_planned: '2025-06-02'
  date_end_planned: '2025-06-12'
  datetime_modified: '2025-05-19T01:06:44Z'
  datetime_created: '2025-04-25T11:10:24Z'

```
##### Beispiel Session: One-day sitting period of a cantonal parliament

```yaml
sessions:
- global_uri: ops:session_gl_landrat_2025_02_26
  spatial: https://ld.admin.ch/canton/8
  name:
  - text: Sitzung des Landrates vom 26.02.2025
    language: de
  url:
  - text: https://www.gl.ch/parlament/landrat/landratsprotokolle-ab-30-juni-2010.html/239
    language: de
  date_begin_planned: '2025-02-26'
  date_end_planned: '2025-02-26'
  datetime_modified: '2025-04-25T13:40:34Z'
  datetime_created: '2025-04-23T22:58:39Z'

```






</div>

## Meeting (Einzelne Sitzung)

Ein Meeting ist die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Beschlüsse gefasst und Wortmeldungen festgehalten werden.

### Sitzungstypen

`meeting_type` unterscheidet vier Typen: `session` für Plenarsitzungen eines Parlaments oder einer Kammer, `committee` für Kommissionssitzungen, `sitting` für Versammlungen wie Landsgemeinden, Gemeinde- und Bürgergemeindeversammlungen und `various` als Auffangwert. Der Wert `sitting` ist eine bewusste Setzung: Landsgemeinden und Gemeindeversammlungen sind Versammlungen der Stimmberechtigten selbst, entscheiden aber als tagendes Organ mit Traktandenliste und werden deshalb wie eine Ratssitzung abgebildet.

### Planung und Verlauf

Auf dieser Ebene fallen die geplanten und die tatsächlichen Zeiten regelmässig auseinander: Eine für 14:00 angesetzte Sitzung beginnt wegen Verzögerungen erst um 14:25 und endet statt um 18:00 bereits um 17:30. Ob eine Sitzung überhaupt wie vorgesehen stattfindet, hält `state` fest (`planned`, `canceled`, `postponed`); `state_name` nimmt eine abweichende, freitextliche Statusbezeichnung auf. `location` erfasst den Sitzungsort — den physischen Raum („Bundeshaus, Nationalratssaal“), eine Videokonferenz oder ein hybrides Format.

### Anknüpfungspunkte

Das Meeting ist der Knoten, an dem die übrigen Klassen dieses Standards hängen: Traktanden (`AgendaItem`), Abstimmungen und Wahlen (`Voting`, `Election`), Wortmeldungen (`Speech`) sowie die Anwesenheitsliste (`Attendance.parent_meeting`). `documents` verknüpft Sitzungsunterlagen wie Tagblatt oder Beilagen, `protocol_ref` das Protokoll. `parent_meeting` bildet Sitzungen ab, die Teil einer übergeordneten Sitzung sind; `actor_name`, `group_name` und `group_id` halten Organ und Gruppierung zusätzlich im Klartext fest.



### Klasse: Meeting []{#Meeting}


_Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sessionssitzung und andere verschiedene Versammlungen verwendet wird._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| spatial | 0..1 <br/> String | Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer, Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234, Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23, Bund: https://ld.admin.ch/country/CHE.  |
| meeting_type | 0..1 <br/> [MeetingTypeEnum](#MeetingTypeEnum) | Art der Sitzung, z.B. Session, Kommission, Sessionssitzung, Verschiedenes.  |
| administrative_id | 0..1 <br/> String | Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Mehrsprachige vollständige Bezeichnung.  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing Page oder weiterführende Webadresse, mehrsprachig.  |
| group_name | 0..1 <br/> String | Name der Gruppe oder des Gremiums.  |
| group_id | 0..1 <br/> [GroupReference](#GroupReference) | Referenz auf die Gruppe oder das Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| number | 0..1 <br/> String | Laufende Nummer, z.B. innerhalb der Legislatur, der Session oder des Jahres.  |
| landing_page | 0..1 <br/> String | URL mit weiteren Informationen.  |
| sequential_number | 0..1 <br/> Integer | Laufende Nummer der Sitzung, die zur Sortierung verwendet wird.  |
| position | 0..1 <br/> String | Ganzzahlige Position innerhalb der übergeordneten Reihenfolge.  |
| meeting_abbreviation | 0..1 <br/> String | Kurzbezeichnung der Session oder Sitzung (z.B. „FS24“ für die Frühjahrssession 2024).  |
| actor_name | 0..1 <br/> String | Name des politischen Organs (z.B. Nationalrat).  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Referenz auf das handelnde Organ/Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| state | 0..1 <br/> [StateEnum](#StateEnum) | Aktueller Status der Sitzung (geplant, abgesagt, verschoben).  |
| state_name | 0..1 <br/> String | Benutzerdefinierte Zustandsbeschreibung für die Sitzung.  |
| description | 0..1 <br/> String | Beschreibender Text zum Element.  |
| location | 0..1 <br/> String | Ort, an dem die Sitzung stattfindet (physischer Raum, Videokonferenz oder hybrides Format).  |
| parent_meeting | 0..1 <br/> String | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| parent_legislature | 0..1 <br/> String | Der gesetzgebende Körper, auf dem die Sitzung basiert.  |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| protocol_ref | 0..1 <br/> [Protocol](#Protocol) | Das nach der Sitzung erstellte Protokoll dieser Sitzung.  |
| date_begin_actual | 0..1 <br/> Date | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | meetings | range | [Meeting](#Meeting) |
| [Session](#Session) | meetings | range | [Meeting](#Meeting) |














#### Beispiele
##### Beispiel Meeting: Ständeratssitzung mit Protokoll und Wortmeldungen

```yaml
meetings:
- global_uri: parl:sr_winter25_sitzung_6
  spatial: https://ld.admin.ch/country/CHE
  meeting_type: session
  name:
  - text: Sechste Sitzung
    language: de
  - text: Sixième séance
    language: fr
  url:
  - text: https://www.parlament.ch/de/ratsbetrieb/suche-Amtliches-bulletin
    language: de
  actor_id:
    global_uri: https://api.openparldata.ch/v1/bodies/42
    label: Ständerat
    abbreviation:
    - value: SR
      language: de
  actor_name: Ständerat
  datetime_begin_planned: '2025-12-19T08:15:00+01:00'
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'

```
##### Beispiel Meeting: Cantonal parliament sitting with agenda items and votings

```yaml
meetings:
- global_uri: ops:meeting_sg_2025_03_15
  spatial: https://ld.admin.ch/canton/17
  meeting_type: session
  name:
  - text: Kantonsratssitzung vom 15. März 2025
    language: de
  url:
  - text: https://www.ratsinfo.sg.ch/sessions/2025-03-15
    language: de
  actor_id:
    global_uri: https://api.openparldata.ch/v1/bodies/265
    label: Kantonsrat St. Gallen
    abbreviation:
    - value: KR
      language: de
  actor_name: Kantonsrat St. Gallen
  datetime_begin_planned: '2025-03-15T08:00:00Z'
  datetime_end_planned: '2025-03-15T18:00:00Z'
  datetime_begin_actual: '2025-03-15T08:15:00Z'
  datetime_end_actual: '2025-03-15T17:30:00Z'
  state: planned
  location: Kantonsratssaal, Regierungsgebäude St. Gallen
  parent_legislature: ops:legislature_sg_2024_2028
  datetime_created: '2025-02-01T10:00:00Z'
  datetime_modified: '2025-03-15T17:30:00Z'

```
##### Beispiel Meeting: Half-day sitting within a session

```yaml
meetings:
- spatial: https://ld.admin.ch/canton/2
  global_uri: ops:e7c5d453-848a-430a-b024-1dd2f6873aa6
  meeting_type: session
  name:
  - text: Donnerstag (Nachmittag)
    language: de
  url:
  - text: >-
      https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
    language: de
  - text: >-
      https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
    language: fr
  actor_id:
    global_uri: https://api.openparldata.ch/v1/bodies/253
    label: Grosser Rat Bern
    abbreviation:
    - value: GR
      language: de
  actor_name: Grosser Rat Bern
  date_begin_planned: '2025-06-05'
  date_end_planned: '2025-06-05'
  datetime_created: '2025-04-25T11:10:25Z'
  datetime_modified: '2025-05-19T01:06:45Z'

```
##### Beispiel Meeting: Committee sitting with an attendance list

```yaml
meetings:
- global_uri: ops:meeting_be_committee_wak_2025_05_12
  spatial: https://ld.admin.ch/canton/2
  meeting_type: committee
  name:
  - text: Sitzung Kommission für Wirtschaft und Abgaben
    language: de
  - text: Séance Commission de l'économie et des redevances
    language: fr
  url:
  - text: https://www.gr.be.ch/kommissionen/wak/2025-05-12
    language: de
  actor_id:
    global_uri: actors:committee_wak_be
    label: Kommission für Wirtschaft und Abgaben (WAK)
    abbreviation:
    - value: WAK
      language: de
  actor_name: Kommission für Wirtschaft und Abgaben (WAK)
  datetime_begin_planned: '2025-05-12T14:00:00Z'
  datetime_end_planned: '2025-05-12T17:00:00Z'
  datetime_begin_actual: '2025-05-12T14:10:00Z'
  datetime_end_actual: '2025-05-12T16:45:00Z'
  state: planned
  location: Kommissionszimmer 301, Rathaus Bern
  parent_legislature: ops:legislature_be_2022_2026
  datetime_created: '2025-04-15T09:00:00Z'
  datetime_modified: '2025-05-12T16:45:00Z'

```
##### Beispiel Meeting: Government sitting with a bilingual designation

```yaml
meetings:
- spatial: https://ld.admin.ch/canton/2
  global_uri: ops:340dcf932fb044dd8f8c5c943267fbcc
  meeting_type: session
  name:
  - text: Regierungssitzung vom 31. März 2021
    language: de
  - text: Séance du gouvernement du 31 mars 2021
    language: fr
  url:
  - text: >-
      https://www.rr.be.ch/de/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc
    language: de
  - text: >-
      https://www.rr.be.ch/fr/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc
    language: fr
  actor_id:
    global_uri: actors:rr_be
    label: Regierungsrat Bern
    abbreviation:
    - value: RR
      language: de
  actor_name: Regierungsrat Bern
  date_begin_planned: '2021-03-31'
  date_end_planned: '2021-03-31'
  datetime_created: '2024-10-28T01:22:26Z'
  datetime_modified: '2024-11-27T20:40:57Z'

```
##### Beispiel Meeting: Landsgemeinde as meeting type sitting

```yaml
meetings:
- global_uri: ops:meeting_gl_landsgemeinde_2025
  spatial: https://ld.admin.ch/canton/8
  meeting_type: sitting
  name:
  - text: Landsgemeinde 2025
    language: de
  url:
  - text: https://www.landsgemeinde.gl.ch/2025
    language: de
  actor_id:
    global_uri: https://api.openparldata.ch/v1/bodies/258
    label: Landsgemeinde Glarus
    abbreviation:
    - value: LG
      language: de
  actor_name: Landsgemeinde Glarus
  datetime_begin_planned: '2025-05-04T09:30:00Z'
  datetime_end_planned: '2025-05-04T14:00:00Z'
  datetime_begin_actual: '2025-05-04T09:30:00Z'
  datetime_end_actual: '2025-05-04T13:45:00Z'
  state: planned
  location: Zaunplatz, Glarus
  parent_legislature: ops:legislature_gl_2024_2028
  datetime_created: '2025-01-10T12:00:00Z'
  datetime_modified: '2025-05-04T13:45:00Z'

```






</div>

### Enum: MeetingTypeEnum []{#MeetingTypeEnum}




_Art der Sitzung._




<div data-search-exclude markdown="1">

URI: [ops:MeetingTypeEnum](https://ch.paf.link/schema/operations/MeetingTypeEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| session |  Plenarsitzung des gesamten Parlaments oder einer Kammer.  |
| | [ops:enum/meeting_type/session](ops:enum/meeting_type/session) |
| committee |  Sitzung einer parlamentarischen Kommission.  |
| | [ops:enum/meeting_type/committee](ops:enum/meeting_type/committee) |
| sitting |  Besondere Versammlungsformen (z.B. Landsgemeinde, Gemeindeversammlung).  |
| | [ops:enum/meeting_type/sitting](ops:enum/meeting_type/sitting) |
| various |  Andere Sitzungsformen, die nicht in die obigen Kategorien fallen.  |
| | [ops:enum/meeting_type/various](ops:enum/meeting_type/various) |







</div>

### Enum: StateEnum []{#StateEnum}




_Status der Sitzung._




<div data-search-exclude markdown="1">

URI: [ops:StateEnum](https://ch.paf.link/schema/operations/StateEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| planned |  Die Sitzung ist geplant und findet wie vorgesehen statt.  |
| | [ops:enum/state/planned](ops:enum/state/planned) |
| canceled |  Die Sitzung wurde abgesagt.  |
| | [ops:enum/state/canceled](ops:enum/state/canceled) |
| postponed |  Die Sitzung wurde verschoben.  |
| | [ops:enum/state/postponed](ops:enum/state/postponed) |







</div>

\newpage

<!-- ToDo: Michel -->

# Tagesordnung (Traktandenliste), Protokoll und Beschlüsse

Die Tagesordnung einer Sitzung wird durch Traktanden strukturiert. Die Traktanden gelten als Planung einer Sitzung und bleiben nach Beginn der Sitzung in den Daten nicht mehr geändert. Anschliessend werden die gleichen Datenelemente genutzt um das Protkoll und die enthaltenen Beschlüsse fest zu halten. 

Im Falle dass es Änderungen der Traktanden während einer Sitzung gibt, werden diese im Protokoll erfasst, und damit die Traktandenliste der nächsten Sitzung angepasst.

## AgendaItem (Traktandum)

### Zweck der Entität

AgendaItem strukturiert die Tagesordnung einer Sitzung und verbindet die zeitliche Organisation (Meeting) mit den inhaltlichen Geschäften (Affairs aus eCH-0295). Es ist die zentrale Entität zur Abbildung des Sitzungsablaufs.

### Hierarchie und Struktur

Agenda Items können hierarchisch organisiert sein, um die Struktur komplexer Tagesordnungen abzubilden:

```
Meeting (Sitzung vom 4. März 2024)
  ├─ AgendaItem 1: Mitteilungen und Begrüssung
  ├─ AgendaItem 2: Gesetzesberatungen
  │   ├─ AgendaItem 2.1: Energiegesetz (Detailberatung)
  │   ├─ AgendaItem 2.2: Energiegesetz (Schlussabstimmung)
  │   └─ AgendaItem 2.3: Gesundheitsgesetz (Eintretensdebatte)
  └─ AgendaItem 3: Verschiedenes
```

Die Hierarchie wird über das Feld **parent_agenda_item** abgebildet, das auf das übergeordnete Traktandum verweist.

### Identifikation und Nummerierung

- **id**: Eindeutiger Identifikator
- **number**: Traktandennummer auf der Tagesordnung (z.B. "2.1", "3")
- **position**: Sortierreihenfolge (für die Darstellung)
- **title**: Titel des Traktandums

### Typen von Agenda Items

Das Feld **agenda_item_type** unterscheidet verschiedene Arten:

- **item**: Ein reguläres Traktandum mit Beratung und ggf. Abstimmung
- **item_group**: Eine Gruppe von Traktanden (z.B. "Gesetzesberatungen")
- **note**: Informative Einträge ohne Abstimmung (z.B. "Mitteilungen")

### Beziehung zu parlamentarischen Geschäften

Das Feld **affairs** verweist auf die zugehörigen parlamentarischen Geschäfte gemäss eCH-0295. Ein Traktandum kann sich auf mehrere Geschäfte beziehen:

- **Einzelnes Geschäft**: Ein Traktandum behandelt eine spezifische Vorlage
- **Mehrere Geschäfte**: Ein Traktandum fasst zusammenhängende Geschäfte zusammen
- **Kein Geschäft**: Administrative Traktanden (z.B. "Genehmigung des Protokolls")

**Beispiel:** Das Traktandum "Energiegesetz - Schlussabstimmung" verweist auf das Geschäft "23.XXX Energiegesetz" in eCH-0295.

### Zeitliche Planung

- **date_time**: Geplanter Zeitpunkt der Behandlung
- **date_time_actual**: Tatsächlicher Zeitpunkt der Behandlung

Diese Unterscheidung ist wichtig, da:
- Die Tagesordnung im Voraus festgelegt wird
- Der tatsächliche Ablauf davon abweichen kann
- Traktanden vorgezogen, verschoben oder vertagt werden können

### Status und Ergebnis

#### Status
Das Feld **status** zeigt den Bearbeitungsstand:
- "pending": Noch nicht behandelt
- "in_progress": Aktuell in Beratung
- "completed": Behandlung abgeschlossen
- "postponed": Vertagt auf eine spätere Sitzung
- "withdrawn": Zurückgezogen

#### Ergebnis
Das Feld **result** erfasst das Ergebnis der Behandlung:
- "accepted": Angenommen
- "rejected": Abgelehnt
- "referred": Zurückgewiesen (z.B. an Kommission)
- "noted": Zur Kenntnis genommen
- "no_decision": Keine Beschlussfassung

### Kategorisierung

Das Feld **category** erlaubt die Gruppierung nach inhaltlichen Kriterien:
- "Gesetzgebung"
- "Budget und Finanzen"
- "Interpellationen und Anfragen"
- "Wahlen"
- "Diverses"

Diese Kategorisierung ist nicht standardisiert und kann je nach Föderaleinheit variieren.

### Resolutionen zu Traktanden

Das Feld **resolution** verweist auf die Resolution(en), die zu diesem Traktandum gefasst wurde(n). Eine Resolution dokumentiert den formalen Beschluss:

```
AgendaItem: "Energiegesetz - Schlussabstimmung"
  └─ Resolution: "Annahme des Energiegesetzes mit 120 zu 75 Stimmen bei 5 Enthaltungen"
      └─ Voting: Details der Abstimmung
```

### Beschreibung und URL

- **description**: Ausführliche Beschreibung des Traktandums
- **url**: Array von mehrsprachigen URLs zu Sitzungsunterlagen:
  - Botschaften und Berichte
  - Anträge
  - Änderungsanträge
  - Abstimmungsergebnisse

### Besonderheiten verschiedener Verfahren

#### Gesetzgebungsverfahren
Ein Geschäft durchläuft mehrere Traktanden:
1. Eintretensdebatte
2. Detailberatung
3. Schlussabstimmung
4. Ggf. Differenzbereinigung zwischen den Räten

#### Interpellationen und Anfragen
- Einreichung als Traktandum
- Antwort der Regierung
- Ggf. Diskussion

#### Wahlen
- Wahlvorschlag als Traktandum
- Durchführung der Wahl
- Verkündung des Ergebnisses

### Verknüpfung mit anderen Entitäten

Ein AgendaItem ist das zentrale Bindeglied zwischen:

- **Meeting**: Die Sitzung, in der es behandelt wird
- **Affairs** (eCH-0295): Die inhaltlichen Geschäfte
- **Resolution**: Der formale Beschluss
- **Voting**: Die Abstimmung(en) zum Traktandum
- **Speech**: Voten und Wortmeldungen zum Traktandum

### Anwendungsbeispiele

...

### Verwendungszwecke

1. Strukturierung des Sitzungsablaufs und Tagesordnung
2. Verknüpfung zwischen Meetings und Affairs (eCH-0295)
3. Dokumentation von Status und Ergebnis pro Traktandum
4. Grundlage für Sitzungsprotokolle und Publikationen



### Klasse: AgendaItem []{#AgendaItem}


_Ein Traktandum einer Sitzung._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen.  |
| agenda_item_number | 0..1 <br/> String | Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern).  |
| agenda_item_position | 0..1 <br/> Integer | Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge.  |
| leading_actor_id | 0..1 <br/> String | Das federführende Departement für das Traktandum.  |
| speaking_actor_id | 0..1 <br/> String | Der Sprecher oder die Sprecherin bzw. die Departementsvorsteherin oder der Departementsvorsteher für das Traktandum.  |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | Titel des Traktandums.  |
| affair_id | 0..1 <br/> String | Die Verbindung zu den Geschäften des Traktandums.  |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | Untertitel oder ausführliche Beschreibung des Traktandums.  |
| state_id | 0..1 <br/> String | Zustands-Identifikator (Verweis auf das Status-Enum oder auf einen eigenen Zustand).  |
| state_name | 0..1 <br/> String | Benutzerdefinierte Zustandsbeschreibung für die Sitzung.  |
| landing_page | 0..1 <br/> String | URL mit weiteren Informationen.  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing Page oder weiterführende Webadresse, mehrsprachig.  |
| agenda_item_category | 0..1 <br/> String | Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden).  |
| parent_agenda_item | 0..1 <br/> String | Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf.  |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | Die Resolution oder Entscheidung zu diesem Traktandum.  |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_begin_actual | 0..1 <br/> Date | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | agenda_items | range | [AgendaItem](#AgendaItem) |
| [JointDebate](#JointDebate) | agenda_items | range | [AgendaItem](#AgendaItem) |














#### Beispiele
##### Beispiel AgendaItem: Budgettraktandum

```yaml
agenda_items:
- global_uri: ops:agenda_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  agenda_item_type: item
  agenda_item_number: '8'
  agenda_item_position: 8
  agenda_item_title:
  - text: Budget 2026
    language: de
  agenda_item_description:
  - text: Beratung und Beschlussfassung über das Kantonsbudget für das Jahr 2026
    language: de
  agenda_item_category: Budget und Finanzen
  state_id: completed
  datetime_begin_planned: '2025-11-20T16:00:00Z'
  datetime_begin_actual: '2025-11-20T16:45:00Z'
  affair_id: affairs:zh_2025_budget_2026
  datetime_created: '2025-10-01T08:00:00Z'
  datetime_modified: '2025-11-20T16:50:00Z'

```
##### Beispiel AgendaItem: Motion within a group of agenda items

```yaml
agenda_items:
- global_uri: ops:16155798_3
  parent_meeting: ops:meeting_schaffhausen_2025_03_31
  agenda_item_type: item
  datetime_begin_planned: '2025-03-31T00:00:00Z'
  agenda_item_position: 2
  agenda_item_number: '2'
  agenda_item_title:
  - text: >-
      Motion Nr. 2023/9 von Rainer Schmidig vom 18. Dezember 2023 betreffend zeitgemässe
      Abzüge in den Art. 35 und 37 des Gesetzes über die direkten Steuern
    language: de
  agenda_item_category: Traktanden
  affair_id: affairs:MOT_2023_9
  datetime_created: '2025-05-02T11:23:49Z'
  datetime_modified: '2025-05-02T11:23:49Z'

```
##### Beispiel AgendaItem: Agenda item of a Council of States sitting

```yaml
agenda_items:
- global_uri: ops:69905
  parent_meeting: parl:sr_winter25_sitzung_6
  agenda_item_type: item
  datetime_begin_planned: '2025-12-19T09:15:00+01:00'
  datetime_begin_actual: '2025-12-19T09:20:00+01:00'
  agenda_item_number: '6'
  agenda_item_position: 4
  agenda_item_title:
  - text: >-
      Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich durchführen,
      um die Verzögerungen zu verstehen
    language: de
  affair_id: affairs:24.4471
  landing_page: >-
    https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
  agenda_item_category: agenda_item
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'

```
##### Beispiel AgendaItem: Postulate category voting

```yaml
agenda_items:
- global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
  parent_meeting: ops:meeting_luzern_2025_01_28
  agenda_item_type: item
  datetime_begin_planned: '2025-01-28T00:00:00Z'
  agenda_item_position: 29
  agenda_item_number: '29'
  agenda_item_title:
  - text: >-
      Postulat Widmer Reichlin Gisela und Mit. über Massnahmen zur Erfüllung des Sonderschulkonkordats
      und zur gezielten Behebung des Fachkräftemangels im Bereich schulische Heilpädagogik
      / Bildungs- und Kulturdepartement
    language: de
  agenda_item_category: voting
  url:
  - text: >-
      https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
    language: de
  affair_id: affairs:2024P_125
  datetime_created: '2025-01-29T06:59:41Z'
  datetime_modified: '2025-01-29T06:59:41Z'

```
##### Beispiel AgendaItem: Interpellation of a parliamentary group

```yaml
agenda_items:
- global_uri: ops:cea750a5bd7b420fa4da1c914f801384
  parent_meeting: ops:meeting_bern_2022_03_17
  agenda_item_type: item
  datetime_begin_planned: '2022-03-17T17:00:00Z'
  agenda_item_position: 29
  agenda_item_number: '8'
  agenda_item_title:
  - text: >-
      Interpellation Fraktion GB/JA! (Katharina Gallizzi, GB): Welche Konsequenzen
      haben die Klimaziele für das Gasnetz in Bern?
    language: de
  affair_id: affairs:2020.SR.000007
  url:
  - text: >-
      https://stadtrat.bern.ch/de/sitzungen/detail.php?gid=000d6cf5f0bc4d89a5171e0123cfbff5#cea750a5bd7b420fa4da1c914f801384
    language: de
  datetime_created: '2025-01-17T21:25:52Z'
  datetime_modified: '2025-01-17T21:25:52Z'

```
##### Beispiel AgendaItem: Petition as an agenda item

```yaml
agenda_items:
- global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
  parent_meeting: ops:meeting_bern_rr_2025_04_02
  agenda_item_type: item
  datetime_begin_planned: '2025-04-02T00:00:00Z'
  agenda_item_title:
  - text: >-
      Petition «Gleichberechtigung für Tagesfamilien: Gleich hohe Betreuungsgutscheine
      für alle Anbieter im Kanton Bern». Regierungsrätliches Antwortschreiben
    language: de
  affair_id: affairs:2025.STA.622
  url:
  - text: >-
      https://www.rr.be.ch/de/start/beschluesse/suche/geschaeftsdetail.html?guid=21c50b86d21b4b4baeb1a76738ff82a3
    language: de
  datetime_created: '2025-04-25T11:11:40Z'
  datetime_modified: '2025-04-25T11:11:40Z'

```
##### Beispiel AgendaItem: Partial revision of several ordinances in French

```yaml
agenda_items:
- global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
  parent_meeting: ops:meeting_vaud_2008_04_30
  agenda_item_type: item
  datetime_begin_planned: '2008-04-30T00:00:00Z'
  agenda_item_position: 7
  agenda_item_number: '7'
  agenda_item_title:
  - text: >-
      Révision partielle de sept ordonnances fédérales relatives aux produits chimiques
    language: fr
  agenda_item_description:
  - text: 'Le Conseil d''Etat approuve le projet de révision partielle de sept ordonnances
      fédérales relatives aux produits chimiques. Il salue la volonté des autorités
      fédérales d''introduire dans la législation fédérale les modifications nécessaires
      découlant des nouveaux règlements européens, afin d''éliminer des entraves au
      commerce et d''augmenter la sécurité d''évaluation des produits chimiques.

      '
    language: fr
  url:
  - text: >-
      https://www.vd.ch/actualites/decisions-du-conseil-detat/seance-du-conseil-detat/seance/265632#7b3545e4-57dc-3901-aaa8-4020da6ab0c6
    language: fr
  datetime_created: '2024-12-06T10:50:04Z'
  datetime_modified: '2024-12-06T10:50:04Z'

```
##### Beispiel AgendaItem: Substantive affair without an agenda category

```yaml
agenda_items:
- global_uri: ops:49_253
  parent_meeting: ops:meeting_2025_03_31
  agenda_item_type: item
  datetime_begin_planned: '2025-03-31T00:00:00Z'
  agenda_item_position: 2
  agenda_item_number: '2'
  agenda_item_title:
  - text: Programmvereinbarungen 2024
    language: de
  datetime_created: '2025-03-29T01:07:14Z'
  datetime_modified: '2025-03-29T01:07:14Z'

```
##### Beispiel AgendaItem: Detailed deliberation of an article of an act

```yaml
agenda_items:
- global_uri: ops:agenda_item_be_2025_042
  parent_meeting: ops:meeting_be_committee_wak_2025_05_12
  agenda_item_type: item
  agenda_item_number: '4.2'
  agenda_item_position: 42
  agenda_item_title:
  - text: Steuergesetz - Detailberatung Art. 5
    language: de
  - text: Loi fiscale - Délibération détaillée art. 5
    language: fr
  agenda_item_description:
  - text: Beratung von Änderungsanträgen zu Artikel 5 des Steuergesetzes
    language: de
  - text: >-
      Délibération sur les propositions de modification de l'article 5 de la loi fiscale
    language: fr
  agenda_item_category: Gesetzgebung
  state_id: completed
  datetime_begin_planned: '2025-05-12T15:00:00Z'
  datetime_begin_actual: '2025-05-12T15:15:00Z'
  affair_id: affairs:be_2024_089_steuergesetz
  datetime_created: '2025-04-15T09:00:00Z'
  datetime_modified: '2025-05-12T15:20:00Z'

```
##### Beispiel AgendaItem: Interpellation as an agenda item

```yaml
agenda_items:
- global_uri: ops:06fb582b753c416d8fdb05fa13873545
  parent_meeting: ops:meeting_2011_11_23
  agenda_item_type: item
  datetime_begin_planned: '2011-11-23T00:00:00Z'
  agenda_item_position: 2
  agenda_item_title:
  - text: >-
      Interpellation Peter Mark betr. elektronische Datenerfassung durch Mitarbeiter
      im Werkhof – Versuchsphase
    language: de
  datetime_created: '2025-03-21T23:15:19Z'
  datetime_modified: '2025-03-21T23:15:19Z'

```
##### Beispiel AgendaItem: Substantive affair from a cantonal parliamentary information system

```yaml
agenda_items:
- global_uri: ops:87b69a72919445a493a061d9b0daeba3
  parent_meeting: ops:meeting_be_2025_06_02
  agenda_item_type: item
  datetime_begin_planned: '2025-06-02T00:00:00Z'
  agenda_item_title:
  - text: Differenzierte Anpassung des Gehalts von Lehrpersonen ohne Lehrdiplom
    language: de
  affair_id: affairs:2025.GRPARL.81
  datetime_created: '2025-04-25T11:10:35Z'
  datetime_modified: '2025-04-25T11:10:35Z'

```
##### Beispiel AgendaItem: Agenda item with a final vote

```yaml
agenda_items:
- global_uri: ops:agenda_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  agenda_item_type: item
  agenda_item_number: '15'
  agenda_item_position: 15
  agenda_item_title:
  - text: Energiegesetz - Schlussabstimmung
    language: de
  agenda_item_description:
  - text: Schlussabstimmung über das revidierte Energiegesetz des Kantons St. Gallen
    language: de
  agenda_item_category: Gesetzgebung
  state_id: completed
  datetime_begin_planned: '2025-03-15T14:00:00Z'
  datetime_begin_actual: '2025-03-15T14:30:00Z'
  affair_id: affairs:sg_2024_123_energiegesetz
  datetime_created: '2025-02-01T10:00:00Z'
  datetime_modified: '2025-03-15T14:35:00Z'

```
##### Beispiel AgendaItem: Popular motion within a group of agenda items

```yaml
agenda_items:
- global_uri: ops:16155798_4
  parent_meeting: ops:meeting_schaffhausen_2025_03_31_b
  agenda_item_type: item
  datetime_begin_planned: '2025-03-31T00:00:00Z'
  agenda_item_position: 3
  agenda_item_number: '3'
  agenda_item_title:
  - text: >-
      Volksmotion Nr. 2024/1 von Sandro Mamedow und Livia Schraff (Erstunterzeichnende)
      sowie weitere 150 Mitunterzeichnende vom 22. März 2024 mit dem Titel: «Für eine
      Stimme der Studierenden im Hochschulrat der Pädagogischen Hochschule Schaffhausen
      (PHSH)»
    language: de
  agenda_item_category: Traktanden
  affair_id: affairs:MOT_2024_1
  datetime_created: '2025-05-02T11:23:49Z'
  datetime_modified: '2025-05-02T11:23:49Z'

```
##### Beispiel AgendaItem: French-language agenda item postulate

```yaml
agenda_items:
- global_uri: ops:2023_10_03-52
  parent_meeting: ops:meeting_lausanne_2023_10_03
  agenda_item_type: item
  datetime_begin_planned: '2023-10-03T00:00:00Z'
  agenda_item_position: 52
  agenda_item_number: '52'
  agenda_item_title:
  - text: >-
      Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité commerciale »
      (FIM)
    language: fr
  state_id: postponed
  agenda_item_category: RAPPORTS
  affair_id: affairs:POS22/029
  url:
  - text: >-
      https://www.lausanne.ch/apps/agir/affaire/81/b7157ea2a4994086b65cf176768c6381.htm
    language: fr
  datetime_created: '2025-02-08T12:33:10Z'
  datetime_modified: '2025-02-08T12:33:10Z'

```
##### Beispiel AgendaItem: Postulate with a voting

```yaml
agenda_items:
- global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
  parent_meeting: ops:meeting_luzern_2025_01_28_b
  agenda_item_type: item
  datetime_begin_planned: '2025-01-28T00:00:00Z'
  agenda_item_position: 14
  agenda_item_number: '14'
  agenda_item_title:
  - text: >-
      Postulat Stadelmann Karin Andrea und Mit. über die Überprüfung und Anpassung
      der Kriterien zum früheren Eintritt von Kindern in die Basisstufe (den freiwilligen
      Kindergarten) / Bildungs- und Kulturdepartement
    language: de
  agenda_item_category: voting
  url:
  - text: >-
      https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=fa732e0e-7e5f-4d45-994a-fc74720c0781
    language: de
  affair_id: affairs:2023P_102
  datetime_created: '2025-01-29T06:59:41Z'
  datetime_modified: '2025-01-29T06:59:41Z'

```
##### Beispiel AgendaItem: Urgent interpellation in French

```yaml
agenda_items:
- global_uri: ops:2025_05_20-23
  parent_meeting: ops:meeting_lausanne_2025_05_20
  agenda_item_type: item
  datetime_begin_planned: '2025-05-20T00:00:00Z'
  agenda_item_position: 23
  agenda_item_number: '23'
  agenda_item_title:
  - text: >-
      Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : « Interpellation
      urgente de Kulmiye Yusuf et crts – Solidarité sans frontières, Lausanne en faveur
      du respect du droit international et de la protection des populations civiles
      à Gaza »
    language: fr
  state_id: not_treated
  agenda_item_category: ANNONCES ET INTERPELLATIONS
  affair_id: affairs:INT25/027
  url:
  - text: >-
      https://www.lausanne.ch/apps/agir/affaire/6c/049b6c612fe2428f9be66ea39522ac6c.htm
    language: fr
  datetime_created: '2025-06-07T23:50:18Z'
  datetime_modified: '2025-06-07T23:50:18Z'

```






</div>

### Enum: AgendaItemTypeEnum []{#AgendaItemTypeEnum}




_Art des Traktandums, unterscheidet einzelne von gruppierten Traktanden._




<div data-search-exclude markdown="1">

URI: [ops:AgendaItemTypeEnum](https://ch.paf.link/schema/operations/AgendaItemTypeEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| item |  Einzelnes Traktandum  |
| | [ops:enum/agenda_item_type/item](ops:enum/agenda_item_type/item) |
| group |  Traktandengruppe  |
| | [ops:enum/agenda_item_type/group](ops:enum/agenda_item_type/group) |







</div>

## Protokoll (Protocol)

### Zweck der Entität

Während die Traktanden die **Planung** einer Sitzung abbilden, hält das Protokoll den **tatsächlichen Verlauf** nach der Sitzung fest. `Protocol` ist ein Wrapper-Container, der pro Sitzung (`Meeting`) genau einmal geführt wird und die effektiv behandelten Traktanden (`protocol_items`), Abstimmungen, Wortmeldungen sowie Wortlaut-Textsegmente und Dokumente bündelt.

```
Meeting
  ├─ agenda_items   (vorher: geplante Traktanden)
  └─ protocol_ref   (nachher: Niederschrift)
        ├─ protocol_items  → ProtocolItem (wie AgendaItem)
        ├─ votings
        ├─ speeches
        ├─ text_segments
        └─ documents
```



### Klasse: Protocol []{#Protocol}


_Das nach der Sitzung erstellte Protokoll. Ein Wrapper-Container, der die tatsächlich behandelten Traktanden (protocol_items), Abstimmungen, Wortmeldungen, Wortlaut-Textsegmente und verknüpfte Dokumente bündelt._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| protocol_items | * <br/> [ProtocolItem](#ProtocolItem) | Traktanden, wie sie im Protokoll tatsächlich festgehalten wurden.  |
| votings | * <br/> [Voting](#Voting) | Sammlung der Abstimmungen.  |
| speeches | * <br/> [Speech](#Speech) | Sammlung der Wortmeldungen.  |
| text_segments | * <br/> [TextSegment](#TextSegment) | Sammlung von Textsegmenten (z.B. Wortprotokoll).  |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | protocols | range | [Protocol](#Protocol) |
| [Meeting](#Meeting) | protocol_ref | range | [Protocol](#Protocol) |



















</div>

### ProtocolItem (protokolliertes Traktandum)

`ProtocolItem` erbt sämtliche Felder von `AgendaItem` (`is_a: AgendaItem`) und bildet ein Traktandum so ab, wie es im Protokoll tatsächlich festgehalten wurde.



### Klasse: ProtocolItem []{#ProtocolItem}


_Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| agenda_item_number | 0..1 <br/> String | Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern). <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| agenda_item_position | 0..1 <br/> Integer | Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| leading_actor_id | 0..1 <br/> String | Das federführende Departement für das Traktandum. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| speaking_actor_id | 0..1 <br/> String | Der Sprecher oder die Sprecherin bzw. die Departementsvorsteherin oder der Departementsvorsteher für das Traktandum. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | Titel des Traktandums. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| affair_id | 0..1 <br/> String | Die Verbindung zu den Geschäften des Traktandums. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | Untertitel oder ausführliche Beschreibung des Traktandums. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| state_id | 0..1 <br/> String | Zustands-Identifikator (Verweis auf das Status-Enum oder auf einen eigenen Zustand). <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| state_name | 0..1 <br/> String | Benutzerdefinierte Zustandsbeschreibung für die Sitzung. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| landing_page | 0..1 <br/> String | URL mit weiteren Informationen. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing Page oder weiterführende Webadresse, mehrsprachig. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| agenda_item_category | 0..1 <br/> String | Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden). <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| parent_agenda_item | 0..1 <br/> String | Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | Die Resolution oder Entscheidung zu diesem Traktandum. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. <br/><br/>Vererbung: [AgendaItem](#AgendaItem) |
| date_begin_actual | 0..1 <br/> Date | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Protocol](#Protocol) | protocol_items | range | [ProtocolItem](#ProtocolItem) |



















</div>

## Gemeinsame Beratung (JointDebate)

### Zweck der Entität

`JointDebate` fasst mehrere Traktanden zusammen, die gemeinsam beraten werden – etwa inhaltlich zusammenhängende Geschäfte, die in einer einzigen Debatte behandelt werden.



### Klasse: JointDebate []{#JointDebate}


_Traktanden die gemeinsam behandelt werden._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | Sammlung der Traktanden.  |






















</div>

## Resolution (Beschluss)

### Zweck der Entität

Die Resolution-Entität erfasst den formalen Beschluss zu einem Traktandum. Sie dokumentiert **was** entschieden wurde, während Voting dokumentiert **wie** (mit welchem Verfahren und Stimmenverhältnis) entschieden wurde.

### Beziehung zu AgendaItem und Voting

```
AgendaItem (Energiegesetz - Schlussabstimmung)
  ├─ Resolution (Annahme des Energiegesetzes)
  └─ Voting (120 Ja, 75 Nein, 5 Enthaltungen)
```

Ein AgendaItem kann mehrere Resolutions haben (z.B. bei mehreren Abstimmungen zum selben Traktandum). Jede Resolution referenziert typischerweise ein Voting, das die Abstimmungsdetails enthält.

### Typen von Resolutionen

Das **resolution_type**-Feld verwendet ein kontrolliertes Vokabular:

#### accepted
Das Traktandum wurde angenommen

**Anwendung:**
- Gesetzesvorlagen wurden angenommen
- Anträge wurden gutgeheissen
- Beschlüsse wurden gefasst

#### rejected
Das Traktandum wurde abgelehnt

**Anwendung:**
- Gesetzesvorlagen wurden abgelehnt
- Anträge wurden abgewiesen
- Ablehnungsbeschlüsse

#### referred_back
Rückweisung an ein anderes Gremium

**Anwendung:**
- Rückweisung an Kommission zur Überarbeitung
- Rückweisung an Regierung
- Zurück an andere Kammer (in Zweikammersystemen)

#### noted
Zur Kenntnis genommen

**Anwendung:**
- Berichte ohne Abstimmung
- Mitteilungen
- Informative Traktanden

#### postponed
Vertagt auf später

**Anwendung:**
- Aufschub der Behandlung
- Noch nicht entscheidungsreif
- Weitere Abklärungen nötig

#### withdrawn
Zurückgezogen

**Anwendung:**
- Antragsteller zieht Vorlage zurück
- Geschäft wird nicht weiterverfolgt

#### amended
Mit Änderungen angenommen

**Anwendung:**
- Gesetz mit Amendments angenommen
- Modifizierte Fassung beschlossen
- Kompromisslösung

#### no_decision
Kein Beschluss gefasst

**Anwendung:**
- Keine Mehrheit für irgendeinen Antrag
- Patt-Situation ohne Stichentscheid
- Nicht beschlussfähig

### Designentscheid: Warum separate Resolution-Entität?

**Alternative wäre gewesen:** Resolution-Typ direkt im AgendaItem speichern.

**Gründe für separate Entität:**

1. **Mehrere Beschlüsse pro Traktandum**: Ein Traktandum kann mehrere Beschlüsse haben (z.B. erst Änderungsantrag, dann Gesamtabstimmung)

2. **Strukturierte Verknüpfung zu Votings**: Klare 1:1-Beziehung zwischen Resolution und Voting

3. **Mehrsprachige Beschlusstexte**: Resolution kann ausführliche Beschlusstexte in mehreren Sprachen enthalten

4. **Zeitliche Flexibilität**: Resolution kann zeitlich vom AgendaItem getrennt erfasst werden

### Beschlusstext

- **title**: Kurze Zusammenfassung des Beschlusses
- **description**: Ausführlicher Beschlusstext

**Beispiel:**
- title: "Annahme Energiegesetz"
- description: "Der Nationalrat nimmt das Bundesgesetz über die Energiewende in der Fassung der Kommission mit 120 zu 75 Stimmen bei 5 Enthaltungen an."

### Verknüpfung zur Abstimmung

Das Feld **voting_id** verweist auf das zugehörige Voting, das die Abstimmungsdetails enthält:

- Stimmenverhältnis
- Abstimmungsverfahren
- Einzelstimmen (bei namentlichen Abstimmungen)

**Nicht alle Resolutions haben ein Voting:**
- "Zur Kenntnis genommen" erfolgt oft ohne formale Abstimmung
- Stille Annahmen
- Administrativbeschlüsse

### Zeitstempel

- **datetime_created**: Zeitpunkt des Beschlusses
- **datetime_modified**: Letzte Änderung (z.B. bei Korrekturen)

### URLs und Dokumentation

Das Feld **url** kann auf weiterführende Dokumente verweisen:
- Detaillierte Beschlusstexte
- Begründungen
- Rechtliche Grundlagen

### Anwendungsfälle in verschiedenen Kontexten

#### Gesetzgebungsverfahren
Mehrere Resolutions zu verschiedenen Phasen:
1. Resolution "Eintreten" (accepted/rejected)
2. Resolution zu Artikel 1 (accepted/amended)
3. Resolution zu Artikel 2 (accepted)
4. Resolution Gesamtabstimmung (accepted/rejected)

#### Differenzbereinigung (Zweikammersystem)
- Resolution "Zustimmung zur Fassung des Erstrats"
- Resolution "Festhalten an eigener Fassung"
- Resolution "Annahme Kompromissvorschlag"

#### Kommissionsarbeit
- Resolution "Rückweisung an Kommission mit Zusatzauftrag"
- Resolution "Annahme Kommissionsbericht"

### Technische Überlegungen

#### Granularität
Die Granularität der Resolution-Erfassung variiert:
- **Detailliert**: Jede Einzelabstimmung erhält eigene Resolution
- **Aggregiert**: Nur finaler Beschluss wird erfasst

Der Standard erlaubt beide Ansätze.

#### Mehrsprachigkeit
Bei mehrsprachigen Parlamenten (CH, BE, etc.) müssen Beschlusstexte in allen Amtssprachen erfasst werden. Dies erfolgt über MultilingualString-Arrays in title und description.

### Verwendungszwecke

1. **Offizielle Dokumentation**: Was wurde entschieden?
2. **Rechtliche Verbindlichkeit**: Formaler Beschlussnachweis
3. **Öffentliche Information**: Verständliche Zusammenfassung komplexer Abstimmungen
4. **Geschäftsführung**: Nachverfolgung von Beschlüssen und deren Umsetzung
5. **Statistische Auswertung**: Annahme-/Ablehnungsquoten



### Klasse: Resolution []{#Resolution}


_Eine Resolution oder Entscheidung zu einem Traktandum, einschliesslich Abstimmungsverfahren._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](#ResolutionTypeEnum) | Art der Resolution zum Traktandum.  |
| type_label | 0..1 <br/> String | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| vote_procedures | * <br/> String | Verfahren für die Abstimmung, wie geheime Abstimmung oder offene Abstimmung.  |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | resolutions | range | [Resolution](#Resolution) |
| [AgendaItem](#AgendaItem) | has_resolution | range | [Resolution](#Resolution) |
| [ProtocolItem](#ProtocolItem) | has_resolution | range | [Resolution](#Resolution) |



















</div>

### Enum: ResolutionTypeEnum []{#ResolutionTypeEnum}




_Art der Resolution zu einem Traktandum._




<div data-search-exclude markdown="1">

URI: [ops:ResolutionTypeEnum](https://ch.paf.link/schema/operations/ResolutionTypeEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| accepted |  Annahme  |
| | [ops:enum/resolution_type/accepted](ops:enum/resolution_type/accepted) |
| rejected |  Ablehnung  |
| | [ops:enum/resolution_type/rejected](ops:enum/resolution_type/rejected) |
| noted |  Kenntnisnahme  |
| | [ops:enum/resolution_type/noted](ops:enum/resolution_type/noted) |
| accepted_point_by_point |  Punktweise Annahme  |
| | [ops:enum/resolution_type/accepted_point_by_point](ops:enum/resolution_type/accepted_point_by_point) |
| accepted_with_postulate |  Annahme mit Postulat  |
| | [ops:enum/resolution_type/accepted_with_postulate](ops:enum/resolution_type/accepted_with_postulate) |
| orally_settled |  Mündlich erledigt  |
| | [ops:enum/resolution_type/orally_settled](ops:enum/resolution_type/orally_settled) |
| nearly_unanimous |  Beinahe einstimmig  |
| | [ops:enum/resolution_type/nearly_unanimous](ops:enum/resolution_type/nearly_unanimous) |
| other |  Andere Resolution, nicht durch Standardkategorien abgedeckt  |
| | [ops:enum/resolution_type/other](ops:enum/resolution_type/other) |







</div>

## Motion (Anträge)

### Zweck

Erfasst Anträge, die während der Sitzung gestellt werden (Änderungsanträge, Verfahrensanträge, etc.).

### Struktur

- **motion_type**: Art des Antrags
  - **amendment**: Änderungsantrag zu Gesetzestext
  - **procedural**: Verfahrensantrag (z.B. Schluss der Debatte)
  - **referral**: Rückweisungsantrag
  - **other**: Sonstige Anträge
- **title**: Kurztitel des Antrags
- **description**: Vollständiger Antragstext
- **proposer_person_id**: Antragsteller/in
- **seconder_person_id**: Mitstimmende (falls erforderlich)
- **result**: Ergebnis (accepted, rejected, withdrawn)

### Designentscheid

**Warum eigene Entität statt nur in AgendaItem?**
- Ein Traktandum kann mehrere Anträge enthalten
- Anträge haben eigene Lifecycle (gestellt, unterstützt, abgestimmt)
- Strukturierte Erfassung von Antragsteller und Unterstützern
- Separate Abstimmungen pro Antrag möglich

### Anwendung

Verknüpft mit AgendaItem und optional mit Voting:

```
AgendaItem (Energiegesetz - Art. 15)
  ├─ Motion (Änderungsantrag Person A)
  │   └─ Voting (Abstimmung über Änderungsantrag)
  ├─ Motion (Änderungsantrag Person B)
  │   └─ Voting (Abstimmung über Änderungsantrag)
  └─ Voting (Abstimmung über Artikel in Gesamtheit)
```



### Klasse: Motion []{#Motion}


_Ein formeller Antrag, der während der Verhandlungen eingereicht wird._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| title | 0..1 <br/> String | Titel des Elements.  |
| description | 0..1 <br/> String | Beschreibender Text zum Element.  |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |






















</div>

\newpage

<!-- ToDo: Nicole -->

# Abstimmungen und Wahlen

Parlamentarische Beschlussfassungen erfolgen entweder durch Abstimmungen über Sachfragen oder durch Wahlen von Personen. Der Standard unterscheidet diese beiden Mechanismen klar und erfasst bei offenen Verfahren zudem das individuelle Stimm- und Wahlverhalten jedes Parlamentsmitglieds. Parlamentspräsidentinnen oder Parlamentspräsidenten nehmen an Abstimmungen grundsätzlich nicht teil; sie stimmen nur bei Wahlen mit. Bei Abstimmungen mit Stimmengleichstand fällen sie den Stichentscheid. 

## Voting (Abstimmung)

## Zweck der Entität

"Voting" erfasst den Abstimmungsprozess und das Ergebnis einer formalen Entscheidung im Parlament. Die Entität dokumentiert sowohl den Abstimmungsgegenstand (Frage), als auch das Verfahren (wie wurde abgestimmt) und das Resultat (mit welchem Stimmenverhältnis).

## Arten von Abstimmungen

Der Standard unterscheidet verschiedene Abstimmungstypen über das Feld **voting_type**:

### intermediate
Zwischenabstimmungen während der Beratung.

**Beispiele:**
- Abstimmung über Eintreten auf ein Geschäft
- Abstimmung über einen Antrag
- Gegenüberstellung von zwei Anträgen, die sich gegenseitig ausschliessen oder sich auf denselben Textabschnitt beziehen
- Eventualabstimmung wenn zu einem Abstimmungsgegenstand mehr als zwei Anträge vorliegen
- Abstimmung über einen einzelnen Artikel eines Gesetzes
- Gesamtabstimmung nach der ersten Lesung eines Erlasses, der in zwei Lesungen beraten wird

### final
Die abschliessende Abstimmung über die gesamte Vorlage

**Beispiele:**
- Schlussabstimmung nach der letzten Lesung eines Erlasses
- Gesamtabstimmung über einen Beschluss
- Annahme oder Ablehnung einer Vorlage in ihrer Gesamtheit
- Punktweise Abstimmung über einen Vorstoss

### casting
Stichentscheid des/der Vorsitzenden bei Stimmengleichheit. Vorsitzende nehmen an Abstimmungen nicht teil, haben bei Stimmengleichheit jedoch den Stichentscheid. Bei geheimer Abstimmung gilt bei Stimmengleichheit der Antrag des vorberatenden Ratsorgans als angenommen. 

### secret
Geheime Stimmabgabe bei Abstimmungen und Wahlen

**Anwendung:**
- Wahl von Personen
- Abstimmung über besonders heikles Sachgeschäft wie Gnadengesuch oder Aufhebung der Immunität
- Abstimmung nach geheimer Beratung
- Geheime Abstimmung auf Antrag 

## Struktur einer Abstimmung

Eine Abstimmung ist immer einer Sitzungsphase und/oder einer Sitzung, einem Traktandum (Agenda-Item) und einem Geschäft mit Geschäftstitel und mit Geschäftsnummer zugeordnet. Sie umfasst den Abstimmungstyp, den Abstimmungsgegenstand (Frage), das Ergebnis und – bei nicht geheimer Abstimmung – die Einzelstimmen der Mitglieder. 
Sie kann entweder:

```
AgendaItem (15) Geschäft (Energiegesetz - Art. 15)
  └─ Voting (Zwischenabstimmung über Art. 15)
      ├─ IndividualVote (Person A: Ja)
      ├─ IndividualVote (Person B: Nein)
      └─ IndividualVote (Person C: Ja)
```


Beispiel Auswahl:
3 Optionen: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
5 Optionen: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=23f01ba9b3f3410cb9cfb85f32f3dfe0

## Abstimmungsverfahren

Das Feld **procedure** beschreibt die Art der Durchführung:

### Open procedures (Offene Abstimmungen)
- **show_of_hands**: Handzeichen (traditionell)
- **standing**: Aufstehen (seltener)
- **electronic**: Elektronische Abstimmung (häufig auf Bundesebene und Kantonsebene)
- **roll_call**: Namentliche Abstimmung mit Namensaufruf
- **remote_voting**: Externe Stimmabgabe bei Krisen (Einzelne Ratsmitglieder geben ihre Stimme dem Parlamentspräsidium im Vorfeld des Sitzungstags bekannt. Die extern abgegebenen Stimmen werden gleichzeitig mit der im Rat laufenden Abstimmung erfasst.
- **circulation_voting**: Zirkulationsverfahren bei Krisen (Das Parlamentspräsidium führt die Abstimmung im Zirkulationsverfahren durch und informiert über das Ergebnis)
- **virtual_voting**: Stimmabgabe an virtuellen Sitzungen in Krisenfällen.

### Secret procedures (Geheime Abstimmungen)
- **secret_ballot**: Geheime Wahl mit Stimmzetteln
- **electronic_secret**: Elektronische geheime Abstimmung

Die Wahl des Verfahrens beeinflusst, ob Einzelstimmen erfasst werden können:
- Offene Verfahren: Einzelstimmen dokumentierbar
- Geheime Verfahren: Nur Gesamtergebnis verfügbar


## Abstimmungsergebnis

Das Ergebnis wird auf zwei Arten erfasst:

### Detaillierte Zahlen
- **total_count_yes**: Anzahl Ja-Stimmen
- **total_count_no**: Anzahl Nein-Stimmen
- **total_count_abstention**: Anzahl Enthaltungen
- **total_other**: Stimmenzahlen für zusätzliche Optionen, wenn nicht nur Ja/Nein/Enthaltung zur Auswahl stehen (siehe Abschnitt "Mehrfachoptionen")
- **total_absent**: Anzahl Abwesende (die nicht abstimmen konnten)
- **total**: Gesamtzahl der abstimmenden Mitglieder (ohne Abwesende und Präsidiumsstimme)
- **majority_count**: Anzahl Stimmen, die für die erforderliche Mehrheit nötig waren

### Gesamtergebnis
Das Ergebnis wird als Freitext im Feld **result_text** beschrieben (z.B. "Mit 120 zu 75 Stimmen bei 5 Enthaltungen angenommen"). Die kategorische Entscheidung (angenommen / abgelehnt / Kenntnisnahme usw.) wird nicht auf der Abstimmung selbst, sondern über die Klasse **Resolution** (Slot **resolution_type**) zum Traktandum festgehalten. Bei Stimmengleichheit wird ein allfälliger Stichentscheid des Präsidiums über eine eigene Abstimmung (`voting_type: tie_breaker_president`) bzw. eine neue Abstimmung modelliert.

**Beispiel** (Schlussabstimmung, einfache Ja/Nein-Abstimmung):
- total_count_yes: 120
- total_count_no: 75
- total_count_abstention: 5
- total_absent: 0
- total: 200
- result_text: "Mit 120 zu 75 Stimmen bei 5 Enthaltungen angenommen"
- Resolution.resolution_type: accepted

<!-- TODO: weitere komplexere Beispiele ergänzen — Ordnungsantrag, Wiederholung einer Abstimmung. (Cup-/Mehrfachabstimmung und Stichentscheid sind abgedeckt.) -->

### Mehrfachoptionen (Auswahlabstimmungen / "gleichgerichtete Anträge")

Nicht jede Abstimmung kennt nur Ja, Nein und Enthaltung. Liegen zu derselben Sachfrage mehrere gleichgerichtete Anträge vor, stimmen die Mitglieder über mehr als zwei Varianten gleichzeitig ab (in Zürich umgangssprachlich "Cup-Abstimmung", technisch über mehrere Abstimmungsknöpfe). Die obsiegende Variante ist diejenige mit den meisten Stimmen.

Solche Verfahren werden wie folgt abgebildet:

- **voting_type** = `other`, ergänzt durch ein sprechendes **type_label** (z.B. "Gleichgerichtete Anträge (Mehrfachauswahl)").
- Die Standardfelder **total_count_yes / total_count_no / total_count_abstention** bleiben leer, da die Optionen nicht Ja/Nein/Enthaltung entsprechen.
- Jede Auswahloption erhält stattdessen einen Eintrag in **total_other** (Liste von `TotalOther` mit **count** und **label**). So lassen sich beliebig viele Optionen mit ihrer jeweiligen Stimmenzahl erfassen.
- Auf Ebene der Einzelstimme wird **individual_vote_type** = `other` gesetzt und die gewählte Option über **type_label** (z.B. "Auswahl A") festgehalten; abwesende Mitglieder erhalten `not_voted`.
- Als **majority_type** wird `other` verwendet, da nicht eine fixe Schwelle, sondern die relative Mehrheit unter den Optionen entscheidet.

**Beispiel** (Gemeinderat der Stadt Zürich, 86. Sitzung vom 28.02.2024, Geschäft 2023/361 "Wohnhaus Magnusstrasse 27, Netto-Zusatzkredit") — gleichgerichtete Anträge mit vier Auswahloptionen:

| Option | Stimmen |
|--------|---------|
| Auswahl A (obsiegend) | 75 |
| Auswahl B | 25 |
| Auswahl C | 12 |
| Auswahl D | 0 |
| Abwesend | 13 |

- Total abgegeben: 112 (von 125 Mitgliedern)
- Ergebnis: Auswahl A angenommen (relative Mehrheit)

Die vollständige Modellierung dieses Falls findet sich in `data_voting.yaml` (`ops:voting_zh_gr_2024_2023_361`).

## Mehrheitstypen

Das Feld **majority_type** definiert die erforderliche Mehrheit:

### simple
Einfache Mehrheit (mehr Ja als Nein)

**Anwendung:**
- Standardfall für die meisten Beschlüsse
- Enthaltungen zählen nicht mit

**Beispiel:** 100 Ja, 80 Nein, 20 Enthaltungen → Angenommen

### absolute
Absolute Mehrheit (mehr als die Hälfte aller Mitglieder)

**Anwendung:**
- Wahlen
- Verfassungsänderungen in einigen Kantonen
- Besonders wichtige Beschlüsse

**Beispiel:** Bei 200 Mitgliedern sind mindestens 101 Ja-Stimmen erforderlich

### two_thirds
Zweidrittelmehrheit

**Anwendung:**
- Dringlichkeitsklauseln auf Bundesebene
- Verfassungsänderungen in einigen Kantonen
- Aufhebung der Immunität

**Beispiel:** Bei 200 Mitgliedern sind mindestens 134 Ja-Stimmen erforderlich

### qualified
Qualifizierte Mehrheit (andere Schwellenwerte)

**Anwendung:**
- Spezielle Anforderungen in einzelnen Kantonen oder Gemeinden
- Das konkrete Quorum wird in **majority_threshold** angegeben

## Schwellenwert

Das Feld **majority_threshold** gibt bei qualifizierten Mehrheiten den genauen Schwellenwert an (z.B. 0.6 für 60%).

## Quorum

Das Feld **quorum** definiert die Mindestanzahl anwesender Mitglieder für die Beschlussfähigkeit:

**Beispiel:** Ein Parlament mit 200 Mitgliedern ist beschlussfähig, wenn mindestens 100 Mitglieder anwesend sind (quorum: 100).

## Namentliche Abstimmungen
Das Feld **named_vote** zeigt an, ob es sich um eine namentliche Abstimmung handelt: 

- **true**: Die Einzelstimmen werden erfasst und publiziert
- **false**: Nur das Gesamtergebnis wird erfasst

Namentliche Abstimmungen sind wichtig für:
- Transparenz des Abstimmungsverhaltens
- Analyse von Abstimmungsmustern
- Rechenschaftspflicht gegenüber Wählerinnen

## Beziehung zu Einzelstimmen

Bei namentlichen Abstimmungen verweist die Voting-Entität auf die einzelnen IndividualVote-Entitäten:

```
Voting
  ├─ IndividualVote (Person A)
  ├─ IndividualVote (Person B)
  └─ ...
```

**Beispiel:** Namensliste in Akkordeon https://www.tagblatt.gr.be.ch/shareparl?agendaItemUid=e65d81c90d1d43deb19ef078f7e363f3&segmentType=vote&unitName=default&scroll=true&autoplay=false 


## Beschreibung und Dokumentation

- **description**: Beschreibung worüber abgestimmt wurde (Abstimmungsgegenstand, Abstimmungsfrage)
- **url**: Mehrsprachige URLs zu Abstimmungsdetails

## Zeitstempel

- **datetime_created**: Zeitpunkt der Durchführung der Abstimmung
- **datetime_modified**: Letzte Aktualisierung (z.B. bei Korrekturen des Abstimmungsprotkolls)




### Klasse: Voting []{#Voting}


_Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| datetime_begin | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| voting_type | 0..1 <br/> [VotingTypeEnum](#VotingTypeEnum) | Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc.).  |
| type_label | 0..1 <br/> String | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| voting_title | * <br/> [MultilingualString](#MultilingualString) | Abstimmungstitel bzw. Gegenstand oder Frage. Wenn kein Gegenstand vorhanden ist, sollte nicht der Geschäftstitel verwendet werden.  |
| optional | 0..1 <br/> Boolean | Gibt an, ob die Sitzung oder Abstimmung optional ist.  |
| landing_page | 0..1 <br/> String | URL mit weiteren Informationen.  |
| label_yes | 0..1 <br/> String | Bedeutung einer „Ja“-Stimme.  |
| label_no | 0..1 <br/> String | Bedeutung einer „Nein“-Stimme.  |
| label_abstention | 0..1 <br/> String | Bedeutung einer Enthaltungsstimme.  |
| tie_breaker | 0..1 <br/> Boolean | Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde.  |
| total_count_yes | 0..1 <br/> Integer | Gesamtzahl der „Ja“-Stimmen.  |
| total_count_no | 0..1 <br/> Integer | Gesamtzahl der „Nein“-Stimmen.  |
| total_count_abstention | 0..1 <br/> Integer | Gesamtzahl der Enthaltungen.  |
| total_other | * <br/> [TotalOther](#TotalOther) | Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B. 5 Knöpfe in Zürich).  |
| total_absent | 0..1 <br/> Integer | Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total | 0..1 <br/> Integer | Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.).  |
| majority_count | 0..1 <br/> Integer | Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind.  |
| result_text | 0..1 <br/> String | Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. „Mit 78 Stimmen angenommen“.  |
| parent_meeting | 0..1 <br/> String | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| parent_agenda_item | 0..1 <br/> String | Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf.  |
| affair_id | 0..1 <br/> String | Die Verbindung zu den Geschäften des Traktandums.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Referenz auf das handelnde Organ/Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | votings | range | [Voting](#Voting) |
| [Protocol](#Protocol) | votings | range | [Voting](#Voting) |
| [IndividualVote](#IndividualVote) | parent_voting | range | [Voting](#Voting) |














#### Beispiele
##### Beispiel Voting: Zwischenabstimmung über einen Änderungsantrag

```yaml
votings:
- global_uri: ops:voting_be_2025_042
  voting_title:
  - text: Änderungsantrag Art. 5 Abs. 2
    language: de
  - text: Proposition de modification art. 5 al. 2
    language: fr
  voting_type: preliminary_vote
  datetime_begin: '2025-06-05T10:15:00Z'
  datetime_end: '2025-06-05T10:17:00Z'
  total_count_yes: 45
  total_count_no: 87
  total_count_abstention: 8
  total_absent: 10
  total: 150
  majority_type: absolute
  majority_count: 76
  result_text: Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt
  parent_agenda_item: ops:agenda_item_be_2025_042
  parent_meeting: ops:meeting_be_2025_06_05
  actor_id:
    global_uri: https://api.openparldata.ch/v1/bodies/253
    label: Grosser Rat Bern
    abbreviation:
    - value: GR
      language: de
  datetime_created: '2025-06-05T10:15:00Z'
  datetime_modified: '2025-06-05T10:15:00Z'

```
##### Beispiel Voting: Final vote with individual votes

```yaml
votings:
- global_uri: ops:voting_sg_2025_001
  voting_title:
  - text: Schlussabstimmung Energiegesetz
    language: de
  voting_type: final_vote
  datetime_begin: '2025-03-15T14:30:00Z'
  datetime_end: '2025-03-15T14:35:00Z'
  total_count_yes: 78
  total_count_no: 42
  total_count_abstention: 5
  total_absent: 3
  total: 128
  majority_type: absolute
  majority_count: 65
  result_text: Mit 78 zu 42 Stimmen bei 5 Enthaltungen angenommen
  parent_agenda_item: ops:agenda_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  actor_id:
    global_uri: https://api.openparldata.ch/v1/bodies/265
    label: Kantonsrat St. Gallen
    abbreviation:
    - value: KR
      language: de
  datetime_created: '2025-03-15T14:30:00Z'
  datetime_modified: '2025-03-15T14:35:00Z'

```
##### Beispiel Voting: Final vote on the budget

```yaml
votings:
- global_uri: ops:voting_zh_budget_2026
  voting_title:
  - text: Budgetbeschluss 2026
    language: de
  voting_type: final_vote
  datetime_begin: '2025-11-20T16:45:00Z'
  datetime_end: '2025-11-20T16:50:00Z'
  total_count_yes: 105
  total_count_no: 70
  total_count_abstention: 5
  total_absent: 0
  total: 180
  majority_type: absolute
  majority_count: 91
  result_text: Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen
  parent_agenda_item: ops:agenda_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  actor_id:
    global_uri: https://api.openparldata.ch/v1/bodies/275
    label: Kantonsrat Zürich
    abbreviation:
    - value: KR
      language: de
  datetime_created: '2025-11-20T16:45:00Z'
  datetime_modified: '2025-11-20T16:50:00Z'

```
##### Beispiel Voting: Motions in the same direction with multiple choice

```yaml
votings:
- global_uri: ops:voting_zh_gr_2024_2023_361
  voting_title:
  - text: >-
      Liegenschaften Stadt Zürich, Wohnhaus Magnusstrasse 27, Gesamtinstandsetzung,
      Grundrissanpassung, Netto-Zusatzkredit (Geschäft 2023/361)
    language: de
  voting_type: other
  type_label: Gleichgerichtete Anträge (Mehrfachauswahl)
  datetime_begin: '2024-02-28T00:00:00Z'
  datetime_end: '2024-02-28T00:00:00Z'
  landing_page: >-
    https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
  total_other:
  - count: 75
    label: Auswahl A (siegreich)
  - count: 25
    label: Auswahl B
  - count: 12
    label: Auswahl C
  - count: 0
    label: Auswahl D
  total_absent: 13
  total: 112
  majority_type: other
  result_text: >-
    Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25, Auswahl
    C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern).
  parent_agenda_item: ops:agenda_item_zh_gr_2024_2023_361
  parent_meeting: ops:meeting_zh_gr_2024_02_28
  affair_id: 2023/361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/
    label: Gemeinderat der Stadt Zürich
    abbreviation:
    - value: GR
      language: de
  datetime_created: '2024-02-28T00:00:00Z'
  datetime_modified: '2024-02-28T00:00:00Z'

```






</div>

### Enum: VotingTypeEnum []{#VotingTypeEnum}




_Art des Abstimmungsverfahrens._




<div data-search-exclude markdown="1">

URI: [ops:VotingTypeEnum](https://ch.paf.link/schema/operations/VotingTypeEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| preliminary_vote |  Zwischenabstimmung  |
| | [ops:enum/voting_type/preliminary_vote](ops:enum/voting_type/preliminary_vote) |
| final_vote |  Schlussabstimmung  |
| | [ops:enum/voting_type/final_vote](ops:enum/voting_type/final_vote) |
| tie_breaker_president |  Stichentscheid Präsidium  |
| | [ops:enum/voting_type/tie_breaker_president](ops:enum/voting_type/tie_breaker_president) |
| secret_vote |  Geheime Wahl/Abstimmung  |
| | [ops:enum/voting_type/secret_vote](ops:enum/voting_type/secret_vote) |
| other |  Andere Abstimmungsart  |
| | [ops:enum/voting_type/other](ops:enum/voting_type/other) |







</div>

### Enum: MajorityTypeEnum []{#MajorityTypeEnum}




_Art der für die Abstimmung erforderlichen Mehrheit._




<div data-search-exclude markdown="1">

URI: [ops:MajorityTypeEnum](https://ch.paf.link/schema/operations/MajorityTypeEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| absolute |  Absolutes Mehr.  |
| | [ops:enum/majority_type/absolute](ops:enum/majority_type/absolute) |
| two_thirds |  Zweidrittelmehr.  |
| | [ops:enum/majority_type/two_thirds](ops:enum/majority_type/two_thirds) |
| other |  Andere Mehrheitsschwelle, nicht durch die Standardkategorien abgedeckt.  |
| | [ops:enum/majority_type/other](ops:enum/majority_type/other) |







</div>



### Klasse: TotalOther []{#TotalOther}


_Zusätzliche Stimmzahlen, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B. Zürich verwendet 5 Knöpfe)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| count | 0..1 <br/> Integer | Die Anzahl der Stimmen für die Kategorie „Andere“.  |
| label | 0..1 <br/> String | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Voting](#Voting) | total_other | range | [TotalOther](#TotalOther) |



















</div>

## Individual Vote (Einzelstimme)

## Zweck der Entität

IndividualVote erfasst das Stimmverhalten einzelner Parlamentsmitglieder bei namentlichen Abstimmungen. Die Entität wird nur erstellt, wenn eine Abstimmung nicht geheim durchgeführt wird (Voting.is_nominal = true).

## Beziehung zur Abstimmung

Jede Individual Vote ist Teil eines übergeordneten Votings (Abstimmung):

```
Voting (Schlussabstimmung Energiegesetz)
  ├─ IndividualVote (Nationalrätin Anna Müller: Ja)
  ├─ IndividualVote (Nationalrat Beat Schweizer: Nein)
  ├─ IndividualVote (Nationalrätin Carla Rossi: Enthaltung)
  └─ ...
```

## Identifikation der Person

Die stimmende Person wird über das Feld **person_id** referenziert. Diese ID entspricht einer Person gemäss eCH-0294 Actors Standard.

Zusätzlich können weitere Identifikationsdaten erfasst werden:
- **person_name**: Name der Person (für schnellen Zugriff)
- **person_number**: Interne Nummer (z.B. Mandatsnummer)
- **person_political_group**: Fraktionszugehörigkeit
- **person_party**: Parteizugehörigkeit

## Arten von Stimmen

Neben `yes`, `no` und `abstention` kennt das Feld drei weitere Werte: `not_voted` für Mitglieder, die anwesend waren, aber nicht gestimmt haben, `tie_breaker` für den Stichentscheid des Präsidiums und `other` für alles, was sich nicht auf diese Achse bringen lässt. `other` ist das individuelle Gegenstück zu `total_other`: Bei einer Auswahlabstimmung hat die Person gestimmt, aber weder Ja noch Nein — welche Option sie gewählt hat, hält `type_label` fest („Auswahl A“). So bleibt die Einzelstimme auswertbar, ohne dass der Standard jede kantonale Auswahlmechanik als eigenen Enum-Wert führen muss.

Das Feld **vote** erfasst die Art der Stimmabgabe:

### yes
Ja-Stimme (Zustimmung)

**Bedeutung:** Die Person stimmt der Vorlage/dem Antrag zu.

### no
Nein-Stimme (Ablehnung)

**Bedeutung:** Die Person lehnt die Vorlage/den Antrag ab.

### abstention
Enthaltung

**Bedeutung:** Die Person nimmt an der Abstimmung teil, enthält sich aber der Stimme. Bei elektronischer Stimmabgabe drückt sie den Knopf "Enthaltung". 

## Stimmgewicht

Das Feld **weight** erfasst das Stimmgewicht:

- **Standardfall**: 1.0 (eine Stimme)
- **Spezialfälle**: Andere Werte möglich

### Anwendungsfälle für abweichendes Stimmgewicht

1. **Stellvertretung**: In einigen Systemen kann eine Person für eine abwesende Person mitstimmen (weight: 2.0)
3. **Gemeindeversammlungen**: In speziellen Fällen können juristische Personen mehrere Stimmen haben
4. **Historische Systeme**: Früher hatten in einigen Kantonen verschiedene Personengruppen unterschiedliches Stimmgewicht

## Gruppenzugehörigkeit

Das Feld **group_id** erfasst die Fraktionszugehörigkeit zum Zeitpunkt der Abstimmung:

**Nutzen:**
- Analyse des Abstimmungsverhaltens nach Fraktionen
- Ermittlung der Parteidisziplin
- Identifikation von Koalitionen

**Beispiel:** Bei einer Abstimmung über das Energiegesetz stimmen 90% der SP-Fraktion mit Ja, 80% der SVP-Fraktion mit Nein.

## Position und Reihenfolge

Das Feld **position** definiert die Gruppierung und Sortierreihenfolge bei der Darstellung:

**Anwendung:**
- Alphabetische Sortierung nach Nachname
- Sortierung nach Fraktion
- Sortierung nach Stimmabgabe (erst Ja, dann Nein, dann Enthaltungen)
- Gruppierung nach Fraktion, innerhalb der Fraktion nach Ja, Nein, Enthaltungen und innerhalb der Untergruppe alphabetisch sortiert

## Beschreibung und Kontext

Das Feld **description** kann zusätzliche Informationen erfassen:

**Beispiele:**
- "Enthaltung wegen Interessenkonflikt (Verwaltungsrat Energieunternehmen)"
- "Abwesend wegen Krankheit"

## Zeitstempel

- **datetime_created**: Erste Publikation
- **datetime_modified**: Letzte Aktualisierung (z.B. bei Korrekturen der Publikation)

## Anwesenheit vs. Stimmabgabe

Wichtiger Unterschied:

- **Attendance** (andere Entität): Erfasst die generelle Anwesenheit bei einer Sitzung
- **IndividualVote**: Erfasst die spezifische Stimmabgabe bei einer Abstimmung

Eine Person kann bei einer Sitzung anwesend sein (Attendance), aber bei einzelnen Abstimmungen mit "absent" oder "did_not_vote" erfasst werden (z.B. wenn sie kurz den Raum verlässt).

## Namentliche vs. geheime Abstimmungen

IndividualVote-Entitäten werden nur bei namentlichen (offenen) Abstimmungen erfasst:

- **Namentliche Abstimmung**: Jede Stimme wird erfasst und ist öffentlich
- **Geheime Abstimmung**: Nur das Gesamtergebnis wird erfasst, keine IndividualVotes



### Klasse: IndividualVote []{#IndividualVote}


_Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| parent_voting | 0..1 <br/> [Voting](#Voting) | Die ID der Abstimmung, die mit der Einzelstimme verbunden ist.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Referenz auf die handelnde Person (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| seat_nr | 0..1 <br/> String | Die Sitznummer der Einzelstimme, falls zutreffend.  |
| weight | 0..1 <br/> Integer | Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B. in Fällen, in denen eine Person mehrere Stimmen hat).  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](#IndividualVoteTypeEnum) | Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc.).  |
| type_label | 0..1 <br/> String | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | individual_votes | range | [IndividualVote](#IndividualVote) |














#### Beispiele
##### Beispiel IndividualVote: Ja-Stimme

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_123
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27235
    label: Paul Schlegel
  seat_nr: '1'
  individual_vote_type: 'yes'
  datetime_created: '2025-03-15T14:30:00Z'

```
##### Beispiel IndividualVote: No vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_456
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27234
    label: Andreas Eggenberger
  seat_nr: '2'
  individual_vote_type: 'no'
  datetime_created: '2025-03-15T14:30:00Z'

```
##### Beispiel IndividualVote: Abstention

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_789
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27233
    label: Thomas Ammann
  seat_nr: '3'
  individual_vote_type: abstention
  datetime_created: '2025-03-15T14:30:00Z'

```
##### Beispiel IndividualVote: Absent in a multiple-choice voting

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_abs1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/4
    label: Abwesendes Mitglied
  seat_nr: '103'
  individual_vote_type: not_voted
  datetime_created: '2024-02-28T00:00:00Z'

```
##### Beispiel IndividualVote: Yes vote on the budget

```yaml
individual_votes:
- global_uri: ops:vote_zh_budget_2026_person_101
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27237
    label: Thomas Wolf
  seat_nr: '1'
  individual_vote_type: 'yes'
  datetime_created: '2025-11-20T16:45:00Z'

```
##### Beispiel IndividualVote: No vote on the budget

```yaml
individual_votes:
- global_uri: ops:vote_zh_budget_2026_person_102
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/25208
    label: Jean-Daniel Strub
  seat_nr: '2'
  individual_vote_type: 'no'
  datetime_created: '2025-11-20T16:45:00Z'

```
##### Beispiel IndividualVote: Did not vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_321
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/25177
    label: Ruedi Thomann
  seat_nr: '4'
  individual_vote_type: not_voted
  datetime_created: '2025-03-15T14:30:00Z'

```
##### Beispiel IndividualVote: Individual vote for selection option C

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_c1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/3
    label: Mitglied Auswahl C
  seat_nr: '88'
  individual_vote_type: other
  type_label: Auswahl C
  datetime_created: '2024-02-28T00:00:00Z'

```
##### Beispiel IndividualVote: Individual vote for selection option A

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_a1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/1
    label: Mitglied Auswahl A
  seat_nr: '12'
  individual_vote_type: other
  type_label: Auswahl A
  datetime_created: '2024-02-28T00:00:00Z'

```
##### Beispiel IndividualVote: Individual vote for selection option B

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_b1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/2
    label: Mitglied Auswahl B
  seat_nr: '47'
  individual_vote_type: other
  type_label: Auswahl B
  datetime_created: '2024-02-28T00:00:00Z'

```






</div>

### Enum: IndividualVoteTypeEnum []{#IndividualVoteTypeEnum}




_Art der Einzelstimme eines Mitglieds._




<div data-search-exclude markdown="1">

URI: [ops:IndividualVoteTypeEnum](https://ch.paf.link/schema/operations/IndividualVoteTypeEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| yes |  Ja-Stimme  |
| | [ops:enum/individual_vote_type/yes](ops:enum/individual_vote_type/yes) |
| no |  Nein-Stimme  |
| | [ops:enum/individual_vote_type/no](ops:enum/individual_vote_type/no) |
| abstention |  Enthaltung  |
| | [ops:enum/individual_vote_type/abstention](ops:enum/individual_vote_type/abstention) |
| not_voted |  Nicht abgestimmt  |
| | [ops:enum/individual_vote_type/not_voted](ops:enum/individual_vote_type/not_voted) |
| tie_breaker |  Stichentscheid, meist durch Präsidium  |
| | [ops:enum/individual_vote_type/tie_breaker](ops:enum/individual_vote_type/tie_breaker) |
| other |  Andere Stimmabgabe  |
| | [ops:enum/individual_vote_type/other](ops:enum/individual_vote_type/other) |







</div>

## Election (Wahl)

## Begriff und Bedeutung

Eine Election (Wahl) bezeichnet die Bestimmung einer oder mehrerer Personen für ein Amt oder eine Funktion durch ein parlamentarisches Organ. Im Gegensatz zu Abstimmungen (Votings), bei denen über Sachfragen entschieden wird, geht es bei Wahlen um Personenentscheidungen.

## Unterschied: Wahl vs. Abstimmung

| Kriterium | Election (Wahl) | Voting (Abstimmung) |
|-----------|-----------------|---------------------|
| Gegenstand | Personen | Sachfragen, Vorlagen |
| Ergebnis | Gewählte Person(en) | Angenommen/Abgelehnt |
| Verfahren | Oft geheim | Oft offen |
| Mehrheit | Meist absolut | Meist einfach |

## Arten von Wahlen

Der Standard unterscheidet verschiedene Wahltypen über das Feld **election_type**:

### open
Offene Wahl

**Charakteristik:**
- Stimmabgabe ist öffentlich sichtbar
- Jedes Mitglied gibt seine Stimme offen ab
- Nachvollziehbar, wer wen gewählt hat

**Anwendung:**
- Wenn Transparenz gewünscht ist
- Bei unumstrittenen Wahlen
- In kleineren Gremien

### secret
Geheime Wahl

**Charakteristik:**
- Stimmabgabe ist anonym
- Wahlzettel oder elektronisches Geheimwahlsystem
- Nicht nachvollziehbar, wer wen gewählt hat

**Anwendung:**
- Personenwahlen (Standard)
- Wenn freie, unbeeinflusste Entscheidung gewährleistet werden soll
- Gesetzlich oft vorgeschrieben

**Beispiele auf Bundesebene:**
- Wahl des Bundesrats
- Wahl der Bundesrichter
- Wahl der Kommissionspräsidien

**Beispiele auf Kantonsebene:**
- Wahl der Parlamentspräsidentin oder des Parlamentspräsidenten
- Wahl der Regierungspräsidentin oder des Regierungspräsidenten
- Wahl der Präsidentinnen und Präsidenten der obersten kantonalen Gerichte
- Wahl der Richterinnen und Richter
- Wahl er Staatsschreiberin oder des Staatsschreibers
- Wahl der Kommissionspräsidentinnen oder der Kommissionspräsidenten
- Wahl idien
- Wahl der Kommissions

### tacit
Stille Wahl

**Charakteristik:**
- Keine formale Abstimmung erforderlich
- Wahl erfolgt durch Akklamation oder Konsens
- Nur wenn keine Gegenstimmen erhoben werden

**Anwendung:**
- Bei Einstimmigkeit
- Unumstrittene Wahlen
- Wiederwahlen ohne Gegenkandidaten

**Beispiel:** Wiederwahl eines Kommissionspräsidenten ohne Gegenkandidatur

## Zuordnung zu Traktanden

Jede Wahl ist einem AgendaItem zugeordnet:

```
AgendaItem (Wahl des Bundesrats)
  └─ Election (Wahl für Departement XY)
      ├─ Kandidat A: 120 Stimmen
      ├─ Kandidat B: 75 Stimmen
      └─ Leere Stimmzettel: 5
```

## Beschreibung und Titel

- **title**: Titel der Wahl (z.B. "Wahl Kommissionspräsidium WAK")
- **description**: Ausführliche Beschreibung, Kontext, besondere Umstände

## Wahlergebnis

Das Feld **result** erfasst das Ergebnis:

- **elected**: Person(en) gewählt
- **not_elected**: Keine Person gewählt (z.B. bei absoluter Mehrheit nicht erreicht)
- **deferred**: Wahl verschoben
- **withdrawn**: Wahl zurückgezogen

## Gewählte Person(en)

Das Feld **elected_person_id** enthält die ID(s) der gewählten Person(en) gemäss eCH-0294 Actors.

Bei Mehrfachwahlen (z.B. Wahl mehrerer Kommissionsmitglieder gleichzeitig) können mehrere IDs erfasst werden.

## Stimmenverteilung

Bei offenen Wahlen oder nach Publikation der Ergebnisse:

- **total_votes**: Gesamtzahl abgegebener Stimmen
- **valid_votes**: Gültige Stimmen
- **invalid_votes**: Ungültige Stimmen
- **blank_votes**: Leere Stimmzettel

Zusätzlich Details pro Kandidat (über separate Entitäten oder als strukturierte Daten).

## Wahlverfahren

Das Feld **procedure** beschreibt das konkrete Verfahren:

- **written_ballot**: Schriftliche Wahl mit Stimmzetteln
- **electronic**: Elektronische Wahl
- **show_of_hands**: Handzeichen (bei offenen Wahlen)
- **acclamation**: Akklamation (bei stillen Wahlen)

## Mehrheitsverhältnisse

Das Feld **majority_type** definiert die erforderliche Mehrheit:

### absolute
Absolute Mehrheit (mehr als die Hälfte der Stimmenden)

**Anwendung:**
- Bundesratswahl
- Wahl von Kommissionspräsidien
- Standardfall bei Personenwahlen

**Beispiel:** Bei 200 abgegebenen Stimmen sind mindestens 101 Stimmen erforderlich

**Besonderheit:** Wenn im ersten Wahlgang niemand die absolute Mehrheit erreicht, folgt meist ein zweiter Wahlgang, in dem die einfache Mehrheit genügt.

### simple
Einfache Mehrheit (mehr Stimmen als andere Kandidaten)

**Anwendung:**
- Zweiter Wahlgang nach erfolglosem ersten Wahlgang
- Einige Kommissionswahlen

### qualified
Qualifizierte Mehrheit

**Anwendung:**
- Seltener bei Wahlen
- Spezielle Funktionen mit erhöhten Anforderungen

## Wahlgänge

Bei Wahlen mit absoluter Mehrheit im ersten Wahlgang:

```
1. Wahlgang (absolute Mehrheit erforderlich)
   └─ Kein Kandidat erreicht absolute Mehrheit

2. Wahlgang (einfache Mehrheit genügt)
   └─ Kandidat A gewählt
```

Jeder Wahlgang wird als separate Election-Entität erfasst, verbunden über das gemeinsame AgendaItem.

## Zeitstempel

- **datetime_created**: Zeitpunkt der Durchführung
- **datetime_modified**: Letzte Aktualisierung

## URL und Dokumentation

- **url**: Mehrsprachige URLs zu Wahlunterlagen:
  - Kandidatenprofile
  - Wahlresultate
  - Protokolle

## Besonderheiten verschiedener Wahlen

### Bundesratswahl
- Geheime Wahl
- Absolute Mehrheit erforderlich (im 1. Wahlgang)
- Durch die Vereinigte Bundesversammlung

### Bundesrichterwahl
- Geheime Wahl
- Proporzprinzip (Berücksichtigung von Parteien, Landesteilen, Geschlechtern)

### Kommissionspräsidien
- Wahl durch das jeweilige Parlament
- Oft weniger öffentlich

### Kantons- und Gemeindeebene
- Grosse Vielfalt an Wahlverfahren
- Teilweise Volkswahl statt parlamentarische Wahl
- Unterschiedliche Mehrheitserfordernisse

## Transparenz und Geheimhaltung

Spannungsfeld:
- **Wahlgeheimnis**: Schutz der individuellen Wahlentscheidung
- **Transparenz**: Öffentliches Interesse am Wahlergebnis

Bei geheimen Wahlen:
- Nur Gesamtergebnis wird publiziert
- Keine IndividualVote-Entitäten
- Schutz der Wahlfreiheit

Bei offenen Wahlen:
- Individuelle Stimmabgaben können erfasst werden
- Höhere Transparenz
- Potenzielle soziale Druckeffekte



### Klasse: Election []{#Election}


_Ein Wahlverfahren zur Wahl von Personen in Positionen._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| datetime_begin | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](#ElectionTypeEnum) | Art des Wahlverfahrens.  |
| type_label | 0..1 <br/> String | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| title | 0..1 <br/> String | Titel des Elements.  |
| landing_page | 0..1 <br/> String | URL mit weiteren Informationen.  |
| total_absent | 0..1 <br/> Integer | Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total | 0..1 <br/> Integer | Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.).  |
| majority_count | 0..1 <br/> Integer | Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind.  |
| result_text | 0..1 <br/> String | Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. „Mit 78 Stimmen angenommen“.  |
| parent_meeting | 0..1 <br/> String | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| parent_agenda_item | 0..1 <br/> String | Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf.  |
| affair_id | 0..1 <br/> String | Die Verbindung zu den Geschäften des Traktandums.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Referenz auf das handelnde Organ/Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | elections | range | [Election](#Election) |



















</div>

### Enum: ElectionTypeEnum []{#ElectionTypeEnum}




_Art des Wahlverfahrens._




<div data-search-exclude markdown="1">

URI: [ops:ElectionTypeEnum](https://ch.paf.link/schema/operations/ElectionTypeEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| secret |  Geheime Wahl  |
| | [ops:enum/election_type/secret](ops:enum/election_type/secret) |
| open |  Offene Wahl  |
| | [ops:enum/election_type/open](ops:enum/election_type/open) |
| silent |  Stille Wahl ohne Gegenkandidatur  |
| | [ops:enum/election_type/silent](ops:enum/election_type/silent) |







</div>

\newpage

# Anwesenheit

Anwesenheitslisten halten fest, wer an einer Sitzung teilgenommen hat. Sie dokumentieren die Teilnahme und sind die Grundlage, auf der sich die Beschlussfähigkeit eines Gremiums beurteilen lässt.

## Attendance (Anwesenheit)

## Begriff und Bedeutung

Die Attendance (Anwesenheit) erfasst, welche Mitglieder eines parlamentarischen Organs bei einer Sitzung anwesend, abwesend oder entschuldigt waren. Sie dient der Dokumentation der Teilnahme und ist Voraussetzung für die Beschlussfähigkeit (Quorum).

## Zweiebenen-Struktur

Der Standard unterscheidet zwischen zwei Ebenen der Anwesenheitserfassung:

### 1. Attendance (Aggregierte Ebene)
Zusammenfassung der Anwesenheit für ein Meeting:
- Gesamtzahl Anwesende
- Gesamtzahl Abwesende (entschuldigt/unentschuldigt)
- Beschlussfähigkeit

### 2. IndividualAttendance (Individuelle Ebene)
Detaillierte Erfassung für jede einzelne Person:
- Wer war anwesend?
- Wer war abwesend?
- War die Abwesenheit entschuldigt?

```
Meeting (Nationalratssitzung 4. März 2024)
  └─ Attendance (Aggregierte Anwesenheit)
      ├─ IndividualAttendance (Person A: anwesend)
      ├─ IndividualAttendance (Person B: entschuldigt)
      ├─ IndividualAttendance (Person C: abwesend)
      └─ ...
```

## Attendance (Aggregierte Ebene)

### Zuordnung zu Meeting und Organ

- **parent_meeting**: Verweis auf die spezifische Sitzung, zu der die Anwesenheitsliste gehört
- **actor_id**: Verweis auf das Organ (Parlament, Kommission) gemäss eCH-0294 Actors
- **datetime_begin**: Zeitpunkt der Anwesenheitserfassung

### Aggregierte Zahlen

- **total_count**: Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen, z.B. 200 für Nationalrat, 46 für Ständerat)
- **total_present**: Anzahl anwesender Mitglieder
- **total_excused**: Anzahl entschuldigter Mitglieder
- **total_absent**: Anzahl unentschuldigt abwesender Mitglieder

**Beispiel:**
- Total: 200
- Anwesend: 185
- Entschuldigt: 12
- Abwesend: 3

### Beschlussfähigkeit

Die Beschlussfähigkeit (Quorum) ergibt sich aus dem Verhältnis von `total_present` zu `total_count` und den jeweiligen Quorum-Regeln des Gremiums. Sie wird daher nicht als eigenes Feld gespeichert, sondern bei Bedarf datenseitig berechnet.

## IndividualAttendance (Individuelle Ebene)

### Verknüpfung

- **parent_attendance**: Verweis auf das übergeordnete `Attendance`-Aggregat (das wiederum am Meeting hängt). So wird die individuelle Erfassung sauber dem Meeting zugeordnet.
- **actor_id**: Verweis auf die Person gemäss eCH-0294 Actors

### Anwesenheitstyp

Das Feld **attendance_type** (Enum `AttendanceTypeEnum`) erfasst die Art der Anwesenheit:

- **present**: Persönlich anwesend
- **remote**: Per Fernzugriff (z.B. Videokonferenz) anwesend
- **substitute**: Stellvertretung — eine andere Person hat in der Vertretung teilgenommen

> Die Modellierung der Stellvertretung (z.B. wer hat wen vertreten, mit welchem Stimmrecht) wird in [Issue #24](https://github.com/swiss/political-affairs-ech-group/issues/24) weiter ausgearbeitet.
>
> Eine zweite Status-Achse `present` / `excused` / `absent` ("ob anwesend") parallel zur bestehenden Achse "wie anwesend" ist als Erweiterung in Diskussion.

### Grund

Das Feld **reason** (mehrsprachig) kann den Grund für Abwesenheit oder Verspätung als Freitext erfassen.

## Unterschied: Attendance vs. IndividualVote

Wichtige Abgrenzung:

| Aspekt | Attendance | IndividualVote |
|--------|------------|----------------|
| Erfasst | Anwesenheit bei Sitzung | Stimmabgabe bei Abstimmung |
| Zeitpunkt | Beginn/während Sitzung | Zeitpunkt der Abstimmung |
| Granularität | Pro Meeting | Pro Voting |

**Beispiel:** Eine Person kann bei der Sitzung anwesend sein (Attendance: present), aber bei einer spezifischen Abstimmung als absent erfasst werden (IndividualVote: absent), weil sie in diesem Moment kurz den Raum verlassen hat.

## Verwendungszwecke

Die Attendance-Entitäten ermöglichen:

1. **Dokumentation**: Nachvollziehbare Erfassung der Teilnahme
2. **Quorum-Prüfung**: Sicherstellung der Beschlussfähigkeit
3. **Transparenz**: Öffentliche Information über Anwesenheit
4. **Rechenschaft**: Kontrolle der Pflichtenerfüllung
5. **Statistik**: Auswertung von Anwesenheitsquoten
6. **Administration**: Berechnung von Entschädigungen und Spesen



### Klasse: Attendance []{#Attendance}


_Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, Entschuldigte)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| datetime_begin | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Referenz auf das handelnde Organ/Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| total_count | 0..1 <br/> Integer | Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen).  |
| total_present | 0..1 <br/> Integer | Gesamtzahl der anwesenden Mitglieder.  |
| total_absent | 0..1 <br/> Integer | Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total_excused | 0..1 <br/> Integer | Gesamtzahl der entschuldigten Abwesenheiten.  |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | attendances | range | [Attendance](#Attendance) |
| [IndividualAttendance](#IndividualAttendance) | parent_attendance | range | [Attendance](#Attendance) |



















</div>



### Klasse: IndividualAttendance []{#IndividualAttendance}


_Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft über das übergeordnete Attendance-Aggregat)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| parent_attendance | 0..1 <br/> [Attendance](#Attendance) | Das Attendance-Aggregat, zu dem dieser einzelne Anwesenheits-Eintrag gehört.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Referenz auf die handelnde Person (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| attendance_type | 0..1 <br/> [AttendanceTypeEnum](#AttendanceTypeEnum) | Art der individuellen Anwesenheit.  |
| reason | * <br/> [MultilingualString](#MultilingualString) | Grund für Abwesenheit oder Verspätung (Freitext, mehrsprachig).  |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | individual_attendances | range | [IndividualAttendance](#IndividualAttendance) |



















</div>

### Enum: AttendanceTypeEnum []{#AttendanceTypeEnum}




_Art der individuellen Anwesenheit._




<div data-search-exclude markdown="1">

URI: [ops:AttendanceTypeEnum](https://ch.paf.link/schema/operations/AttendanceTypeEnum)

#### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| remote |  Teilnahme per Fernzugriff  |
| | [ops:enum/attendance_type/remote](ops:enum/attendance_type/remote) |
| substitute |  Stellvertretung  |
| | [ops:enum/attendance_type/substitute](ops:enum/attendance_type/substitute) |
| present |  Persönlich anwesend  |
| | [ops:enum/attendance_type/present](ops:enum/attendance_type/present) |







</div>

\newpage

<!-- ToDo: David -->

<!--
Debatte

* -> Video Aufzeichnung -> Worttransskript
*   -> Wortprotokol -> Text to Timestamp -> Text beinhaltet die Timestamps -> Textdokument (mit oder ohne definition vom Format (spantypen))
*   -> Aufbereitetes Proktoll -> AgendaItem to Timestamp
-->

# Wortmeldungen

Wortmeldungen halten die parlamentarische Debatte fest — wer wann zu welchem Traktandum gesprochen hat, mit dem Wortlaut als Text und, wo vorhanden, als Audio- oder Videoaufzeichnung.

## Speech (Wortmeldung, Votum)

## Begriff und Bedeutung

Eine Speech (Wortmeldung, Votum) bezeichnet einen mündlichen Beitrag einer Person während einer parlamentarischen Sitzung. Sie ist das zentrale Instrument der politischen Debatte und Meinungsäusserung im Parlament.

## Arten von Speeches

Parlamentarische Wortmeldungen haben verschiedene Formen:

### Hauptvoten
- Ausführliche Stellungnahmen zu einem Geschäft
- Begründung von Anträgen
- Darlegung der Fraktionsmeinung

### Kurzinterventionen
- Kurze Wortmeldungen
- Zwischenfragen
- Richtigstellungen

### Fraktionserklärungen
- Offizielle Stellungnahme einer Fraktion
- Vorgetragen durch Fraktionssprecher/in

### Regierungsvoten
- Stellungnahmen von Regierungsmitgliedern
- Beantwortung von Fragen
- Verteidigung von Vorlagen

## Struktur und Zuordnung

Eine Speech ist immer einem bestimmten Kontext zugeordnet:

```
Meeting (Sitzung)
  └─ AgendaItem (Traktandum)
      └─ Speech (Wortmeldung Person A)
          ├─ TextSegment (Transkription)
          ├─ Media (Audio-Aufzeichnung)
          └─ Media (Video-Aufzeichnung)
```

### Zuordnungsfelder

- **meeting_id**: Die Sitzung, in der die Wortmeldung erfolgte
- **agenda_item_id**: Das Traktandum, zu dem gesprochen wurde
- **person_id**: Die sprechende Person (gemäss eCH-0294 Actors)

## Identifikation der Sprechenden

- **person_id**: Eindeutige Identifikation der Person
- **person_name**: Name für schnellen Zugriff
- **role**: Rolle der Person (z.B. "Fraktionspräsident/in", "Berichterstatter/in", "Bundesrat/Bundesrätin")

## Zeitliche Erfassung

- **start_time**: Beginn der Wortmeldung
- **end_time**: Ende der Wortmeldung
- **duration**: Dauer in Sekunden (berechnet oder erfasst)

Diese Zeitangaben ermöglichen:
- Genaue Referenzierung in Audio-/Video-Aufzeichnungen
- Analyse der Redezeit pro Person/Fraktion
- Kontrolle der Einhaltung von Zeitlimiten

## Sprache der Wortmeldung

Das Feld **language** erfasst die Sprache, in der gesprochen wurde:

- **de**: Deutsch
- **fr**: Französisch
- **it**: Italienisch
- **rm**: Rätoromanisch
- **en**: Englisch

## Textdokumente

Das Feld **text_segments** verweist auf TextSegment-Entitäten, die den gesprochenen Text enthalten.

### Verschiedene Textversionen

#### Rohtranskript
- Wörtliche Niederschrift
- Unbearbeitet, mit Füllwörtern
- Direkt nach der Sitzung verfügbar

#### Bearbeitetes Transkript
- Redaktionell überarbeitet
- Grammatikalisch korrigiert
- Offizielle Protokollversion

#### Übersetzungen
- In andere Landessprachen
- Für internationale Publikationen

### TextSegment-Struktur

Jedes TextSegment kann enthalten:
- **text**: Der eigentliche Text
- **language**: Sprache des Texts
- **version**: Art der Version (raw, edited, translated)
- **format**: Format (plain, markdown, HTML)

## Multimedia-Aufzeichnungen

Das Feld **media** verweist auf Media-Entitäten mit Audio- und Video-Aufzeichnungen.

### Audio-Aufzeichnungen
- Originalton der Wortmeldung
- Format: MP3, WAV, etc.
- Technische Metadaten (Qualität, Bitrate)

### Video-Aufzeichnungen
- Visuelle Aufzeichnung (bei Plenarsitzungen)
- Format: MP4, WebM, etc.
- Verschiedene Auflösungen

### Livestreaming
- Echtzeit-Übertragung
- URL zum Stream
- Archivierung nach der Sitzung

## Titel und Beschreibung

- **title**: Kurzer Titel (z.B. "Votum zur Energiepolitik")
- **description**: Zusammenfassung oder Kontext der Wortmeldung

## Typ der Wortmeldung

Das Feld **speech_type** kann verschiedene Arten unterscheiden:

- **statement**: Stellungnahme
- **question**: Frage
- **response**: Antwort (z.B. Regierung auf Frage)
- **procedural**: Verfahrensantrag
- **declaration**: Erklärung



### Klasse: Speech []{#Speech}


_Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| language | 0..1 <br/> String | Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z.B. "de", "fr", "it", "en").  |
| start | 0..1 <br/> String | Startangabe oder Position.  |
| datetime_begin | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| actor_fullname | 0..1 <br/> String | Vollständiger Name der Akteurin oder des Akteurs bzw. der Person.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Referenz auf die handelnde Person (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| role | 0..1 <br/> String | Rolle der Person (z.B. Kommissionssprecherin oder Kommissionssprecher).  |
| text | 1 <br/> String | Textinhalt des Elements.  |
| text_format | 0..1 <br/> String | Format des Textes (text, html, html_with_timestamps).  |
| text_type | 0..1 <br/> String | Typ des Textes (Rohfassung, bearbeitete Fassung).  |
| landing_page | 0..1 <br/> String | URL mit weiteren Informationen.  |
| media_url | 0..1 <br/> String | URL zur Mediendatei (Audio/Video).  |
| media_type | 0..1 <br/> String | Art des Mediums (Audio, Video, Dokument).  |
| media_format | 0..1 <br/> String | MIME-Typ der Mediendatei.  |
| documents | * <br/> Work | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | speeches | range | [Speech](#Speech) |
| [Protocol](#Protocol) | speeches | range | [Speech](#Speech) |














#### Beispiele
##### Beispiel Speech: Wortmeldung mit Wortlauttext und Videoaufzeichnung

```yaml
speeches:
- global_uri: ops:366631
  language: fr
  datetime_begin: '2025-12-19T09:20:00+01:00'
  datetime_end: '2025-12-19T09:25:00+01:00'
  actor_fullname: Pascal Broulis
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/18682
    wikidata_uri: http://www.wikidata.org/entity/Q116407
    label: Pascal Broulis
  role: speaker
  text: >-
    Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec
    attention les différents commentaires qui ont été effectués sur mon postulat.
    Cela reste un postulat, ce n'est pas une motion. D'abord, je ne partage pas l'avis
    selon lequel ce postulat n'apporterait pas une valeur ajoutée. En effet, un "benchmark",
    à savoir un modèle chiffré de performance, permettrait de mieux comprendre les
    raisons des retards que notre pays rencontre en comparaison avec les principaux
    pays européens.
  text_format: html
  text_type: final
  landing_page: >-
    https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631
  media_url: https://par-pcache.simplex.tv/content?externalid=366631
  media_type: video
  media_format: video/mp4

```






</div>

\newpage

# Texte und Medien

Parlamentarische Debatten werden nicht nur als strukturierte Daten erfasst, sondern auch als Texte und Multimedia-Aufzeichnungen. Diese Entitäten ermöglichen die Verwaltung von Transkripten, Audio-/Video-Aufzeichnungen und weiteren Medienformaten sowie die technische Infrastruktur für Datenaustausch und Mehrsprachigkeit.

## TextSegment

### Zweck
Erfasst Textabschnitte mit Versionierung und Sprachvarianten. Wird primär für Transkriptionen von Wortmeldungen verwendet, kann aber auch für andere Textdokumente eingesetzt werden.

### Struktur
- **text**: Der eigentliche Textinhalt
- **language**: Sprachcode (ISO 639-1)
- **format**: Format des Texts (plain, markdown, html)
- **version_type**: Art der Version
  - **raw**: Unbearbeitetes Rohtranskript
  - **edited**: Redaktionell bearbeitete Version
  - **translated**: Übersetzung in andere Sprache
  - **summary**: Zusammenfassung

### Designentscheid
**Warum separate Entität?**
- Ermöglicht mehrere Versionen desselben Texts (Rohfassung, bearbeitet, übersetzt)
- Versionskontrolle und Nachvollziehbarkeit von Änderungen
- Flexibilität bei Formaten (Plain, Markdown, HTML für unterschiedliche Ausgabekanäle)

### Anwendung
Hauptsächlich verknüpft mit Speech-Entitäten:
```
Speech
  ├─ TextSegment (Rohtranskript, de)
  ├─ TextSegment (Bearbeitetes Protokoll, de)
  ├─ TextSegment (Übersetzung, fr)
  └─ TextSegment (Zusammenfassung, de)
```

## Media

### Zweck
Referenziert Mediendateien (Audio, Video, Dokumente), die zu parlamentarischen Aktivitäten gehören.

### Struktur
- **media_type**: Art der Mediendatei
  - **audio**: Audio-Aufzeichnung
  - **video**: Video-Aufzeichnung
  - **document**: Dokumente (PDF, etc.)
  - **image**: Bilder
- **url**: URL zur Mediendatei
- **mime_type**: MIME-Type (audio/mp3, video/mp4, application/pdf, etc.)
- **title**: Titel der Mediendatei
- **description**: Beschreibung
- **language**: Sprache (bei sprachbasierten Medien)
- **duration**: Dauer (bei Audio/Video, in Sekunden)
- **file_size**: Dateigrösse in Bytes
- **quality**: Qualitätsangabe (z.B. "720p", "high", "low")

### Designentscheid
**Warum generische Media-Entität?**
- Einheitliche Struktur für alle Medientypen
- Erweiterbar für neue Formate
- Technische Metadaten zentral erfasst
- Mehrere Qualitätsstufen derselben Aufzeichnung möglich

### Anwendung
Kann an verschiedene Entitäten gehängt werden:
```
Speech
  ├─ Media (Audio-Aufzeichnung, MP3, 256kbps)
  ├─ Media (Audio-Aufzeichnung, MP3, 128kbps)
  ├─ Media (Video-Aufzeichnung, MP4, 1080p)
  └─ Media (Video-Aufzeichnung, MP4, 480p)

AgendaItem
  └─ Media (PDF der Vorlage)

Meeting
  └─ Media (Livestream-URL)
```



### Klasse: TextSegment []{#TextSegment}


_Ein Textsegment wie Querverweise oder Zwischentitel in Sitzungsprotokollen._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| text | 1 <br/> String | Textinhalt des Elements.  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Protocol](#Protocol) | text_segments | range | [TextSegment](#TextSegment) |



















</div>



### Klasse: Media []{#Media}


_Mediendateien oder Dokumente (einschliesslich Protokolle in PDF/HTML/WORD oder Links zu Audio/Video)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](#HasIdentification) |
| title | 0..1 <br/> String | Titel des Elements.  |
| media_type | 0..1 <br/> String | Art des Mediums (Audio, Video, Dokument).  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing Page oder weiterführende Webadresse, mehrsprachig.  |
| version | 0..1 <br/> String | Versionsnummer oder Versionskennung.  |
| parent_type | 0..1 <br/> String | Typ des übergeordneten Objekts (Sitzung, Traktandum, Wortmeldung, Geschäft).  |






















</div>

\newpage

# Geteilte Elemente

## Referenzklassen

`PersonReference` und `GroupReference` benennen eine Person beziehungsweise eine Gruppe, ohne sie hier zu beschreiben: Wer eine Person oder ein Organ ist, definiert eCH-0294; der Ratsbetrieb verweist nur darauf. Neben dem Verweis hält die Referenz die wichtigsten Merkmale zum **Zeitpunkt der Verknüpfung** fest — bei einer Wortmeldung etwa die Fraktion, der die sprechende Person damals angehörte.

Das dient drei Zwecken:

- **Nützliche lokale Daten** ohne aufwändige Abfragen der vollständigen Entität
- **Keine Redundanz**, da nicht alle Angaben bei jeder Erwähnung wiederholt werden müssen
- **Implizite Versionierung**, da die Referenz unverändert bleibt, auch wenn sich die verknüpfte Person oder Gruppe später ändert

Anders als eine Entität ist eine Referenz nicht aus sich heraus identifiziert — sie benennt bloss eine identifizierte Entität. Deshalb ist die `global_uri` hier nicht obligatorisch: Verlangt wird nur, dass mindestens eine der beiden Angaben `local_id` oder `global_uri` gesetzt ist. Ein System, das von der referenzierten Entität nur die lokale Id kennt, gibt diese an; sie wird innerhalb derselben Lieferung aufgelöst. Über die Lieferung hinaus verweist die `global_uri`.



### Klasse: PersonReference []{#PersonReference}


_Kurzreferenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung. Ermöglicht historische Korrektheit auch wenn sich die Person später ändert. Die referenzierte Person wird über `local_id` oder `global_uri` bezeichnet; mindestens eines von beiden ist erforderlich._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator der referenzierten Entität. Er wird innerhalb derselben Lieferung aufgelöst. <br/><br/>Vererbung: HasReferenceIdentification |
| global_uri | 0..1 <br/> Uriorcurie | Die eindeutige, global gültige URI der referenzierten Entität. Im Unterschied zu einer local_id ist sie auch über die Lieferung hinaus auflösbar. <br/><br/>Vererbung: HasReferenceIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: HasReferenceIdentification |
| label | 1 <br/> String | Obligatorischer Kurzname zur Identifikation der Person innerhalb der Organisation (z.B. mit Geburtsjahr zur Unterscheidung von Personen mit gleichem Namen).  |
| label_long | 0..1 <br/> String | Optionaler langer Anzeigename mit akademischen Titeln und vollständigem amtlichem Namen (z.B. "Dr. Maria Muster-Beispiel").  |
| group_label | 0..1 <br/> String | Name des Gremiums zum Zeitpunkt der Verknüpfung.  |

###### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- local_id
- global_uri










#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [IndividualVote](#IndividualVote) | actor_id | range | [PersonReference](#PersonReference) |
| [IndividualAttendance](#IndividualAttendance) | actor_id | range | [PersonReference](#PersonReference) |
| [Speech](#Speech) | actor_id | range | [PersonReference](#PersonReference) |



















</div>



### Klasse: GroupReference []{#GroupReference}


_Kurzreferenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung. Die referenzierte Gruppe wird über `local_id` oder `global_uri` bezeichnet; mindestens eines von beiden ist erforderlich. Eine `local_id` wird innerhalb derselben Lieferung aufgelöst, eine `global_uri` auch darüber hinaus._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator der referenzierten Entität. Er wird innerhalb derselben Lieferung aufgelöst. <br/><br/>Vererbung: HasReferenceIdentification |
| global_uri | 0..1 <br/> Uriorcurie | Die eindeutige, global gültige URI der referenzierten Entität. Im Unterschied zu einer local_id ist sie auch über die Lieferung hinaus auflösbar. <br/><br/>Vererbung: HasReferenceIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: HasReferenceIdentification |
| label | 0..1 <br/> String | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| abbreviation | * <br/> MultilingualValue | Abkürzung (kann mehrsprachig sein).  |

###### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- local_id
- global_uri










#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Legislature](#Legislature) | actor_id | range | [GroupReference](#GroupReference) |
| [Meeting](#Meeting) | group_id | range | [GroupReference](#GroupReference) |
| [Meeting](#Meeting) | actor_id | range | [GroupReference](#GroupReference) |
| [Voting](#Voting) | actor_id | range | [GroupReference](#GroupReference) |
| [Election](#Election) | actor_id | range | [GroupReference](#GroupReference) |
| [Attendance](#Attendance) | actor_id | range | [GroupReference](#GroupReference) |



















</div>

## Mehrsprachige Texte

Bezeichnungen, Titel und Beschreibungen liegen in der Schweiz häufig in mehreren Sprachen vor. Statt je Sprache ein eigenes Feld zu führen, nimmt ein Slot vom Typ `MultilingualString` eine Liste von Einträgen mit `text` und `language` auf. Wer nur eine Sprache führt, liefert einen einzigen Eintrag — die Sprache ist auch dann anzugeben. Ebenso modelliert sind die Links: Viele Ratsinformationssysteme führen je Sprache eine eigene Adresse, weshalb auch `url` mehrsprachig ist.



### Klasse: MultilingualString []{#MultilingualString}


_Ein String, der Text in mehreren Sprachen enthalten kann._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| text | 1 <br/> String | Textinhalt des Elements.  |
| language | 1 <br/> String | Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z.B. "de", "fr", "it", "en").  |





#### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Legislature](#Legislature) | name | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | name | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | url | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | name | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | url | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | agenda_item_title | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | agenda_item_description | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | url | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | agenda_item_title | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | agenda_item_description | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | url | range | [MultilingualString](#MultilingualString) |
| [Voting](#Voting) | voting_title | range | [MultilingualString](#MultilingualString) |
| [IndividualAttendance](#IndividualAttendance) | reason | range | [MultilingualString](#MultilingualString) |
| [Media](#Media) | url | range | [MultilingualString](#MultilingualString) |



















</div>

## Mixin-Klassen

Drei Klassen tragen keine eigenen Daten, sondern bündeln Slots, die in vielen Klassen gleich aussehen: die Identifikation einer Entität, ihre Erstellungs- und Änderungsdaten sowie der zeitliche Verlauf eines Ereignisses mit geplantem und tatsächlichem Beginn und Ende. Sie stammen aus dem gemeinsamen Schema der Fachgruppe (eCH-0292) und werden von deren Standards eingebunden, damit dieselben Angaben überall gleich heissen und gleich funktionieren.

Ein Mixin ist keine Oberklasse: Es entsteht keine Instanz einer Mixin-Klasse, und in den Daten ist von ihr nichts zu sehen. Die Attributtabellen der Klassen führen die geerbten Slots deshalb einzeln auf und vermerken mit „Vererbung" die Herkunft — die drei folgenden Abschnitte erklären, was hinter dieser Angabe steht.



### Klasse: HasIdentification []{#HasIdentification}


_Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügung stellt. Sie wird für Entitäten verwendet, die aus sich heraus identifiziert sind; deren `global_uri` ist der Identifikator und daher obligatorisch._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.  |
| global_uri | 1 <br/> Uriorcurie | Eine eindeutige, global gültige URI für die Entität.  |
| wikidata_uri | 0..1 <br/> Uriorcurie | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans.  |



#### Mixin-Verwendung

[Container](#Container), [Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem), [Protocol](#Protocol), [Voting](#Voting), [IndividualVote](#IndividualVote), [Election](#Election), [Attendance](#Attendance), [IndividualAttendance](#IndividualAttendance), [Speech](#Speech), [TextSegment](#TextSegment), [Motion](#Motion), [Media](#Media)





















</div>



### Klasse: HasCreationModificationDates []{#HasCreationModificationDates}


_Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderungsdaten einer Entität zur Verfügung stellt._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| date_created | 0..1 <br/> Date | Das Datum, an dem eine Entität erstellt wurde.  |
| datetime_created | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.  |
| date_modified | 0..1 <br/> Date | Das Datum, an dem eine Entität zuletzt geändert wurde.  |
| datetime_modified | 0..1 <br/> Datetime | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.  |



#### Mixin-Verwendung

[Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem), [Protocol](#Protocol), [Voting](#Voting), [IndividualVote](#IndividualVote), [Election](#Election), [Attendance](#Attendance), [IndividualAttendance](#IndividualAttendance), [Speech](#Speech)





















</div>



### Klasse: IsEventWithDuration []{#IsEventWithDuration}


_Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder Vorkommnissen mit Zeitdauer zur Verfügung stellt._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| date_begin_actual | 0..1 <br/> Date | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| datetime_begin_actual | 0..1 <br/> Datetime | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| date_begin_planned | 0..1 <br/> Date | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| datetime_begin_planned | 0..1 <br/> Datetime | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| date_end_actual | 0..1 <br/> Date | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| datetime_end_actual | 0..1 <br/> Datetime | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| date_end_planned | 0..1 <br/> Date | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |
| datetime_end_planned | 0..1 <br/> Datetime | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer.  |



#### Mixin-Verwendung

[Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem)





















</div>

\newpage

# Anhang A – Referenzen & Bibliographie

Wo eine Version genannt ist, ist es diejenige, gegen die dieser Standard erarbeitet wurde.

## Standards der Fachgruppe „Politische Geschäfte"

Die Standards der Fachgruppe entstehen gemeinsam und verweisen aufeinander. Sie stehen zurzeit alle im Status „In Arbeit" (Stand: 10. August 2026); eine Version ist deshalb nicht angegeben.

| | |
|------------------|----------------------------------------------------------------------------------|
|eCH-0292|eCH-0292: Metaprozesse zu politischen Geschäften – gemeinsame Datenelemente, aus denen dieser Standard die Referenzklassen und die Mixins bezieht: [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|eCH-0294|eCH-0294: Politische Akteure – definiert Personen und Gruppen, auf die `PersonReference` und `GroupReference` verweisen: [https://www.ech.ch/de/ech/ech-0294](https://www.ech.ch/de/ech/ech-0294)|
|eCH-0295|eCH-0295: Parlamentarische Geschäfte – die Geschäfte, die in Traktanden, Abstimmungen und Wortmeldungen behandelt werden: [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|eCH-0296|eCH-0296: Erlasse und Gesetzestexte: [https://www.ech.ch/de/ech/ech-0296](https://www.ech.ch/de/ech/ech-0296)|
|eCH-0297|eCH-0297: Öffentliche Konsultationen: [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Codelisten und weitere Quellen

| | |
|------------------|----------------------------------------------------------------------------------|
|ISO 639-1|ISO (International Organization for Standardization). Sprachcodes, verwendet im Slot `language` von `MultilingualString`.|
|Dublin Core|DCMI Metadata Terms. Quelle mehrerer `slot_uri`-Zuordnungen (Präfix `dcterms`): [https://www.dublincore.org/specifications/dublin-core/dcmi-terms/](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)|
|LinkML|Modellierungssprache, in der dieser Standard definiert ist: [https://linkml.io](https://linkml.io)|

