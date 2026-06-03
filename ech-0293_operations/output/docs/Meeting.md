---
search:
  boost: 10.0
---

# Class: Meeting 


_[en] A general meeting class used for Sessions, Comittee Meetings, individual session Sittings and other various Meetings._

_[de] Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sessionssitzung und andere verschiedene Versammlungen verwendet wird._

__



<div data-search-exclude markdown="1">



URI: [ops:Meeting](https://ch.paf.link/schema/operations/Meeting)





```mermaid
 classDiagram
    class Meeting
    click Meeting href "../Meeting/"
      HasIdentification <|-- Meeting
        click HasIdentification href "../HasIdentification/"
      IsEventWithDuration <|-- Meeting
        click IsEventWithDuration href "../IsEventWithDuration/"
      HasCreationModificationDates <|-- Meeting
        click HasCreationModificationDates href "../HasCreationModificationDates/"
      
      Meeting : actor_id
        
          
    
        
        
        Meeting --> "0..1" GroupReference : actor_id
        click GroupReference href "../GroupReference/"
    

        
      Meeting : actor_name
        
      Meeting : administrative_id
        
      Meeting : body_key
        
      Meeting : date_begin_actual
        
      Meeting : date_begin_planned
        
      Meeting : date_created
        
      Meeting : date_end_actual
        
      Meeting : date_end_planned
        
      Meeting : date_modified
        
      Meeting : datetime_begin_actual
        
      Meeting : datetime_begin_planned
        
      Meeting : datetime_created
        
      Meeting : datetime_end_actual
        
      Meeting : datetime_end_planned
        
      Meeting : datetime_modified
        
      Meeting : description
        
      Meeting : documents
        
          
    
        
        
        Meeting --> "*" Work : documents
        click Work href "../Work/"
    

        
      Meeting : global_uri
        
      Meeting : group_id
        
          
    
        
        
        Meeting --> "0..1" GroupReference : group_id
        click GroupReference href "../GroupReference/"
    

        
      Meeting : group_name
        
      Meeting : landing_page
        
      Meeting : local_id
        
      Meeting : location
        
      Meeting : meeting_abbreviation
        
      Meeting : meeting_type
        
          
    
        
        
        Meeting --> "0..1" MeetingTypeEnum : meeting_type
        click MeetingTypeEnum href "../MeetingTypeEnum/"
    

        
      Meeting : name
        
          
    
        
        
        Meeting --> "*" MultilingualString : name
        click MultilingualString href "../MultilingualString/"
    

        
      Meeting : number
        
      Meeting : parent_legislature
        
      Meeting : parent_meeting
        
      Meeting : position
        
      Meeting : protocol
        
          
    
        
        
        Meeting --> "0..1" Protocol : protocol
        click Protocol href "../Protocol/"
    

        
      Meeting : sequential_number
        
      Meeting : state
        
          
    
        
        
        Meeting --> "0..1" StateEnum : state
        click StateEnum href "../StateEnum/"
    

        
      Meeting : state_name
        
      Meeting : url
        
          
    
        
        
        Meeting --> "*" MultilingualString : url
        click MultilingualString href "../MultilingualString/"
    

        
      Meeting : wikidata_uri
        
      
```





## Inheritance
* **Meeting** [ [HasIdentification](HasIdentification.md) [IsEventWithDuration](IsEventWithDuration.md) [HasCreationModificationDates](HasCreationModificationDates.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [body_key](body_key.md) | 0..1 <br/> [String](String.md) | [en] Key identifying the political body or jurisdiction (e | direct |
| [meeting_type](meeting_type.md) | 0..1 <br/> [MeetingTypeEnum](MeetingTypeEnum.md) | Type of the meeting, e | direct |
| [administrative_id](administrative_id.md) | 0..1 <br/> [String](String.md) | [en] Administrative ID of the legislative body, such as a municipality, canto... | direct |
| [name](name.md) | * <br/> [MultilingualString](MultilingualString.md) |  | direct |
| [url](url.md) | * <br/> [MultilingualString](MultilingualString.md) |  | direct |
| [group_name](group_name.md) | 0..1 <br/> [String](String.md) | Name of the group or body | direct |
| [group_id](group_id.md) | 0..1 <br/> [GroupReference](GroupReference.md) | [en] Reference to the group or body (lightweight snapshot at time of linking) | direct |
| [number](number.md) | 0..1 <br/> [String](String.md) |  | direct |
| [landing_page](landing_page.md) | 0..1 <br/> [String](String.md) | [en] URL providing further information | direct |
| [sequential_number](sequential_number.md) | 0..1 <br/> [Integer](Integer.md) | [en] Sequential number of the meeting, used for ordering | direct |
| [position](position.md) | 0..1 <br/> [String](String.md) |  | direct |
| [meeting_abbreviation](meeting_abbreviation.md) | 0..1 <br/> [String](String.md) |  | direct |
| [actor_name](actor_name.md) | 0..1 <br/> [String](String.md) | [en] Name of the political body (e | direct |
| [actor_id](actor_id.md) | 0..1 <br/> [GroupReference](GroupReference.md) | [en] Reference to the acting body/organ (lightweight snapshot at time of link... | direct |
| [state](state.md) | 0..1 <br/> [StateEnum](StateEnum.md) |  | direct |
| [state_name](state_name.md) | 0..1 <br/> [String](String.md) | [en] Custom state description for the meeting | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [location](location.md) | 0..1 <br/> [String](String.md) |  | direct |
| [parent_meeting](parent_meeting.md) | 0..1 <br/> [String](String.md) | [en] The linked meeting ID that groups the current meeting | direct |
| [parent_legislature](parent_legislature.md) | 0..1 <br/> [String](String.md) | [en] The legislative body in which the meeting is based | direct |
| [documents](documents.md) | * <br/> [Work](Work.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind | direct |
| [protocol](protocol.md) | 0..1 <br/> [Protocol](Protocol.md) | [en] The protocol (minutes) of this meeting, recorded after the meeting | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | Local identifier | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e | [HasIdentification](HasIdentification.md) |
| [date_begin_actual](date_begin_actual.md) | 0..1 <br/> [Date](Date.md) | The actual start date of an event or occurrence with time duration | [IsEventWithDuration](IsEventWithDuration.md) |
| [datetime_begin_actual](datetime_begin_actual.md) | 0..1 <br/> [Datetime](Datetime.md) | The actual start date and time of an event or occurrence with time duration | [IsEventWithDuration](IsEventWithDuration.md) |
| [date_begin_planned](date_begin_planned.md) | 0..1 <br/> [Date](Date.md) | The planned start date of an event or occurrence with time duration | [IsEventWithDuration](IsEventWithDuration.md) |
| [datetime_begin_planned](datetime_begin_planned.md) | 0..1 <br/> [Datetime](Datetime.md) | The planned start date and time of an event or occurrence with time duration | [IsEventWithDuration](IsEventWithDuration.md) |
| [date_end_actual](date_end_actual.md) | 0..1 <br/> [Date](Date.md) | The actual end date of an event or occurrence with time duration | [IsEventWithDuration](IsEventWithDuration.md) |
| [datetime_end_actual](datetime_end_actual.md) | 0..1 <br/> [Datetime](Datetime.md) | The actual end date and time of an event or occurrence with time duration | [IsEventWithDuration](IsEventWithDuration.md) |
| [date_end_planned](date_end_planned.md) | 0..1 <br/> [Date](Date.md) | The planned end date of an event or occurrence with time duration | [IsEventWithDuration](IsEventWithDuration.md) |
| [datetime_end_planned](datetime_end_planned.md) | 0..1 <br/> [Datetime](Datetime.md) | The planned end date and time of an event or occurrence with time duration | [IsEventWithDuration](IsEventWithDuration.md) |
| [date_created](date_created.md) | 0..1 <br/> [Date](Date.md) | The date when an entity was created | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_created](datetime_created.md) | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [date_modified](date_modified.md) | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_modified](datetime_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified | [HasCreationModificationDates](HasCreationModificationDates.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [meetings](meetings.md) | range | [Meeting](Meeting.md) |
| [Session](Session.md) | [meetings](meetings.md) | range | [Meeting](Meeting.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:Meeting |
| native | ops:Meeting |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Meeting
description: '[en] A general meeting class used for Sessions, Comittee Meetings, individual
  session Sittings and other various Meetings.

  [de] Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sessionssitzung
  und andere verschiedene Versammlungen verwendet wird.

  '
from_schema: https://ch.paf.link/schema/operations
mixins:
- HasIdentification
- IsEventWithDuration
- HasCreationModificationDates
slots:
- body_key
- meeting_type
- administrative_id
- name
- url
- group_name
- group_id
- number
- landing_page
- sequential_number
- position
- meeting_abbreviation
- actor_name
- actor_id
- state
- state_name
- description
- location
- parent_meeting
- parent_legislature
- documents
- protocol
slot_usage:
  actor_id:
    name: actor_id
    description: '[en] Reference to the acting body/organ (lightweight snapshot at
      time of linking).

      [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum
      Zeitpunkt der Verknüpfung).

      '
    range: GroupReference
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: Meeting
description: '[en] A general meeting class used for Sessions, Comittee Meetings, individual
  session Sittings and other various Meetings.

  [de] Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sessionssitzung
  und andere verschiedene Versammlungen verwendet wird.

  '
from_schema: https://ch.paf.link/schema/operations
mixins:
- HasIdentification
- IsEventWithDuration
- HasCreationModificationDates
slot_usage:
  actor_id:
    name: actor_id
    description: '[en] Reference to the acting body/organ (lightweight snapshot at
      time of linking).

      [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum
      Zeitpunkt der Verknüpfung).

      '
    range: GroupReference
    inlined: true
attributes:
  body_key:
    name: body_key
    description: '[en] Key identifying the political body or jurisdiction (e.g., BE
      for Bern, CHE for Switzerland).

      [de] Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit
      (z.B. BE für Bern, CHE für Schweiz).

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Session
    - Meeting
    range: string
  meeting_type:
    name: meeting_type
    description: Type of the meeting, e.g. session, committee, sitting, various
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: ops:meetingType
    owner: Meeting
    domain_of:
    - Meeting
    range: MeetingTypeEnum
  administrative_id:
    name: administrative_id
    description: '[en] Administrative ID of the legislative body, such as a municipality,
      canton, or country.

      [de] Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder
      Land.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Legislature
    - Meeting
    range: string
  name:
    name: name
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Legislature
    - Session
    - Meeting
    range: MultilingualString
    multivalued: true
    inlined: true
    inlined_as_list: true
  url:
    name: url
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Session
    - Meeting
    - AgendaItem
    - Media
    - Manifestation
    range: MultilingualString
    multivalued: true
    inlined: true
    inlined_as_list: true
  group_name:
    name: group_name
    description: Name of the group or body
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Meeting
    range: string
  group_id:
    name: group_id
    description: '[en] Reference to the group or body (lightweight snapshot at time
      of linking).

      [de] Referenz auf die Gruppe oder das Gremium (leichtgewichtiger Snapshot zum
      Zeitpunkt der Verknüpfung).

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Meeting
    range: GroupReference
    inlined: true
  number:
    name: number
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Session
    - Meeting
    range: string
  landing_page:
    name: landing_page
    description: '[en] URL providing further information.

      [de] URL mit weiteren Informationen.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: ops:landingPage
    owner: Meeting
    domain_of:
    - Legislature
    - Meeting
    - AgendaItem
    - Voting
    - Election
    - Speech
    range: string
  sequential_number:
    name: sequential_number
    description: '[en] Sequential number of the meeting, used for ordering.

      [de] Laufende Nummer der Sitzung, die zur Sortierung verwendet wird.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Session
    - Meeting
    range: integer
  position:
    name: position
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Session
    - Meeting
    range: string
  meeting_abbreviation:
    name: meeting_abbreviation
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Session
    - Meeting
    range: string
  actor_name:
    name: actor_name
    description: '[en] Name of the political body (e.g., Nationalrat).

      [de] Name des politischen Organs (z.B. Nationalrat).

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Meeting
    range: string
  actor_id:
    name: actor_id
    description: '[en] Reference to the acting body/organ (lightweight snapshot at
      time of linking).

      [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum
      Zeitpunkt der Verknüpfung).

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Legislature
    - Meeting
    - Voting
    - IndividualVote
    - Election
    - Attendance
    - IndividualAttendance
    - Speech
    range: GroupReference
    inlined: true
  state:
    name: state
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Meeting
    range: StateEnum
  state_name:
    name: state_name
    description: '[en] Custom state description for the meeting.

      [de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Meeting
    - AgendaItem
    range: string
  description:
    name: description
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Legislature
    - Meeting
    - Motion
    - Expression
    range: string
  location:
    name: location
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Meeting
    range: string
  parent_meeting:
    name: parent_meeting
    description: '[en] The linked meeting ID that groups the current meeting.

      [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Meeting
    - AgendaItem
    - Protocol
    - Voting
    - Election
    - Attendance
    range: string
  parent_legislature:
    name: parent_legislature
    description: '[en] The legislative body in which the meeting is based.

      [de] Der gesetzgebende Körper, auf dem die Sitzung basiert.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    owner: Meeting
    domain_of:
    - Session
    - Meeting
    range: string
  documents:
    name: documents
    description: '[de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft
      sind.

      [en] List of documents (FRBR Works) linked to the entity.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: meta:documents
    owner: Meeting
    domain_of:
    - Legislature
    - Session
    - Meeting
    - AgendaItem
    - Protocol
    - Resolution
    - Voting
    - Election
    - Speech
    - Motion
    range: Work
    multivalued: true
    inlined: true
    inlined_as_list: true
  protocol:
    name: protocol
    description: '[en] The protocol (minutes) of this meeting, recorded after the
      meeting.

      [de] Das nach der Sitzung erstellte Protokoll dieser Sitzung.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: ops:protocol
    owner: Meeting
    domain_of:
    - Meeting
    range: Protocol
    inlined: true
  local_id:
    name: local_id
    annotations:
      description_de:
        tag: description_de
        value: 'Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

          '
    description: 'Local identifier. For example, a UUID from the council information
      system.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:localId
    owner: Meeting
    domain_of:
    - HasIdentification
    range: string
  global_uri:
    name: global_uri
    annotations:
      description_de:
        tag: description_de
        value: 'Eine eindeutige, global gültige URI für die Entität.

          '
    description: 'A unique, globally valid URI for the entity.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:globalURI
    identifier: true
    owner: Meeting
    domain_of:
    - HasIdentification
    range: uriorcurie
    required: true
  wikidata_uri:
    name: wikidata_uri
    annotations:
      description_de:
        tag: description_de
        value: 'Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39
          für die Schweiz.

          '
    description: 'A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39
      for Switzerland.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:wikidataUri
    owner: Meeting
    domain_of:
    - HasIdentification
    range: uriorcurie
  date_begin_actual:
    name: date_begin_actual
    annotations:
      description_de:
        tag: description_de
        value: 'Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit
          Zeitdauer.

          '
    description: 'The actual start date of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateBeginActual
    owner: Meeting
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_begin_actual:
    name: datetime_begin_actual
    annotations:
      description_de:
        tag: description_de
        value: 'Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder
          Vorkommnissen mit Zeitdauer.

          '
    description: 'The actual start date and time of an event or occurrence with time
      duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeBeginActual
    owner: Meeting
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_begin_planned:
    name: date_begin_planned
    annotations:
      description_de:
        tag: description_de
        value: 'Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

          '
    description: 'The planned start date of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateBeginPlanned
    owner: Meeting
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_begin_planned:
    name: datetime_begin_planned
    annotations:
      description_de:
        tag: description_de
        value: 'Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
          mit Zeitdauer.

          '
    description: 'The planned start date and time of an event or occurrence with time
      duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeBeginPlanned
    owner: Meeting
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_end_actual:
    name: date_end_actual
    annotations:
      description_de:
        tag: description_de
        value: 'Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit
          Zeitdauer.

          '
    description: 'The actual end date of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateEndActual
    owner: Meeting
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_end_actual:
    name: datetime_end_actual
    annotations:
      description_de:
        tag: description_de
        value: 'Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
          mit Zeitdauer.

          '
    description: 'The actual end date and time of an event or occurrence with time
      duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeEndActual
    owner: Meeting
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_end_planned:
    name: date_end_planned
    annotations:
      description_de:
        tag: description_de
        value: 'Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

          '
    description: 'The planned end date of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateEndPlanned
    owner: Meeting
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_end_planned:
    name: datetime_end_planned
    annotations:
      description_de:
        tag: description_de
        value: 'Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
          mit Zeitdauer.

          '
    description: 'The planned end date and time of an event or occurrence with time
      duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeEndPlanned
    owner: Meeting
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_created:
    name: date_created
    annotations:
      description_de:
        tag: description_de
        value: 'Das Datum, an dem eine Entität erstellt wurde.

          '
    description: 'The date when an entity was created.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateCreated
    owner: Meeting
    domain_of:
    - HasCreationModificationDates
    range: date
  datetime_created:
    name: datetime_created
    annotations:
      description_de:
        tag: description_de
        value: 'Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.

          '
    description: 'The date and time when an entity was created.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeCreated
    owner: Meeting
    domain_of:
    - HasCreationModificationDates
    range: datetime
  date_modified:
    name: date_modified
    annotations:
      description_de:
        tag: description_de
        value: 'Das Datum, an dem eine Entität zuletzt geändert wurde.

          '
    description: 'The date when an entity was last modified.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateModified
    owner: Meeting
    domain_of:
    - HasCreationModificationDates
    range: date
  datetime_modified:
    name: datetime_modified
    annotations:
      description_de:
        tag: description_de
        value: 'Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.

          '
    description: 'The date and time when an entity was last modified.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeModified
    owner: Meeting
    domain_of:
    - HasCreationModificationDates
    range: datetime

```
</details></div>