---
search:
  boost: 5.0
---

# Slot: organization_address 


_[en] Address of the organization._

_[de] Adresse der Organisation._

__



<div data-search-exclude markdown="1">



URI: [act:organizationAddress](https://ld.ech.ch/schema/0294/actors/organizationAddress)
Alias: organization_address

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
| Slot URI | [act:organizationAddress](https://ld.ech.ch/schema/0294/actors/organizationAddress) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:organizationAddress |
| native | act:organization_address |




## LinkML Source

<details>
```yaml
name: organization_address
description: '[en] Address of the organization.

  [de] Adresse der Organisation.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationAddress
alias: organization_address
domain_of:
- InterestLink
range: string

```
</details></div>