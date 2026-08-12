---
search:
  boost: 5.0
---

# Slot: value 


_Generisches Wert-Attribut (@value), in mehreren AkomaNtoso-Elementen verwendet._



<div data-search-exclude markdown="1">



URI: [laws:value](https://ld.ech.ch/schema/0296/laws/value)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FRBRName](FRBRName.md) | Ein mehrsprachiger Namenseintrag des FRBR-Works (akn:FRBRname) |  no  |
| [ValueType](ValueType.md) | Einfacher Halter mit einem einzelnen @value-Attribut (AKN valueType) |  no  |
| [FormatType](FormatType.md) | Halter für akn:FRBRformat: ein @value (typischerweise 'xml') plus das optiona... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [FRBRName](FRBRName.md), [ValueType](ValueType.md), [FormatType](FormatType.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: value
annotations:
  description_de:
    tag: description_de
    value: Generisches Wert-Attribut (@value), in mehreren AkomaNtoso-Elementen verwendet.
  xml_attribute:
    tag: xml_attribute
    value: 'true'
description: Generisches Wert-Attribut (@value), in mehreren AkomaNtoso-Elementen
  verwendet.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FRBRName
- ValueType
- FormatType
range: string

```
</details></div>