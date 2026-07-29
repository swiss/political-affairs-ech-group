---
search:
  boost: 5.0
---

# Slot: document_category 


_Catégorie du document. Si elle n'est pas renseignée, la valeur 'other' est utilisée automatiquement._




<div data-search-exclude markdown="1">



URI: [meta:documentCategory](https://ch.paf.link/schema/meta/documentCategory)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work : le document abstrait en tant que tel, indépendamment d'une versio... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [DocumentCategoryEnum](DocumentCategoryEnum.md) |
| Domaine de | [Work](Work.md) |
| URI du slot | [meta:documentCategory](https://ch.paf.link/schema/meta/documentCategory) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
### Caractéristiques du slot

| Propriété | Valeur |
| --- | --- |
| If Absent | `string(other)` |














## Source LinkML

<details>
```yaml
name: document_category
annotations:
  description_de:
    tag: description_de
    value: 'Kategorie des Dokuments. Wenn nicht gesetzt, wird automatisch ''other''
      verwendet.

      '
  description_fr:
    tag: description_fr
    value: 'Catégorie du document. Si elle n''est pas renseignée, la valeur ''other''
      est utilisée automatiquement.

      '
description: 'Catégorie du document. Si elle n''est pas renseignée, la valeur ''other''
  est utilisée automatiquement.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:documentCategory
ifabsent: string(other)
domain_of:
- Work
range: DocumentCategoryEnum

```
</details></div>