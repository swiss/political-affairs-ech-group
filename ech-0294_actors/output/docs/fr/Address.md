

## Classe: Address 


_Une adresse avec un type (p. ex. adresse privée, adresse professionnelle) et une valeur._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| address_type | 0..1 <br/> [AddressTypeEnum](AddressTypeEnum.md) | Type d'adresse.  |
| address_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | URI de l'adresse issue du Répertoire officiel des adresses de bâtiments (swisstopo). Le dernier segment de l'URI est l'EGAID, l'identifiant fédéral d'adresse de bâtiment de ce répertoire. Exemple d'URI valide : https://geo.ld.admin.ch/location/address/101904050 — le même répertoire est consultable comme couche cartographique à l'adresse https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis  |
| street_address | 0..1 <br/> [String](String.md) | Adresse (rue).  |
| postal_code | 0..1 <br/> [Integer](Integer.md) | Code postal.  |
| postal_locality | 0..1 <br/> [String](String.md) | Localité.  |
| country | 0..1 <br/> [String](String.md) | Code de pays ISO 3166-1 alpha-2.  |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [postal_locality](postal_locality.md)
- [address_uri](address_uri.md)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [addresses](addresses.md) | range | [Address](Address.md) |
| [Group](Group.md) | [addresses](addresses.md) | range | [Address](Address.md) |














### Exemples
#### Exemple Address : swiss politicians Beat Jans 1

```yaml
addresses:
- address_type: businessAddress
  postal_locality: Basel-Stadt

```
#### Exemple Address : groups Konsumenteninformation und -schutz 1

```yaml
addresses:
- address_type: businessAddress
  address_uri: https://geo.ld.admin.ch/location/address/101009806
  street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale
    585
  postal_code: '1001'
  postal_locality: Lausanne
  country: CH

```






</div>