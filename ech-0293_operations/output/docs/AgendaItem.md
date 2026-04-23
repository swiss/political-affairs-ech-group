

# Class: AgendaItem 


_[en] An agenda item of a meeting._

_[de] Ein Traktandum einer Sitzung._

__





URI: [ops:AgendaItem](https://ch.paf.link/schema/operations/AgendaItem)





```mermaid
 classDiagram
    class AgendaItem
    click AgendaItem href "../AgendaItem/"
      HasIdentification <|-- AgendaItem
        click HasIdentification href "../HasIdentification/"
      IsEventWithDuration <|-- AgendaItem
        click IsEventWithDuration href "../IsEventWithDuration/"
      HasCreationModificationDates <|-- AgendaItem
        click HasCreationModificationDates href "../HasCreationModificationDates/"
      
      AgendaItem : affair_id
        
      AgendaItem : agenda_item_category
        
      AgendaItem : agenda_item_description
        
          
    
        
        
        AgendaItem --> "*" MultilingualString : agenda_item_description
        click MultilingualString href "../MultilingualString/"
    

        
      AgendaItem : agenda_item_number
        
      AgendaItem : agenda_item_position
        
      AgendaItem : agenda_item_title
        
          
    
        
        
        AgendaItem --> "*" MultilingualString : agenda_item_title
        click MultilingualString href "../MultilingualString/"
    

        
      AgendaItem : agenda_item_type
        
          
    
        
        
        AgendaItem --> "0..1" AgendaItemTypeEnum : agenda_item_type
        click AgendaItemTypeEnum href "../AgendaItemTypeEnum/"
    

        
      AgendaItem : date_begin_actual
        
      AgendaItem : date_begin_planned
        
      AgendaItem : date_created
        
      AgendaItem : date_end_actual
        
      AgendaItem : date_end_planned
        
      AgendaItem : date_modified
        
      AgendaItem : datetime_begin_actual
        
      AgendaItem : datetime_begin_planned
        
      AgendaItem : datetime_created
        
      AgendaItem : datetime_end_actual
        
      AgendaItem : datetime_end_planned
        
      AgendaItem : datetime_modified
        
      AgendaItem : global_uri
        
      AgendaItem : has_resolution
        
          
    
        
        
        AgendaItem --> "0..1" Resolution : has_resolution
        click Resolution href "../Resolution/"
    

        
      AgendaItem : landing_page
        
      AgendaItem : leading_actor_id
        
      AgendaItem : local_id
        
      AgendaItem : parent_agenda_item
        
      AgendaItem : parent_meeting
        
      AgendaItem : speaking_actor_id
        
      AgendaItem : state_id
        
      AgendaItem : state_name
        
      AgendaItem : url
        
          
    
        
        
        AgendaItem --> "*" MultilingualString : url
        click MultilingualString href "../MultilingualString/"
    

        
      AgendaItem : wikidata_uri
        
      
```





## Inheritance
* **AgendaItem** [ [HasIdentification](HasIdentification.md) [IsEventWithDuration](IsEventWithDuration.md) [HasCreationModificationDates](HasCreationModificationDates.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [parent_meeting](parent_meeting.md) | 0..1 <br/> [String](String.md) | [en] The linked meeting ID that groups the current meeting | direct |
| [agenda_item_type](agenda_item_type.md) | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | [en] Type of agenda item, distinguishing individual items from groups | direct |
| [agenda_item_number](agenda_item_number.md) | 0..1 <br/> [String](String.md) | [en] Sequential number of the agenda item (string type to support roman numer... | direct |
| [agenda_item_position](agenda_item_position.md) | 0..1 <br/> [Integer](Integer.md) | [en] Integer position of the agenda item in the meeting sequence | direct |
| [leading_actor_id](leading_actor_id.md) | 0..1 <br/> [String](String.md) | [en] The leading department for the agenda item | direct |
| [speaking_actor_id](speaking_actor_id.md) | 0..1 <br/> [String](String.md) | [en] The speaker or head of the department for the agenda item | direct |
| [agenda_item_title](agenda_item_title.md) | * <br/> [MultilingualString](MultilingualString.md) | [en] Title of the agenda item | direct |
| [affair_id](affair_id.md) | 0..1 <br/> [String](String.md) | [en] The connection to the affairs (business items) of the agenda item | direct |
| [agenda_item_description](agenda_item_description.md) | * <br/> [MultilingualString](MultilingualString.md) | [en] Subtitle or detailed description of the agenda item | direct |
| [state_id](state_id.md) | 0..1 <br/> [String](String.md) | State identifier (reference to state enum or custom state) | direct |
| [state_name](state_name.md) | 0..1 <br/> [String](String.md) | [en] Custom state description for the meeting | direct |
| [landing_page](landing_page.md) | 0..1 <br/> [String](String.md) | [en] URL providing further information | direct |
| [url](url.md) | * <br/> [MultilingualString](MultilingualString.md) |  | direct |
| [agenda_item_category](agenda_item_category.md) | 0..1 <br/> [String](String.md) | [en] Category for grouped agenda items (e | direct |
| [parent_agenda_item](parent_agenda_item.md) | 0..1 <br/> [String](String.md) | [en] If needed, this slot builds a hierarchy of agenda items | direct |
| [has_resolution](has_resolution.md) | 0..1 <br/> [Resolution](Resolution.md) | [en] The resolutionor decision taken on this agenda item | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](HasIdentification.md) |
| [date_begin_actual](date_begin_actual.md) | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit Zeitda... | [IsEventWithDuration](IsEventWithDuration.md) |
| [datetime_begin_actual](datetime_begin_actual.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorko... | [IsEventWithDuration](IsEventWithDuration.md) |
| [date_begin_planned](date_begin_planned.md) | 0..1 <br/> [Date](Date.md) | [de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer | [IsEventWithDuration](IsEventWithDuration.md) |
| [datetime_begin_planned](datetime_begin_planned.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommen... | [IsEventWithDuration](IsEventWithDuration.md) |
| [date_end_actual](date_end_actual.md) | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens mit Zeitdaue... | [IsEventWithDuration](IsEventWithDuration.md) |
| [datetime_end_actual](datetime_end_actual.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkomm... | [IsEventWithDuration](IsEventWithDuration.md) |
| [date_end_planned](date_end_planned.md) | 0..1 <br/> [Date](Date.md) | [de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer | [IsEventWithDuration](IsEventWithDuration.md) |
| [datetime_end_planned](datetime_end_planned.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens ... | [IsEventWithDuration](IsEventWithDuration.md) |
| [date_created](date_created.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_created](datetime_created.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [date_modified](date_modified.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_modified](datetime_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [agenda_items](agenda_items.md) | range | [AgendaItem](AgendaItem.md) |
| [JointDebate](JointDebate.md) | [agenda_items](agenda_items.md) | range | [AgendaItem](AgendaItem.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:AgendaItem |
| native | ops:AgendaItem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AgendaItem
description: '[en] An agenda item of a meeting.

  [de] Ein Traktandum einer Sitzung.

  '
from_schema: https://ch.paf.link/schema/operations
mixins:
- HasIdentification
- IsEventWithDuration
- HasCreationModificationDates
slots:
- parent_meeting
- agenda_item_type
- agenda_item_number
- agenda_item_position
- leading_actor_id
- speaking_actor_id
- agenda_item_title
- affair_id
- agenda_item_description
- state_id
- state_name
- landing_page
- url
- agenda_item_category
- parent_agenda_item
- has_resolution

```
</details>

### Induced

<details>
```yaml
name: AgendaItem
description: '[en] An agenda item of a meeting.

  [de] Ein Traktandum einer Sitzung.

  '
from_schema: https://ch.paf.link/schema/operations
mixins:
- HasIdentification
- IsEventWithDuration
- HasCreationModificationDates
attributes:
  parent_meeting:
    name: parent_meeting
    description: '[en] The linked meeting ID that groups the current meeting.

      [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: parent_meeting
    owner: AgendaItem
    domain_of:
    - Meeting
    - AgendaItem
    - Voting
    - Election
    range: string
  agenda_item_type:
    name: agenda_item_type
    description: '[en] Type of agenda item, distinguishing individual items from groups.

      [de] Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: agenda_item_type
    owner: AgendaItem
    domain_of:
    - AgendaItem
    range: agenda_item_type_enum
  agenda_item_number:
    name: agenda_item_number
    description: '[en] Sequential number of the agenda item (string type to support
      roman numerals).

      [de] Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern).

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: agenda_item_number
    owner: AgendaItem
    domain_of:
    - AgendaItem
    range: string
  agenda_item_position:
    name: agenda_item_position
    description: '[en] Integer position of the agenda item in the meeting sequence.

      [de] Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: agenda_item_position
    owner: AgendaItem
    domain_of:
    - AgendaItem
    range: integer
  leading_actor_id:
    name: leading_actor_id
    description: '[en] The leading department for the agenda item.

      [de] Das federführende Departement für den Tagesordnungspunkt.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: leading_actor_id
    owner: AgendaItem
    domain_of:
    - AgendaItem
    range: string
  speaking_actor_id:
    name: speaking_actor_id
    description: '[en] The speaker or head of the department for the agenda item.

      [de] Der Sprecher oder Departementsvorsteher für den Tagesordnungspunkt.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: speaking_actor_id
    owner: AgendaItem
    domain_of:
    - AgendaItem
    range: string
  agenda_item_title:
    name: agenda_item_title
    description: '[en] Title of the agenda item.

      [de] Titel des Traktandums.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: agenda_item_title
    owner: AgendaItem
    domain_of:
    - AgendaItem
    range: MultilingualString
    multivalued: true
    inlined: true
    inlined_as_list: true
  affair_id:
    name: affair_id
    description: '[en] The connection to the affairs (business items) of the agenda
      item.

      [de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: affair_id
    owner: AgendaItem
    domain_of:
    - AgendaItem
    - Voting
    - Election
    range: string
  agenda_item_description:
    name: agenda_item_description
    description: '[en] Subtitle or detailed description of the agenda item.

      [de] Untertitel oder ausführliche Beschreibung des Traktandums.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: agenda_item_description
    owner: AgendaItem
    domain_of:
    - AgendaItem
    range: MultilingualString
    multivalued: true
    inlined: true
    inlined_as_list: true
  state_id:
    name: state_id
    description: State identifier (reference to state enum or custom state)
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: state_id
    owner: AgendaItem
    domain_of:
    - AgendaItem
    range: string
  state_name:
    name: state_name
    description: '[en] Custom state description for the meeting.

      [de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: state_name
    owner: AgendaItem
    domain_of:
    - Meeting
    - AgendaItem
    range: string
  landing_page:
    name: landing_page
    description: '[en] URL providing further information.

      [de] URL mit weiteren Informationen.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: ops:landingPage
    alias: landing_page
    owner: AgendaItem
    domain_of:
    - Legislature
    - Meeting
    - AgendaItem
    - Voting
    - Election
    - Speech
    range: string
  url:
    name: url
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: url
    owner: AgendaItem
    domain_of:
    - Session
    - Meeting
    - AgendaItem
    - Media
    range: MultilingualString
    multivalued: true
    inlined: true
    inlined_as_list: true
  agenda_item_category:
    name: agenda_item_category
    description: '[en] Category for grouped agenda items (e.g., introduction, by department,
      technical agenda items).

      [de] Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement,
      technische Traktanden).

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: agenda_item_category
    owner: AgendaItem
    domain_of:
    - AgendaItem
    range: string
  parent_agenda_item:
    name: parent_agenda_item
    description: '[en] If needed, this slot builds a hierarchy of agenda items.

      [de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten
      auf.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: parent_agenda_item
    owner: AgendaItem
    domain_of:
    - AgendaItem
    - Voting
    - Election
    range: string
  has_resolution:
    name: has_resolution
    description: '[en] The resolutionor decision taken on this agenda item.

      [de] Die Resolution oder Entscheidung zu diesem Traktandum.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    alias: has_resolution
    owner: AgendaItem
    domain_of:
    - AgendaItem
    range: Resolution
  local_id:
    name: local_id
    description: '[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

      [en] Local identifier. For example, a UUID from the council information system.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:localId
    alias: local_id
    owner: AgendaItem
    domain_of:
    - HasIdentification
    range: string
  global_uri:
    name: global_uri
    description: '[de] Eine eindeutige, global gültige URI für die Entität.

      [en] A unique, globally valid URI for the entity.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:globalURI
    identifier: true
    alias: global_uri
    owner: AgendaItem
    domain_of:
    - HasIdentification
    range: uriorcurie
    required: true
  wikidata_uri:
    name: wikidata_uri
    description: '[de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39
      für die Schweiz.

      [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39
      for Switzerland.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:wikidataUri
    alias: wikidata_uri
    owner: AgendaItem
    domain_of:
    - HasIdentification
    range: uriorcurie
  date_begin_actual:
    name: date_begin_actual
    description: '[de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens
      mit Zeitdauer.

      [en] The actual start date of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateBeginActual
    alias: date_begin_actual
    owner: AgendaItem
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_begin_actual:
    name: datetime_begin_actual
    description: '[de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses
      oder Vorkommens mit Zeitdauer.

      [en] The actual start date and time of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeBeginActual
    alias: datetime_begin_actual
    owner: AgendaItem
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_begin_planned:
    name: date_begin_planned
    description: '[de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit
      Zeitdauer.

      [en] The planned start date of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateBeginPlanned
    alias: date_begin_planned
    owner: AgendaItem
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_begin_planned:
    name: datetime_begin_planned
    description: '[de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder
      Vorkommens mit Zeitdauer.

      [en] The planned start date and time of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeBeginPlanned
    alias: datetime_begin_planned
    owner: AgendaItem
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_end_actual:
    name: date_end_actual
    description: '[de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens
      mit Zeitdauer.

      [en] The actual end date of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateEndActual
    alias: date_end_actual
    owner: AgendaItem
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_end_actual:
    name: datetime_end_actual
    description: '[de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses
      oder Vorkommens mit Zeitdauer.

      [en] The actual end date and time of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeEndActual
    alias: datetime_end_actual
    owner: AgendaItem
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_end_planned:
    name: date_end_planned
    description: '[de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit
      Zeitdauer.

      [en] The planned end date of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateEndPlanned
    alias: date_end_planned
    owner: AgendaItem
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_end_planned:
    name: datetime_end_planned
    description: '[de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder
      Vorkommens mit Zeitdauer.

      [en] The planned end date and time of an event or occurrence with time duration.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeEndPlanned
    alias: datetime_end_planned
    owner: AgendaItem
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_created:
    name: date_created
    description: '[de] Das Datum, an dem eine Entität erstellt wurde.

      [en] The date when an entity was created.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateCreated
    alias: date_created
    owner: AgendaItem
    domain_of:
    - HasCreationModificationDates
    range: date
  datetime_created:
    name: datetime_created
    description: '[de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.

      [en] The date and time when an entity was created.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeCreated
    alias: datetime_created
    owner: AgendaItem
    domain_of:
    - HasCreationModificationDates
    range: datetime
  date_modified:
    name: date_modified
    description: '[de] Das Datum, an dem eine Entität zuletzt geändert wurde.

      [en] The date when an entity was last modified.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:dateModified
    alias: date_modified
    owner: AgendaItem
    domain_of:
    - HasCreationModificationDates
    range: date
  datetime_modified:
    name: datetime_modified
    description: '[de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert
      wurde.

      [en] The date and time when an entity was last modified.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:datetimeModified
    alias: datetime_modified
    owner: AgendaItem
    domain_of:
    - HasCreationModificationDates
    range: datetime

```
</details>