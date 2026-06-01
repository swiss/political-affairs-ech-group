---
search:
  boost: 5.0
---

# Slot: enterprise_uid 


_UID of the enterprise._

__



<div data-search-exclude markdown="1">



URI: [act:enterpriseUid](https://ld.ech.ch/schema/0294/actors/enterpriseUid)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Occupation](Occupation.md) |
| Slot URI | [act:enterpriseUid](https://ld.ech.ch/schema/0294/actors/enterpriseUid) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: enterprise_uid
annotations:
  description_de:
    tag: description_de
    value: 'UID des Unternehmens.

      '
description: 'UID of the enterprise.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:enterpriseUid
domain_of:
- Occupation
range: string

```
</details></div>