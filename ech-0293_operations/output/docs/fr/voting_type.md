---
search:
  boost: 5.0
---

# Slot: voting_type 


_Type de procédure de vote (vote intermédiaire, vote final, vote secret, etc.)._




<div data-search-exclude markdown="1">



URI: [ops:voting_type](https://ch.paf.link/schema/operations/voting_type)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [VotingTypeEnum](VotingTypeEnum.md) |
| Domaine de | [Voting](Voting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| final_vote |
| other |
| preliminary_vote |





## Source LinkML

<details>
```yaml
name: voting_type
annotations:
  description_de:
    tag: description_de
    value: 'Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc.).

      '
  description_fr:
    tag: description_fr
    value: 'Type de procédure de vote (vote intermédiaire, vote final, vote secret,
      etc.).

      '
description: 'Type de procédure de vote (vote intermédiaire, vote final, vote secret,
  etc.).

  '
examples:
- value: final_vote
- value: other
- value: preliminary_vote
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: VotingTypeEnum

```
</details></div>