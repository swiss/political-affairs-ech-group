---
search:
  boost: 5.0
---

# Slot: type_label 


_Custom type label when standard type values don't apply._




<div data-search-exclude markdown="1">



URI: [ops:type_label](https://ch.paf.link/schema/operations/type_label)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resolution](Resolution.md) | A resolution or decision taken on an agenda item, including voting procedures |  no  |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [IndividualVote](IndividualVote.md) | An individual vote cast by a member during a voting procedure |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Resolution](Resolution.md), [Voting](Voting.md), [IndividualVote](IndividualVote.md), [Election](Election.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: type_label
annotations:
  description_de:
    tag: description_de
    value: 'Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.

      '
  description_fr:
    tag: description_fr
    value: 'Libellé de type personnalisé lorsque les valeurs de type standard ne s''appliquent
      pas.

      '
description: 'Custom type label when standard type values don''t apply.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Resolution
- Voting
- IndividualVote
- Election
range: string

```
</details></div>