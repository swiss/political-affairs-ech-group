---
search:
  boost: 5.0
---

# Slot: person_reference 


_Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung._

__



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
    value: 'Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.

      '
  description_fr:
    tag: description_fr
    value: 'Référence à une personne avec des données instantanées au moment de la
      mise en relation.

      '
description: 'Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.

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