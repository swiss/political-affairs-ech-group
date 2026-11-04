---
search:
  boost: 5.0
---

# Slot: person_reference 


_Kurzreferenz auf eine Person gemäss eCH-0294, welche deren Merkmale zum Zeitpunkt der Verknüpfung festhält._




<div data-search-exclude markdown="1">



URI: [actors:personReference](https://ld.ech.ch/schema/0294/actors/personReference)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | Die Stimme, die ein einzelnes Mitglied in einer Abstimmung abgibt |  yes  |
| [IndividualAttendance](IndividualAttendance.md) | Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft üb... |  yes  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt):... |  yes  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [PersonReference](PersonReference.md) |
| Domäne von | [IndividualVote](IndividualVote.md), [IndividualAttendance](IndividualAttendance.md), [Speech](Speech.md) |
| Slot-URI | [actors:personReference](https://ld.ech.ch/schema/0294/actors/personReference) |

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
    value: 'Kurzreferenz auf eine Person gemäss eCH-0294, welche deren Merkmale zum
      Zeitpunkt der Verknüpfung festhält.

      '
  description_fr:
    tag: description_fr
    value: 'Référence abrégée à une personne selon eCH-0294, retenant ses caractéristiques
      au moment de la mise en relation.

      '
description: 'Kurzreferenz auf eine Person gemäss eCH-0294, welche deren Merkmale
  zum Zeitpunkt der Verknüpfung festhält.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: actors:personReference
domain_of:
- IndividualVote
- IndividualAttendance
- Speech
range: PersonReference
inlined: true

```
</details></div>