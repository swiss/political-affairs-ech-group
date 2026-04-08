---
search:
  boost: 5.0
---

# Slot: date_actual 


_[de] Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommens (ohne Zeitdauer)._

_[en] The actual date of an instantaneous event or occurrence (without time duration)._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateActual](https://ld.ech.ch/schema/0292/meta-common/dateActual)
Alias: date_actual

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
| Slot URI | [mcm:dateActual](https://ld.ech.ch/schema/0292/meta-common/dateActual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:dateActual |
| native | act:date_actual |




## LinkML Source

<details>
```yaml
name: date_actual
description: '[de] Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommens
  (ohne Zeitdauer).

  [en] The actual date of an instantaneous event or occurrence (without time duration).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateActual
alias: date_actual
domain_of:
- IsInstantaneousEvent
range: date

```
</details></div>