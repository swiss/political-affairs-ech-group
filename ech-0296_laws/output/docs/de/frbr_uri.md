---
search:
  boost: 5.0
---

# Slot: frbr_uri 


_Basis-ELI-URI dieser FRBR-Entität (akn:FRBRuri/@value)._



<div data-search-exclude markdown="1">



URI: [laws:frbr_uri](https://ld.ech.ch/schema/0296/laws/frbr_uri)
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
| Wertebereich | [UriValueType](UriValueType.md) |
| Domäne von | [FRBRWork](FRBRWork.md), [FRBRExpression](FRBRExpression.md), [FRBRManifestation](FRBRManifestation.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: frbr_uri
annotations:
  description_de:
    tag: description_de
    value: Basis-ELI-URI dieser FRBR-Entität (akn:FRBRuri/@value).
  xml_element:
    tag: xml_element
    value: akn:FRBRuri
description: Basis-ELI-URI dieser FRBR-Entität (akn:FRBRuri/@value).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FRBRWork
- FRBRExpression
- FRBRManifestation
range: UriValueType

```
</details></div>