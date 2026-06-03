---
search:
  boost: 5.0
---

# Slot: datetime_actual 


_The actual date and time of an instantaneous event or occurrence (without time duration)._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimeActual](https://ld.ech.ch/schema/0292/meta-common/datetimeActual)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | A mixin class that provides slots for modeling instantaneous events or occurr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [IsInstantaneousEvent](IsInstantaneousEvent.md) |
| Slot URI | [mcm:datetimeActual](https://ld.ech.ch/schema/0292/meta-common/datetimeActual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_de | Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses oder Vorkommnissen (ohne Zeitdauer).
 |




### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:datetimeActual |
| native | ops:datetime_actual |




## LinkML Source

<details>
```yaml
name: datetime_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses oder
      Vorkommnissen (ohne Zeitdauer).

      '
description: 'The actual date and time of an instantaneous event or occurrence (without
  time duration).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:datetimeActual
domain_of:
- IsInstantaneousEvent
range: datetime

```
</details></div>