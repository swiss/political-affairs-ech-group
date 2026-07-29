---
search:
  boost: 5.0
---

# Slot: voting_type 


_Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc.)._




<div data-search-exclude markdown="1">



URI: [ops:voting_type](https://ch.paf.link/schema/operations/voting_type)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [VotingTypeEnum](VotingTypeEnum.md) |
| Domäne von | [Voting](Voting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| final_vote |
| other |
| preliminary_vote |





## LinkML-Quelle

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
description: 'Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim,
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