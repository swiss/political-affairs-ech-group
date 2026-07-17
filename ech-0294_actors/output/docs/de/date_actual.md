---
search:
  boost: 5.0
---

# Slot: date_actual 


_Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommnissen (ohne Zeitdauer)._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateActual](https://ld.ech.ch/schema/0292/meta-common/dateActual)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereignissen... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Date](Date.md) |
| Domäne von | [IsInstantaneousEvent](IsInstantaneousEvent.md) |
| Slot-URI | [mcm:dateActual](https://ld.ech.ch/schema/0292/meta-common/dateActual) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: date_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommnissen
      (ohne Zeitdauer).

      '
  description_fr:
    tag: description_fr
    value: 'La date effective d''un événement ou d''une occurrence instantané (sans
      durée).

      '
description: 'Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommnissen
  (ohne Zeitdauer).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateActual
domain_of:
- IsInstantaneousEvent
range: date

```
</details></div>