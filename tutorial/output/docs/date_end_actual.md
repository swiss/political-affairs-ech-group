---
search:
  boost: 5.0
---

# Slot: date_end_actual 


_The actual end date of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateEndActual](https://ld.ech.ch/schema/0292/meta-common/dateEndActual)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) |  |  no  |
| [IsEventWithDuration](IsEventWithDuration.md) | A mixin class that provides slots for modeling events or occurrences with tim... |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Session](Session.md), [IsEventWithDuration](IsEventWithDuration.md) |
| Slot URI | [mcm:dateEndActual](https://ld.ech.ch/schema/0292/meta-common/dateEndActual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_de | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.
 |




### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:dateEndActual |
| native | tutorial:date_end_actual |




## LinkML Source

<details>
```yaml
name: date_end_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

      '
description: 'The actual end date of an event or occurrence with time duration.

  '
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: mcm:dateEndActual
domain_of:
- Session
- IsEventWithDuration
range: date

```
</details></div>