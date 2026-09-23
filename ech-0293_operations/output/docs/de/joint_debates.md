---
search:
  boost: 5.0
---

# Slot: joint_debates 


_An diesem Eintrag angehängte gemeinsame Beratungen: bei einem Traktandum die Beratungen, in denen es zusammen mit anderen Traktanden behandelt wird; bei einer Sitzung oder Session die darin geführten gemeinsamen Beratungen._




<div data-search-exclude markdown="1">



URI: [ops:jointDebate](https://ch.paf.link/schema/operations/jointDebate)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Session: eine zusammenhängende Sitzungsperiode innerhalb einer Legislatu... |  no  |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |  no  |
| [AgendaItem](AgendaItem.md) | Ein vorgängig geplantes Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [JointDebate](JointDebate.md) |
| Domäne von | [Session](Session.md), [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md) |
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
description: 'An diesem Eintrag angehängte gemeinsame Beratungen: bei einem Traktandum
  die Beratungen, in denen es zusammen mit anderen Traktanden behandelt wird; bei
  einer Sitzung oder Session die darin geführten gemeinsamen Beratungen.

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