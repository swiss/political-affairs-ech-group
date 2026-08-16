---
search:
  boost: 5.0
---

# Slot: doc_name 


_Art des beiliegenden Dokuments (akn:doc/@name)._



<div data-search-exclude markdown="1">



URI: [laws:doc_name](https://ld.ech.ch/schema/0296/laws/doc_name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Doc](Doc.md) | Ein beiliegendes Dokument (akn:doc) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [DocNameEnum](DocNameEnum.md) |
| Domäne von | [Doc](Doc.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| annex |





## LinkML-Quelle

<details>
```yaml
name: doc_name
annotations:
  description_de:
    tag: description_de
    value: Art des beiliegenden Dokuments (akn:doc/@name).
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: name
description: Art des beiliegenden Dokuments (akn:doc/@name).
examples:
- value: annex
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Doc
range: DocNameEnum

```
</details></div>