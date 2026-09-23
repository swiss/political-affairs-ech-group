

## Class: Meeting 


_The individual sitting of a body — the level at which agenda items are deliberated, decisions taken and speeches recorded. The meeting is the node to which the other classes of this standard attach via `parent_meeting`: agenda items (AgendaItem), votings and elections (Voting, Election), speeches (Speech) and the attendance list (Attendance). At this level, scheduled and actual times regularly diverge — a sitting scheduled for 14:00 only begins at 14:25 because of delays and ends at 17:30 instead of 18:00 — which is why both the planned and the actual begin and end are recorded._




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
| number | 0..1 <br/> [String](String.md) | Sequential number, e.g. within the legislature, the session or the year.  |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information.  |
| sequential_number | 0..1 <br/> [Integer](Integer.md) | Sequential number of the meeting, used for ordering.  |
| position | 0..1 <br/> [String](String.md) | Integer position within the superordinate sequence.  |
| meeting_abbreviation | 0..1 <br/> [String](String.md) | Short designation of the session or meeting (e.g. "FS24" for the 2024 spring session).  |
| actor_name | 0..1 <br/> [String](String.md) | Name of the political body in plain text (e.g., Nationalrat), in addition to the reference `actor_id`.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| state | 0..1 <br/> [StateEnum](StateEnum.md) | Whether the meeting takes place as planned at all (planned, canceled, postponed). A diverging, free-text designation goes into `state_name`.  |
| state_name | 0..1 <br/> [String](String.md) | Diverging, free-text status designation of the meeting, where the values of `state` do not suffice.  |
| description | 0..1 <br/> [String](String.md) | Descriptive text of the element.  |
| location | 0..1 <br/> [String](String.md) | Place where the meeting is held — the physical room ("Federal Palace, National Council chamber"), a video conference or a hybrid format.  |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on an agenda item, voting, election, speech or protocol it names the meeting in which the record arose.  |
| parent_session | 0..1 <br/> [String](String.md) | Identifier of the session to which the meeting belongs.  |
| documents | * <br/> [Work](Work.md) | Sitting documents such as the bulletin (Tagblatt) or annexes, as FRBR Works. The protocol is not linked here but via `has_protocol`.  |
| has_protocol | 0..1 <br/> [Protocol](Protocol.md) | Reference to the protocol (minutes) of this meeting, recorded after the meeting. Only the identifier of the protocol is given; the protocol itself is delivered in the container's `protocols` list. It is an entity in its own right with its own identifier and is usually published later than the meeting, so it is referenced rather than embedded.  |
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
  datetime_created: '2025-04-15T09:00:00Z'
  datetime_modified: '2025-05-12T16:45:00Z'

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

```






</div>