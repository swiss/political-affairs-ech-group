---
search:
  boost: 5.0
---

# Slot: media_format 


_Type MIME du fichier média._




<div data-search-exclude markdown="1">



URI: [ops:media_format](https://ch.paf.link/schema/operations/media_format)
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
| video/mp4 |





## Source LinkML

<details>
```yaml
name: media_format
annotations:
  description_de:
    tag: description_de
    value: 'MIME-Typ der Mediendatei.

      '
  description_fr:
    tag: description_fr
    value: 'Type MIME du fichier média.

      '
description: 'Type MIME du fichier média.

  '
examples:
- value: video/mp4
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>