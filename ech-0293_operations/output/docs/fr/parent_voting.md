---
search:
  boost: 5.0
---

# Slot: parent_voting 


_L'identifiant du vote auquel se rattache la voix individuelle._




<div data-search-exclude markdown="1">



URI: [ops:parentVoting](https://ch.paf.link/schema/operations/parentVoting)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | Une voix individuelle exprimée par un membre lors d'une procédure de vote |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Voting](Voting.md) |
| Domaine de | [IndividualVote](IndividualVote.md) |
| URI du slot | [ops:parentVoting](https://ch.paf.link/schema/operations/parentVoting) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: parent_voting
annotations:
  description_de:
    tag: description_de
    value: 'Die ID der Abstimmung, die mit der Einzelstimme verbunden ist.

      '
  description_fr:
    tag: description_fr
    value: 'L''identifiant du vote auquel se rattache la voix individuelle.

      '
description: 'L''identifiant du vote auquel se rattache la voix individuelle.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:parentVoting
domain_of:
- IndividualVote
range: Voting

```
</details></div>