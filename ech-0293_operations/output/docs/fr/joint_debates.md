---
search:
  boost: 5.0
---

# Slot: joint_debates 


_Délibérations communes rattachées à cet enregistrement : pour un point de l'ordre du jour, les délibérations dans lesquelles il est traité conjointement avec d'autres points ; pour une séance ou une session, les délibérations communes qui s'y tiennent._




<div data-search-exclude markdown="1">



URI: [ops:jointDebate](https://ch.paf.link/schema/operations/jointDebate)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance, tel que planifié à l'avance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [JointDebate](JointDebate.md) |
| Domaine de | [Session](Session.md), [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md) |
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
    value: 'An diesem Eintrag angehängte gemeinsame Beratungen: bei einem Traktandum
      die Beratungen, in denen es zusammen mit anderen Traktanden behandelt wird;
      bei einer Sitzung oder Session die darin geführten gemeinsamen Beratungen.

      '
  description_fr:
    tag: description_fr
    value: 'Délibérations communes rattachées à cet enregistrement : pour un point
      de l''ordre du jour, les délibérations dans lesquelles il est traité conjointement
      avec d''autres points ; pour une séance ou une session, les délibérations communes
      qui s''y tiennent.

      '
description: 'Délibérations communes rattachées à cet enregistrement : pour un point
  de l''ordre du jour, les délibérations dans lesquelles il est traité conjointement
  avec d''autres points ; pour une séance ou une session, les délibérations communes
  qui s''y tiennent.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:jointDebate
domain_of:
- Session
- Meeting
- IsAgendaItem
range: JointDebate
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>