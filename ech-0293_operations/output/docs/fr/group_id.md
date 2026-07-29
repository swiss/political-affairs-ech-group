---
search:
  boost: 5.0
---

# Slot: group_id 


_Référence au groupe ou à l'organe (instantané allégé au moment de la mise en relation)._




<div data-search-exclude markdown="1">



URI: [ops:group_id](https://ch.paf.link/schema/operations/group_id)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [GroupReference](GroupReference.md) |
| Domaine de | [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: group_id
annotations:
  description_de:
    tag: description_de
    value: 'Referenz auf die Gruppe oder das Gremium (leichtgewichtiger Snapshot zum
      Zeitpunkt der Verknüpfung).

      '
  description_fr:
    tag: description_fr
    value: 'Référence au groupe ou à l''organe (instantané allégé au moment de la
      mise en relation).

      '
description: 'Référence au groupe ou à l''organe (instantané allégé au moment de la
  mise en relation).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: GroupReference
inlined: true

```
</details></div>