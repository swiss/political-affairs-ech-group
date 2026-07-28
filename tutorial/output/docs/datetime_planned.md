---
search:
  boost: 5.0
---

# Slot: datetime_planned 


_The planned date and time of an instantaneous event or occurrence (without time duration)._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimePlanned](https://ld.ech.ch/schema/0292/meta-common/datetimePlanned)
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
| Slot URI | [mcm:datetimePlanned](https://ld.ech.ch/schema/0292/meta-common/datetimePlanned) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: datetime_planned
annotations:
  description_de:
    tag: description_de
    value: 'Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder
      Vorkommnissen (ohne Zeitdauer).

      '
description: 'The planned date and time of an instantaneous event or occurrence (without
  time duration).

  '
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: mcm:datetimePlanned
domain_of:
- IsInstantaneousEvent
range: datetime

```
</details></div>