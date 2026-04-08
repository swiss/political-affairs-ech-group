---
search:
  boost: 10.0
---

# Class: IsEventWithDuration 


_[de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder Vorkommnissen mit Zeitdauer zur Verfügung stellt._

_[en] A mixin class that provides slots for modeling events or occurrences with time duration._

__



<div data-search-exclude markdown="1">



URI: [act:IsEventWithDuration](https://ld.ech.ch/schema/0294/actors/IsEventWithDuration)




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [date_begin_actual](date_begin_actual.md) | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit Zeitda... | direct |
| [datetime_begin_actual](datetime_begin_actual.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorko... | direct |
| [date_begin_planned](date_begin_planned.md) | 0..1 <br/> [Date](Date.md) | [de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer | direct |
| [datetime_begin_planned](datetime_begin_planned.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommen... | direct |
| [date_end_actual](date_end_actual.md) | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens mit Zeitdaue... | direct |
| [datetime_end_actual](datetime_end_actual.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkomm... | direct |
| [date_end_planned](date_end_planned.md) | 0..1 <br/> [Date](Date.md) | [de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer | direct |
| [datetime_end_planned](datetime_end_planned.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens ... | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |














## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:IsEventWithDuration |
| native | act:IsEventWithDuration |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IsEventWithDuration
description: '[de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen
  oder Vorkommnissen mit Zeitdauer zur Verfügung stellt.

  [en] A mixin class that provides slots for modeling events or occurrences with time
  duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixin: true
slots:
- date_begin_actual
- datetime_begin_actual
- date_begin_planned
- datetime_begin_planned
- date_end_actual
- datetime_end_actual
- date_end_planned
- datetime_end_planned

```
</details>

### Induced

<details>
```yaml
name: IsEventWithDuration
description: '[de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen
  oder Vorkommnissen mit Zeitdauer zur Verfügung stellt.

  [en] A mixin class that provides slots for modeling events or occurrences with time
  duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixin: true
attributes:
  date_begin_actual:
    name: date_begin_actual
    description: '[de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens
      mit Zeitdauer.

      [en] The actual start date of an event or occurrence with time duration.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:dateBeginActual
    alias: date_begin_actual
    owner: IsEventWithDuration
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_begin_actual:
    name: datetime_begin_actual
    description: '[de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses
      oder Vorkommens mit Zeitdauer.

      [en] The actual start date and time of an event or occurrence with time duration.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:datetimeBeginActual
    alias: datetime_begin_actual
    owner: IsEventWithDuration
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_begin_planned:
    name: date_begin_planned
    description: '[de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit
      Zeitdauer.

      [en] The planned start date of an event or occurrence with time duration.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:dateBeginPlanned
    alias: date_begin_planned
    owner: IsEventWithDuration
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_begin_planned:
    name: datetime_begin_planned
    description: '[de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder
      Vorkommens mit Zeitdauer.

      [en] The planned start date and time of an event or occurrence with time duration.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:datetimeBeginPlanned
    alias: datetime_begin_planned
    owner: IsEventWithDuration
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_end_actual:
    name: date_end_actual
    description: '[de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens
      mit Zeitdauer.

      [en] The actual end date of an event or occurrence with time duration.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:dateEndActual
    alias: date_end_actual
    owner: IsEventWithDuration
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_end_actual:
    name: datetime_end_actual
    description: '[de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses
      oder Vorkommens mit Zeitdauer.

      [en] The actual end date and time of an event or occurrence with time duration.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:datetimeEndActual
    alias: datetime_end_actual
    owner: IsEventWithDuration
    domain_of:
    - IsEventWithDuration
    range: datetime
  date_end_planned:
    name: date_end_planned
    description: '[de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit
      Zeitdauer.

      [en] The planned end date of an event or occurrence with time duration.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:dateEndPlanned
    alias: date_end_planned
    owner: IsEventWithDuration
    domain_of:
    - IsEventWithDuration
    range: date
  datetime_end_planned:
    name: datetime_end_planned
    description: '[de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder
      Vorkommens mit Zeitdauer.

      [en] The planned end date and time of an event or occurrence with time duration.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:datetimeEndPlanned
    alias: datetime_end_planned
    owner: IsEventWithDuration
    domain_of:
    - IsEventWithDuration
    range: datetime

```
</details></div>