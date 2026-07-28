

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
| country | 0..1 <br/> [String](String.md) | ISO 3166-1 alpha-2 Ländercode.  |

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
#### Beispiel: swiss politicians Beat Jans 1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```
#### Beispiel: groups Konsumenteninformation und -schutz 1

```yaml
address_type: businessAddress
address_uri: https://geo.ld.admin.ch/location/address/101009806
street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale 585
postal_code: '1001'
postal_locality: Lausanne
country: CH

```






</div>