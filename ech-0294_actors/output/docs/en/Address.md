

## Class: Address 


_An address with a type (e.g., private address, business address) and a value._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| address_type | 0..1 <br/> [AddressTypeEnum](AddressTypeEnum.md) | Type of address.  |
| address_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | URI of the address from the Swiss federal building address register. The layer can be accessed at https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis. Example of a valid URI: https://geo.ld.admin.ch/location/address/101904050  |
| street_address | 0..1 <br/> [String](String.md) | Street address.  |
| postal_code | 0..1 <br/> [Integer](Integer.md) | Postal code.  |
| postal_locality | 0..1 <br/> [String](String.md) | Locality.  |
| country | 0..1 <br/> [String](String.md) | ISO 3166-1 alpha-2 country code.  |

##### Constraints


At least one of the following must be set:

- [postal_locality](postal_locality.md)
- [address_uri](address_uri.md)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [addresses](addresses.md) | range | [Address](Address.md) |
| [Group](Group.md) | [addresses](addresses.md) | range | [Address](Address.md) |














### Examples
#### Example: swiss politicians Beat Jans 1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```
#### Example: groups Konsumenteninformation und -schutz 1

```yaml
address_type: businessAddress
address_uri: https://geo.ld.admin.ch/location/address/101009806
street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale
  585
postal_code: '1001'
postal_locality: Lausanne
country: CH

```






</div>