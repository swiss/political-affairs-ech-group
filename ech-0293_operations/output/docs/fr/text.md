---
search:
  boost: 5.0
---

# Slot: text 


_Contenu textuel de l'élément._




<div data-search-exclude markdown="1">



URI: [ops:text](https://ch.paf.link/schema/operations/text)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |
| [TextSegment](TextSegment.md) | Un segment de texte tel qu'un renvoi ou un intertitre dans un procès-verbal d... |  no  |
| [MultilingualString](MultilingualString.md) | Une chaîne de caractères pouvant contenir du texte en plusieurs langues |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Speech](Speech.md), [TextSegment](TextSegment.md), [MultilingualString](MultilingualString.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Requis | Yes |












## Source LinkML

<details>
```yaml
name: text
annotations:
  description_de:
    tag: description_de
    value: 'Textinhalt des Elements.

      '
  description_fr:
    tag: description_fr
    value: 'Contenu textuel de l''élément.

      '
description: 'Contenu textuel de l''élément.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
- TextSegment
- MultilingualString
range: string
required: true

```
</details></div>