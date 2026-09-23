---
search:
  boost: 5.0
---

# Slot: joint_debates 


_Délibérations communes dans lesquelles ce point de l'ordre du jour est traité conjointement avec d'autres points._




<div data-search-exclude markdown="1">



URI: [ops:jointDebate](https://ch.paf.link/schema/operations/jointDebate)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [JointDebate](JointDebate.md) |
| Domaine de | [IsAgendaItem](IsAgendaItem.md) |
| URI du slot | [ops:jointDebate](https://ch.paf.link/schema/operations/jointDebate) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: joint_debates
annotations:
  description_de:
    tag: description_de
    value: 'Gemeinsame Beratungen, in denen dieses Traktandum zusammen mit anderen
      Traktanden behandelt wird.

      '
  description_fr:
    tag: description_fr
    value: 'Délibérations communes dans lesquelles ce point de l''ordre du jour est
      traité conjointement avec d''autres points.

      '
description: 'Délibérations communes dans lesquelles ce point de l''ordre du jour
  est traité conjointement avec d''autres points.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:jointDebate
domain_of:
- IsAgendaItem
range: JointDebate
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>