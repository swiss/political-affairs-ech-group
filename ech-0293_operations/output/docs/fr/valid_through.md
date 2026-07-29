---
search:
  boost: 5.0
---

# Slot: valid_through 


_La date jusqu'à laquelle l'information est valable, incluse._




<div data-search-exclude markdown="1">



URI: [schema:validThrough](http://schema.org/validThrough)
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
| URI du slot | [schema:validThrough](http://schema.org/validThrough) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: valid_through
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, bis und mit dem die Information gültig ist.

      '
  description_fr:
    tag: description_fr
    value: 'La date jusqu''à laquelle l''information est valable, incluse.

      '
description: 'La date jusqu''à laquelle l''information est valable, incluse.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: schema:validThrough
domain_of:
- HasTemporalValidity
range: date

```
</details></div>