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
  description_fr:
    tag: description_fr
    value: 'La date et l''heure planifiées d''un événement ou d''une occurrence instantané
      (sans durée).

      '
description: 'The planned date and time of an instantaneous event or occurrence (without
  time duration).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimePlanned
domain_of:
- IsInstantaneousEvent
range: datetime

```
</details></div>