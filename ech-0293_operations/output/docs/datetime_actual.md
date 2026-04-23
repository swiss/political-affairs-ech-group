

# Slot: datetime_actual 


_[de] Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses oder Vorkommens (ohne Zeitdauer)._

_[en] The actual date and time of an instantaneous event or occurrence (without time duration)._

__





URI: [mcm:datetimeActual](https://ld.ech.ch/schema/0292/meta-common/datetimeActual)
Alias: datetime_actual

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereign... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [IsInstantaneousEvent](IsInstantaneousEvent.md) |
| Slot URI | [mcm:datetimeActual](https://ld.ech.ch/schema/0292/meta-common/datetimeActual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:datetimeActual |
| native | ops:datetime_actual |




## LinkML Source

<details>
```yaml
name: datetime_actual
description: '[de] Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses
  oder Vorkommens (ohne Zeitdauer).

  [en] The actual date and time of an instantaneous event or occurrence (without time
  duration).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:datetimeActual
alias: datetime_actual
domain_of:
- IsInstantaneousEvent
range: datetime

```
</details>