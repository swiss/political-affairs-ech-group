---
title: "eCH-0293 Public Council Operations"
lang: en
toc: false
---

|**Name**|**Public Council Operations**|
|---|---|
|**eCH number**|eCH-0293|
|**Category**|Standard|
|**Maturity level**|Defined|
|**Version**|0.1.0|
|**Status**|In progress|
|**Adopted on**||
|**Issue date**||
|**Replaces version**||
|**Prerequisites**||
|**Annexes**|-|
|**Languages**|German (original) - English (data model)|
|**Authors**|Political Affairs specialist group: Nicole Aeby, David Imseng, Jonas Schärer, Lena Mina Friedrich, Manuel Weingartner, Orhan Saeedi, Michel Moret, Laurens Abu-Talib|
|**Publisher / Distribution**|eCH Association, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)|

\newpage

# Abstract

The standard eCH-0293 defines a common data model for recording and publishing information on public council operations in Switzerland. It covers the temporal organisation of parliamentary work (legislatures, sessions), the structuring of meetings and agenda items, votings and elections, individual votes, attendance lists as well as speeches and resolutions.

This standard is aimed at parliamentary services, software providers of parliamentary management systems, data users for analyses and visualisations, and open data platforms.

eCH-0293 is part of a family of standards for political data and works closely together with eCH-0294 (Political Actors), eCH-0295 (Parliamentary Affairs), eCH-0296 (Laws and Legal Texts) and eCH-0297 (Public Consultations).

\newpage

# Table of Contents

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
    <w:t>Right-click &gt; "Update field" to generate the table of contents.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```

\newpage

# Introduction

## The "Political Affairs" standard family

Political activity in Switzerland takes place at federal, cantonal and communal level – in parliaments and communal assemblies, in executives and administrations, in consultations and hearings, as well as through the direct-democratic participation of eligible voters. To this end, the "Political Affairs" specialist group of the eCH Association is developing a family of coordinated standards that structure this data across all federal levels. The standards use common data elements (eCH-0292) and reference one another via unique identifiers.

The family comprises:

- **eCH-0292 – Common Data Elements (Meta):** Defines the cross-cutting data elements and meta-processes on which the other standards build. eCH-0293 adopts from it, among other things, the identification and date elements as well as the FRBR structure for linked documents.
- **eCH-0293 – Public Council Operations (Operations) – this standard:** Describes public council operations – legislatures and sessions, meetings and agenda items, protocols and decisions, votings and elections, attendance as well as speeches.
- **eCH-0294 – Political Actors (Actors):** Defines persons, groups and bodies in the political context, as well as their memberships and interest links. eCH-0293 references these actors via `actor_id` – for instance which parliament convened and which person voted.
- **eCH-0295 – Parliamentary Affairs (Affairs):** Describes the life cycle of political affairs. Agenda items in eCH-0293 point to the corresponding affair via `affair_id`.
- **eCH-0296 – Enactments and Legal Texts (Laws):** Records the results of the parliamentary process – the adopted laws and enactments.
- **eCH-0297 – Public Consultations (Consultations):** Structures consultation procedures, which are often the starting point for parliamentary affairs.

The aim of this standard family is to create a commonly usable structure for political data and to provide organisations that publish information on political affairs with a robust data model.

## Structure of a delivery

A delivery is a `Container`: an envelope with a `global_uri` of its own and one collection per class — `legislatures`, `sessions`, `meetings`, `protocols`, `votings`, `elections`, `individual_votes`, `attendances`, `individual_attendances`, `speeches` and `resolutions`. Agenda items have no collection of their own: they are delivered within their meeting or session (`agenda_items`). All collections are optional: those who only publish sittings deliver only `meetings`.

The entities sit side by side in a flat structure and are connected by references — `parent_meeting`, `parent_voting`, `parent_attendance` and so on — rather than nested inside one another. A single sitting can thus be delivered later without resending the entire legislature, and the same entity can be referenced from several places. Where nesting renders the connection better, it remains possible: the session takes its sittings as a list, the protocol its agenda items, votings and speeches.



### Class: Container []{#Container}


_Container for the records of public council operations: legislatures, sessions, meetings, protocols, votings, elections, attendances, speeches and resolutions._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| legislatures | * <br/> [Legislature](#Legislature) | Collection of legislature records.  |
| sessions | * <br/> [Session](#Session) | Collection of session records.  |
| meetings | * <br/> [Meeting](#Meeting) | Collection of meeting records.  |
| protocols | * <br/> [Protocol](#Protocol) | Collection of protocol records.  |
| votings | * <br/> [Voting](#Voting) | Collection of voting records.  |
| elections | * <br/> [Election](#Election) | Collection of election records.  |
| individual_votes | * <br/> [IndividualVote](#IndividualVote) | Collection of individual vote records.  |
| attendances | * <br/> [Attendance](#Attendance) | Collection of attendance records.  |
| individual_attendances | * <br/> [IndividualAttendance](#IndividualAttendance) | Collection of individual attendance records.  |
| speeches | * <br/> [Speech](#Speech) | Collection of speech records.  |
| resolutions | * <br/> [Resolution](#Resolution) | Collection of resolution records.  |

















#### Examples
##### Example Container: legislature

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
    global_uri: "actors:gr_be"
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
##### Example Container: session

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
  agenda_items:
    - global_uri: ops:agenda_item_gl_landsgemeinde_2025_01
      agenda_item_type: "item"
      agenda_item_number: "1"
      agenda_item_position: 1
      agenda_item_title:
        - text: "Eröffnung der Landsgemeinde"
          language: "de"
  datetime_modified: "2025-04-25T13:40:34Z"
  datetime_created: "2025-04-23T22:58:39Z"

```
##### Example Container: meeting sr winter25 Sitzung6

```yaml
global_uri: ops:data_meeting_sr_winter25_Sitzung6

meetings:
  - global_uri: "parl:sr_winter25_sitzung_6"
    spatial: "https://ld.admin.ch/country/CHE"
    name:
      - text: "Sechste Sitzung"
        language: "de"
      - text: "Sixième séance"
        language: "fr"
    url:
      - text: "https://www.parlament.ch/de/ratsbetrieb/suche-Amtliches-bulletin"
        language: "de"
    actor_id:
      global_uri: "actors:staenderat"
      label: "Ständerat"
      abbreviation:
        - value: "SR"
          language: de
    actor_name: "Ständerat"
    datetime_begin_planned: "2025-12-19T08:15:00+01:00"
    # Referenz auf das Protokoll: nur der Identifikator. Das Protokoll selbst
    # steht unten unter `protocols` und wird in der Regel spaeter geliefert als
    # die Sitzung.
    has_protocol: "ops:protokoll_sr_winter25_sitzung_6"
    datetime_created: "2026-01-12T00:00:00+01:00"
    datetime_modified: "2026-01-12T00:00:00+01:00"
    agenda_items:
      - global_uri: ops:69905
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
    parent_meeting: "parl:sr_winter25_sitzung_6"
    parent_agenda_item: "ops:69905"
    language: "fr"
    datetime_begin: "2025-12-19T09:20:00+01:00"
    datetime_end: "2025-12-19T09:25:00+01:00"
    actor_fullname: "Pascal Broulis"
    actor_id:
      global_uri: "actors:person_pascal_broulis"
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

protocols:
  - global_uri: ops:protokoll_sr_winter25_sitzung_6
    parent_meeting: "parl:sr_winter25_sitzung_6"
    protocol_items:
      - global_uri: ops:protokollpunkt_69905
        agenda_item_type: "item"
        agenda_item_number: "6"
        agenda_item_position: 4
        agenda_item_title:
          - text: "Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich durchführen, um die Verzögerungen zu verstehen"
            language: "de"
        affair_id: "affairs:24.4471"
        datetime_begin_actual: "2025-12-19T09:20:00+01:00"
        landing_page: "https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3"
        agenda_item_category: "agenda_item"
        datetime_created: "2026-01-12T00:00:00+01:00"
        datetime_modified: "2026-01-12T00:00:00+01:00"
    datetime_created: "2026-01-12T00:00:00+01:00"
    datetime_modified: "2026-01-12T00:00:00+01:00"

```
##### Example Container: voting

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
  parent_protocol: ops:protocol_sg_2025_03_15
  parent_protocol_item: ops:protocol_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  actor_id:
    global_uri: "actors:kr_sg"
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
  parent_protocol: ops:protocol_be_2025_06_05
  parent_protocol_item: ops:protocol_item_be_2025_042
  parent_meeting: ops:meeting_be_2025_06_05
  actor_id:
    global_uri: "actors:gr_be"
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
  parent_protocol: ops:protocol_zh_2025_11_20
  parent_protocol_item: ops:protocol_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  actor_id:
    global_uri: "actors:kr_zh"
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
  parent_protocol: ops:protocol_zh_gr_2024_02_28
  parent_protocol_item: ops:protocol_item_zh_gr_2024_2023_361
  parent_meeting: ops:meeting_zh_gr_2024_02_28
  affair_id: "2023/361"
  actor_id:
    global_uri: "actors:gr_stadt_zuerich"
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
    global_uri: "actors:person_zh_stadt_1"
    label: "Mitglied Auswahl A"
  seat_nr: "12"
  individual_vote_type: "other"
  type_label: "Auswahl A"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_b1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "actors:person_zh_stadt_2"
    label: "Mitglied Auswahl B"
  seat_nr: "47"
  individual_vote_type: "other"
  type_label: "Auswahl B"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_c1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "actors:person_zh_stadt_3"
    label: "Mitglied Auswahl C"
  seat_nr: "88"
  individual_vote_type: "other"
  type_label: "Auswahl C"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_abs1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "actors:person_zh_stadt_4"
    label: "Abwesendes Mitglied"
  seat_nr: "103"
  individual_vote_type: "not_voted"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_sg_2025_001_person_123
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "actors:person_paul_schlegel"
    label: "Paul Schlegel"
  seat_nr: "1"
  individual_vote_type: "yes"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_456
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "actors:person_andreas_eggenberger"
    label: "Andreas Eggenberger"
  seat_nr: "2"
  individual_vote_type: "no"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_789
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "actors:person_thomas_ammann"
    label: "Thomas Ammann"
  seat_nr: "3"
  individual_vote_type: "abstention"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_321
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "actors:person_ruedi_thomann"
    label: "Ruedi Thomann"
  seat_nr: "4"
  individual_vote_type: "not_voted"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_zh_budget_2026_person_101
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: "actors:person_thomas_wolf"
    label: "Thomas Wolf"
  seat_nr: "1"
  individual_vote_type: "yes"
  datetime_created: "2025-11-20T16:45:00Z"

- global_uri: ops:vote_zh_budget_2026_person_102
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: "actors:person_jean_daniel_strub"
    label: "Jean-Daniel Strub"
  seat_nr: "2"
  individual_vote_type: "no"
  datetime_created: "2025-11-20T16:45:00Z"

```
##### Example Container: meeting complete

```yaml
global_uri: ops:meeting_examples_2025

meetings:

- global_uri: ops:meeting_sg_2025_03_15
  spatial: "https://ld.admin.ch/canton/17"
  name:
    - text: "Kantonsratssitzung vom 15. März 2025"
      language: "de"
  url:
    - text: "https://www.ratsinfo.sg.ch/sessions/2025-03-15"
      language: "de"
  actor_id:
    global_uri: "actors:kr_sg"
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
  parent_session: ops:session_sg_2025_03
  datetime_created: "2025-02-01T10:00:00Z"
  datetime_modified: "2025-03-15T17:30:00Z"
  agenda_items:
    - global_uri: ops:agenda_item_sg_2025_015
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

- global_uri: ops:meeting_be_committee_wak_2025_05_12
  spatial: "https://ld.admin.ch/canton/2"
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
  agenda_items:
    - global_uri: ops:agenda_item_be_2025_042
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

- global_uri: ops:meeting_gl_landsgemeinde_2025
  spatial: "https://ld.admin.ch/canton/8"
  name:
    - text: "Landsgemeinde 2025"
      language: "de"
  url:
    - text: "https://www.landsgemeinde.gl.ch/2025"
      language: "de"
  actor_id:
    global_uri: "actors:landsgemeinde_gl"
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
  parent_session: ops:session_gl_landsgemeinde_2025
  datetime_created: "2025-01-10T12:00:00Z"
  datetime_modified: "2025-05-04T13:45:00Z"

- global_uri: ops:meeting_zh_2025_11_20
  date_begin_planned: "2025-11-20"
  agenda_items:
    - global_uri: ops:agenda_item_zh_budget_2026
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
##### Example Container: meeting

```yaml
global_uri: ops:meetings_1
meetings:
  - spatial: "https://ld.admin.ch/canton/2"
    global_uri: ops:340dcf932fb044dd8f8c5c943267fbcc
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
    name:
      - text: "Donnerstag (Nachmittag)"
        language: "de"
    url:
      - text: "https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
        language: "de"
      - text: "https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
        language: "fr"
    actor_id:
      global_uri: "actors:gr_be"
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
##### Example Container: meeting item

```yaml
global_uri: ops:agenda_items_1

meetings:
  - global_uri: ops:meeting_bern_2022_03_17
    date_begin_planned: "2022-03-17"
    agenda_items:
      - global_uri: ops:cea750a5bd7b420fa4da1c914f801384
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

  - global_uri: ops:meeting_lausanne_2023_10_03
    date_begin_planned: "2023-10-03"
    agenda_items:
      - global_uri: ops:2023_10_03-52
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

  - global_uri: ops:meeting_lausanne_2025_05_20
    date_begin_planned: "2025-05-20"
    agenda_items:
      - global_uri: ops:2025_05_20-23
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

  - global_uri: ops:meeting_vaud_2008_04_30
    date_begin_planned: "2008-04-30"
    agenda_items:
      - global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
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

  - global_uri: ops:meeting_2011_11_23
    date_begin_planned: "2011-11-23"
    agenda_items:
      - global_uri: ops:06fb582b753c416d8fdb05fa13873545
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

  - global_uri: ops:meeting_schaffhausen_2025_03_31
    date_begin_planned: "2025-03-31"
    agenda_items:
      - global_uri: ops:16155798_3
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

  - global_uri: ops:meeting_bern_rr_2025_04_02
    date_begin_planned: "2025-04-02"
    agenda_items:
      - global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
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

  - global_uri: ops:meeting_2025_03_31
    date_begin_planned: "2025-03-31"
    agenda_items:
      - global_uri: ops:49_253
        agenda_item_type: item
        datetime_begin_planned: '2025-03-31T00:00:00Z'
        agenda_item_position: 2
        agenda_item_number: '2'
        agenda_item_title:
          - text: Programmvereinbarungen 2024
            language: de
        datetime_created: '2025-03-29T01:07:14Z'
        datetime_modified: '2025-03-29T01:07:14Z'

  - global_uri: ops:meeting_schaffhausen_2025_03_31_b
    date_begin_planned: "2025-03-31"
    agenda_items:
      - global_uri: ops:16155798_4
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

  - global_uri: ops:meeting_be_2025_06_02
    date_begin_planned: "2025-06-02"
    agenda_items:
      - global_uri: ops:87b69a72919445a493a061d9b0daeba3
        agenda_item_type: item
        datetime_begin_planned: '2025-06-02T00:00:00Z'
        agenda_item_title:
          - text: Differenzierte Anpassung des Gehalts von Lehrpersonen ohne Lehrdiplom
            language: de
        affair_id: affairs:2025.GRPARL.81
        datetime_created: '2025-04-25T11:10:35Z'
        datetime_modified: '2025-04-25T11:10:35Z'

  - global_uri: ops:meeting_luzern_2025_01_28
    date_begin_planned: "2025-01-28"
    agenda_items:
      - global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
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

  - global_uri: ops:meeting_luzern_2025_01_28_b
    date_begin_planned: "2025-01-28"
    agenda_items:
      - global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
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






</div>

\newpage

<!-- ToDo: Christian -->

# Temporal organisation of council operations

Council operations are structured in time by four classes:

```
Legislature (legislature)
  └─ Session (e.g. spring session)
      └─ Meeting (individual sitting)
          └─ AgendaItem (agenda item)
```

The legislature forms the long-term frame, the session structures the work within a legislature, the meeting is the concrete sitting in which affairs are deliberated, and the agenda item structures the individual sitting. The levels interlock in two ways: downwards they are embedded — the session takes up its sittings (`meetings`), sitting and session their agenda items (`agenda_items`); upwards, references point — the session to its legislature (`parent_legislature`), the sitting to its session (`parent_session`) or, where there is no session, directly to the legislature (`parent_legislature`). Within the agenda, `parent_agenda_item` represents the division into sub-items.

The first three classes are described below, the agenda item in the next chapter.

## Common elements

The three classes are deliberately built alike. The following fields have the same meaning on all levels.

**Identification.** `global_uri` is the identifier and is mandatory. `local_id` takes the id of the delivering system, `wikidata_uri` points to the Wikidata entry where one exists.

**Begin and end.** The temporal data is recorded twice: `date_begin_planned` and `date_end_planned` hold what was scheduled, `date_begin_actual` and `date_end_actual` what actually happened. Where the time of day matters, the `datetime_*` variants are available.

**Space and body.** `spatial` points to the spatial unit according to LINDAS — country, canton, district or commune, thus `https://ld.admin.ch/canton/2` rather than "BE". It is the same field with which eCH-0294 locates its groups, so that council operations and the actors who carry them point to the same resource. Who convenes within that spatial unit is stated by `actor_id`, a lightweight reference to the body according to eCH-0294.

**Linked documents.** `documents` links documents as FRBR works according to eCH-0292 — for the legislature, for instance, membership and affair registers, for the session the session programme, for the meeting the bulletin and annexes (the protocol, by contrast, via `has_protocol`).

## Legislature

A legislature denotes the period for which a parliament is elected and acts in its current composition.



### Class: Legislature []{#Legislature}


_Term of office of a parliament as a legislative assembly. Usually lasts four years._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| spatial | 0..1 <br/> String | Spatial reference to a LINDAS resource (fos-municipality number, fos-canton number, district, or country). Formats: municipality: https://ld.admin.ch/municipality/1234, district: https://ld.admin.ch/district/2301, canton: https://ld.admin.ch/canton/23, country: https://ld.admin.ch/country/CHE.  |
| administrative_id | 0..1 <br/> String | Administrative ID of the legislative body, such as a municipality, canton, or country.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Multilingual full designation.  |
| description | 0..1 <br/> String | Descriptive text of the element.  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | legislatures | range | [Legislature](#Legislature) |














#### Examples
##### Example Legislature: Cantonal legislature with a four-year term

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
    global_uri: actors:gr_be
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
##### Example Legislature: Completed federal legislature

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
##### Example Legislature: Ongoing cantonal legislature with a five-year term

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






</div>

## Session (sitting period)

A session is a continuous sitting period in which several meetings take place.



### Class: Session []{#Session}


_A session: a contiguous period of sittings within a legislature. It groups its meetings (meetings) and may also carry agenda items directly (agenda_items). The session is the only one of the three temporal levels that may be omitted: federal units without formal sessions leave it out and attach their meetings directly to the legislature (parent_legislature). Session and meeting may also coincide — a one-day sitting of a cantonal parliament or a Landsgemeinde is represented as a session with a single meeting, or as a session that carries its agenda items directly without any meeting._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| spatial | 0..1 <br/> String | Spatial reference to a LINDAS resource (fos-municipality number, fos-canton number, district, or country). Formats: municipality: https://ld.admin.ch/municipality/1234, district: https://ld.admin.ch/district/2301, canton: https://ld.admin.ch/canton/23, country: https://ld.admin.ch/country/CHE.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Multilingual full designation.  |
| number | 0..1 <br/> String | Number of the session or meeting as designated by the body, e.g. within the legislature, the session or the year. As a string it also allows roman numerals. Numbering practices vary widely, which is why number, sequential_number, position and meeting_abbreviation are available side by side.  |
| sequential_number | 0..1 <br/> Integer | Sequential number of the session or meeting as an integer, used for ordering.  |
| position | 0..1 <br/> String | Integer position within the superordinate sequence, e.g. of a session within the legislature.  |
| meeting_abbreviation | 0..1 <br/> String | Short designation of the session or meeting (e.g. "FS24" for the 2024 spring session).  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing page or further web address, multilingual.  |
| parent_legislature | 0..1 <br/> String | Identifier of the legislature to which the session or meeting belongs. A meeting that belongs to a session is assigned to the legislature through the session (parent_session); a meeting without a session — for instance a committee sitting or a sitting in a federal unit without formal sessions — refers to the legislature directly.  |
| meetings | * <br/> [Meeting](#Meeting) | Collection of meeting records.  |
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | Agenda items planned for this meeting or session, embedded as a list. On a meeting they form the agenda of the sitting. On a session they hold agenda items planned directly at the level of the session — where a federal unit does not break the session down into individual meetings (e.g. a Landsgemeinde or a one-day sitting of a cantonal parliament), or for items not (yet) assigned to a specific meeting, as in a session programme. The counterpart after the sitting are the items recorded in the protocol (Protocol.protocol_items).  |
| joint_debates | * <br/> [JointDebate](#JointDebate) | Joint debates attached to this record: on an agenda item, the debates in which it is deliberated together with other agenda items; on a meeting or a session, the joint debates held within it.  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | sessions | range | [Session](#Session) |














#### Examples
##### Example Session: One-day sitting period of a cantonal parliament

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
##### Example Session: Landsgemeinde as a sitting period

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
  agenda_items:
  - global_uri: ops:agenda_item_gl_landsgemeinde_2025_01
    agenda_item_type: item
    agenda_item_number: '1'
    agenda_item_position: 1
    agenda_item_title:
    - text: Eröffnung der Landsgemeinde
      language: de
  datetime_modified: '2025-04-25T13:40:34Z'
  datetime_created: '2025-04-23T22:58:39Z'

```
##### Example Session: Federal session with a trilingual designation

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
##### Example Session: Cantonal session with a bilingual designation

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






</div>

## Meeting (individual sitting)

A meeting is the individual sitting of a body — the level at which agenda items are deliberated, decisions taken and speeches recorded.



### Class: Meeting []{#Meeting}


_The individual sitting of a body — the level at which agenda items are deliberated, decisions taken and speeches recorded. The meeting is the node to which the other classes of this standard attach: its agenda items (AgendaItem) are embedded in it (agenda_items), while votings and elections (Voting, Election), speeches (Speech) and the attendance list (Attendance) reference it via `parent_meeting`. At this level, scheduled and actual times regularly diverge — a sitting scheduled for 14:00 only begins at 14:25 because of delays and ends at 17:30 instead of 18:00 — which is why both the planned and the actual begin and end are recorded._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| spatial | 0..1 <br/> String | Spatial reference to a LINDAS resource (fos-municipality number, fos-canton number, district, or country). Formats: municipality: https://ld.admin.ch/municipality/1234, district: https://ld.admin.ch/district/2301, canton: https://ld.admin.ch/canton/23, country: https://ld.admin.ch/country/CHE.  |
| administrative_id | 0..1 <br/> String | Administrative ID of the legislative body, such as a municipality, canton, or country.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Multilingual full designation.  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing page or further web address, multilingual.  |
| group_name | 0..1 <br/> String | Name of the group or body in plain text, in addition to the reference `group_id`.  |
| group_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the group or body (lightweight snapshot at time of linking).  |
| number | 0..1 <br/> String | Number of the session or meeting as designated by the body, e.g. within the legislature, the session or the year. As a string it also allows roman numerals. Numbering practices vary widely, which is why number, sequential_number, position and meeting_abbreviation are available side by side.  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| sequential_number | 0..1 <br/> Integer | Sequential number of the session or meeting as an integer, used for ordering.  |
| position | 0..1 <br/> String | Integer position within the superordinate sequence, e.g. of a session within the legislature.  |
| meeting_abbreviation | 0..1 <br/> String | Short designation of the session or meeting (e.g. "FS24" for the 2024 spring session).  |
| actor_name | 0..1 <br/> String | Name of the political body in plain text (e.g., Nationalrat), in addition to the reference `actor_id`.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| state | 0..1 <br/> [StateEnum](#StateEnum) | Whether the meeting takes place as planned at all (planned, canceled, postponed). A diverging, free-text designation goes into `state_name`.  |
| state_name | 0..1 <br/> String | Diverging, free-text status designation of the meeting, where the values of `state` do not suffice.  |
| description | 0..1 <br/> String | Descriptive text of the element.  |
| location | 0..1 <br/> String | Place where the meeting is held — the physical room ("Federal Palace, National Council chamber"), a video conference or a hybrid format.  |
| parent_meeting | 0..1 <br/> String | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on a voting, election, speech, attendance list or protocol it names the meeting in which the record arose. Agenda items do not carry it: they are embedded in their meeting.  |
| parent_legislature | 0..1 <br/> String | Identifier of the legislature to which the session or meeting belongs. A meeting that belongs to a session is assigned to the legislature through the session (parent_session); a meeting without a session — for instance a committee sitting or a sitting in a federal unit without formal sessions — refers to the legislature directly.  |
| parent_session | 0..1 <br/> String | Identifier of the session to which the meeting belongs.  |
| documents | * <br/> Work | Sitting documents such as the bulletin (Tagblatt) or annexes, as FRBR Works. The protocol is not linked here but via `has_protocol`.  |
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | Agenda items planned for this meeting or session, embedded as a list. On a meeting they form the agenda of the sitting. On a session they hold agenda items planned directly at the level of the session — where a federal unit does not break the session down into individual meetings (e.g. a Landsgemeinde or a one-day sitting of a cantonal parliament), or for items not (yet) assigned to a specific meeting, as in a session programme. The counterpart after the sitting are the items recorded in the protocol (Protocol.protocol_items).  |
| has_protocol | 0..1 <br/> [Protocol](#Protocol) | Reference to the protocol (minutes) of this meeting, recorded after the meeting. Only the identifier of the protocol is given; the protocol itself is delivered in the container's `protocols` list. It is an entity in its own right with its own identifier and is usually published later than the meeting, so it is referenced rather than embedded.  |
| joint_debates | * <br/> [JointDebate](#JointDebate) | Joint debates attached to this record: on an agenda item, the debates in which it is deliberated together with other agenda items; on a meeting or a session, the joint debates held within it.  |
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | meetings | range | [Meeting](#Meeting) |
| [Session](#Session) | meetings | range | [Meeting](#Meeting) |














#### Examples
##### Example Meeting: meeting item meeting be 2025 06 02

```yaml
meetings:
- global_uri: ops:meeting_be_2025_06_02
  date_begin_planned: '2025-06-02'
  agenda_items:
  - global_uri: ops:87b69a72919445a493a061d9b0daeba3
    agenda_item_type: item
    datetime_begin_planned: '2025-06-02T00:00:00Z'
    agenda_item_title:
    - text: Differenzierte Anpassung des Gehalts von Lehrpersonen ohne Lehrdiplom
      language: de
    affair_id: affairs:2025.GRPARL.81
    datetime_created: '2025-04-25T11:10:35Z'
    datetime_modified: '2025-04-25T11:10:35Z'

```
##### Example Meeting: Committee sitting with an attendance list

```yaml
meetings:
- global_uri: ops:meeting_be_committee_wak_2025_05_12
  spatial: https://ld.admin.ch/canton/2
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
  agenda_items:
  - global_uri: ops:agenda_item_be_2025_042
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
        Délibération sur les propositions de modification de l'article 5 de la loi
        fiscale
      language: fr
    agenda_item_category: Gesetzgebung
    state_id: completed
    datetime_begin_planned: '2025-05-12T15:00:00Z'
    datetime_begin_actual: '2025-05-12T15:15:00Z'
    affair_id: affairs:be_2024_089_steuergesetz
    datetime_created: '2025-04-15T09:00:00Z'
    datetime_modified: '2025-05-12T15:20:00Z'

```
##### Example Meeting: meeting item meeting schaffhausen 2025 03 31 b

```yaml
meetings:
- global_uri: ops:meeting_schaffhausen_2025_03_31_b
  date_begin_planned: '2025-03-31'
  agenda_items:
  - global_uri: ops:16155798_4
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 3
    agenda_item_number: '3'
    agenda_item_title:
    - text: >-
        Volksmotion Nr. 2024/1 von Sandro Mamedow und Livia Schraff (Erstunterzeichnende)
        sowie weitere 150 Mitunterzeichnende vom 22. März 2024 mit dem Titel: «Für
        eine Stimme der Studierenden im Hochschulrat der Pädagogischen Hochschule
        Schaffhausen (PHSH)»
      language: de
    agenda_item_category: Traktanden
    affair_id: affairs:MOT_2024_1
    datetime_created: '2025-05-02T11:23:49Z'
    datetime_modified: '2025-05-02T11:23:49Z'

```
##### Example Meeting: meeting item meeting vaud 2008 04 30

```yaml
meetings:
- global_uri: ops:meeting_vaud_2008_04_30
  date_begin_planned: '2008-04-30'
  agenda_items:
  - global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
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
        découlant des nouveaux règlements européens, afin d''éliminer des entraves
        au commerce et d''augmenter la sécurité d''évaluation des produits chimiques.

        '
      language: fr
    url:
    - text: >-
        https://www.vd.ch/actualites/decisions-du-conseil-detat/seance-du-conseil-detat/seance/265632#7b3545e4-57dc-3901-aaa8-4020da6ab0c6
      language: fr
    datetime_created: '2024-12-06T10:50:04Z'
    datetime_modified: '2024-12-06T10:50:04Z'

```
##### Example Meeting: Landsgemeinde as meeting type sitting

```yaml
meetings:
- global_uri: ops:meeting_gl_landsgemeinde_2025
  spatial: https://ld.admin.ch/canton/8
  name:
  - text: Landsgemeinde 2025
    language: de
  url:
  - text: https://www.landsgemeinde.gl.ch/2025
    language: de
  actor_id:
    global_uri: actors:landsgemeinde_gl
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
  parent_session: ops:session_gl_landsgemeinde_2025
  datetime_created: '2025-01-10T12:00:00Z'
  datetime_modified: '2025-05-04T13:45:00Z'

```
##### Example Meeting: meeting item meeting bern 2022 03 17

```yaml
meetings:
- global_uri: ops:meeting_bern_2022_03_17
  date_begin_planned: '2022-03-17'
  agenda_items:
  - global_uri: ops:cea750a5bd7b420fa4da1c914f801384
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
##### Example Meeting: Council of States sitting with protocol and speeches

```yaml
meetings:
- global_uri: parl:sr_winter25_sitzung_6
  spatial: https://ld.admin.ch/country/CHE
  name:
  - text: Sechste Sitzung
    language: de
  - text: Sixième séance
    language: fr
  url:
  - text: https://www.parlament.ch/de/ratsbetrieb/suche-Amtliches-bulletin
    language: de
  actor_id:
    global_uri: actors:staenderat
    label: Ständerat
    abbreviation:
    - value: SR
      language: de
  actor_name: Ständerat
  datetime_begin_planned: '2025-12-19T08:15:00+01:00'
  has_protocol: ops:protokoll_sr_winter25_sitzung_6
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'
  agenda_items:
  - global_uri: ops:69905
    agenda_item_type: item
    datetime_begin_planned: '2025-12-19T09:15:00+01:00'
    datetime_begin_actual: '2025-12-19T09:20:00+01:00'
    agenda_item_number: '6'
    agenda_item_position: 4
    agenda_item_title:
    - text: >-
        Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich
        durchführen, um die Verzögerungen zu verstehen
      language: de
    affair_id: affairs:24.4471
    landing_page: >-
      https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
    agenda_item_category: agenda_item
    datetime_created: '2026-01-12T00:00:00+01:00'
    datetime_modified: '2026-01-12T00:00:00+01:00'

```
##### Example Meeting: Government sitting with a bilingual designation

```yaml
meetings:
- spatial: https://ld.admin.ch/canton/2
  global_uri: ops:340dcf932fb044dd8f8c5c943267fbcc
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
##### Example Meeting: Cantonal parliament sitting with agenda items and votings

```yaml
meetings:
- global_uri: ops:meeting_sg_2025_03_15
  spatial: https://ld.admin.ch/canton/17
  name:
  - text: Kantonsratssitzung vom 15. März 2025
    language: de
  url:
  - text: https://www.ratsinfo.sg.ch/sessions/2025-03-15
    language: de
  actor_id:
    global_uri: actors:kr_sg
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
  parent_session: ops:session_sg_2025_03
  datetime_created: '2025-02-01T10:00:00Z'
  datetime_modified: '2025-03-15T17:30:00Z'
  agenda_items:
  - global_uri: ops:agenda_item_sg_2025_015
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
##### Example Meeting: meeting item meeting 2011 11 23

```yaml
meetings:
- global_uri: ops:meeting_2011_11_23
  date_begin_planned: '2011-11-23'
  agenda_items:
  - global_uri: ops:06fb582b753c416d8fdb05fa13873545
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
##### Example Meeting: meeting item meeting lausanne 2025 05 20

```yaml
meetings:
- global_uri: ops:meeting_lausanne_2025_05_20
  date_begin_planned: '2025-05-20'
  agenda_items:
  - global_uri: ops:2025_05_20-23
    agenda_item_type: item
    datetime_begin_planned: '2025-05-20T00:00:00Z'
    agenda_item_position: 23
    agenda_item_number: '23'
    agenda_item_title:
    - text: >-
        Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : « Interpellation
        urgente de Kulmiye Yusuf et crts – Solidarité sans frontières, Lausanne en
        faveur du respect du droit international et de la protection des populations
        civiles à Gaza »
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
##### Example Meeting: meeting item meeting 2025 03 31

```yaml
meetings:
- global_uri: ops:meeting_2025_03_31
  date_begin_planned: '2025-03-31'
  agenda_items:
  - global_uri: ops:49_253
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
##### Example Meeting: meeting item meeting schaffhausen 2025 03 31

```yaml
meetings:
- global_uri: ops:meeting_schaffhausen_2025_03_31
  date_begin_planned: '2025-03-31'
  agenda_items:
  - global_uri: ops:16155798_3
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
##### Example Meeting: meeting item meeting bern rr 2025 04 02

```yaml
meetings:
- global_uri: ops:meeting_bern_rr_2025_04_02
  date_begin_planned: '2025-04-02'
  agenda_items:
  - global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
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
##### Example Meeting: Half-day sitting within a session

```yaml
meetings:
- spatial: https://ld.admin.ch/canton/2
  global_uri: ops:e7c5d453-848a-430a-b024-1dd2f6873aa6
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
    global_uri: actors:gr_be
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
##### Example Meeting: meeting item meeting lausanne 2023 10 03

```yaml
meetings:
- global_uri: ops:meeting_lausanne_2023_10_03
  date_begin_planned: '2023-10-03'
  agenda_items:
  - global_uri: ops:2023_10_03-52
    agenda_item_type: item
    datetime_begin_planned: '2023-10-03T00:00:00Z'
    agenda_item_position: 52
    agenda_item_number: '52'
    agenda_item_title:
    - text: >-
        Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité commerciale
        » (FIM)
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
##### Example Meeting: meeting complete meeting zh 2025 11 20

```yaml
meetings:
- global_uri: ops:meeting_zh_2025_11_20
  date_begin_planned: '2025-11-20'
  agenda_items:
  - global_uri: ops:agenda_item_zh_budget_2026
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
##### Example Meeting: meeting item meeting luzern 2025 01 28

```yaml
meetings:
- global_uri: ops:meeting_luzern_2025_01_28
  date_begin_planned: '2025-01-28'
  agenda_items:
  - global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
    agenda_item_type: item
    datetime_begin_planned: '2025-01-28T00:00:00Z'
    agenda_item_position: 29
    agenda_item_number: '29'
    agenda_item_title:
    - text: >-
        Postulat Widmer Reichlin Gisela und Mit. über Massnahmen zur Erfüllung des
        Sonderschulkonkordats und zur gezielten Behebung des Fachkräftemangels im
        Bereich schulische Heilpädagogik / Bildungs- und Kulturdepartement
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
##### Example Meeting: meeting item meeting luzern 2025 01 28 b

```yaml
meetings:
- global_uri: ops:meeting_luzern_2025_01_28_b
  date_begin_planned: '2025-01-28'
  agenda_items:
  - global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
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






</div>

### Enum: StateEnum []{#StateEnum}




_State of the meeting._




<div data-search-exclude markdown="1">

URI: [ops:StateEnum](https://ch.paf.link/schema/operations/StateEnum)

#### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| planned |  The meeting is planned and will take place as scheduled.  |
| | [ops:enum/state/planned](ops:enum/state/planned) |
| canceled |  The meeting has been cancelled.  |
| | [ops:enum/state/canceled](ops:enum/state/canceled) |
| postponed |  The meeting has been postponed.  |
| | [ops:enum/state/postponed](ops:enum/state/postponed) |







</div>

\newpage

<!-- ToDo: Michel -->

# Agenda, protocol and decisions

The agenda of a sitting is structured by agenda items; what was actually dealt with and decided is recorded in the protocol.

## AgendaItem



### Class: AgendaItem []{#AgendaItem}


_An agenda item of a meeting as planned beforehand. It structures the agenda and connects the temporal organisation (Meeting) with the substantive affairs (eCH-0295). It is embedded in its meeting (Meeting.agenda_items) or directly in its session (Session.agenda_items). Agenda items represent the planning of a meeting and are no longer changed in the data once the meeting has started: deviations during the meeting — items brought forward, postponed or added — are recorded in the protocol (ProtocolItem) and feed into the agenda of the next meeting. For the same reason, planned and actual times are kept separately._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | Type of agenda item, distinguishing individual items from groups. <br/><br/>Inheritance: IsAgendaItem |
| agenda_item_number | 0..1 <br/> String | Number of the agenda item on the agenda, e.g. "2.1" or "3" (string type to also support roman numerals). <br/><br/>Inheritance: IsAgendaItem |
| agenda_item_position | 0..1 <br/> Integer | Integer position of the agenda item in the meeting sequence, used for sorting and display. <br/><br/>Inheritance: IsAgendaItem |
| leading_actor_id | 0..1 <br/> String | The leading department for the agenda item. <br/><br/>Inheritance: IsAgendaItem |
| speaking_actor_id | 0..1 <br/> String | The speaker or head of the department for the agenda item. <br/><br/>Inheritance: IsAgendaItem |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | Title of the agenda item. <br/><br/>Inheritance: IsAgendaItem |
| affair_id | 0..1 <br/> String | Identifier of the affair (eCH-0295) the record refers to. Administrative agenda items (e.g. approval of the minutes) have no affair. An affair usually runs through several agenda items — in legislation, for instance, the debate on entering into the matter, the detailed deliberation, the final vote and, where applicable, the procedure for resolving differences between the chambers. <br/><br/>Inheritance: IsAgendaItem |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | Subtitle or detailed description of the agenda item. <br/><br/>Inheritance: IsAgendaItem |
| state_id | 0..1 <br/> String | State identifier of the agenda item (reference to a state enumeration or a custom state), e.g. pending (not yet dealt with), in_progress, completed, postponed (to a later meeting) or withdrawn. <br/><br/>Inheritance: IsAgendaItem |
| state_name | 0..1 <br/> String | Diverging, free-text status designation, where the status enumeration does not suffice. <br/><br/>Inheritance: IsAgendaItem |
| landing_page | 0..1 <br/> String | URL providing further information. <br/><br/>Inheritance: IsAgendaItem |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing page or further web address, multilingual. <br/><br/>Inheritance: IsAgendaItem |
| agenda_item_category | 0..1 <br/> String | Free categorisation of the agenda item by content or grouping, e.g. "Gesetzgebung", "Budget und Finanzen", "Interpellationen und Anfragen", "Wahlen", by department, or introductory and technical items. The categorisation is not standardised and may vary between federal units. <br/><br/>Inheritance: IsAgendaItem |
| parent_agenda_item | 0..1 <br/> String | Identifier of the agenda item this record belongs to. On an agenda item it builds a hierarchy of agenda items — e.g. an item group "Gesetzesberatungen" with the sub-items "Energiegesetz (Detailberatung)" and "Energiegesetz (Schlussabstimmung)"; on a speech it names the agenda item under which the speech was given. <br/><br/>Inheritance: IsAgendaItem |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | The formal decision taken on this agenda item, e.g. the adoption of the energy law. The underlying voting with its vote ratio is recorded separately as a Voting. <br/><br/>Inheritance: IsAgendaItem |
| joint_debates | * <br/> [JointDebate](#JointDebate) | Joint debates attached to this record: on an agenda item, the debates in which it is deliberated together with other agenda items; on a meeting or a session, the joint debates held within it. <br/><br/>Inheritance: IsAgendaItem |
| text_segments | * <br/> [TextSegment](#TextSegment) | Collection of text segments (e.g. verbatim protocol). <br/><br/>Inheritance: IsAgendaItem |
| documents | * <br/> Work | Documents on the agenda item as FRBR Works, e.g. dispatches and reports, motions and amendments. <br/><br/>Inheritance: IsAgendaItem |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Session](#Session) | agenda_items | range | [AgendaItem](#AgendaItem) |
| [Meeting](#Meeting) | agenda_items | range | [AgendaItem](#AgendaItem) |














#### Examples
##### Example AgendaItem: French-language agenda item postulate

```yaml
agenda_items:
- global_uri: ops:2023_10_03-52
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
##### Example AgendaItem: Postulate with a voting

```yaml
agenda_items:
- global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
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
##### Example AgendaItem: session session gl landsgemeinde 2025 05 04 agenda item gl landsgemeinde 2025 01

```yaml
agenda_items:
- global_uri: ops:agenda_item_gl_landsgemeinde_2025_01
  agenda_item_type: item
  agenda_item_number: '1'
  agenda_item_position: 1
  agenda_item_title:
  - text: Eröffnung der Landsgemeinde
    language: de

```
##### Example AgendaItem: Popular motion within a group of agenda items

```yaml
agenda_items:
- global_uri: ops:16155798_4
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
##### Example AgendaItem: Substantive affair without an agenda category

```yaml
agenda_items:
- global_uri: ops:49_253
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
##### Example AgendaItem: Agenda item with a final vote

```yaml
agenda_items:
- global_uri: ops:agenda_item_sg_2025_015
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
##### Example AgendaItem: Petition as an agenda item

```yaml
agenda_items:
- global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
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
##### Example AgendaItem: Agenda item of a Council of States sitting

```yaml
agenda_items:
- global_uri: ops:69905
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
##### Example AgendaItem: Postulate category voting

```yaml
agenda_items:
- global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
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
##### Example AgendaItem: Interpellation as an agenda item

```yaml
agenda_items:
- global_uri: ops:06fb582b753c416d8fdb05fa13873545
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
##### Example AgendaItem: Urgent interpellation in French

```yaml
agenda_items:
- global_uri: ops:2025_05_20-23
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
##### Example AgendaItem: Motion within a group of agenda items

```yaml
agenda_items:
- global_uri: ops:16155798_3
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
##### Example AgendaItem: Budget agenda item

```yaml
agenda_items:
- global_uri: ops:agenda_item_zh_budget_2026
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
##### Example AgendaItem: Substantive affair from a cantonal parliamentary information system

```yaml
agenda_items:
- global_uri: ops:87b69a72919445a493a061d9b0daeba3
  agenda_item_type: item
  datetime_begin_planned: '2025-06-02T00:00:00Z'
  agenda_item_title:
  - text: Differenzierte Anpassung des Gehalts von Lehrpersonen ohne Lehrdiplom
    language: de
  affair_id: affairs:2025.GRPARL.81
  datetime_created: '2025-04-25T11:10:35Z'
  datetime_modified: '2025-04-25T11:10:35Z'

```
##### Example AgendaItem: Detailed deliberation of an article of an act

```yaml
agenda_items:
- global_uri: ops:agenda_item_be_2025_042
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
##### Example AgendaItem: Interpellation of a parliamentary group

```yaml
agenda_items:
- global_uri: ops:cea750a5bd7b420fa4da1c914f801384
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
##### Example AgendaItem: Partial revision of several ordinances in French

```yaml
agenda_items:
- global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
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






</div>

### Enum: AgendaItemTypeEnum []{#AgendaItemTypeEnum}




_Type of agenda item, distinguishing individual items from grouped items._




<div data-search-exclude markdown="1">

URI: [ops:AgendaItemTypeEnum](https://ch.paf.link/schema/operations/AgendaItemTypeEnum)

#### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| item |  Individual agenda item (Traktandum) with deliberation and, where applicable, a vote.  |
| | [ops:enum/agenda_item_type/item](ops:enum/agenda_item_type/item) |
| group |  Group of agenda items (Traktandengruppe) under which sub-items are arranged via parent_agenda_item, e.g. "Gesetzesberatungen".  |
| | [ops:enum/agenda_item_type/group](ops:enum/agenda_item_type/group) |







</div>

## Protocol

The protocol is **referenced, not embedded**. The rule this standard applies throughout therefore holds here as well — what has no identity of its own is embedded (`PersonReference` or `GroupReference`, say), what has one is referenced.

```
Container
  ├─ meetings       → Meeting
  │                     ├─ agenda_items → AgendaItem  (before: planned agenda items)
  │                     └─ has_protocol → identifier of the protocol
  └─ protocols      → Protocol    (after: the record, parent_meeting)
                        ├─ protocol_items  → ProtocolItem (same elements as AgendaItem)
                        ├─ votings
                        ├─ elections
                        ├─ speeches
                        ├─ text_segments
                        └─ documents
```



### Class: Protocol []{#Protocol}


_The minutes of a meeting, recorded after the meeting and kept exactly once per meeting. A wrapper container bundling the agenda items actually dealt with (protocol_items), votings, elections, speeches, verbatim text segments and linked documents. The protocol has its own identifier, can be cited on its own and is usually published later than the meeting; the meeting therefore only references it (Meeting.has_protocol), and the protocol itself is delivered in Container.protocols, so that it can be delivered later without delivering the meeting again. Within the protocol the collections are embedded, because they arise and are delivered together with it. Whoever publishes votings or speeches independently of the protocol delivers them flat in Container.votings or Container.speeches and links them via parent_meeting and the respective agenda item reference._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on a voting, election, speech, attendance list or protocol it names the meeting in which the record arose. Agenda items do not carry it: they are embedded in their meeting.  |
| protocol_items | * <br/> [ProtocolItem](#ProtocolItem) | Agenda items as actually recorded in the protocol.  |
| votings | * <br/> [Voting](#Voting) | Collection of voting records.  |
| elections | * <br/> [Election](#Election) | Collection of election records.  |
| speeches | * <br/> [Speech](#Speech) | Collection of speech records.  |
| text_segments | * <br/> [TextSegment](#TextSegment) | Collection of text segments (e.g. verbatim protocol).  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | protocols | range | [Protocol](#Protocol) |
| [Meeting](#Meeting) | has_protocol | range | [Protocol](#Protocol) |
| [Voting](#Voting) | parent_protocol | range | [Protocol](#Protocol) |
| [Election](#Election) | parent_protocol | range | [Protocol](#Protocol) |














#### Examples
##### Example Protocol: Protocol as an entity in its own right referenced by the meeting

```yaml
protocols:
- global_uri: ops:protokoll_sr_winter25_sitzung_6
  parent_meeting: parl:sr_winter25_sitzung_6
  protocol_items:
  - global_uri: ops:protokollpunkt_69905
    agenda_item_type: item
    agenda_item_number: '6'
    agenda_item_position: 4
    agenda_item_title:
    - text: >-
        Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich
        durchführen, um die Verzögerungen zu verstehen
      language: de
    affair_id: affairs:24.4471
    datetime_begin_actual: '2025-12-19T09:20:00+01:00'
    landing_page: >-
      https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
    agenda_item_category: agenda_item
    datetime_created: '2026-01-12T00:00:00+01:00'
    datetime_modified: '2026-01-12T00:00:00+01:00'
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'

```






</div>

### ProtocolItem (agenda item as recorded)



### Class: ProtocolItem []{#ProtocolItem}


_An agenda item as actually recorded in the protocol. It carries the same elements as AgendaItem through the IsAgendaItem mixin, but is a class in its own right: the record is not a special case of the plan. It arises independently and may contain items that were never put on the agenda, just as the agenda may contain items that were never dealt with._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | Type of agenda item, distinguishing individual items from groups. <br/><br/>Inheritance: IsAgendaItem |
| agenda_item_number | 0..1 <br/> String | Number of the agenda item on the agenda, e.g. "2.1" or "3" (string type to also support roman numerals). <br/><br/>Inheritance: IsAgendaItem |
| agenda_item_position | 0..1 <br/> Integer | Integer position of the agenda item in the meeting sequence, used for sorting and display. <br/><br/>Inheritance: IsAgendaItem |
| leading_actor_id | 0..1 <br/> String | The leading department for the agenda item. <br/><br/>Inheritance: IsAgendaItem |
| speaking_actor_id | 0..1 <br/> String | The speaker or head of the department for the agenda item. <br/><br/>Inheritance: IsAgendaItem |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | Title of the agenda item. <br/><br/>Inheritance: IsAgendaItem |
| affair_id | 0..1 <br/> String | Identifier of the affair (eCH-0295) the record refers to. Administrative agenda items (e.g. approval of the minutes) have no affair. An affair usually runs through several agenda items — in legislation, for instance, the debate on entering into the matter, the detailed deliberation, the final vote and, where applicable, the procedure for resolving differences between the chambers. <br/><br/>Inheritance: IsAgendaItem |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | Subtitle or detailed description of the agenda item. <br/><br/>Inheritance: IsAgendaItem |
| state_id | 0..1 <br/> String | State identifier of the agenda item (reference to a state enumeration or a custom state), e.g. pending (not yet dealt with), in_progress, completed, postponed (to a later meeting) or withdrawn. <br/><br/>Inheritance: IsAgendaItem |
| state_name | 0..1 <br/> String | Diverging, free-text status designation, where the status enumeration does not suffice. <br/><br/>Inheritance: IsAgendaItem |
| landing_page | 0..1 <br/> String | URL providing further information. <br/><br/>Inheritance: IsAgendaItem |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing page or further web address, multilingual. <br/><br/>Inheritance: IsAgendaItem |
| agenda_item_category | 0..1 <br/> String | Free categorisation of the agenda item by content or grouping, e.g. "Gesetzgebung", "Budget und Finanzen", "Interpellationen und Anfragen", "Wahlen", by department, or introductory and technical items. The categorisation is not standardised and may vary between federal units. <br/><br/>Inheritance: IsAgendaItem |
| parent_agenda_item | 0..1 <br/> String | Identifier of the agenda item this record belongs to. On an agenda item it builds a hierarchy of agenda items — e.g. an item group "Gesetzesberatungen" with the sub-items "Energiegesetz (Detailberatung)" and "Energiegesetz (Schlussabstimmung)"; on a speech it names the agenda item under which the speech was given. <br/><br/>Inheritance: IsAgendaItem |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | The formal decision taken on this agenda item, e.g. the adoption of the energy law. The underlying voting with its vote ratio is recorded separately as a Voting. <br/><br/>Inheritance: IsAgendaItem |
| joint_debates | * <br/> [JointDebate](#JointDebate) | Joint debates attached to this record: on an agenda item, the debates in which it is deliberated together with other agenda items; on a meeting or a session, the joint debates held within it. <br/><br/>Inheritance: IsAgendaItem |
| text_segments | * <br/> [TextSegment](#TextSegment) | Collection of text segments (e.g. verbatim protocol). <br/><br/>Inheritance: IsAgendaItem |
| documents | * <br/> Work | Documents on the agenda item as FRBR Works, e.g. dispatches and reports, motions and amendments. <br/><br/>Inheritance: IsAgendaItem |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Protocol](#Protocol) | protocol_items | range | [ProtocolItem](#ProtocolItem) |
| [Voting](#Voting) | parent_protocol_item | range | [ProtocolItem](#ProtocolItem) |
| [Election](#Election) | parent_protocol_item | range | [ProtocolItem](#ProtocolItem) |



















</div>

## Joint debate (JointDebate)



### Class: JointDebate []{#JointDebate}


_A joint debate: several agenda items are deliberated together, for instance substantively related affairs dealt with in a single debate. The joint debate hangs on an agenda item (AgendaItem), a protocol item (ProtocolItem), a meeting (Meeting) or a session (Session) and references the items debated jointly by their identifiers. Attached to a meeting or a session, it can also bring together agenda items that are distributed over several agenda positions or meetings._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| joint_agenda_item_ids | * <br/> String | Identifiers of the agenda items (AgendaItem or ProtocolItem) debated jointly.  |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Session](#Session) | joint_debates | range | [JointDebate](#JointDebate) |
| [Meeting](#Meeting) | joint_debates | range | [JointDebate](#JointDebate) |
| IsAgendaItem | joint_debates | range | [JointDebate](#JointDebate) |
| [AgendaItem](#AgendaItem) | joint_debates | range | [JointDebate](#JointDebate) |
| [ProtocolItem](#ProtocolItem) | joint_debates | range | [JointDebate](#JointDebate) |



















</div>

## Resolution



### Class: Resolution []{#Resolution}


_The formal decision taken on an agenda item, including the voting procedures applied. It records what was decided, whereas Voting records how it was decided (procedure and vote ratio). Not every decision rests on a formal vote: noting a report, tacit acceptance or administrative decisions come about without one._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](#ResolutionTypeEnum) | Type of resolution taken on the agenda item.  |
| type_label | 0..1 <br/> String | Custom type label when standard type values don't apply.  |
| vote_procedures | * <br/> String | Procedures by which the vote was taken. Open procedures: show of hands, standing, electronic voting, roll call, and in crisis situations remote voting (votes communicated to the presidency beforehand and recorded together with the vote in the chamber), circulation procedure or voting in virtual sittings. Secret procedures: secret ballot with ballot papers, electronic secret voting. The procedure determines whether individual votes can be recorded.  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | resolutions | range | [Resolution](#Resolution) |
| IsAgendaItem | has_resolution | range | [Resolution](#Resolution) |
| [AgendaItem](#AgendaItem) | has_resolution | range | [Resolution](#Resolution) |
| [ProtocolItem](#ProtocolItem) | has_resolution | range | [Resolution](#Resolution) |



















</div>

### Enum: ResolutionTypeEnum []{#ResolutionTypeEnum}




_Type of resolution taken on an agenda item._




<div data-search-exclude markdown="1">

URI: [ops:ResolutionTypeEnum](https://ch.paf.link/schema/operations/ResolutionTypeEnum)

#### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| accepted |  Accepted (Annahme): e.g. a bill adopted, a motion approved, a decision taken.  |
| | [ops:enum/resolution_type/accepted](ops:enum/resolution_type/accepted) |
| rejected |  Rejected (Ablehnung): e.g. a bill rejected, a motion dismissed.  |
| | [ops:enum/resolution_type/rejected](ops:enum/resolution_type/rejected) |
| noted |  Noted (Kenntnisnahme): e.g. reports without a vote, communications, informative agenda items.  |
| | [ops:enum/resolution_type/noted](ops:enum/resolution_type/noted) |
| accepted_point_by_point |  Accepted point by point (Punktweise Annahme)  |
| | [ops:enum/resolution_type/accepted_point_by_point](ops:enum/resolution_type/accepted_point_by_point) |
| accepted_with_postulate |  Accepted with postulate (Annahme mit Postulat)  |
| | [ops:enum/resolution_type/accepted_with_postulate](ops:enum/resolution_type/accepted_with_postulate) |
| orally_settled |  Orally settled (Mündlich erledigt)  |
| | [ops:enum/resolution_type/orally_settled](ops:enum/resolution_type/orally_settled) |
| nearly_unanimous |  Nearly unanimous (Beinahe einstimmig)  |
| | [ops:enum/resolution_type/nearly_unanimous](ops:enum/resolution_type/nearly_unanimous) |
| other |  Other resolution type not covered by standard categories  |
| | [ops:enum/resolution_type/other](ops:enum/resolution_type/other) |







</div>

## Motion



### Class: Motion []{#Motion}


_A formal proposal submitted during the proceedings, such as an amendment to a legal text, a procedural motion (e.g. closure of the debate) or a motion to refer back. It is an entity in its own right because an agenda item may contain several motions, each with its own course (submitted, supported, voted on) and possibly a vote of its own._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| title | 0..1 <br/> String | Short title of the motion.  |
| description | 0..1 <br/> String | Full text of the motion.  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |






















</div>

\newpage

<!-- ToDo: Nicole -->

# Votings and elections

Parliamentary decisions are taken either by votings on substantive questions or by elections of persons. The standard clearly distinguishes these two mechanisms and additionally records, in open procedures, the individual voting behaviour of every member of parliament.

## Voting



### Class: Voting []{#Voting}


_A voting on a substantive question: the subject (question), the procedure, the result with its vote ratio and — for open votings — the individual votes of the members. A voting is held in the course of the sitting and is therefore anchored in the protocol (parent_protocol, parent_protocol_item); it is also linked to the meeting (parent_meeting) and to the affair (affair_id). The presiding member does not take part in votings but casts the deciding vote in case of a tie (tie_breaker). The categorical decision (accepted, rejected, noted …) is not held on the voting but in the Resolution of the agenda item._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| datetime_begin | 0..1 <br/> Datetime | The date and time when the meeting or voting begins.  |
| datetime_end | 0..1 <br/> Datetime | The date and time when the meeting or voting ends.  |
| voting_type | 0..1 <br/> [VotingTypeEnum](#VotingTypeEnum) | Type of voting procedure (preliminary, final, secret, etc.).  |
| type_label | 0..1 <br/> String | Custom type label when standard type values don't apply.  |
| voting_title | * <br/> [MultilingualString](#MultilingualString) | Title or question being voted on. If no specific subject exists, do not use the business item title.  |
| optional | 0..1 <br/> Boolean | Indicates if the meeting or voting is optional.  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| label_yes | 0..1 <br/> String | Meaning of a 'yes' vote.  |
| label_no | 0..1 <br/> String | Meaning of a 'no' vote.  |
| label_abstention | 0..1 <br/> String | Meaning of an 'abstention' vote.  |
| tie_breaker | 0..1 <br/> Boolean | Indicates whether the result was decided by the casting vote of the presiding member in case of a tie.  |
| total_count_yes | 0..1 <br/> Integer | Total number of 'yes' votes.  |
| total_count_no | 0..1 <br/> Integer | Total number of 'no' votes.  |
| total_count_abstention | 0..1 <br/> Integer | Total number of abstentions.  |
| total_other | * <br/> [TotalOther](#TotalOther) | Vote counts for the options of a multiple-choice voting, one entry per option; used instead of total_count_yes, total_count_no and total_count_abstention (see TotalOther).  |
| total_absent | 0..1 <br/> Integer | Number of absent members who could not take part. Whether an absence was excused is tracked on the attendance list (Attendance).  |
| total | 0..1 <br/> Integer | Total number of votes, excluding absent and president's vote.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | Type of majority required for the vote (absolute, two-thirds, etc.).  |
| majority_count | 0..1 <br/> Integer | Number of votes required for the relevant majority threshold.  |
| result_text | 0..1 <br/> String | Free text describing the outcome, e.g. "Accepted with 120 to 75 votes with 5 abstentions". For votings, the categorical decision (accepted, rejected, noted …) is not recorded here but in the Resolution (resolution_type) of the agenda item.  |
| parent_meeting | 0..1 <br/> String | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on a voting, election, speech, attendance list or protocol it names the meeting in which the record arose. Agenda items do not carry it: they are embedded in their meeting.  |
| parent_protocol | 0..1 <br/> [Protocol](#Protocol) | The protocol in which the voting or election is recorded. A vote is held during the sitting and is therefore anchored in the minutes, not in the agenda planned beforehand: what was put on the agenda does not yet say what was actually voted on. Conversely, the protocol lists its votings and elections (votings, elections).  |
| parent_protocol_item | 0..1 <br/> [ProtocolItem](#ProtocolItem) | The recorded agenda item (ProtocolItem) under which the voting or election took place. Omitted when the vote was taken without an agenda item; the link to the sitting is then given by parent_protocol and parent_meeting alone.  |
| affair_id | 0..1 <br/> String | Identifier of the affair (eCH-0295) the record refers to. Administrative agenda items (e.g. approval of the minutes) have no affair. An affair usually runs through several agenda items — in legislation, for instance, the debate on entering into the matter, the detailed deliberation, the final vote and, where applicable, the procedure for resolving differences between the chambers.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | votings | range | [Voting](#Voting) |
| [Protocol](#Protocol) | votings | range | [Voting](#Voting) |
| [IndividualVote](#IndividualVote) | parent_voting | range | [Voting](#Voting) |














#### Examples
##### Example Voting: Final vote on the budget

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
  parent_protocol: ops:protocol_zh_2025_11_20
  parent_protocol_item: ops:protocol_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  actor_id:
    global_uri: actors:kr_zh
    label: Kantonsrat Zürich
    abbreviation:
    - value: KR
      language: de
  datetime_created: '2025-11-20T16:45:00Z'
  datetime_modified: '2025-11-20T16:50:00Z'

```
##### Example Voting: Motions in the same direction with multiple choice

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
  parent_protocol: ops:protocol_zh_gr_2024_02_28
  parent_protocol_item: ops:protocol_item_zh_gr_2024_2023_361
  parent_meeting: ops:meeting_zh_gr_2024_02_28
  affair_id: 2023/361
  actor_id:
    global_uri: actors:gr_stadt_zuerich
    label: Gemeinderat der Stadt Zürich
    abbreviation:
    - value: GR
      language: de
  datetime_created: '2024-02-28T00:00:00Z'
  datetime_modified: '2024-02-28T00:00:00Z'

```
##### Example Voting: Final vote with individual votes

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
  parent_protocol: ops:protocol_sg_2025_03_15
  parent_protocol_item: ops:protocol_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  actor_id:
    global_uri: actors:kr_sg
    label: Kantonsrat St. Gallen
    abbreviation:
    - value: KR
      language: de
  datetime_created: '2025-03-15T14:30:00Z'
  datetime_modified: '2025-03-15T14:35:00Z'

```
##### Example Voting: Intermediate voting on an amendment

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
  parent_protocol: ops:protocol_be_2025_06_05
  parent_protocol_item: ops:protocol_item_be_2025_042
  parent_meeting: ops:meeting_be_2025_06_05
  actor_id:
    global_uri: actors:gr_be
    label: Grosser Rat Bern
    abbreviation:
    - value: GR
      language: de
  datetime_created: '2025-06-05T10:15:00Z'
  datetime_modified: '2025-06-05T10:15:00Z'

```






</div>

### Enum: VotingTypeEnum []{#VotingTypeEnum}




_Type of voting procedure._




<div data-search-exclude markdown="1">

URI: [ops:VotingTypeEnum](https://ch.paf.link/schema/operations/VotingTypeEnum)

#### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| preliminary_vote |  Preliminary vote (Zwischenabstimmung) during the deliberation, e.g. on entering into an affair, on a motion, opposing two motions that exclude each other or refer to the same passage, a contingent vote (Eventualabstimmung) when more than two motions exist on one subject, on a single article of a law, or the overall vote after the first reading of an act deliberated in two readings.  |
| | [ops:enum/voting_type/preliminary_vote](ops:enum/voting_type/preliminary_vote) |
| final_vote |  Final vote (Schlussabstimmung) on the proposal as a whole, e.g. after the last reading of an act, the overall vote on a decree, the adoption or rejection of a proposal in its entirety, or the point-by-point vote on a parliamentary proposal.  |
| | [ops:enum/voting_type/final_vote](ops:enum/voting_type/final_vote) |
| tie_breaker_president |  Casting vote of the presiding member in case of a tie (Stichentscheid Präsidium). The presiding member does not take part in votings but decides in case of a tie. In a secret vote ending in a tie, the proposal of the preparatory body is deemed accepted instead.  |
| | [ops:enum/voting_type/tie_breaker_president](ops:enum/voting_type/tie_breaker_president) |
| secret_vote |  Secret ballot (Geheime Abstimmung), e.g. on particularly sensitive matters such as a request for pardon or the lifting of immunity, after a secret deliberation, or on request. Only the overall result is published.  |
| | [ops:enum/voting_type/secret_vote](ops:enum/voting_type/secret_vote) |
| other |  Other voting type, specified in type_label — e.g. a multiple-choice voting on several proposals pointing in the same direction (see TotalOther).  |
| | [ops:enum/voting_type/other](ops:enum/voting_type/other) |







</div>

### Enum: MajorityTypeEnum []{#MajorityTypeEnum}




_Type of majority required for the vote._




<div data-search-exclude markdown="1">

URI: [ops:MajorityTypeEnum](https://ch.paf.link/schema/operations/MajorityTypeEnum)

#### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| absolute |  Absolute majority: more than half of the reference base (members or votes cast, depending on the applicable rules), e.g. at least 101 of 200. Standard case for elections of persons such as the election of the Federal Council or of committee chairs, and required for constitutional amendments in some cantons. If nobody reaches it in the first ballot of an election, a second ballot usually follows in which the relative majority suffices.  |
| | [ops:enum/majority_type/absolute](ops:enum/majority_type/absolute) |
| two_thirds |  Two-thirds majority, e.g. at least 134 of 200; required in some cantons for constitutional amendments.  |
| | [ops:enum/majority_type/two_thirds](ops:enum/majority_type/two_thirds) |
| other |  Other majority threshold not covered by the standard categories, e.g. the relative majority among several options in a multiple-choice voting.  |
| | [ops:enum/majority_type/other](ops:enum/majority_type/other) |







</div>



### Class: TotalOther []{#TotalOther}


_Vote count for one option of a multiple-choice voting. If several proposals pointing in the same direction are put to the vote at the same time, the members vote on more than two variants and the variant with most votes prevails (in Zurich colloquially a „Cup-Abstimmung“, cast via several voting buttons). Such a voting is represented with voting_type other and a descriptive type_label; total_count_yes, total_count_no and total_count_abstention remain empty, and each option receives an entry with count and label. Example: Gemeinderat of the City of Zurich, sitting of 28 February 2024, affair 2023/361, four options with 75, 25, 12 and 0 votes._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| count | 0..1 <br/> Integer | The count of votes for the total other category.  |
| label | 0..1 <br/> String | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Voting](#Voting) | total_other | range | [TotalOther](#TotalOther) |



















</div>

## Individual Vote



### Class: IndividualVote []{#IndividualVote}


_The vote cast by an individual member in a voting. Individual votes are only recorded for open votings; for secret votings only the overall result is published. An individual vote concerns one specific voting and differs from attendance (Attendance), which records presence at the meeting as a whole: a member present at the meeting may be recorded as not_voted in a single voting, for instance because they briefly left the room._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_voting | 0..1 <br/> [Voting](#Voting) | The ID of the voting associated with the individual vote.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | The member who cast the vote, as a reference to a person according to eCH-0294.  |
| seat_nr | 0..1 <br/> String | The seat number of the individual vote, if applicable.  |
| weight | 0..1 <br/> Integer | Voting weight of the member; normally 1. Other values arise, for instance, where a member also votes for an absent member (proxy, weight 2), in communal assemblies where legal entities hold several votes, or in historical systems in which different groups of persons had different voting weights.  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](#IndividualVoteTypeEnum) | Type of vote cast (yes, no, abstention, no vote, etc.).  |
| type_label | 0..1 <br/> String | Custom type label when standard type values don't apply.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | individual_votes | range | [IndividualVote](#IndividualVote) |














#### Examples
##### Example IndividualVote: No vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_456
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: actors:person_andreas_eggenberger
    label: Andreas Eggenberger
  seat_nr: '2'
  individual_vote_type: 'no'
  datetime_created: '2025-03-15T14:30:00Z'

```
##### Example IndividualVote: No vote on the budget

```yaml
individual_votes:
- global_uri: ops:vote_zh_budget_2026_person_102
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: actors:person_jean_daniel_strub
    label: Jean-Daniel Strub
  seat_nr: '2'
  individual_vote_type: 'no'
  datetime_created: '2025-11-20T16:45:00Z'

```
##### Example IndividualVote: Abstention

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_789
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: actors:person_thomas_ammann
    label: Thomas Ammann
  seat_nr: '3'
  individual_vote_type: abstention
  datetime_created: '2025-03-15T14:30:00Z'

```
##### Example IndividualVote: Yes vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_123
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: actors:person_paul_schlegel
    label: Paul Schlegel
  seat_nr: '1'
  individual_vote_type: 'yes'
  datetime_created: '2025-03-15T14:30:00Z'

```
##### Example IndividualVote: Individual vote for selection option B

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_b1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: actors:person_zh_stadt_2
    label: Mitglied Auswahl B
  seat_nr: '47'
  individual_vote_type: other
  type_label: Auswahl B
  datetime_created: '2024-02-28T00:00:00Z'

```
##### Example IndividualVote: Individual vote for selection option C

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_c1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: actors:person_zh_stadt_3
    label: Mitglied Auswahl C
  seat_nr: '88'
  individual_vote_type: other
  type_label: Auswahl C
  datetime_created: '2024-02-28T00:00:00Z'

```
##### Example IndividualVote: Did not vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_321
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: actors:person_ruedi_thomann
    label: Ruedi Thomann
  seat_nr: '4'
  individual_vote_type: not_voted
  datetime_created: '2025-03-15T14:30:00Z'

```
##### Example IndividualVote: Yes vote on the budget

```yaml
individual_votes:
- global_uri: ops:vote_zh_budget_2026_person_101
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: actors:person_thomas_wolf
    label: Thomas Wolf
  seat_nr: '1'
  individual_vote_type: 'yes'
  datetime_created: '2025-11-20T16:45:00Z'

```
##### Example IndividualVote: Individual vote for selection option A

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_a1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: actors:person_zh_stadt_1
    label: Mitglied Auswahl A
  seat_nr: '12'
  individual_vote_type: other
  type_label: Auswahl A
  datetime_created: '2024-02-28T00:00:00Z'

```
##### Example IndividualVote: Absent in a multiple-choice voting

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_abs1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: actors:person_zh_stadt_4
    label: Abwesendes Mitglied
  seat_nr: '103'
  individual_vote_type: not_voted
  datetime_created: '2024-02-28T00:00:00Z'

```






</div>

### Enum: IndividualVoteTypeEnum []{#IndividualVoteTypeEnum}




_Type of individual vote cast by a member._




<div data-search-exclude markdown="1">

URI: [ops:IndividualVoteTypeEnum](https://ch.paf.link/schema/operations/IndividualVoteTypeEnum)

#### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| yes |  Yes vote: the member approves the proposal or motion.  |
| | [ops:enum/individual_vote_type/yes](ops:enum/individual_vote_type/yes) |
| no |  No vote: the member rejects the proposal or motion.  |
| | [ops:enum/individual_vote_type/no](ops:enum/individual_vote_type/no) |
| abstention |  Abstention: the member takes part in the voting but abstains; with electronic voting, by pressing the "abstention" button.  |
| | [ops:enum/individual_vote_type/abstention](ops:enum/individual_vote_type/abstention) |
| not_voted |  Not voted: the member did not cast a vote, for instance because they were present but did not vote or were absent.  |
| | [ops:enum/individual_vote_type/not_voted](ops:enum/individual_vote_type/not_voted) |
| tie_breaker |  Tie-breaking vote, cast by the presiding member in case of a tie (see voting_type tie_breaker_president).  |
| | [ops:enum/individual_vote_type/tie_breaker](ops:enum/individual_vote_type/tie_breaker) |
| other |  Vote that cannot be placed on the yes/no axis — for instance in a multiple-choice voting, where the member voted but neither yes nor no; the chosen option is held in type_label (e.g. "Auswahl A"). Counterpart of total_other on the voting, which keeps the individual vote evaluable without a separate enumeration value for every cantonal selection mechanism.  |
| | [ops:enum/individual_vote_type/other](ops:enum/individual_vote_type/other) |







</div>

## Election



### Class: Election []{#Election}


_An election in which a parliamentary body appoints one or several persons to an office or function. Unlike a voting (Voting), which decides substantive questions, an election is a decision on persons: it is often held by secret ballot and usually requires an absolute majority, whereas votings are mostly open. The presiding member, who does not take part in votings, does vote in elections. Each ballot is recorded as a separate election; the ballots of one election are linked through the common agenda item — for instance a first ballot requiring an absolute majority that remains without result, followed by a second ballot in which the relative majority suffices._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| datetime_begin | 0..1 <br/> Datetime | The date and time when the meeting or voting begins.  |
| datetime_end | 0..1 <br/> Datetime | The date and time when the meeting or voting ends.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](#ElectionTypeEnum) | Type of election procedure.  |
| type_label | 0..1 <br/> String | Custom type label when standard type values don't apply.  |
| title | 0..1 <br/> String | Title of the election, e.g. "Wahl Kommissionspräsidium WAK".  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| total_absent | 0..1 <br/> Integer | Number of absent members who could not take part. Whether an absence was excused is tracked on the attendance list (Attendance).  |
| total | 0..1 <br/> Integer | Total number of votes, excluding absent and president's vote.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | Type of majority required for the vote (absolute, two-thirds, etc.).  |
| majority_count | 0..1 <br/> Integer | Number of votes required for the relevant majority threshold.  |
| result_text | 0..1 <br/> String | Free text describing the outcome, e.g. "Accepted with 120 to 75 votes with 5 abstentions". For votings, the categorical decision (accepted, rejected, noted …) is not recorded here but in the Resolution (resolution_type) of the agenda item.  |
| parent_meeting | 0..1 <br/> String | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on a voting, election, speech, attendance list or protocol it names the meeting in which the record arose. Agenda items do not carry it: they are embedded in their meeting.  |
| parent_protocol | 0..1 <br/> [Protocol](#Protocol) | The protocol in which the voting or election is recorded. A vote is held during the sitting and is therefore anchored in the minutes, not in the agenda planned beforehand: what was put on the agenda does not yet say what was actually voted on. Conversely, the protocol lists its votings and elections (votings, elections).  |
| parent_protocol_item | 0..1 <br/> [ProtocolItem](#ProtocolItem) | The recorded agenda item (ProtocolItem) under which the voting or election took place. Omitted when the vote was taken without an agenda item; the link to the sitting is then given by parent_protocol and parent_meeting alone.  |
| affair_id | 0..1 <br/> String | Identifier of the affair (eCH-0295) the record refers to. Administrative agenda items (e.g. approval of the minutes) have no affair. An affair usually runs through several agenda items — in legislation, for instance, the debate on entering into the matter, the detailed deliberation, the final vote and, where applicable, the procedure for resolving differences between the chambers.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | elections | range | [Election](#Election) |
| [Protocol](#Protocol) | elections | range | [Election](#Election) |



















</div>

### Enum: ElectionTypeEnum []{#ElectionTypeEnum}




_Type of election procedure._




<div data-search-exclude markdown="1">

URI: [ops:ElectionTypeEnum](https://ch.paf.link/schema/operations/ElectionTypeEnum)

#### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| secret |  Secret election (Geheime Wahl): votes are cast anonymously, by ballot paper or an electronic secret system, so it cannot be traced who elected whom. Standard for elections of persons and often required by law — at federal level e.g. the Federal Council (elected by the United Federal Assembly with an absolute majority in the first ballots), federal judges and committee chairs; at cantonal level e.g. the president of parliament, the president of the government, the presidents of the highest courts, judges, the state chancellor and committee chairs. Only the overall result is published, no individual votes.  |
| | [ops:enum/election_type/secret](ops:enum/election_type/secret) |
| open |  Open election (Offene Wahl): votes are cast openly and it is traceable who elected whom, so individual votes can be recorded. Used where transparency is desired, for uncontested elections or in smaller bodies.  |
| | [ops:enum/election_type/open](ops:enum/election_type/open) |
| silent |  Silent election (Stille Wahl) without formal vote, by acclamation or consensus; possible only when no objection is raised, e.g. the re-election of a committee chair without a rival candidate.  |
| | [ops:enum/election_type/silent](ops:enum/election_type/silent) |







</div>

\newpage

# Attendance

Attendance lists record who took part in a sitting. They document participation and are the basis on which a body's capacity to take decisions can be assessed.

## Attendance

### Term and meaning

Attendance records which members of a parliamentary body were present, absent or excused at a sitting. It serves to document participation and is a prerequisite for the quorum.

### Two-level structure

The standard distinguishes two levels of attendance recording:

#### 1. Attendance (aggregated level)
Summary of attendance for a meeting:
- Total number of persons present
- Total number of persons absent (excused / unexcused)
- Quorum

#### 2. IndividualAttendance (individual level)
Detailed recording for each individual person:
- Who was present?
- Who was absent?
- Was the absence excused?

```
Meeting (National Council sitting 4 March 2024)
  └─ Attendance (aggregated attendance)
      ├─ IndividualAttendance (person A: present)
      ├─ IndividualAttendance (person B: excused)
      ├─ IndividualAttendance (person C: absent)
      └─ ...
```

## Attendance (aggregated level)

#### Assignment to meeting and body

- **parent_meeting**: reference to the specific sitting to which the attendance list belongs
- **actor_id**: reference to the body (parliament, committee) according to eCH-0294 Actors
- **datetime_begin**: point in time of the attendance recording

#### Aggregated figures

- **total_count**: total number of all members of the body (reference value for quorum calculations, e.g. 200 for the National Council, 46 for the Council of States)
- **total_present**: number of members present
- **total_excused**: number of excused members
- **total_absent**: number of unexcused absent members

**Example:**
- Total: 200
- Present: 185
- Excused: 12
- Absent: 3

#### Quorum

The quorum results from the ratio of `total_present` to `total_count` and the respective quorum rules of the body. It is therefore not stored as a separate field but calculated from the data where needed.

## IndividualAttendance (individual level)

#### Link

- **parent_attendance**: reference to the superordinate `Attendance` aggregate (which in turn hangs on the meeting). The individual record is thereby cleanly assigned to the meeting.
- **actor_id**: reference to the person according to eCH-0294 Actors

#### Attendance type

The field **attendance_type** (enum `AttendanceTypeEnum`) records the type of attendance:

- **present**: present in person
- **remote**: present via remote access (e.g. video conference)
- **substitute**: substitution — another person participated as a stand-in

> The modelling of substitution (e.g. who substituted for whom, with which voting right) is being elaborated further in [issue #24](https://github.com/swiss/political-affairs-ech-group/issues/24).
>
> A second status axis `present` / `excused` / `absent` ("whether present") in parallel to the existing axis "how present" is under discussion as an extension.

#### Reason

The field **reason** (multilingual) can record the reason for absence, lateness or substitution as free text.

### Difference: Attendance vs. IndividualVote

Important delimitation:

| Aspect | Attendance | IndividualVote |
|--------|------------|----------------|
| Records | Presence at the sitting | Vote cast in a voting |
| Point in time | Start of / during the sitting | Point in time of the voting |
| Granularity | Per meeting | Per voting |

**Example:** a person can be present at the sitting (Attendance: present) but be recorded as absent for a specific voting (IndividualVote: absent) because they briefly left the room at that moment.

### Purposes of use

The attendance entities enable:

1. **Documentation**: traceable recording of participation
2. **Quorum check**: ensuring the capacity to take decisions
3. **Transparency**: public information about attendance
4. **Accountability**: monitoring the fulfilment of duties
5. **Statistics**: evaluation of attendance rates
6. **Administration**: calculation of compensation and expenses



### Class: Attendance []{#Attendance}


_Aggregated attendance record for a meeting (number of members present, absent, excused)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on a voting, election, speech, attendance list or protocol it names the meeting in which the record arose. Agenda items do not carry it: they are embedded in their meeting.  |
| datetime_begin | 0..1 <br/> Datetime | The date and time when the meeting or voting begins.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| total_count | 0..1 <br/> Integer | Total number of members of the body (reference value for quorum calculations).  |
| total_present | 0..1 <br/> Integer | Total number of members present.  |
| total_absent | 0..1 <br/> Integer | Number of absent members who could not take part. Whether an absence was excused is tracked on the attendance list (Attendance).  |
| total_excused | 0..1 <br/> Integer | Total number of excused absences.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | attendances | range | [Attendance](#Attendance) |
| [IndividualAttendance](#IndividualAttendance) | parent_attendance | range | [Attendance](#Attendance) |



















</div>



### Class: IndividualAttendance []{#IndividualAttendance}


_Individual attendance record for a specific person at a meeting (linked via the parent Attendance aggregate)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_attendance | 0..1 <br/> [Attendance](#Attendance) | The Attendance aggregate this individual attendance record belongs to.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Reference to the acting person (lightweight snapshot at time of linking).  |
| attendance_type | 0..1 <br/> [AttendanceTypeEnum](#AttendanceTypeEnum) | Type of individual attendance.  |
| reason | * <br/> [MultilingualString](#MultilingualString) | Reason for absence, lateness or substitution (free-text, multilingual).  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | individual_attendances | range | [IndividualAttendance](#IndividualAttendance) |



















</div>

### Enum: AttendanceTypeEnum []{#AttendanceTypeEnum}




_Type of individual attendance._




<div data-search-exclude markdown="1">

URI: [ops:AttendanceTypeEnum](https://ch.paf.link/schema/operations/AttendanceTypeEnum)

#### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| remote |  Remote participation  |
| | [ops:enum/attendance_type/remote](ops:enum/attendance_type/remote) |
| substitute |  Substitute (Stellvertretung)  |
| | [ops:enum/attendance_type/substitute](ops:enum/attendance_type/substitute) |
| present |  Present in person  |
| | [ops:enum/attendance_type/present](ops:enum/attendance_type/present) |







</div>

\newpage

<!-- ToDo: David -->

<!--
Debate

* -> video recording -> speech transcript
*   -> verbatim protocol -> text to timestamp -> text contains the timestamps -> text document (with or without a definition of the format (span types))
*   -> edited protocol -> agenda item to timestamp
-->

# Speeches

Speeches record the parliamentary debate — who spoke when and on which agenda item, with the verbatim text and, where available, an audio or video recording.

## Speech

### Term and meaning

A speech denotes an oral contribution by a person during a parliamentary sitting. It is the central instrument of political debate and of expressing opinions in parliament.

### Types of speeches

Parliamentary speeches take various forms:

#### Main statements
- Detailed positions on an affair
- Justification of motions
- Presentation of the group's opinion

#### Short interventions
- Brief statements
- Interposed questions
- Corrections

#### Group declarations
- Official position of a parliamentary group
- Delivered by the group's spokesperson

#### Government statements
- Positions of government members
- Answering of questions
- Defence of bills

### Structure and assignment

A speech is always assigned to a specific context:

```
Meeting (sitting)
  └─ AgendaItem
      └─ Speech (statement of person A)
          ├─ TextSegment (transcription)
          ├─ Media (audio recording)
          └─ Media (video recording)
```

#### Assignment fields

- **meeting_id**: the sitting in which the speech was made
- **agenda_item_id**: the agenda item that was spoken to
- **person_id**: the speaking person (according to eCH-0294 Actors)

### Identification of the speakers

- **person_id**: unique identification of the person
- **person_name**: name for quick access
- **role**: role of the person (e.g. "group president", "rapporteur", "Federal Councillor")

### Temporal recording

- **start_time**: start of the speech
- **end_time**: end of the speech
- **duration**: duration in seconds (calculated or recorded)

These time indications enable:
- precise referencing in audio and video recordings
- analysis of speaking time per person / group
- monitoring of compliance with time limits

### Language of the speech

The field **language** records the language in which the speech was made:

- **de**: German
- **fr**: French
- **it**: Italian
- **rm**: Romansh
- **en**: English

### Text documents

The field **text_segments** references TextSegment entities containing the spoken text.

#### Different text versions

##### Raw transcript
- Verbatim transcription
- Unedited, with filler words
- Available directly after the sitting

##### Edited transcript
- Editorially revised
- Grammatically corrected
- Official protocol version

##### Translations
- Into other national languages
- For international publications

#### TextSegment structure

Every TextSegment can contain:
- **text**: the actual text
- **language**: language of the text
- **version**: kind of version (raw, edited, translated)
- **format**: format (plain, markdown, HTML)

### Multimedia recordings

The field **media** references Media entities with audio and video recordings.

#### Audio recordings
- Original sound of the speech
- Format: MP3, WAV, etc.
- Technical metadata (quality, bitrate)

#### Video recordings
- Visual recording (in plenary sittings)
- Format: MP4, WebM, etc.
- Various resolutions

#### Livestreaming
- Real-time transmission
- URL of the stream
- Archiving after the sitting

### Title and description

- **title**: short title (e.g. "Statement on energy policy")
- **description**: summary or context of the speech

### Type of speech

The field **speech_type** can distinguish various kinds:

- **statement**: position statement
- **question**: question
- **response**: answer (e.g. government to a question)
- **procedural**: procedural motion
- **declaration**: declaration

### Placing a speech within the sitting

`parent_meeting` and `parent_agenda_item` record in which sitting and under which agenda item a speech was given. Both are needed because a speech can be delivered in two ways: embedded in the protocol, where the sitting follows from the surrounding `Protocol` but the agenda item does not — or flat in `Container.speeches`, where without these references any link would be missing. They carry the same values as on `Voting` and `Election` and thus make the speech evaluable regardless of the delivery form it came in.



### Class: Speech []{#Speech}


_A speech or statement made during a meeting (also called Votum or speaker segment)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on a voting, election, speech, attendance list or protocol it names the meeting in which the record arose. Agenda items do not carry it: they are embedded in their meeting.  |
| parent_agenda_item | 0..1 <br/> String | Identifier of the agenda item this record belongs to. On an agenda item it builds a hierarchy of agenda items — e.g. an item group "Gesetzesberatungen" with the sub-items "Energiegesetz (Detailberatung)" and "Energiegesetz (Schlussabstimmung)"; on a speech it names the agenda item under which the speech was given.  |
| language | 0..1 <br/> String | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |
| start | 0..1 <br/> String | Start indicator or position.  |
| datetime_begin | 0..1 <br/> Datetime | The date and time when the meeting or voting begins.  |
| datetime_end | 0..1 <br/> Datetime | The date and time when the meeting or voting ends.  |
| actor_fullname | 0..1 <br/> String | Full name of the actor/person.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Reference to the acting person (lightweight snapshot at time of linking).  |
| role | 0..1 <br/> String | Role of the person (e.g., commission speaker).  |
| text | 1 <br/> String | Text content of the element.  |
| text_format | 0..1 <br/> String | Format of text (text, html, html_with_timestamps).  |
| text_type | 0..1 <br/> String | Type of text (raw draft, edited version).  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| media_url | 0..1 <br/> String | URL to media file (audio/video).  |
| media_type | 0..1 <br/> String | Type of media (audio, video, document).  |
| media_format | 0..1 <br/> String | MIME type of the media file.  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | speeches | range | [Speech](#Speech) |
| [Protocol](#Protocol) | speeches | range | [Speech](#Speech) |














#### Examples
##### Example Speech: Speech with verbatim text and video recording

```yaml
speeches:
- global_uri: ops:366631
  parent_meeting: parl:sr_winter25_sitzung_6
  parent_agenda_item: ops:69905
  language: fr
  datetime_begin: '2025-12-19T09:20:00+01:00'
  datetime_end: '2025-12-19T09:25:00+01:00'
  actor_fullname: Pascal Broulis
  actor_id:
    global_uri: actors:person_pascal_broulis
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

# Texts and media

Parliamentary debates are recorded not only as structured data but also as texts and multimedia recordings. These entities enable the management of transcripts, audio and video recordings and further media formats, as well as the technical infrastructure for data exchange and multilingualism.

## TextSegment

### Purpose
Records text passages with versioning and language variants. Used primarily for transcriptions of speeches, but can also be applied to other text documents.

### Structure
- **text**: the actual text content
- **language**: language code (ISO 639-1)
- **format**: format of the text (plain, markdown, html)
- **version_type**: kind of version
  - **raw**: unedited raw transcript
  - **edited**: editorially revised version
  - **translated**: translation into another language
  - **summary**: summary

### Design decision
**Why a separate entity?**
- Allows several versions of the same text (raw, edited, translated)
- Version control and traceability of changes
- Flexibility regarding formats (plain, markdown, HTML for different output channels)

### Application
Mainly linked with Speech entities:
```
Speech
  ├─ TextSegment (raw transcript, de)
  ├─ TextSegment (edited protocol, de)
  ├─ TextSegment (translation, fr)
  └─ TextSegment (summary, de)
```

### Carriers of a text segment

Text segments are not tied to the verbatim record alone: `Protocol` carries them for the wording of the whole sitting, and `AgendaItem` — respectively the recorded `ProtocolItem` — for text belonging to one agenda item, such as a subtitle, a cross-reference or a reasoning already published with the agenda. Because both classes carry the `IsAgendaItem` mixin, `text_segments` is available on the planned as well as on the recorded side. A single contribution, by contrast, carries its wording directly in `text`, `text_format` and `text_type`.

## Media

### Purpose
References media files (audio, video, documents) belonging to parliamentary activities.

### Structure
- **media_type**: kind of media file
  - **audio**: audio recording
  - **video**: video recording
  - **document**: documents (PDF, etc.)
  - **image**: images
- **url**: URL of the media file
- **mime_type**: MIME type (audio/mp3, video/mp4, application/pdf, etc.)
- **title**: title of the media file
- **description**: description
- **language**: language (for language-based media)
- **duration**: duration (for audio/video, in seconds)
- **file_size**: file size in bytes
- **quality**: quality indication (e.g. "720p", "high", "low")

### Design decision
**Why a generic Media entity?**
- Uniform structure for all media types
- Extensible for new formats
- Technical metadata recorded centrally
- Several quality levels of the same recording possible

### Application
Can be attached to various entities:
```
Speech
  ├─ Media (audio recording, MP3, 256 kbps)
  ├─ Media (audio recording, MP3, 128 kbps)
  ├─ Media (video recording, MP4, 1080p)
  └─ Media (video recording, MP4, 480p)

AgendaItem
  └─ Media (PDF of the bill)

Meeting
  └─ Media (livestream URL)
```



### Class: TextSegment []{#TextSegment}


_A text segment such as cross-references or subtitles. Text segments are carried by the protocol, by a speech or by an agenda item (planned AgendaItem or recorded ProtocolItem)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| text | 1 <br/> String | Text content of the element.  |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| IsAgendaItem | text_segments | range | [TextSegment](#TextSegment) |
| [AgendaItem](#AgendaItem) | text_segments | range | [TextSegment](#TextSegment) |
| [Protocol](#Protocol) | text_segments | range | [TextSegment](#TextSegment) |
| [ProtocolItem](#ProtocolItem) | text_segments | range | [TextSegment](#TextSegment) |



















</div>



### Class: Media []{#Media}


_Media files or documents (including protocols in PDF/HTML/WORD or links to audio/video)._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| title | 0..1 <br/> String | Title of the element.  |
| media_type | 0..1 <br/> String | Type of media (audio, video, document).  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing page or further web address, multilingual.  |
| version | 0..1 <br/> String | Version number or identifier.  |
| parent_type | 0..1 <br/> String | Type of parent object (meeting, agenda, speech, affair).  |






















</div>

\newpage

# Shared elements

## Reference classes

`PersonReference` and `GroupReference` name a person or a group without describing them here: what a person or a body is, is defined by eCH-0294; council operations merely point to it. Besides the pointer, the reference retains the key characteristics **at the time of linking** — for a speech, for instance, the parliamentary group the speaker belonged to back then.

This serves three purposes:

- **Useful local data** without costly queries of the complete entity
- **No redundancy**, since not all information has to be repeated at every mention
- **Implicit versioning**, as the reference stays unchanged even if the linked person or group changes later

Unlike an entity, a reference is not identified in its own right — it merely names an identified entity. That is why `global_uri` is not mandatory here: all that is required is that at least one of `local_id` or `global_uri` is set. A system that only knows the local id of the referenced entity states that; it is resolved within the same delivery. Beyond the delivery, the `global_uri` does the pointing.



### Class: PersonReference []{#PersonReference}


_Lightweight reference to a person with key identification data at time of linking. Preserves historical accuracy even if the person changes later. The referenced person is identified by `local_id` or `global_uri`; at least one of the two is required._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier of the referenced entity. It is resolved within the same delivery. <br/><br/>Inheritance: HasReferenceIdentification |
| global_uri | 0..1 <br/> Uriorcurie | The unique, globally valid URI of the referenced entity. Unlike a local_id it also resolves beyond the delivery. <br/><br/>Inheritance: HasReferenceIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: HasReferenceIdentification |
| label | 1 <br/> String | Mandatory short display name to identify the person within the organisation (e.g. with added birth year to distinguish persons with the same name).  |
| label_long | 0..1 <br/> String | Optional long display name including academic titles and full official name (e.g. "Dr. Maria Muster-Beispiel").  |
| group_label | 0..1 <br/> String | Name of the body/group at time of linking.  |

###### Constraints


At least one of the following must be set:

- local_id
- global_uri










#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [IndividualVote](#IndividualVote) | actor_id | range | [PersonReference](#PersonReference) |
| [IndividualAttendance](#IndividualAttendance) | actor_id | range | [PersonReference](#PersonReference) |
| [Speech](#Speech) | actor_id | range | [PersonReference](#PersonReference) |



















</div>



### Class: GroupReference []{#GroupReference}


_Lightweight reference to a group with key identification data at time of linking. The referenced group is identified by `local_id` or `global_uri`; at least one of the two is required. A `local_id` is resolved within the same delivery, a `global_uri` also beyond it._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier of the referenced entity. It is resolved within the same delivery. <br/><br/>Inheritance: HasReferenceIdentification |
| global_uri | 0..1 <br/> Uriorcurie | The unique, globally valid URI of the referenced entity. Unlike a local_id it also resolves beyond the delivery. <br/><br/>Inheritance: HasReferenceIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: HasReferenceIdentification |
| label | 0..1 <br/> String | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| abbreviation | * <br/> MultilingualValue | Abbreviation (can be multilingual).  |

###### Constraints


At least one of the following must be set:

- local_id
- global_uri










#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Legislature](#Legislature) | actor_id | range | [GroupReference](#GroupReference) |
| [Meeting](#Meeting) | group_id | range | [GroupReference](#GroupReference) |
| [Meeting](#Meeting) | actor_id | range | [GroupReference](#GroupReference) |
| [Voting](#Voting) | actor_id | range | [GroupReference](#GroupReference) |
| [Election](#Election) | actor_id | range | [GroupReference](#GroupReference) |
| [Attendance](#Attendance) | actor_id | range | [GroupReference](#GroupReference) |



















</div>

## Multilingual texts

In Switzerland, designations, titles and descriptions often exist in several languages. Rather than keeping a separate field per language, a slot of type `MultilingualString` takes a list of entries with `text` and `language`. Those who keep only one language deliver a single entry — the language is to be stated there as well. Links are modelled the same way: many parliamentary information systems keep a separate address per language, which is why `url` is multilingual too.



### Class: MultilingualString []{#MultilingualString}


_A string that can contain text in multiple languages._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| text | 1 <br/> String | Text content of the element.  |
| language | 1 <br/> String | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |





#### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Legislature](#Legislature) | name | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | name | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | url | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | name | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | url | range | [MultilingualString](#MultilingualString) |
| IsAgendaItem | agenda_item_title | range | [MultilingualString](#MultilingualString) |
| IsAgendaItem | agenda_item_description | range | [MultilingualString](#MultilingualString) |
| IsAgendaItem | url | range | [MultilingualString](#MultilingualString) |
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

## Mixin classes

Three classes carry no data of their own; they bundle slots that look the same across many classes — the identification of an entity, its creation and modification dates, and the temporal course of an event with planned and actual start and end. They come from the specialist group's common schema (eCH-0292) and are imported by its standards so that the same information is named alike and behaves alike everywhere.

A mixin is not a superclass: no instance of a mixin class is ever created, and nothing of it shows in the data. The attribute tables of the classes therefore list the inherited slots individually and note their origin under "Inheritance" — the three sections below explain what stands behind that note.



### Class: HasIdentification []{#HasIdentification}


_A mixin class that provides slots for the identification of an entity. It is used for entities that are identified in their own right; their `global_uri` is the identifier and therefore mandatory._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system.  |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity.  |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans.  |



#### Mixin Usage

[Container](#Container), [Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem), [Protocol](#Protocol), [ProtocolItem](#ProtocolItem), [Voting](#Voting), [IndividualVote](#IndividualVote), [Election](#Election), [Attendance](#Attendance), [IndividualAttendance](#IndividualAttendance), [Speech](#Speech), [TextSegment](#TextSegment), [Motion](#Motion), [Media](#Media)





















</div>



### Class: HasCreationModificationDates []{#HasCreationModificationDates}


_A mixin class that provides slots for modeling creation and modification dates of an entity._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| date_created | 0..1 <br/> Date | The date when an entity was created.  |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created.  |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified.  |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified.  |



#### Mixin Usage

[Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem), [Protocol](#Protocol), [ProtocolItem](#ProtocolItem), [Voting](#Voting), [IndividualVote](#IndividualVote), [Election](#Election), [Attendance](#Attendance), [IndividualAttendance](#IndividualAttendance), [Speech](#Speech)





















</div>



### Class: IsEventWithDuration []{#IsEventWithDuration}


_A mixin class that provides slots for modeling events or occurrences with time duration._




<div data-search-exclude markdown="1">




#### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration.  |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration.  |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration.  |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration.  |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration.  |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration.  |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration.  |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration.  |



#### Mixin Usage

[Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem), [ProtocolItem](#ProtocolItem)





















</div>

\newpage

# Copyrights

Persons preparing eCH-standards shall remain the owners of their intellectual property rights. These persons, however, obligate themselves to provide their intellectual property rights or other rights in third party intellectual property rights, to the extent possible, to the relevant technical units and the registered association eCH for free and for unlimited use and further development as part of the purpose of the association.

The standards prepared by the technical units can be used, distributed and developed further for free and to an unlimited extent by stating the name of the respective author of eCH.

eCH-standards are fully documented and free of any restrictions of licence and/or patent law. The associated documentation can be requested for free.

These provisions shall apply to the standards prepared by eCH only, however, not to any standards or products of third parties which include reference to eCH-standards. The standards include the relevant references to third party rights.

\newpage

# Appendix A – References & bibliography

Where a version is stated, it is the one this standard was developed against.

## Standards of the "Political Affairs" specialist group

The standards of the specialist group are developed jointly and reference one another. All of them currently carry the status "In Arbeit" (in progress; as of 10 August 2026); no version is therefore stated.

| | |
|------------------|----------------------------------------------------------------------------------|
|eCH-0292|eCH-0292: Meta-processes for political affairs – shared data elements, from which this standard takes the reference classes and the mixins: [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|eCH-0294|eCH-0294: Political actors – defines the persons and groups that `PersonReference` and `GroupReference` point to: [https://www.ech.ch/de/ech/ech-0294](https://www.ech.ch/de/ech/ech-0294)|
|eCH-0295|eCH-0295: Parliamentary affairs – the affairs dealt with in agenda items, votings and speeches: [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|eCH-0296|eCH-0296: Legal acts and legislative texts: [https://www.ech.ch/de/ech/ech-0296](https://www.ech.ch/de/ech/ech-0296)|
|eCH-0297|eCH-0297: Public consultations: [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Code lists and further sources

| | |
|------------------|----------------------------------------------------------------------------------|
|ISO 639-1|ISO (International Organization for Standardization). Language codes, used in the `language` slot of `MultilingualString`.|
|Dublin Core|DCMI Metadata Terms. Source of several `slot_uri` assignments (prefix `dcterms`): [https://www.dublincore.org/specifications/dublin-core/dcmi-terms/](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)|
|LinkML|Modelling language in which this standard is defined: [https://linkml.io](https://linkml.io)|

