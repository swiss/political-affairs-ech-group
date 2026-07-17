---
search:
  boost: 5.0
---

# Slot: date_planned 


_The planned date of an instantaneous event or occurrence (without time duration)._

__



<div data-search-exclude markdown="1">



URI: [mcm:datePlanned](https://ld.ech.ch/schema/0292/meta-common/datePlanned)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | A mixin class that provides slots for modeling instantaneous events or occurr... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Date](Date.md) |
| Domäne von | [IsInstantaneousEvent](IsInstantaneousEvent.md) |
| Slot-URI | [mcm:datePlanned](https://ld.ech.ch/schema/0292/meta-common/datePlanned) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: date_planned
annotations:
  description_de:
    tag: description_de
    value: 'Das geplante Datum eines instantanen Ereignisses oder Vorkommnissen (ohne
      Zeitdauer).

      '
description: 'The planned date of an instantaneous event or occurrence (without time
  duration).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datePlanned
domain_of:
- IsInstantaneousEvent
range: date

```
</details></div>