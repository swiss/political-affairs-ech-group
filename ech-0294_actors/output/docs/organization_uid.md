---
search:
  boost: 5.0
---

# Slot: organization_uid 


_UID of the organization (for analysis with NOGA codes, etc.)._

__



<div data-search-exclude markdown="1">



URI: [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid)
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
| Slot URI | [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: organization_uid
annotations:
  description_de:
    tag: description_de
    value: 'UID der Organisation (für Auswertungen mit NOGA-Codes, etc.).

      '
description: 'UID of the organization (for analysis with NOGA codes, etc.).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationUid
domain_of:
- InterestLink
range: string

```
</details></div>