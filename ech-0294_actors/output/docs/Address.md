

# Class: Address 


_[de] Eine Adresse mit einem Typ (z.B. Privatadresse, Geschäftsadresse) und einem Wert._

_[en] An address with a type (e.g., private address, business address) and a value._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'address_type',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Typ der Adresse.\n[en] Type of address.\n',
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': 'businessAddress'}), Example({'value': 'privateAddress'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:addressType',
  'owner': 'Address',
  'domain_of': ['Address'],
  'range': 'AddressTypeEnum'
}) | 0..1 <br/> [AddressTypeEnum](AddressTypeEnum.md) | [de] Typ der Adresse.
[en] Type of address.
 | direct |
| SlotDefinition({
  'name': 'address_uri',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] URI der Adresse.\n[en] URI of the address.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:addressURI',
  'owner': 'Address',
  'domain_of': ['Address'],
  'range': 'uriorcurie'
}) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] URI der Adresse.
[en] URI of the address.
 | direct |
| SlotDefinition({
  'name': 'street_address',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Strassenadresse.\n[en] Street address.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:streetAddress',
  'owner': 'Address',
  'domain_of': ['Address'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Strassenadresse.
[en] Street address.
 | direct |
| SlotDefinition({
  'name': 'postal_code',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Postleitzahl.\n[en] Postal code.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:postalCode',
  'owner': 'Address',
  'domain_of': ['Address'],
  'range': 'integer'
}) | 0..1 <br/> [Integer](Integer.md) | [de] Postleitzahl.
[en] Postal code.
 | direct |
| SlotDefinition({
  'name': 'postal_locality',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Ort.\n[en] Locality.\n',
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': 'Basel-Stadt'}), Example({'value': 'London'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:postalLocality',
  'owner': 'Address',
  'domain_of': ['Address'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Ort.
[en] Locality.
 | direct |





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




## Examples
### Example: Address-swiss_politicians_Beat_Jans_1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```
### Example: Address-douglas_adams_Douglas_Adams_1

```yaml
address_type: privateAddress
address_uri: https://www.wikidata.org/wiki/Q42#P969
street_address: 1234 Fictional St, London, UK
postal_code: 12345
postal_locality: London

```




