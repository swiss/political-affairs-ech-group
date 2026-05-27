---
search:
  boost: 5.0
---

# Slot: enterprise_uid 


_[de] UID des Unternehmens._

_[en] UID of the enterprise._

__



<div data-search-exclude markdown="1">



URI: [act:enterpriseUid](https://ld.ech.ch/schema/0294/actors/enterpriseUid)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Occupation](Occupation.md) | [de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19... |  no  |






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
description: '[de] UID des Unternehmens.

  [en] UID of the enterprise.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:enterpriseUid
domain_of:
- Occupation
range: string

```
</details></div>