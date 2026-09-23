---
search:
  boost: 5.0
---

# Slot: joint_agenda_item_ids 


_Identifiants des points de l'ordre du jour traités conjointement (AgendaItem ou ProtocolItem)._




<div data-search-exclude markdown="1">



URI: [ops:jointAgendaItem](https://ch.paf.link/schema/operations/jointAgendaItem)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [JointDebate](JointDebate.md) | Une délibération commune : plusieurs points de l'ordre du jour sont traités e... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [JointDebate](JointDebate.md) |
| URI du slot | [ops:jointAgendaItem](https://ch.paf.link/schema/operations/jointAgendaItem) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

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
description: 'Identifiants des points de l''ordre du jour traités conjointement (AgendaItem
  ou ProtocolItem).

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