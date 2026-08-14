---
search:
  boost: 5.0
---

# Slot: frbr_authors 


_Autoren-/Rechteinhaber-Einträge dieser FRBR-Entität (akn:FRBRauthor)._



<div data-search-exclude markdown="1">



URI: [laws:frbr_authors](https://ld.ech.ch/schema/0296/laws/frbr_authors)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FRBRWork](FRBRWork.md) | FRBR-Work-Ebene (akn:FRBRWork): der abstrakte Erlass unabhängig von Sprache u... |  no  |
| [FRBRExpression](FRBRExpression.md) | FRBR-Expression-Ebene (akn:FRBRExpression): eine sprachspezifische Version de... |  no  |
| [FRBRManifestation](FRBRManifestation.md) | FRBR-Manifestations-Ebene (akn:FRBRManifestation): ein spezifisches Dateiform... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [FRBRAuthor](FRBRAuthor.md) |
| Domäne von | [FRBRWork](FRBRWork.md), [FRBRExpression](FRBRExpression.md), [FRBRManifestation](FRBRManifestation.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: frbr_authors
annotations:
  description_de:
    tag: description_de
    value: Autoren-/Rechteinhaber-Einträge dieser FRBR-Entität (akn:FRBRauthor).
description: Autoren-/Rechteinhaber-Einträge dieser FRBR-Entität (akn:FRBRauthor).
from_schema: https://ld.ech.ch/schema/0296/laws
close_mappings:
- eli:passed_by
rank: 1000
domain_of:
- FRBRWork
- FRBRExpression
- FRBRManifestation
range: FRBRAuthor
multivalued: true

```
</details></div>