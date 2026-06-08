---
search:
  boost: 5.0
---

# Slot: optional 


_[en] Indicates if the meeting or voting is optional._

_[de] Gibt an, ob die Sitzung oder Abstimmung optional ist._

__



<div data-search-exclude markdown="1">



URI: [ops:optional](https://ch.paf.link/schema/operations/optional)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |






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
description: '[en] Indicates if the meeting or voting is optional.

  [de] Gibt an, ob die Sitzung oder Abstimmung optional ist.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: boolean

```
</details></div>