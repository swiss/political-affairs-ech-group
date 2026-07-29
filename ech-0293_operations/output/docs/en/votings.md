---
search:
  boost: 5.0
---

# Slot: votings 


_Collection of voting records._




<div data-search-exclude markdown="1">



URI: [ops:voting](https://ch.paf.link/schema/operations/voting)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |
| [Protocol](Protocol.md) | The minutes of a meeting, recorded after the meeting |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Voting](Voting.md) |
| Domain Of | [Container](Container.md), [Protocol](Protocol.md) |
| Slot URI | [ops:voting](https://ch.paf.link/schema/operations/voting) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: votings
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Abstimmungen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des votes.

      '
description: 'Collection of voting records.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:voting
domain_of:
- Container
- Protocol
range: Voting
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>