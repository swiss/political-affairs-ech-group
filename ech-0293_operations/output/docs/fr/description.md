---
search:
  boost: 5.0
---

# Slot: description 


_Texte descriptif de l'élément._




<div data-search-exclude markdown="1">



URI: [ops:description](https://ch.paf.link/schema/operations/description)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |
| [Motion](Motion.md) | Une proposition formelle déposée au cours des délibérations |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Legislature](Legislature.md), [Meeting](Meeting.md), [Motion](Motion.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: description
annotations:
  description_de:
    tag: description_de
    value: 'Beschreibender Text zum Element.

      '
  description_fr:
    tag: description_fr
    value: 'Texte descriptif de l''élément.

      '
description: 'Texte descriptif de l''élément.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Meeting
- Motion
range: string

```
</details></div>