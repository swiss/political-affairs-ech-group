---
search:
  boost: 5.0
---

# Slot: datetime_planned 


_[de] Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vorkommens (ohne Zeitdauer)._

_[en] The planned date and time of an instantaneous event or occurrence (without time duration)._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimePlanned](https://ld.ech.ch/schema/0292/meta-common/datetimePlanned)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereign... |  no  |






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
description: '[de] Das geplante Datum und die Uhrzeit eines instantanen Ereignisses
  oder Vorkommens (ohne Zeitdauer).

  [en] The planned date and time of an instantaneous event or occurrence (without
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