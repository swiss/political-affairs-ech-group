

# Class: Address 



URI: [act:Address](https://ch.paf.link/schema/actors/Address)





```mermaid
 classDiagram
    class Address
    click Address href "../Address/"
      Address : addressType
        
          
    
        
        
        Address --> "1" AddressTypeEnum : addressType
        click AddressTypeEnum href "../AddressTypeEnum/"
    

        
      Address : addressURI
        
      Address : postalCode
        
      Address : postalLocality
        
      Address : streetAddress
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [addressType](addressType.md) | 1 <br/> [AddressTypeEnum](AddressTypeEnum.md) |  | direct |
| [addressURI](addressURI.md) | 0..1 <br/> [String](String.md) | Preferred URI of address | direct |
| [streetAddress](streetAddress.md) | 0..1 <br/> [String](String.md) |  | direct |
| [postalCode](postalCode.md) | 0..1 <br/> [String](String.md) |  | direct |
| [postalLocality](postalLocality.md) | 0..1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [addresses](addresses.md) | range | [Address](Address.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Address |
| native | act:Address |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Address
from_schema: https://ch.paf.link/schema/actors
attributes:
  addressType:
    name: addressType
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Address
    range: AddressTypeEnum
    required: true
  addressURI:
    name: addressURI
    description: Preferred URI of address
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Address
  streetAddress:
    name: streetAddress
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Address
  postalCode:
    name: postalCode
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Address
  postalLocality:
    name: postalLocality
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    domain_of:
    - Address

```
</details>

### Induced

<details>
```yaml
name: Address
from_schema: https://ch.paf.link/schema/actors
attributes:
  addressType:
    name: addressType
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: addressType
    owner: Address
    domain_of:
    - Address
    range: AddressTypeEnum
    required: true
  addressURI:
    name: addressURI
    description: Preferred URI of address
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: addressURI
    owner: Address
    domain_of:
    - Address
    range: string
  streetAddress:
    name: streetAddress
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: streetAddress
    owner: Address
    domain_of:
    - Address
    range: string
  postalCode:
    name: postalCode
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: postalCode
    owner: Address
    domain_of:
    - Address
    range: string
  postalLocality:
    name: postalLocality
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: postalLocality
    owner: Address
    domain_of:
    - Address
    range: string

```
</details>