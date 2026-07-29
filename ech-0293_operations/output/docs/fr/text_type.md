---
search:
  boost: 5.0
---

# Slot: text_type 


_Type de texte (version brute, version éditée)._




<div data-search-exclude markdown="1">



URI: [ops:text_type](https://ch.paf.link/schema/operations/text_type)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Speech](Speech.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| final |





## Source LinkML

<details>
```yaml
name: text_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ des Textes (Rohfassung, bearbeitete Fassung).

      '
  description_fr:
    tag: description_fr
    value: 'Type de texte (version brute, version éditée).

      '
description: 'Type de texte (version brute, version éditée).

  '
examples:
- value: final
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>