

## Class: Address 


_An address with a type (e.g., private address, business address) and a value._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| address_type | 0..1 <br/> [AddressTypeEnum](AddressTypeEnum.md) | Type of address.  |
| address_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | URI of the address.  |
| street_address | 0..1 <br/> [String](String.md) | Street address.  |
| postal_code | 0..1 <br/> [Integer](Integer.md) | Postal code.  |
| postal_locality | 0..1 <br/> [String](String.md) | Locality.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [addresses](addresses.md) | range | [Address](Address.md) |
| [Group](Group.md) | [addresses](addresses.md) | range | [Address](Address.md) |














### Examples
#### Example: Address-douglas_adams_Douglas_Adams_1

```yaml
address_type: privateAddress
address_uri: https://www.wikidata.org/wiki/Q42#P969
street_address: 1234 Fictional St, London, UK
postal_code: 12345
postal_locality: London

```
#### Example: Address-swiss_politicians_Beat_Jans_1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```






</div>