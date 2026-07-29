---
search:
  boost: 5.0
---

# Slot: id 


_Identifiant univoque de l'élément._




<div data-search-exclude markdown="1">



URI: [ops:id](https://ch.paf.link/schema/operations/id)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work : le document abstrait en tant que tel, indépendamment d'une versio... |  no  |
| [Expression](Expression.md) | FRBR Expression : une version linguistique concrète d'un Work |  no  |
| [Manifestation](Manifestation.md) | FRBR Manifestation : une forme de fichier concrète d'une Expression, adressab... |  no  |
| [WorkContainer](WorkContainer.md) | Conteneur pour les documents (FRBR Works) de ce schéma |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Work](Work.md), [Expression](Expression.md), [Manifestation](Manifestation.md), [WorkContainer](WorkContainer.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Requis | Yes |
### Caractéristiques du slot

| Propriété | Valeur |
| --- | --- |
| Identifiant | Yes |














## Source LinkML

<details>
```yaml
name: id
annotations:
  description_de:
    tag: description_de
    value: 'Eindeutiger Identifikator des Elements.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant univoque de l''élément.

      '
description: 'Identifiant univoque de l''élément.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
identifier: true
domain_of:
- Work
- Expression
- Manifestation
- WorkContainer
range: string
required: true

```
</details></div>