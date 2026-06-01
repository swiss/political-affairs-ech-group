---
search:
  boost: 5.0
---

# Slot: date_end_planned 


_The planned end date of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateEndPlanned](https://ld.ech.ch/schema/0292/meta-common/dateEndPlanned)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | A mixin class that provides slots for modeling events or occurrences with tim... |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |






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
annotations:
  description_de:
    tag: description_de
    value: 'Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

      '
description: 'The planned end date of an event or occurrence with time duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateEndPlanned
domain_of:
- IsEventWithDuration
range: date

```
</details></div>