---
search:
  boost: 5.0
---

# Slot: dates 


_Dates relatives à l'élément, chacune assortie d'une indication de type._




<div data-search-exclude markdown="1">



URI: [meta:dates](https://ch.paf.link/schema/meta/dates)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Expression](Expression.md) | FRBR Expression : une version linguistique concrète d'un Work |  no  |
| [Manifestation](Manifestation.md) | FRBR Manifestation : une forme de fichier concrète d'une Expression, adressab... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Date](Date.md) |
| Domaine de | [Expression](Expression.md), [Manifestation](Manifestation.md) |
| URI du slot | [meta:dates](https://ch.paf.link/schema/meta/dates) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: dates
annotations:
  description_de:
    tag: description_de
    value: 'Datumsangaben zum Element, jeweils mit Typangabe.

      '
  description_fr:
    tag: description_fr
    value: 'Dates relatives à l''élément, chacune assortie d''une indication de type.

      '
description: 'Dates relatives à l''élément, chacune assortie d''une indication de
  type.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:dates
domain_of:
- Expression
- Manifestation
range: Date
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>