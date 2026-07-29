---
search:
  boost: 5.0
---

# Slot: is_active 


_Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist._




<div data-search-exclude markdown="1">



URI: [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [HasTemporalValidity](HasTemporalValidity.md) | Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Boolean](Boolean.md) |
| Domäne von | [HasTemporalValidity](HasTemporalValidity.md) |
| Slot-URI | [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: is_active
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn
      diese Information explizit vorhanden ist.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si l''information est actuellement valable. Peut être utile lorsque
      cette information est explicitement disponible.

      '
description: 'Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein,
  wenn diese Information explizit vorhanden ist.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:isCurrent
domain_of:
- HasTemporalValidity
range: boolean

```
</details></div>