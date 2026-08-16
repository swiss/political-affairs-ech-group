---
search:
  boost: 5.0
---

# Slot: frbr_language 


_Sprachcode dieser Expression (akn:FRBRlanguage/@language)._



<div data-search-exclude markdown="1">



URI: [eli:language](http://data.europa.eu/eli/ontology#language)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [FRBRExpression](FRBRExpression.md) | FRBR-Expression-Ebene (akn:FRBRExpression): eine sprachspezifische Version de... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [LanguageType](LanguageType.md) |
| Domäne von | [FRBRExpression](FRBRExpression.md) |
| Slot-URI | [eli:language](http://data.europa.eu/eli/ontology#language) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: frbr_language
annotations:
  description_de:
    tag: description_de
    value: Sprachcode dieser Expression (akn:FRBRlanguage/@language).
  xml_element:
    tag: xml_element
    value: akn:FRBRlanguage
description: Sprachcode dieser Expression (akn:FRBRlanguage/@language).
from_schema: https://ld.ech.ch/schema/0296/laws
exact_mappings:
- akn:FRBRlanguage
rank: 1000
slot_uri: eli:language
domain_of:
- FRBRExpression
range: LanguageType

```
</details></div>