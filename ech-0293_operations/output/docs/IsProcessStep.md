---
search:
  boost: 10.0
---

# Class: IsProcessStep 


_[de] Eine Mixin-Klasse für einen einzelnen Schritt in einem_

_mehrstufigen Prozess (z. B. Bearbeitungsschritt eines Geschäfts oder_

_Phasen­schritt einer Konsultation). Kombiniert Identifikations- und_

_Zeitdauer-Slots und ergänzt einen freien Bemerkungs-Slot. Konkrete_

_Step-Klassen ergänzen ihre eigenen typ-spezifischen Slots._

_[en] A mixin class for a single step in a multi-stage process (e.g.,_

_a deliberation step of an affair or a phase step of a consultation)._

_Combines identification and event-duration slots and adds a free-text_

_remark slot. Concrete step classes add their own type-specific slots._

__



<div data-search-exclude markdown="1">



URI: [ops:IsProcessStep](https://ch.paf.link/schema/operations/IsProcessStep)





```mermaid
 classDiagram
    class IsProcessStep
    click IsProcessStep href "../IsProcessStep/"
      HasIdentification <|-- IsProcessStep
        click HasIdentification href "../HasIdentification/"
      IsEventWithDuration <|-- IsProcessStep
        click IsEventWithDuration href "../IsEventWithDuration/"
      
      IsProcessStep : date_begin_actual
        
      IsProcessStep : date_begin_planned
        
      IsProcessStep : date_end_actual
        
      IsProcessStep : date_end_planned
        
      IsProcessStep : datetime_begin_actual
        
      IsProcessStep : datetime_begin_planned
        
      IsProcessStep : datetime_end_actual
        
      IsProcessStep : datetime_end_planned
        
      IsProcessStep : global_uri
        
      IsProcessStep : local_id
        
      IsProcessStep : remark
        
      IsProcessStep : wikidata_uri
        
      
```





## Inheritance
* **IsProcessStep** [ [HasIdentification](HasIdentification.md) [IsEventWithDuration](IsEventWithDuration.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [remark](remark.md) | 0..1 <br/> [String](String.md) | [de] Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext ... | direct |
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



## Mixin Usage

| mixed into | description |
| --- | --- |














## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:IsProcessStep |
| native | ops:IsProcessStep |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IsProcessStep
description: '[de] Eine Mixin-Klasse für einen einzelnen Schritt in einem

  mehrstufigen Prozess (z. B. Bearbeitungsschritt eines Geschäfts oder

  Phasen­schritt einer Konsultation). Kombiniert Identifikations- und

  Zeitdauer-Slots und ergänzt einen freien Bemerkungs-Slot. Konkrete

  Step-Klassen ergänzen ihre eigenen typ-spezifischen Slots.

  [en] A mixin class for a single step in a multi-stage process (e.g.,

  a deliberation step of an affair or a phase step of a consultation).

  Combines identification and event-duration slots and adds a free-text

  remark slot. Concrete step classes add their own type-specific slots.

  '
from_schema: https://ch.paf.link/schema/operations
mixin: true
mixins:
- HasIdentification
- IsEventWithDuration
slots:
- remark

```
</details>

### Induced

<details>
```yaml
name: IsProcessStep
description: '[de] Eine Mixin-Klasse für einen einzelnen Schritt in einem

  mehrstufigen Prozess (z. B. Bearbeitungsschritt eines Geschäfts oder

  Phasen­schritt einer Konsultation). Kombiniert Identifikations- und

  Zeitdauer-Slots und ergänzt einen freien Bemerkungs-Slot. Konkrete

  Step-Klassen ergänzen ihre eigenen typ-spezifischen Slots.

  [en] A mixin class for a single step in a multi-stage process (e.g.,

  a deliberation step of an affair or a phase step of a consultation).

  Combines identification and event-duration slots and adds a free-text

  remark slot. Concrete step classes add their own type-specific slots.

  '
from_schema: https://ch.paf.link/schema/operations
mixin: true
mixins:
- HasIdentification
- IsEventWithDuration
attributes:
  remark:
    name: remark
    description: '[de] Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen
      Kontext zu einem Prozessschritt oder einer Entität.

      [en] Free-text remark or note for edge cases or additional context on a process
      step or an entity.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:remark
    owner: IsProcessStep
    domain_of:
    - IsProcessStep
    range: string
  local_id:
    name: local_id
    description: '[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

      [en] Local identifier. For example, a UUID from the council information system.

      '
    from_schema: https://ch.paf.link/schema/operations
    rank: 1000
    slot_uri: mcm:localId
    owner: IsProcessStep
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
    owner: IsProcessStep
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
    owner: IsProcessStep
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
    owner: IsProcessStep
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
    owner: IsProcessStep
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
    owner: IsProcessStep
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
    owner: IsProcessStep
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
    owner: IsProcessStep
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
    owner: IsProcessStep
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
    owner: IsProcessStep
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
    owner: IsProcessStep
    domain_of:
    - IsEventWithDuration
    range: datetime

```
</details></div>