---
search:
  boost: 5.0
---

# Slot: group_reference 


_Kurzreferenz auf eine Gruppe oder ein Organ gemäss eCH-0294, welche deren Merkmale zum Zeitpunkt der Verknüpfung festhält._




<div data-search-exclude markdown="1">



URI: [actors:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |  yes  |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  yes  |
| [Voting](Voting.md) | Eine Abstimmung über eine Sachfrage: der Abstimmungsgegenstand (Frage), das V... |  yes  |
| [Election](Election.md) | Eine Wahl, mit der ein parlamentarisches Organ eine oder mehrere Personen für... |  yes  |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |  yes  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [GroupReference](GroupReference.md) |
| Domäne von | [Legislature](Legislature.md), [Meeting](Meeting.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md) |
| Slot-URI | [actors:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: group_reference
annotations:
  description_de:
    tag: description_de
    value: 'Kurzreferenz auf eine Gruppe oder ein Organ gemäss eCH-0294, welche deren
      Merkmale zum Zeitpunkt der Verknüpfung festhält.

      '
  description_fr:
    tag: description_fr
    value: 'Référence abrégée à un groupe ou à un organe selon eCH-0294, retenant
      ses caractéristiques au moment de la mise en relation.

      '
description: 'Kurzreferenz auf eine Gruppe oder ein Organ gemäss eCH-0294, welche
  deren Merkmale zum Zeitpunkt der Verknüpfung festhält.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: actors:groupReference
domain_of:
- Legislature
- Meeting
- Voting
- Election
- Attendance
range: GroupReference
inlined: true

```
</details></div>