---
search:
  boost: 5.0
---

# Slot: is_active 


_Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible._




<div data-search-exclude markdown="1">



URI: [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [HasTemporalValidity](HasTemporalValidity.md) | Une classe mixin qui fournit des slots pour modéliser la validité temporelle ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Boolean](Boolean.md) |
| Domaine de | [HasTemporalValidity](HasTemporalValidity.md) |
| URI du slot | [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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
description: 'Indique si l''information est actuellement valable. Peut être utile
  lorsque cette information est explicitement disponible.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:isCurrent
domain_of:
- HasTemporalValidity
range: boolean

```
</details></div>