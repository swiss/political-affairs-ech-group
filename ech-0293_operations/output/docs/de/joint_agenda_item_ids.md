---
search:
  boost: 5.0
---

# Slot: joint_agenda_item_ids 


_Identifikatoren der gemeinsam behandelten Traktanden (AgendaItem oder ProtocolItem)._




<div data-search-exclude markdown="1">



URI: [ops:jointAgendaItem](https://ch.paf.link/schema/operations/jointAgendaItem)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [JointDebate](JointDebate.md) | Eine gemeinsame Beratung: Mehrere Traktanden werden zusammen behandelt |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [JointDebate](JointDebate.md) |
| Slot-URI | [ops:jointAgendaItem](https://ch.paf.link/schema/operations/jointAgendaItem) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: joint_agenda_item_ids
annotations:
  description_de:
    tag: description_de
    value: 'Identifikatoren der gemeinsam behandelten Traktanden (AgendaItem oder
      ProtocolItem).

      '
  description_fr:
    tag: description_fr
    value: 'Identifiants des points de l''ordre du jour traités conjointement (AgendaItem
      ou ProtocolItem).

      '
description: 'Identifikatoren der gemeinsam behandelten Traktanden (AgendaItem oder
  ProtocolItem).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:jointAgendaItem
domain_of:
- JointDebate
range: string
multivalued: true

```
</details></div>