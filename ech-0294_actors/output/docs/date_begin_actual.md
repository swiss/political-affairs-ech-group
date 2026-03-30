

# Slot: date_begin_actual 


_[de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer._

_[en] The actual start date of an event or occurrence with time duration._

__





URI: [mcm:dateBeginActual](https://ld.ech.ch/schema/0292/meta-common/dateBeginActual)
Alias: date_begin_actual

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder V... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [IsEventWithDuration](IsEventWithDuration.md) |
| Slot URI | [mcm:dateBeginActual](https://ld.ech.ch/schema/0292/meta-common/dateBeginActual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:dateBeginActual |
| native | act:date_begin_actual |




## LinkML Source

<details>
```yaml
name: date_begin_actual
description: '[de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit
  Zeitdauer.

  [en] The actual start date of an event or occurrence with time duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateBeginActual
alias: date_begin_actual
domain_of:
- IsEventWithDuration
range: date

```
</details>