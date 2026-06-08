---
search:
  boost: 5.0
---

# Slot: total_other 


_[en] Used when multiple options are presented for voting (e.g., 5 buttons in Zurich)._

_[de] Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B. 5 Knöpfe in Zürich)._

__



<div data-search-exclude markdown="1">



URI: [ops:total_other](https://ch.paf.link/schema/operations/total_other)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |






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
description: '[en] Used when multiple options are presented for voting (e.g., 5 buttons
  in Zurich).

  [de] Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B.
  5 Knöpfe in Zürich).

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