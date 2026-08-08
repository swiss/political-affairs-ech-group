---
search:
  boost: 5.0
---

# Slot: person_reference 


_Kurzreferenz auf eine Person, welche deren Merkmale zum Zeitpunkt der Verknüpfung festhält._




<div data-search-exclude markdown="1">



URI: [act:personReference](https://ld.ech.ch/schema/0294/actors/personReference)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |  yes  |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  yes  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [PersonReference](PersonReference.md) |
| Domäne von | [Membership](Membership.md), [InterestLink](InterestLink.md) |
| Slot-URI | [act:personReference](https://ld.ech.ch/schema/0294/actors/personReference) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: person_reference
annotations:
  description_de:
    tag: description_de
    value: 'Kurzreferenz auf eine Person, welche deren Merkmale zum Zeitpunkt der
      Verknüpfung festhält.

      '
  description_fr:
    tag: description_fr
    value: 'Référence abrégée à une personne, retenant ses caractéristiques au moment
      de la mise en relation.

      '
description: 'Kurzreferenz auf eine Person, welche deren Merkmale zum Zeitpunkt der
  Verknüpfung festhält.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:personReference
domain_of:
- Membership
- InterestLink
range: PersonReference
inlined: true

```
</details></div>