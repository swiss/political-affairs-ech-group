---
search:
  boost: 5.0
---

# Slot: agenda_items 


_Ensemble des points de l'ordre du jour._




<div data-search-exclude markdown="1">



URI: [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |  no  |
| [JointDebate](JointDebate.md) | Points de l'ordre du jour traités conjointement |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [AgendaItem](AgendaItem.md) |
| Domaine de | [Container](Container.md), [JointDebate](JointDebate.md) |
| URI du slot | [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

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
description: 'Ensemble des points de l''ordre du jour.

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