---
search:
  boost: 5.0
---

# Slot: date_begin_planned 


_The planned start date of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateBeginPlanned](https://ld.ech.ch/schema/0292/meta-common/dateBeginPlanned)
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
| Domain Of | [IsEventWithDuration](IsEventWithDuration.md), [IsProcessStep](IsProcessStep.md) |
| Slot URI | [mcm:dateBeginPlanned](https://ld.ech.ch/schema/0292/meta-common/dateBeginPlanned) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: date_begin_planned
annotations:
  description_de:
    tag: description_de
    value: 'Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

      '
  description_fr:
    tag: description_fr
    value: 'La date de début planifiée d''un événement ou d''une occurrence avec durée.

      '
description: 'The planned start date of an event or occurrence with time duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateBeginPlanned
domain_of:
- IsEventWithDuration
- IsProcessStep
range: date

```
</details></div>