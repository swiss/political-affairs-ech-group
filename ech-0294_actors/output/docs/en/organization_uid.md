---
search:
  boost: 5.0
---

# Slot: organization_uid 


_UID of the organization (eCH-0097 format: CHE-XXX.XXX.XXX) from the federal UID register (uid.admin.ch)._




<div data-search-exclude markdown="1">



URI: [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Group](Group.md), [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot URI | [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^CHE-\d{3}\.\d{3}\.\d{3}$` |











## Examples

| Value |
| --- |
| CHE-106.063.525 |
| CHE-109.810.537 |





## LinkML Source

<details>
```yaml
name: organization_uid
annotations:
  description_de:
    tag: description_de
    value: 'UID der Organisation (Format eCH-0097: CHE-XXX.XXX.XXX) aus dem eidgenössischen
      UID-Register (uid.admin.ch).

      '
  description_fr:
    tag: description_fr
    value: 'IDE de l''organisation (format eCH-0097 : CHE-XXX.XXX.XXX) issu du registre
      fédéral IDE (uid.admin.ch).

      '
description: 'UID of the organization (eCH-0097 format: CHE-XXX.XXX.XXX) from the
  federal UID register (uid.admin.ch).

  '
examples:
- value: CHE-106.063.525
- value: CHE-109.810.537
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationUid
domain_of:
- Group
- InterestLink
- Occupation
range: string
pattern: ^CHE-\d{3}\.\d{3}\.\d{3}$

```
</details></div>