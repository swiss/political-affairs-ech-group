---
search:
  boost: 5.0
---

# Slot: datetime_begin_actual 


_Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimeBeginActual](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginActual)
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
| Slot-URI | [mcm:datetimeBeginActual](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginActual) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: datetime_begin_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
      mit Zeitdauer.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure de début effectives d''un événement ou d''une occurrence
      avec durée.

      '
description: 'Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
  mit Zeitdauer.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimeBeginActual
domain_of:
- IsEventWithDuration
- IsProcessStep
range: datetime

```
</details></div>