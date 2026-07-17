---
search:
  boost: 5.0
---

# Slot: address_uri 


_URI der Adresse aus dem eidgenössischen Gebäudeadressverzeichnis. Der Layer ist zugänglich unter https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis. Beispiel einer gültigen URI: https://geo.ld.admin.ch/location/address/101904050_

__



<div data-search-exclude markdown="1">



URI: [act:addressURI](https://ld.ech.ch/schema/0294/actors/addressURI)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Address](Address.md) | Eine Adresse mit einem Typ (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Uriorcurie](Uriorcurie.md) |
| Domäne von | [Address](Address.md) |
| Slot-URI | [act:addressURI](https://ld.ech.ch/schema/0294/actors/addressURI) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'URI der Adresse aus dem eidgenössischen Gebäudeadressverzeichnis. Der
  Layer ist zugänglich unter https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis.
  Beispiel einer gültigen URI: https://geo.ld.admin.ch/location/address/101904050

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:addressURI
domain_of:
- Address
range: uriorcurie

```
</details></div>