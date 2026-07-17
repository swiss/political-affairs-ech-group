

## Klasse: Address 


_Eine Adresse mit einem Typ (z.B. Privatadresse, Geschäftsadresse) und einem Wert._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| address_type | 0..1 <br/> [AddressTypeEnum](AddressTypeEnum.md) | Typ der Adresse.  |
| address_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | URI der Adresse aus dem eidgenössischen Gebäudeadressverzeichnis. Der Layer ist zugänglich unter https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis. Beispiel einer gültigen URI: https://geo.ld.admin.ch/location/address/101904050  |
| street_address | 0..1 <br/> [String](String.md) | Strassenadresse.  |
| postal_code | 0..1 <br/> [Integer](Integer.md) | Postleitzahl.  |
| postal_locality | 0..1 <br/> [String](String.md) | Ort.  |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [postal_locality](postal_locality.md)
- [address_uri](address_uri.md)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [addresses](addresses.md) | range | [Address](Address.md) |
| [Group](Group.md) | [addresses](addresses.md) | range | [Address](Address.md) |














### Beispiele
#### Beispiel: Address-swiss_politicians_Beat_Jans_1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```






</div>