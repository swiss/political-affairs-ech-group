---
search:
  boost: 5.0
---

# Slot: result_text 


_[en] Free text describing the outcome of the vote, e.g., "Accepted with 78 votes"._

_[de] Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. "Mit 78 Stimmen angenommen"._

__



<div data-search-exclude markdown="1">



URI: [ops:result_text](https://ch.paf.link/schema/operations/result_text)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |






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
| Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen |
| Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt |
| Mit 78 zu 42 Stimmen bei 5 Enthaltungen angenommen |





## LinkML Source

<details>
```yaml
name: result_text
description: '[en] Free text describing the outcome of the vote, e.g., "Accepted with
  78 votes".

  [de] Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. "Mit 78 Stimmen
  angenommen".

  '
examples:
- value: Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen
- value: Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt
- value: Mit 78 zu 42 Stimmen bei 5 Enthaltungen angenommen
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: string

```
</details></div>