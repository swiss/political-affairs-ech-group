---
search:
  boost: 5.0
---

# Slot: organization_uid 


_[en] UID of the organization (for analysis with NOGA codes, etc.)._

_[de] UID der Organisation (für Auswertungen mit NOGA-Codes, etc.)._

__



<div data-search-exclude markdown="1">



URI: [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid)
Alias: organization_uid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:organizationUid |
| native | act:organization_uid |




## LinkML Source

<details>
```yaml
name: organization_uid
description: '[en] UID of the organization (for analysis with NOGA codes, etc.).

  [de] UID der Organisation (für Auswertungen mit NOGA-Codes, etc.).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationUid
alias: organization_uid
domain_of:
- InterestLink
range: string

```
</details></div>