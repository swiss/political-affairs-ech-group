---
search:
  boost: 5.0
---

# Slot: remark 


_Free-text remark or note for edge cases or additional context on a process step or an entity._

__



<div data-search-exclude markdown="1">



URI: [mcm:remark](https://ld.ech.ch/schema/0292/meta-common/remark)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [IsProcessStep](IsProcessStep.md) |
| Slot-URI | [mcm:remark](https://ld.ech.ch/schema/0292/meta-common/remark) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: remark
annotations:
  description_de:
    tag: description_de
    value: 'Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext
      zu einem Prozessschritt oder einer Entität.

      '
description: 'Free-text remark or note for edge cases or additional context on a process
  step or an entity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:remark
domain_of:
- IsProcessStep
range: string

```
</details></div>