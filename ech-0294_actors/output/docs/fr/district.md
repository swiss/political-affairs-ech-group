---
search:
  boost: 5.0
---

# Slot: district 


_Circonscription ou région électorale._

__



<div data-search-exclude markdown="1">



URI: [act:district](https://ld.ech.ch/schema/0294/actors/district)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [ElectoralDistrict](ElectoralDistrict.md) | Circonscription ou région électorale dans laquelle une personne est politique... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [ElectoralDistrict](ElectoralDistrict.md) |
| URI du slot | [act:district](https://ld.ech.ch/schema/0294/actors/district) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| Basel-Stadt |





## Source LinkML

<details>
```yaml
name: district
annotations:
  description_de:
    tag: description_de
    value: 'Wahlkreis oder Wahlregion.

      '
  description_fr:
    tag: description_fr
    value: 'Circonscription ou région électorale.

      '
description: 'Circonscription ou région électorale.

  '
examples:
- value: Basel-Stadt
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:district
domain_of:
- ElectoralDistrict
range: string

```
</details></div>