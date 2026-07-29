---
search:
  boost: 5.0
---

# Slot: text_format 


_Format du texte (text, html, html_with_timestamps)._




<div data-search-exclude markdown="1">



URI: [ops:text_format](https://ch.paf.link/schema/operations/text_format)
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
| html |





## Source LinkML

<details>
```yaml
name: text_format
annotations:
  description_de:
    tag: description_de
    value: 'Format des Textes (text, html, html_with_timestamps).

      '
  description_fr:
    tag: description_fr
    value: 'Format du texte (text, html, html_with_timestamps).

      '
description: 'Format du texte (text, html, html_with_timestamps).

  '
examples:
- value: html
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>