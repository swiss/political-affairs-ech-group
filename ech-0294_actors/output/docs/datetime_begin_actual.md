

# Slot: datetime_begin_actual 


_[de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer._

_[en] The actual start date and time of an event or occurrence with time duration._

__





URI: [mcm:datetimeBeginActual](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginActual)
Alias: datetime_begin_actual

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder V... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [IsEventWithDuration](IsEventWithDuration.md) |
| Slot URI | [mcm:datetimeBeginActual](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginActual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:datetimeBeginActual |
| native | act:datetime_begin_actual |




## LinkML Source

<details>
```yaml
name: datetime_begin_actual
description: '[de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder
  Vorkommens mit Zeitdauer.

  [en] The actual start date and time of an event or occurrence with time duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimeBeginActual
alias: datetime_begin_actual
domain_of:
- IsEventWithDuration
range: datetime

```
</details>