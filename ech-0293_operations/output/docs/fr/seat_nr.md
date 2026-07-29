---
search:
  boost: 5.0
---

# Slot: seat_nr 


_Le numéro de siège correspondant à la voix individuelle, le cas échéant._




<div data-search-exclude markdown="1">



URI: [ops:seat_nr](https://ch.paf.link/schema/operations/seat_nr)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | Une voix individuelle exprimée par un membre lors d'une procédure de vote |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [IndividualVote](IndividualVote.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: seat_nr
annotations:
  description_de:
    tag: description_de
    value: 'Die Sitznummer der Einzelstimme, falls zutreffend.

      '
  description_fr:
    tag: description_fr
    value: 'Le numéro de siège correspondant à la voix individuelle, le cas échéant.

      '
description: 'Le numéro de siège correspondant à la voix individuelle, le cas échéant.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: string

```
</details></div>