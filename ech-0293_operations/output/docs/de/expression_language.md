---
search:
  boost: 5.0
---

# Slot: expression_language 


_Sprachcode im ISO 639-1-Format._




<div data-search-exclude markdown="1">



URI: [dcterms:language](http://purl.org/dc/terms/language)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Expression](Expression.md) | FRBR Expression: eine konkrete Sprachfassung eines Works |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Expression](Expression.md) |
| Slot-URI | [dcterms:language](http://purl.org/dc/terms/language) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Erforderlich | Yes |
### Wertebeschränkungen

| Eigenschaft | Wert |
| --- | --- |
| Regex Pattern | `^[a-z]{2}$` |














## LinkML-Quelle

<details>
```yaml
name: expression_language
annotations:
  description_de:
    tag: description_de
    value: 'Sprachcode im ISO 639-1-Format.

      '
  description_fr:
    tag: description_fr
    value: 'Code de langue au format ISO 639-1.

      '
description: 'Sprachcode im ISO 639-1-Format.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: dcterms:language
domain_of:
- Expression
range: string
required: true
pattern: ^[a-z]{2}$

```
</details></div>