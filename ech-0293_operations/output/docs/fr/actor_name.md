---
search:
  boost: 5.0
---

# Slot: actor_name 


_Nom de l'organe politique (p. ex. Conseil national)._




<div data-search-exclude markdown="1">



URI: [ops:actor_name](https://ch.paf.link/schema/operations/actor_name)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: actor_name
annotations:
  description_de:
    tag: description_de
    value: 'Name des politischen Organs (z.B. Nationalrat).

      '
  description_fr:
    tag: description_fr
    value: 'Nom de l''organe politique (p. ex. Conseil national).

      '
description: 'Nom de l''organe politique (p. ex. Conseil national).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>