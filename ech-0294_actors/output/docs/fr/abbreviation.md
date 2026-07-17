---
search:
  boost: 5.0
---

# Slot: abbreviation 


_Abréviation (peut être multilingue)._

__



<div data-search-exclude markdown="1">



URI: [mcm:abbreviation](https://ld.ech.ch/schema/0292/meta-common/abbreviation)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |  no  |
| [GroupReference](GroupReference.md) | Référence légère à un groupe avec les principales données d'identification au... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [MultilingualValue](MultilingualValue.md) |
| Domaine de | [Group](Group.md), [GroupReference](GroupReference.md) |
| URI du slot | [mcm:abbreviation](https://ld.ech.ch/schema/0292/meta-common/abbreviation) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: abbreviation
annotations:
  description_de:
    tag: description_de
    value: 'Abkürzung (kann mehrsprachig sein).

      '
  description_fr:
    tag: description_fr
    value: 'Abréviation (peut être multilingue).

      '
description: 'Abréviation (peut être multilingue).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:abbreviation
domain_of:
- Group
- GroupReference
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>