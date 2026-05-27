---
search:
  boost: 5.0
---

# Slot: remark 


_[de] Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext zu einem Prozessschritt oder einer Entität._

_[en] Free-text remark or note for edge cases or additional context on a process step or an entity._

__



<div data-search-exclude markdown="1">



URI: [mcm:remark](https://ld.ech.ch/schema/0292/meta-common/remark)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsProcessStep](IsProcessStep.md) | [de] Eine Mixin-Klasse für einen einzelnen Schritt in einem |  no  |






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
description: '[de] Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen
  Kontext zu einem Prozessschritt oder einer Entität.

  [en] Free-text remark or note for edge cases or additional context on a process
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