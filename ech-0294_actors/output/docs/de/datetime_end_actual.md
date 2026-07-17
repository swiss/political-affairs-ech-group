---
search:
  boost: 5.0
---

# Slot: datetime_end_actual 


_Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimeEndActual](https://ld.ech.ch/schema/0292/meta-common/datetimeEndActual)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder Vorkom... |  no  |
| [IsProcessStep](IsProcessStep.md) | Eine Mixin-Klasse für einen einzelnen Schritt in einem |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Datetime](Datetime.md) |
| Domäne von | [IsEventWithDuration](IsEventWithDuration.md), [IsProcessStep](IsProcessStep.md) |
| Slot-URI | [mcm:datetimeEndActual](https://ld.ech.ch/schema/0292/meta-common/datetimeEndActual) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: datetime_end_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
      mit Zeitdauer.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure de fin effectives d''un événement ou d''une occurrence
      avec durée.

      '
description: 'Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
  mit Zeitdauer.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimeEndActual
domain_of:
- IsEventWithDuration
- IsProcessStep
range: datetime

```
</details></div>