

## Class: Session 


_[en] A parliamentary session that groups multiple meetings and spans a specific time period._

_[de] Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen bestimmten Zeitraum erstreckt._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| body_key | 0..1 <br/> [String](String.md) | [en] Key identifying the political body or jurisdiction (e.g., BE for Bern, CHE for Switzerland). [de] Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit (z.B. BE für Bern, CHE für Schweiz).  |
| name | * <br/> [MultilingualString](MultilingualString.md) | None |
| number | 0..1 <br/> [String](String.md) | None |
| sequential_number | 0..1 <br/> [Integer](Integer.md) | [en] Sequential number of the meeting, used for ordering. [de] Laufende Nummer der Sitzung, die zur Sortierung verwendet wird.  |
| position | 0..1 <br/> [String](String.md) | None |
| meeting_abbreviation | 0..1 <br/> [String](String.md) | None |
| url | * <br/> [MultilingualString](MultilingualString.md) | None |
| parent_legislature | 0..1 <br/> [String](String.md) | [en] The legislative body in which the meeting is based. [de] Der gesetzgebende Körper, auf dem die Sitzung basiert.  |
| meetings | * <br/> [Meeting](Meeting.md) | None |
| documents | * <br/> [Work](Work.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
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
#### Example: Session-session_session_gl_landrat_2025_02_26

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
#### Example: Session-session_session_5207

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
#### Example: Session-session_session_gl_landsgemeinde_2025_05_04

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
#### Example: Session-session_session_be_summer_2025

```yaml
global_uri: ops:session_be_summer_2025
body_key: BE
name:
- text: Sommersession 2025
  language: de
- text: Session d'été 2025
  language: fr
url:
- text: https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
  language: de
- text: https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
  language: fr
date_begin_planned: '2025-06-02'
date_end_planned: '2025-06-12'
datetime_modified: '2025-05-19T01:06:44Z'
datetime_created: '2025-04-25T11:10:24Z'

```






</div>