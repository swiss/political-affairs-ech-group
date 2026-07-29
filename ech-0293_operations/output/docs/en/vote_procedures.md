---
search:
  boost: 5.0
---

# Slot: vote_procedures 


_Procedures for voting, such as secret ballot or open vote._




<div data-search-exclude markdown="1">



URI: [ops:vote_procedures](https://ch.paf.link/schema/operations/vote_procedures)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resolution](Resolution.md) | A resolution or decision taken on an agenda item, including voting procedures |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Resolution](Resolution.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: vote_procedures
annotations:
  description_de:
    tag: description_de
    value: 'Verfahren für die Abstimmung, wie geheime Abstimmung oder offene Abstimmung.

      '
  description_fr:
    tag: description_fr
    value: 'Modalités du vote, p. ex. vote secret ou vote ouvert.

      '
description: 'Procedures for voting, such as secret ballot or open vote.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Resolution
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>