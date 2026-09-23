---
search:
  boost: 5.0
---

# Slot: position 


_Position entière au sein de la séquence supérieure, p. ex. d'une session au sein de la législature._




<div data-search-exclude markdown="1">



URI: [ops:position](https://ch.paf.link/schema/operations/position)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Session](Session.md) | Une session : une période de séances continue au sein d'une législature |  no  |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: position
annotations:
  description_de:
    tag: description_de
    value: 'Ganzzahlige Position innerhalb der übergeordneten Reihenfolge, z.B. einer
      Session innerhalb der Legislaturperiode.

      '
  description_fr:
    tag: description_fr
    value: 'Position entière au sein de la séquence supérieure, p. ex. d''une session
      au sein de la législature.

      '
description: 'Position entière au sein de la séquence supérieure, p. ex. d''une session
  au sein de la législature.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>