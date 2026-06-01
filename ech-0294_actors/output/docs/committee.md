---
search:
  boost: 5.0
---

# Slot: committee 


_Committee or board (e.g., foundation board, board of directors)._

__



<div data-search-exclude markdown="1">



URI: [act:committee](https://ld.ech.ch/schema/0294/actors/committee)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [InterestLink](InterestLink.md) |
| Slot URI | [act:committee](https://ld.ech.ch/schema/0294/actors/committee) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: committee
annotations:
  description_de:
    tag: description_de
    value: 'Gremium (z.B. Stiftungsrat, Verwaltungsrat).

      '
description: 'Committee or board (e.g., foundation board, board of directors).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:committee
domain_of:
- InterestLink
range: string

```
</details></div>