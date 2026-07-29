---
search:
  boost: 5.0
---

# Slot: valid_from 


_La date à partir de laquelle l'information est valable._




<div data-search-exclude markdown="1">



URI: [schema:validFrom](http://schema.org/validFrom)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [HasTemporalValidity](HasTemporalValidity.md) | Une classe mixin qui fournit des slots pour modéliser la validité temporelle ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Date](Date.md) |
| Domaine de | [HasTemporalValidity](HasTemporalValidity.md) |
| URI du slot | [schema:validFrom](http://schema.org/validFrom) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: valid_from
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, ab dem die Information gültig ist.

      '
  description_fr:
    tag: description_fr
    value: 'La date à partir de laquelle l''information est valable.

      '
description: 'La date à partir de laquelle l''information est valable.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: schema:validFrom
domain_of:
- HasTemporalValidity
range: date

```
</details></div>