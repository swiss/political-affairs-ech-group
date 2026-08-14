---
search:
  boost: 5.0
---

# Slot: xml_lang 


_XML-Sprachattribut (xml:lang), z.B. 'de', 'fr', 'it', 'rm', 'en'._



<div data-search-exclude markdown="1">



URI: [laws:xml_lang](https://ld.ech.ch/schema/0296/laws/xml_lang)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FRBRName](FRBRName.md) | Ein mehrsprachiger Namenseintrag des FRBR-Works (akn:FRBRname) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [FRBRName](FRBRName.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| de |
| en |
| fr |





## LinkML-Quelle

<details>
```yaml
name: xml_lang
annotations:
  description_de:
    tag: description_de
    value: XML-Sprachattribut (xml:lang), z.B. 'de', 'fr', 'it', 'rm', 'en'.
  xml_attribute:
    tag: xml_attribute
    value: 'true'
  xml_name:
    tag: xml_name
    value: xml:lang
description: XML-Sprachattribut (xml:lang), z.B. 'de', 'fr', 'it', 'rm', 'en'.
examples:
- value: de
- value: en
- value: fr
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- FRBRName
range: string

```
</details></div>