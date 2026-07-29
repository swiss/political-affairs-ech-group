---
search:
  boost: 5.0
---

# Slot: date_end_actual 


_Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer._




<div data-search-exclude markdown="1">



URI: [mcm:dateEndActual](https://ld.ech.ch/schema/0292/meta-common/dateEndActual)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder Vorkom... |  no  |
| [IsProcessStep](IsProcessStep.md) | Eine Mixin-Klasse für einen einzelnen Schritt in einem |  no  |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |  no  |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Date](Date.md) |
| Domäne von | [IsEventWithDuration](IsEventWithDuration.md), [IsProcessStep](IsProcessStep.md) |
| Slot-URI | [mcm:dateEndActual](https://ld.ech.ch/schema/0292/meta-common/dateEndActual) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: date_end_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

      '
  description_fr:
    tag: description_fr
    value: 'La date de fin effective d''un événement ou d''une occurrence avec durée.

      '
description: 'Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:dateEndActual
domain_of:
- IsEventWithDuration
- IsProcessStep
range: date

```
</details></div>