---
search:
  boost: 5.0
---

# Slot: text_segments 


_Ensemble de segments de texte (p. ex. procès-verbal in extenso)._




<div data-search-exclude markdown="1">



URI: [ops:textSegment](https://ch.paf.link/schema/operations/textSegment)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Protocol](Protocol.md) | Le procès-verbal établi après la séance |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [TextSegment](TextSegment.md) |
| Domaine de | [Protocol](Protocol.md) |
| URI du slot | [ops:textSegment](https://ch.paf.link/schema/operations/textSegment) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: text_segments
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung von Textsegmenten (z.B. Wortprotokoll).

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble de segments de texte (p. ex. procès-verbal in extenso).

      '
description: 'Ensemble de segments de texte (p. ex. procès-verbal in extenso).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:textSegment
domain_of:
- Protocol
range: TextSegment
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>