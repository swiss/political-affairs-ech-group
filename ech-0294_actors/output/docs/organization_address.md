

# Slot: organization_address 


_[en] Address of the organization._

_[de] Adresse der Organisation._

__





URI: [act:organizationAddress](https://ch.paf.link/schema/actors/organizationAddress)
Alias: organization_address

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




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
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:organizationAddress
alias: organization_address
domain_of:
- InterestLink
range: string

```
</details>