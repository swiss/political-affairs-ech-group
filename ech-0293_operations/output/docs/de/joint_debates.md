---
search:
  boost: 5.0
---

# Slot: joint_debates 


_Gemeinsame Beratungen, in denen dieses Traktandum zusammen mit anderen Traktanden behandelt wird._




<div data-search-exclude markdown="1">



URI: [ops:jointDebate](https://ch.paf.link/schema/operations/jointDebate)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |  no  |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [JointDebate](JointDebate.md) |
| Domäne von | [IsAgendaItem](IsAgendaItem.md) |
| Slot-URI | [ops:jointDebate](https://ch.paf.link/schema/operations/jointDebate) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

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
description: 'Gemeinsame Beratungen, in denen dieses Traktandum zusammen mit anderen
  Traktanden behandelt wird.

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