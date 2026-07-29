---
search:
  boost: 5.0
---

# Slot: title 


_Titre de l'élément._




<div data-search-exclude markdown="1">



URI: [ops:title](https://ch.paf.link/schema/operations/title)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [Motion](Motion.md) | Une proposition formelle déposée au cours des délibérations |  no  |
| [Media](Media.md) | Fichiers médias ou documents (y compris les procès-verbaux en PDF/HTML/WORD o... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Election](Election.md), [Motion](Motion.md), [Media](Media.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: title
annotations:
  description_de:
    tag: description_de
    value: 'Titel des Elements.

      '
  description_fr:
    tag: description_fr
    value: 'Titre de l''élément.

      '
description: 'Titre de l''élément.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Election
- Motion
- Media
range: string

```
</details></div>