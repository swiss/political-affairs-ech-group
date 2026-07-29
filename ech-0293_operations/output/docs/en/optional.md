---
search:
  boost: 5.0
---

# Slot: optional 


_Indicates if the meeting or voting is optional._




<div data-search-exclude markdown="1">



URI: [ops:optional](https://ch.paf.link/schema/operations/optional)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Voting](Voting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: optional
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Sitzung oder Abstimmung optional ist.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si la séance ou le vote est facultatif.

      '
description: 'Indicates if the meeting or voting is optional.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: boolean

```
</details></div>