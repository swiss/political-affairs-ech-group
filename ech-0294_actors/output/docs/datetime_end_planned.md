---
search:
  boost: 5.0
---

# Slot: datetime_end_planned 


_[de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer._

_[en] The planned end date and time of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimeEndPlanned](https://ld.ech.ch/schema/0292/meta-common/datetimeEndPlanned)
Alias: datetime_end_planned

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
| Slot URI | [mcm:datetimeEndPlanned](https://ld.ech.ch/schema/0292/meta-common/datetimeEndPlanned) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:datetimeEndPlanned |
| native | act:datetime_end_planned |




## LinkML Source

<details>
```yaml
name: datetime_end_planned
description: '[de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens
  mit Zeitdauer.

  [en] The planned end date and time of an event or occurrence with time duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimeEndPlanned
alias: datetime_end_planned
domain_of:
- IsEventWithDuration
range: datetime

```
</details></div>