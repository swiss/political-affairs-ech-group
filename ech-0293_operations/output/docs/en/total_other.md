---
search:
  boost: 5.0
---

# Slot: total_other 


_Used when multiple options are presented for voting (e.g., 5 buttons in Zurich)._




<div data-search-exclude markdown="1">



URI: [ops:total_other](https://ch.paf.link/schema/operations/total_other)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |






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
    value: 'Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B.
      5 Knöpfe in Zürich).

      '
  description_fr:
    tag: description_fr
    value: 'Utilisé lorsque plusieurs options sont soumises au vote (p. ex. 5 boutons
      à Zurich).

      '
description: 'Used when multiple options are presented for voting (e.g., 5 buttons
  in Zurich).

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