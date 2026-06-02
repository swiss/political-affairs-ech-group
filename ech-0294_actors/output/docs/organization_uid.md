---
search:
  boost: 5.0
---

# Slot: organization_uid 


_UID of the organization (eCH-0098 format: CHE-XXX.XXX.XXX of the federal UID register (uid.admin.ch)._

__



<div data-search-exclude markdown="1">



URI: [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot URI | [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^CHE-\d{3}\.\d{3}\.\d{3}$` |














## LinkML Source

<details>
```yaml
name: organization_uid
annotations:
  description_de:
    tag: description_de
    value: 'UID der Organisation (für Auswertungen mit NOGA-Codes, etc.).

      '
description: 'UID of the organization (eCH-0098 format: CHE-XXX.XXX.XXX of the federal
  UID register (uid.admin.ch).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationUid
domain_of:
- InterestLink
- Occupation
range: string
pattern: ^CHE-\d{3}\.\d{3}\.\d{3}$

```
</details></div>