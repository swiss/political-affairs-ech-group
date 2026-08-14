---
search:
  boost: 5.0
---

# Slot: frbr_format 


_Dateiformat dieser Manifestation (akn:FRBRformat/@value), typischerweise 'xml'._



<div data-search-exclude markdown="1">



URI: [laws:frbr_format](https://ld.ech.ch/schema/0296/laws/frbr_format)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FRBRManifestation](FRBRManifestation.md) | FRBR-Manifestations-Ebene (akn:FRBRManifestation): ein spezifisches Dateiform... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [FormatType](FormatType.md) |
| Domäne von | [FRBRManifestation](FRBRManifestation.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: frbr_format
annotations:
  description_de:
    tag: description_de
    value: Dateiformat dieser Manifestation (akn:FRBRformat/@value), typischerweise
      'xml'.
  xml_element:
    tag: xml_element
    value: akn:FRBRformat
description: Dateiformat dieser Manifestation (akn:FRBRformat/@value), typischerweise
  'xml'.
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:FRBRformat
close_mappings:
- eli:format
rank: 1000
domain_of:
- FRBRManifestation
range: FormatType

```
</details></div>