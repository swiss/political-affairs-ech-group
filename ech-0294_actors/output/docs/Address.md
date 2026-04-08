---
search:
  boost: 10.0
---

# Class: Address 


_[de] Eine Adresse mit einem Typ (z.B. Privatadresse, Geschäftsadresse) und einem Wert._

_[en] An address with a type (e.g., private address, business address) and a value._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [address_type](address_type.md) | 0..1 <br/> [AddressTypeEnum](AddressTypeEnum.md) | [de] Typ der Adresse | direct |
| [address_uri](address_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] URI der Adresse | direct |
| [street_address](street_address.md) | 0..1 <br/> [String](String.md) | [de] Strassenadresse | direct |
| [postal_code](postal_code.md) | 0..1 <br/> [Integer](Integer.md) | [de] Postleitzahl | direct |
| [postal_locality](postal_locality.md) | 0..1 <br/> [String](String.md) | [de] Ort | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [addresses](addresses.md) | range | [Address](Address.md) |
| [Group](Group.md) | [addresses](addresses.md) | range | [Address](Address.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Address |
| native | act:Address |







