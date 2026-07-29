---
search:
  boost: 5.0
---

# Slot: datetime_end 


_The date and time when the meeting or voting ends._




<div data-search-exclude markdown="1">



URI: [ops:datetime_end](https://ch.paf.link/schema/operations/datetime_end)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: datetime_end
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure auxquelles la séance ou le vote se termine.

      '
description: 'The date and time when the meeting or voting ends.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
- Speech
range: datetime

```
</details></div>