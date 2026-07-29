---
search:
  boost: 5.0
---

# Slot: expression_language 


_Code de langue au format ISO 639-1._




<div data-search-exclude markdown="1">



URI: [dcterms:language](http://purl.org/dc/terms/language)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Expression](Expression.md) | FRBR Expression : une version linguistique concrète d'un Work |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Expression](Expression.md) |
| URI du slot | [dcterms:language](http://purl.org/dc/terms/language) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Requis | Yes |
### Contraintes de valeur

| Propriété | Valeur |
| --- | --- |
| Regex Pattern | `^[a-z]{2}$` |














## Source LinkML

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
description: 'Code de langue au format ISO 639-1.

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