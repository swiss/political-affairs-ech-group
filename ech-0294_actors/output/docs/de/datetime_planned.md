---
search:
  boost: 5.0
---

# Slot: datetime_planned 


_Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vorkommnissen (ohne Zeitdauer)._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimePlanned](https://ld.ech.ch/schema/0292/meta-common/datetimePlanned)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereignissen... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Datetime](Datetime.md) |
| Domäne von | [IsInstantaneousEvent](IsInstantaneousEvent.md) |
| Slot-URI | [mcm:datetimePlanned](https://ld.ech.ch/schema/0292/meta-common/datetimePlanned) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder
  Vorkommnissen (ohne Zeitdauer).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimePlanned
domain_of:
- IsInstantaneousEvent
range: datetime

```
</details></div>