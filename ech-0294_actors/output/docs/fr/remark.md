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





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [IsProcessStep](IsProcessStep.md) |
| URI du slot | [mcm:remark](https://ld.ech.ch/schema/0292/meta-common/remark) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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