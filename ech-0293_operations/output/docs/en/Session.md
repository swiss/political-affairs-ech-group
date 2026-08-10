

## Class: Session 


_A parliamentary session that groups multiple meetings and spans a specific time period._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| body_key | 0..1 <br/> [String](String.md) | Key identifying the political body or jurisdiction (e.g., BE for Bern, CHE for Switzerland).  |
| name | * <br/> [MultilingualString](MultilingualString.md) | Multilingual full designation.  |
| number | 0..1 <br/> [String](String.md) | Sequential number, e.g. within the legislature, the session or the year.  |
| sequential_number | 0..1 <br/> [Integer](Integer.md) | Sequential number of the meeting, used for ordering.  |
| position | 0..1 <br/> [String](String.md) | Integer position within the superordinate sequence.  |
| meeting_abbreviation | 0..1 <br/> [String](String.md) | Short designation of the session or meeting (e.g. "FS24" for the 2024 spring session).  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing page or further web address, multilingual.  |
| parent_legislature | 0..1 <br/> [String](String.md) | The legislative body in which the meeting is based.  |
| meetings | * <br/> [Meeting](Meeting.md) | Collection of meeting records.  |
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

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [sessions](sessions.md) | range | [Session](Session.md) |














### Examples
#### Example Session: Federal session with a trilingual designation

```yaml
global_uri: ops:session_5207
body_key: CHE
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
#### Example Session: Landsgemeinde as a sitting period

```yaml
global_uri: ops:session_gl_landsgemeinde_2025_05_04
body_key: GL
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
#### Example Session: Cantonal session with a bilingual designation

```yaml
global_uri: ops:session_be_summer_2025
body_key: BE
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
#### Example Session: One-day sitting period of a cantonal parliament

```yaml
global_uri: ops:session_gl_landrat_2025_02_26
body_key: GL
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