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





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | A mixin class that provides slots for modeling instantaneous events or occurr... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Datetime](Datetime.md) |
| Domäne von | [IsInstantaneousEvent](IsInstantaneousEvent.md) |
| Slot-URI | [mcm:datetimeActual](https://ld.ech.ch/schema/0292/meta-common/datetimeActual) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimeActual
domain_of:
- IsInstantaneousEvent
range: datetime

```
</details></div>