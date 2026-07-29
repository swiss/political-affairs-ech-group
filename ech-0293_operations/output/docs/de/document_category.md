---
search:
  boost: 5.0
---

# Slot: document_category 


_Kategorie des Dokuments. Wenn nicht gesetzt, wird automatisch 'other' verwendet._




<div data-search-exclude markdown="1">



URI: [meta:documentCategory](https://ch.paf.link/schema/meta/documentCategory)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [DocumentCategoryEnum](DocumentCategoryEnum.md) |
| Domäne von | [Work](Work.md) |
| Slot-URI | [meta:documentCategory](https://ch.paf.link/schema/meta/documentCategory) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
### Slot-Eigenschaften

| Eigenschaft | Wert |
| --- | --- |
| If Absent | `string(other)` |














## LinkML-Quelle

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
description: 'Kategorie des Dokuments. Wenn nicht gesetzt, wird automatisch ''other''
  verwendet.

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