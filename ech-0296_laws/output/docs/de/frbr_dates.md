---
search:
  boost: 5.0
---

# Slot: frbr_dates 


_Datumseinträge dieser FRBR-Entität (akn:FRBRdate). Mehrere Einträge für verschiedene Ereignistypen._




<div data-search-exclude markdown="1">



URI: [laws:frbr_dates](https://ld.ech.ch/schema/0296/laws/frbr_dates)
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
| Wertebereich | [FRBRDate](FRBRDate.md) |
| Domäne von | [FRBRWork](FRBRWork.md), [FRBRExpression](FRBRExpression.md), [FRBRManifestation](FRBRManifestation.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: frbr_dates
annotations:
  description_de:
    tag: description_de
    value: 'Datumseinträge dieser FRBR-Entität (akn:FRBRdate). Mehrere Einträge für
      verschiedene Ereignistypen.

      '
description: 'Datumseinträge dieser FRBR-Entität (akn:FRBRdate). Mehrere Einträge
  für verschiedene Ereignistypen.

  '
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FRBRWork
- FRBRExpression
- FRBRManifestation
range: FRBRDate
multivalued: true

```
</details></div>