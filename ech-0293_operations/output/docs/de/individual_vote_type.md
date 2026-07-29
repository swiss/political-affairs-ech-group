---
search:
  boost: 5.0
---

# Slot: individual_vote_type 


_Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc.)._




<div data-search-exclude markdown="1">



URI: [ops:individual_vote_type](https://ch.paf.link/schema/operations/individual_vote_type)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) |
| Domäne von | [IndividualVote](IndividualVote.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| abstention |
| no |
| not_voted |





## LinkML-Quelle

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
description: 'Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt,
  etc.).

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