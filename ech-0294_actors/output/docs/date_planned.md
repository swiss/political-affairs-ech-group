

# Slot: date_planned 


_[de] Das geplante Datum eines instantanen Ereignisses oder Vorkommens (ohne Zeitdauer)._

_[en] The planned date of an instantaneous event or occurrence (without time duration)._

__





URI: [mcm:datePlanned](https://ld.ech.ch/schema/0292/meta-common/datePlanned)
Alias: date_planned

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereign... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [IsInstantaneousEvent](IsInstantaneousEvent.md) |
| Slot URI | [mcm:datePlanned](https://ld.ech.ch/schema/0292/meta-common/datePlanned) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:datePlanned |
| native | act:date_planned |




## LinkML Source

<details>
```yaml
name: date_planned
description: '[de] Das geplante Datum eines instantanen Ereignisses oder Vorkommens
  (ohne Zeitdauer).

  [en] The planned date of an instantaneous event or occurrence (without time duration).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datePlanned
alias: date_planned
domain_of:
- IsInstantaneousEvent
range: date

```
</details>