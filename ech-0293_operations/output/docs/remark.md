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





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [IsProcessStep](IsProcessStep.md) |
| Slot URI | [mcm:remark](https://ld.ech.ch/schema/0292/meta-common/remark) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: remark
annotations:
  description_de:
    tag: description_de
    value: 'Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext
      zu einem Prozessschritt oder einer Entität.

      '
  description_fr:
    tag: description_fr
    value: 'Remarque ou note en texte libre pour les cas particuliers ou pour un contexte
      supplémentaire relatif à une étape de processus ou à une entité.

      '
description: 'Free-text remark or note for edge cases or additional context on a process
  step or an entity.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:remark
domain_of:
- IsProcessStep
range: string

```
</details></div>