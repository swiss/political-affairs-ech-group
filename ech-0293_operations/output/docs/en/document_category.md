---
search:
  boost: 5.0
---

# Slot: document_category 


_Category of the document. If not set, 'other' is automatically used._




<div data-search-exclude markdown="1">



URI: [meta:documentCategory](https://ch.paf.link/schema/meta/documentCategory)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work: the abstract document as such, independent of a concrete language ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DocumentCategoryEnum](DocumentCategoryEnum.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [meta:documentCategory](https://ch.paf.link/schema/meta/documentCategory) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `string(other)` |














## LinkML Source

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
description: 'Category of the document. If not set, ''other'' is automatically used.

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