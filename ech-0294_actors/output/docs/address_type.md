

# Slot: address_type 



URI: [act:addressType](https://ch.paf.link/schema/actors/addressType)
Alias: address_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Address](Address.md) |  |  no  |






## Properties

* Range: [AddressTypeEnum](AddressTypeEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:addressType |
| native | act:address_type |




## LinkML Source

<details>
```yaml
name: address-type
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:addressType
alias: address_type
owner: Address
domain_of:
- Address
range: AddressTypeEnum
required: true

```
</details>