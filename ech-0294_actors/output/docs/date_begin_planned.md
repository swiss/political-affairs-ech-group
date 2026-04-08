---
search:
  boost: 5.0
---

# Slot: date_begin_planned 


_[de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer._

_[en] The planned start date of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateBeginPlanned](https://ld.ech.ch/schema/0292/meta-common/dateBeginPlanned)
Alias: date_begin_planned

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
| Slot URI | [mcm:dateBeginPlanned](https://ld.ech.ch/schema/0292/meta-common/dateBeginPlanned) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:dateBeginPlanned |
| native | act:date_begin_planned |




## LinkML Source

<details>
```yaml
name: date_begin_planned
description: '[de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer.

  [en] The planned start date of an event or occurrence with time duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateBeginPlanned
alias: date_begin_planned
domain_of:
- IsEventWithDuration
range: date

```
</details></div>