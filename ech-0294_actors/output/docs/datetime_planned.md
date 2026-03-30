

# Slot: datetime_planned 


_[de] Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vorkommens (ohne Zeitdauer)._

_[en] The planned date and time of an instantaneous event or occurrence (without time duration)._

__





URI: [mcm:datetimePlanned](https://ld.ech.ch/schema/0292/meta-common/datetimePlanned)
Alias: datetime_planned

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
| Slot URI | [mcm:datetimePlanned](https://ld.ech.ch/schema/0292/meta-common/datetimePlanned) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:datetimePlanned |
| native | act:datetime_planned |




## LinkML Source

<details>
```yaml
name: datetime_planned
description: '[de] Das geplante Datum und die Uhrzeit eines instantanen Ereignisses
  oder Vorkommens (ohne Zeitdauer).

  [en] The planned date and time of an instantaneous event or occurrence (without
  time duration).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimePlanned
alias: datetime_planned
domain_of:
- IsInstantaneousEvent
range: datetime

```
</details>