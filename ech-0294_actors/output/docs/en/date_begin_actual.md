---
search:
  boost: 5.0
---

# Slot: date_begin_actual 


_The actual start date of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateBeginActual](https://ld.ech.ch/schema/0292/meta-common/dateBeginActual)
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
| Slot URI | [mcm:dateBeginActual](https://ld.ech.ch/schema/0292/meta-common/dateBeginActual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: date_begin_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

      '
  description_fr:
    tag: description_fr
    value: 'La date de début effective d''un événement ou d''une occurrence avec durée.

      '
description: 'The actual start date of an event or occurrence with time duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateBeginActual
domain_of:
- IsEventWithDuration
- IsProcessStep
range: date

```
</details></div>