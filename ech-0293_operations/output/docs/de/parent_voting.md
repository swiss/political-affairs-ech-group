---
search:
  boost: 5.0
---

# Slot: parent_voting 


_Die ID der Abstimmung, die mit der Einzelstimme verbunden ist._




<div data-search-exclude markdown="1">



URI: [ops:parentVoting](https://ch.paf.link/schema/operations/parentVoting)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Voting](Voting.md) |
| Domäne von | [IndividualVote](IndividualVote.md) |
| Slot-URI | [ops:parentVoting](https://ch.paf.link/schema/operations/parentVoting) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Die ID der Abstimmung, die mit der Einzelstimme verbunden ist.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:parentVoting
domain_of:
- IndividualVote
range: Voting

```
</details></div>