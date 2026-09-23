

## Class: Session 


_A session: a contiguous period of sittings within a legislature. It groups its meetings (meetings) and may also carry agenda items directly (agenda_items). The session is the only one of the three temporal levels that may be omitted: federal units without formal sessions leave it out and attach their meetings directly to the legislature (parent_legislature). Session and meeting may also coincide — a one-day sitting of a cantonal parliament or a Landsgemeinde is represented as a session with a single meeting, or as a session that carries its agenda items directly without any meeting._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| spatial | 0..1 <br/> [String](String.md) | Spatial reference to a LINDAS resource (fos-municipality number, fos-canton number, district, or country). Formats: municipality: https://ld.admin.ch/municipality/1234, district: https://ld.admin.ch/district/2301, canton: https://ld.admin.ch/canton/23, country: https://ld.admin.ch/country/CHE.  |
| name | * <br/> [MultilingualString](MultilingualString.md) | Multilingual full designation.  |
| number | 0..1 <br/> [String](String.md) | Number of the session or meeting as designated by the body, e.g. within the legislature, the session or the year. As a string it also allows roman numerals. Numbering practices vary widely, which is why number, sequential_number, position and meeting_abbreviation are available side by side.  |
| sequential_number | 0..1 <br/> [Integer](Integer.md) | Sequential number of the session or meeting as an integer, used for ordering.  |
| position | 0..1 <br/> [String](String.md) | Integer position within the superordinate sequence, e.g. of a session within the legislature.  |
| meeting_abbreviation | 0..1 <br/> [String](String.md) | Short designation of the session or meeting (e.g. "FS24" for the 2024 spring session).  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing page or further web address, multilingual.  |
| parent_legislature | 0..1 <br/> [String](String.md) | Identifier of the legislature to which the session or meeting belongs. A meeting that belongs to a session is assigned to the legislature through the session (parent_session); a meeting without a session — for instance a committee sitting or a sitting in a federal unit without formal sessions — refers to the legislature directly.  |
| meetings | * <br/> [Meeting](Meeting.md) | Collection of meeting records.  |
| agenda_items | * <br/> [AgendaItem](AgendaItem.md) | Agenda items planned for this meeting or session, embedded as a list. On a meeting they form the agenda of the sitting. On a session they hold agenda items planned directly at the level of the session — where a federal unit does not break the session down into individual meetings (e.g. a Landsgemeinde or a one-day sitting of a cantonal parliament), or for items not (yet) assigned to a specific meeting, as in a session programme. The counterpart after the sitting are the items recorded in the protocol (Protocol.protocol_items).  |
| joint_debates | * <br/> [JointDebate](JointDebate.md) | Joint debates attached to this record: on an agenda item, the debates in which it is deliberated together with other agenda items; on a meeting or a session, the joint debates held within it.  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |
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
| [Container](Container.md) | [sessions](sessions.md) | range | [Session](Session.md) |














### Examples
#### Example Session: One-day sitting period of a cantonal parliament

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
#### Example Session: Landsgemeinde as a sitting period

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
#### Example Session: Federal session with a trilingual designation

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
#### Example Session: Cantonal session with a bilingual designation

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