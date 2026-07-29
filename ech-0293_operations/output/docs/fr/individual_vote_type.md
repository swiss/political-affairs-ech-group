---
search:
  boost: 5.0
---

# Slot: individual_vote_type 


_Type de voix exprimée (oui, non, abstention, n'a pas voté, etc.)._




<div data-search-exclude markdown="1">



URI: [ops:individual_vote_type](https://ch.paf.link/schema/operations/individual_vote_type)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | Une voix individuelle exprimée par un membre lors d'une procédure de vote |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) |
| Domaine de | [IndividualVote](IndividualVote.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| abstention |
| no |
| not_voted |





## Source LinkML

<details>
```yaml
name: individual_vote_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc.).

      '
  description_fr:
    tag: description_fr
    value: 'Type de voix exprimée (oui, non, abstention, n''a pas voté, etc.).

      '
description: 'Type de voix exprimée (oui, non, abstention, n''a pas voté, etc.).

  '
examples:
- value: abstention
- value: 'no'
- value: not_voted
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: IndividualVoteTypeEnum

```
</details></div>