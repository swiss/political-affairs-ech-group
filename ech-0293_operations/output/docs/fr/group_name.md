---
search:
  boost: 5.0
---

# Slot: group_name 


_Nom du groupe ou de l'organe en clair, en complément de la référence `group_id`._




<div data-search-exclude markdown="1">



URI: [ops:group_name](https://ch.paf.link/schema/operations/group_name)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |






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
name: group_name
annotations:
  description_de:
    tag: description_de
    value: 'Name der Gruppe oder des Gremiums im Klartext, zusätzlich zur Referenz
      `group_id`.

      '
  description_fr:
    tag: description_fr
    value: 'Nom du groupe ou de l''organe en clair, en complément de la référence
      `group_id`.

      '
description: 'Nom du groupe ou de l''organe en clair, en complément de la référence
  `group_id`.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>