---
search:
  boost: 5.0
---

# Slot: total_other 


_Vote counts for the options of a multiple-choice voting, one entry per option; used instead of total_count_yes, total_count_no and total_count_abstention (see TotalOther)._




<div data-search-exclude markdown="1">



URI: [ops:total_other](https://ch.paf.link/schema/operations/total_other)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TotalOther](TotalOther.md) |
| Domain Of | [Voting](Voting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: total_other
annotations:
  description_de:
    tag: description_de
    value: 'Stimmenzahlen für die Optionen einer Auswahlabstimmung, ein Eintrag pro
      Option; tritt an die Stelle von total_count_yes, total_count_no und total_count_abstention
      (siehe TotalOther).

      '
  description_fr:
    tag: description_fr
    value: 'Nombres de voix pour les options d''un vote à choix multiple, une entrée
      par option ; remplace total_count_yes, total_count_no et total_count_abstention
      (voir TotalOther).

      '
description: 'Vote counts for the options of a multiple-choice voting, one entry per
  option; used instead of total_count_yes, total_count_no and total_count_abstention
  (see TotalOther).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: TotalOther
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>