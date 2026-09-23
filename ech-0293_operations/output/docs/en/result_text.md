---
search:
  boost: 5.0
---

# Slot: result_text 


_Free text describing the outcome, e.g. "Accepted with 120 to 75 votes with 5 abstentions". For votings, the categorical decision (accepted, rejected, noted …) is not recorded here but in the Resolution (resolution_type) of the agenda item._




<div data-search-exclude markdown="1">



URI: [ops:result_text](https://ch.paf.link/schema/operations/result_text)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  no  |
| [Election](Election.md) | An election in which a parliamentary body appoints one or several persons to ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Voting](Voting.md), [Election](Election.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25, Auswahl C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern). |
| Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen |
| Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt |





## LinkML Source

<details>
```yaml
name: result_text
annotations:
  description_de:
    tag: description_de
    value: 'Freitext, der das Ergebnis beschreibt, z.B. „Mit 120 zu 75 Stimmen bei
      5 Enthaltungen angenommen“. Bei Abstimmungen wird der kategorische Entscheid
      (angenommen, abgelehnt, Kenntnisnahme …) nicht hier, sondern in der Resolution
      (resolution_type) des Traktandums festgehalten.

      '
  description_fr:
    tag: description_fr
    value: 'Texte libre décrivant le résultat, p. ex. « Adopté par 120 voix contre
      75 et 5 abstentions ». Pour les votes, la décision catégorielle (adopté, rejeté,
      pris acte …) n''est pas retenue ici, mais dans la Resolution (resolution_type)
      du point de l''ordre du jour.

      '
description: 'Free text describing the outcome, e.g. "Accepted with 120 to 75 votes
  with 5 abstentions". For votings, the categorical decision (accepted, rejected,
  noted …) is not recorded here but in the Resolution (resolution_type) of the agenda
  item.

  '
examples:
- value: 'Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25,
    Auswahl C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern).'
- value: Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen
- value: Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: string

```
</details></div>