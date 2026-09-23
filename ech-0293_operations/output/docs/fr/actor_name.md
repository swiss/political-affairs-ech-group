---
search:
  boost: 5.0
---

# Slot: actor_name 


_Nom de l'organe politique en clair (p. ex. Conseil national), en complément de la référence `actor_id`._




<div data-search-exclude markdown="1">



URI: [ops:actor_name](https://ch.paf.link/schema/operations/actor_name)
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
name: actor_name
annotations:
  description_de:
    tag: description_de
    value: 'Name des politischen Organs im Klartext (z.B. Nationalrat), zusätzlich
      zur Referenz `actor_id`.

      '
  description_fr:
    tag: description_fr
    value: 'Nom de l''organe politique en clair (p. ex. Conseil national), en complément
      de la référence `actor_id`.

      '
description: 'Nom de l''organe politique en clair (p. ex. Conseil national), en complément
  de la référence `actor_id`.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>