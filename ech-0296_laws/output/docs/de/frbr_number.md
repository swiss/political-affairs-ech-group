---
search:
  boost: 5.0
---

# Slot: frbr_number 


_SR-Nummer (akn:FRBRnumber/@value), z.B. '101'._



<div data-search-exclude markdown="1">



URI: [eli:number](http://data.europa.eu/eli/ontology#number)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FRBRWork](FRBRWork.md) | FRBR-Work-Ebene (akn:FRBRWork): der abstrakte Erlass unabhängig von Sprache u... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [ValueType](ValueType.md) |
| Domäne von | [FRBRWork](FRBRWork.md) |
| Slot-URI | [eli:number](http://data.europa.eu/eli/ontology#number) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: frbr_number
annotations:
  description_de:
    tag: description_de
    value: SR-Nummer (akn:FRBRnumber/@value), z.B. '101'.
  xml_element:
    tag: xml_element
    value: akn:FRBRnumber
description: SR-Nummer (akn:FRBRnumber/@value), z.B. '101'.
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:FRBRnumber
rank: 1000
slot_uri: eli:number
domain_of:
- FRBRWork
range: ValueType

```
</details></div>