

## Class: Meeting 


_The individual sitting of a body — the level at which agenda items are deliberated, decisions taken and speeches recorded. The meeting is the node to which the other classes of this standard attach: its agenda items (AgendaItem) are embedded in it (agenda_items), while votings and elections (Voting, Election), speeches (Speech) and the attendance list (Attendance) reference it via `parent_meeting`. At this level, scheduled and actual times regularly diverge — a sitting scheduled for 14:00 only begins at 14:25 because of delays and ends at 17:30 instead of 18:00 — which is why both the planned and the actual begin and end are recorded._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| spatial | 0..1 <br/> [String](String.md) | Spatial reference to a LINDAS resource (fos-municipality number, fos-canton number, district, or country). Formats: municipality: https://ld.admin.ch/municipality/1234, district: https://ld.admin.ch/district/2301, canton: https://ld.admin.ch/canton/23, country: https://ld.admin.ch/country/CHE.  |
| administrative_id | 0..1 <br/> [String](String.md) | Administrative ID of the legislative body, such as a municipality, canton, or country.  |
| name | * <br/> [MultilingualString](MultilingualString.md) | Multilingual full designation.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing page or further web address, multilingual.  |
| group_name | 0..1 <br/> [String](String.md) | Name of the group or body in plain text, in addition to the reference `group_id`.  |
| group_id | 0..1 <br/> [GroupReference](GroupReference.md) | Reference to the group or body (lightweight snapshot at time of linking).  |
| number | 0..1 <br/> [String](String.md) | Number of the session or meeting as designated by the body, e.g. within the legislature, the session or the year. As a string it also allows roman numerals. Numbering practices vary widely, which is why number, sequential_number, position and meeting_abbreviation are available side by side.  |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information.  |
| sequential_number | 0..1 <br/> [Integer](Integer.md) | Sequential number of the session or meeting as an integer, used for ordering.  |
| position | 0..1 <br/> [String](String.md) | Integer position within the superordinate sequence, e.g. of a session within the legislature.  |
| meeting_abbreviation | 0..1 <br/> [String](String.md) | Short designation of the session or meeting (e.g. "FS24" for the 2024 spring session).  |
| actor_name | 0..1 <br/> [String](String.md) | Name of the political body in plain text (e.g., Nationalrat), in addition to the reference `actor_id`.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| state | 0..1 <br/> [StateEnum](StateEnum.md) | Whether the meeting takes place as planned at all (planned, canceled, postponed). A diverging, free-text designation goes into `state_name`.  |
| state_name | 0..1 <br/> [String](String.md) | Diverging, free-text status designation of the meeting, where the values of `state` do not suffice.  |
| description | 0..1 <br/> [String](String.md) | Descriptive text of the element.  |
| location | 0..1 <br/> [String](String.md) | Place where the meeting is held — the physical room ("Federal Palace, National Council chamber"), a video conference or a hybrid format.  |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on a voting, election, speech, attendance list or protocol it names the meeting in which the record arose. Agenda items do not carry it: they are embedded in their meeting.  |
| parent_legislature | 0..1 <br/> [String](String.md) | Identifier of the legislature to which the session or meeting belongs. A meeting that belongs to a session is assigned to the legislature through the session (parent_session); a meeting without a session — for instance a committee sitting or a sitting in a federal unit without formal sessions — refers to the legislature directly.  |
| parent_session | 0..1 <br/> [String](String.md) | Identifier of the session to which the meeting belongs.  |
| documents | * <br/> [Work](Work.md) | Sitting documents such as the bulletin (Tagblatt) or annexes, as FRBR Works. The protocol is not linked here but via `has_protocol`.  |
| agenda_items | * <br/> [AgendaItem](AgendaItem.md) | Agenda items planned for this meeting or session, embedded as a list. On a meeting they form the agenda of the sitting. On a session they hold agenda items planned directly at the level of the session — where a federal unit does not break the session down into individual meetings (e.g. a Landsgemeinde or a one-day sitting of a cantonal parliament), or for items not (yet) assigned to a specific meeting, as in a session programme. The counterpart after the sitting are the items recorded in the protocol (Protocol.protocol_items).  |
| has_protocol | 0..1 <br/> [Protocol](Protocol.md) | Reference to the protocol (minutes) of this meeting, recorded after the meeting. Only the identifier of the protocol is given; the protocol itself is delivered in the container's `protocols` list. It is an entity in its own right with its own identifier and is usually published later than the meeting, so it is referenced rather than embedded.  |
| joint_debates | * <br/> [JointDebate](JointDebate.md) | Joint debates attached to this record: on an agenda item, the debates in which it is deliberated together with other agenda items; on a meeting or a session, the joint debates held within it.  |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [meetings](meetings.md) | range | [Meeting](Meeting.md) |
| [Session](Session.md) | [meetings](meetings.md) | range | [Meeting](Meeting.md) |














### Examples
#### Example Meeting: meeting item meeting be 2025 06 02

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
#### Example Meeting: Committee sitting with an attendance list

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
#### Example Meeting: meeting item meeting schaffhausen 2025 03 31 b

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
#### Example Meeting: meeting item meeting vaud 2008 04 30

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
#### Example Meeting: Landsgemeinde as meeting type sitting

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
#### Example Meeting: meeting item meeting bern 2022 03 17

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
#### Example Meeting: Council of States sitting with protocol and speeches

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
#### Example Meeting: Government sitting with a bilingual designation

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
#### Example Meeting: Cantonal parliament sitting with agenda items and votings

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
#### Example Meeting: meeting item meeting 2011 11 23

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
#### Example Meeting: meeting item meeting lausanne 2025 05 20

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
#### Example Meeting: meeting item meeting 2025 03 31

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
#### Example Meeting: meeting item meeting schaffhausen 2025 03 31

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
#### Example Meeting: meeting item meeting bern rr 2025 04 02

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
#### Example Meeting: Half-day sitting within a session

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
#### Example Meeting: meeting item meeting lausanne 2023 10 03

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
#### Example Meeting: meeting complete meeting zh 2025 11 20

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
#### Example Meeting: meeting item meeting luzern 2025 01 28

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
#### Example Meeting: meeting item meeting luzern 2025 01 28 b

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