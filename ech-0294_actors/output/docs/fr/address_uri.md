---
search:
  boost: 5.0
---

# Slot: address_uri 


_URI de l'adresse issue du répertoire fédéral des adresses de bâtiments. La couche est accessible à l'adresse https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis. Exemple d'URI valide : https://geo.ld.admin.ch/location/address/101904050_

__



<div data-search-exclude markdown="1">



URI: [act:addressURI](https://ld.ech.ch/schema/0294/actors/addressURI)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Address](Address.md) | Une adresse avec un type (p |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Uriorcurie](Uriorcurie.md) |
| Domaine de | [Address](Address.md) |
| URI du slot | [act:addressURI](https://ld.ech.ch/schema/0294/actors/addressURI) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: address_uri
annotations:
  description_de:
    tag: description_de
    value: 'URI der Adresse aus dem eidgenössischen Gebäudeadressverzeichnis. Der
      Layer ist zugänglich unter https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis.
      Beispiel einer gültigen URI: https://geo.ld.admin.ch/location/address/101904050

      '
  description_fr:
    tag: description_fr
    value: 'URI de l''adresse issue du répertoire fédéral des adresses de bâtiments.
      La couche est accessible à l''adresse https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis.
      Exemple d''URI valide : https://geo.ld.admin.ch/location/address/101904050

      '
description: 'URI de l''adresse issue du répertoire fédéral des adresses de bâtiments.
  La couche est accessible à l''adresse https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis.
  Exemple d''URI valide : https://geo.ld.admin.ch/location/address/101904050

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:addressURI
domain_of:
- Address
range: uriorcurie

```
</details></div>