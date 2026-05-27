---
search:
  boost: 5.0
---

# Slot: date_end_planned 


_[de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer._

_[en] The planned end date of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateEndPlanned](https://ld.ech.ch/schema/0292/meta-common/dateEndPlanned)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder V... |  no  |
| [IsProcessStep](IsProcessStep.md) | [de] Eine Mixin-Klasse für einen einzelnen Schritt in einem |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [IsEventWithDuration](IsEventWithDuration.md) |
| Slot URI | [mcm:dateEndPlanned](https://ld.ech.ch/schema/0292/meta-common/dateEndPlanned) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: date_end_planned
description: '[de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer.

  [en] The planned end date of an event or occurrence with time duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateEndPlanned
domain_of:
- IsEventWithDuration
range: date

```
</details></div>