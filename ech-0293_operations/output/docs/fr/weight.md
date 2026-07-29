---
search:
  boost: 5.0
---

# Slot: weight 


_Le nombre de voix dont dispose la personne, le cas échéant (p. ex. lorsqu'une personne détient plusieurs voix)._




<div data-search-exclude markdown="1">



URI: [ops:weight](https://ch.paf.link/schema/operations/weight)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | Une voix individuelle exprimée par un membre lors d'une procédure de vote |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Integer](Integer.md) |
| Domaine de | [IndividualVote](IndividualVote.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: weight
annotations:
  description_de:
    tag: description_de
    value: 'Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B.
      in Fällen, in denen eine Person mehrere Stimmen hat).

      '
  description_fr:
    tag: description_fr
    value: 'Le nombre de voix dont dispose la personne, le cas échéant (p. ex. lorsqu''une
      personne détient plusieurs voix).

      '
description: 'Le nombre de voix dont dispose la personne, le cas échéant (p. ex. lorsqu''une
  personne détient plusieurs voix).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: integer

```
</details></div>