---
search:
  boost: 5.0
---

# Slot: agenda_items 


_Sammlung der Traktanden._




<div data-search-exclude markdown="1">



URI: [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |  no  |
| [JointDebate](JointDebate.md) | Traktanden die gemeinsam behandelt werden |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [AgendaItem](AgendaItem.md) |
| Domäne von | [Container](Container.md), [JointDebate](JointDebate.md) |
| Slot-URI | [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: agenda_items
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Traktanden.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des points de l''ordre du jour.

      '
description: 'Sammlung der Traktanden.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:agendaItem
domain_of:
- Container
- JointDebate
range: AgendaItem
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>