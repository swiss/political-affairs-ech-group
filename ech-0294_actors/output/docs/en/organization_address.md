---
search:
  boost: 5.0
---

# Slot: organization_address 


_Address of the organization._

__



<div data-search-exclude markdown="1">



URI: [act:organizationAddress](https://ld.ech.ch/schema/0294/actors/organizationAddress)
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
| Slot URI | [act:organizationAddress](https://ld.ech.ch/schema/0294/actors/organizationAddress) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: organization_address
annotations:
  description_de:
    tag: description_de
    value: 'Adresse der Organisation.

      '
  description_fr:
    tag: description_fr
    value: 'Adresse de l''organisation.

      '
description: 'Address of the organization.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationAddress
domain_of:
- InterestLink
range: string

```
</details></div>