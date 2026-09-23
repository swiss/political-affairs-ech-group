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
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [Protocol](Protocol.md) | Le procès-verbal établi après la séance |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [TextSegment](TextSegment.md) |
| Domaine de | [IsAgendaItem](IsAgendaItem.md), [Protocol](Protocol.md) |
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
- IsAgendaItem
- Protocol
range: TextSegment
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>