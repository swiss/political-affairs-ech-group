---
search:
  boost: 5.0
---

# Slot: show_as 


_Lesbare Anzeigebezeichnung einer TLC-Referenz (@showAs)._



<div data-search-exclude markdown="1">



URI: [laws:show_as](https://ld.ech.ch/schema/0296/laws/show_as)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TLCOrganization](TLCOrganization.md) | Eine benannte Organisation als Referenz im Dokument (akn:TLCOrganization) |  no  |
| [TLCRole](TLCRole.md) | Eine benannte Rolle als Referenz im Dokument (akn:TLCRole) |  no  |
| [TLCReference](TLCReference.md) | Eine generische benannte Referenz im Dokument (akn:TLCReference) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [TLCOrganization](TLCOrganization.md), [TLCRole](TLCRole.md), [TLCReference](TLCReference.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: show_as
annotations:
  description_de:
    tag: description_de
    value: Lesbare Anzeigebezeichnung einer TLC-Referenz (@showAs).
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: showAs
description: Lesbare Anzeigebezeichnung einer TLC-Referenz (@showAs).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- TLCOrganization
- TLCRole
- TLCReference
range: string

```
</details></div>