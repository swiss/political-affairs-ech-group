---
search:
  boost: 5.0
---

# Slot: name_attr 


_Das @name-Attribut auf akn:inline, z.B. 'man-font-style-normal'._



<div data-search-exclude markdown="1">



URI: [laws:name_attr](https://ld.ech.ch/schema/0296/laws/name_attr)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TLCReference](TLCReference.md) | Eine generische benannte Referenz im Dokument (akn:TLCReference) |  no  |
| [Inline](Inline.md) | Ein benanntes präsentationsbezogenes Inline (akn:inline), z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [TLCReference](TLCReference.md), [Inline](Inline.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: name_attr
annotations:
  description_de:
    tag: description_de
    value: Das @name-Attribut auf akn:inline, z.B. 'man-font-style-normal'.
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: name
description: Das @name-Attribut auf akn:inline, z.B. 'man-font-style-normal'.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- TLCReference
- Inline
range: string

```
</details></div>