---
search:
  boost: 5.0
---

# Slot: actor_id 


_Referenz auf die handelnde Person (Momentaufnahme zum Zeitpunkt der Verknüpfung)._




<div data-search-exclude markdown="1">



URI: [ops:actor_id](https://ch.paf.link/schema/operations/actor_id)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |  yes  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  yes  |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  yes  |
| [IndividualVote](IndividualVote.md) | Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  yes  |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |  yes  |
| [IndividualAttendance](IndividualAttendance.md) | Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft üb... |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [PersonReference](PersonReference.md) |
| Domäne von | [Legislature](Legislature.md), [Meeting](Meeting.md), [Voting](Voting.md), [IndividualVote](IndividualVote.md), [Election](Election.md), [Attendance](Attendance.md), [IndividualAttendance](IndividualAttendance.md), [Speech](Speech.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: actor_id
annotations:
  description_de:
    tag: description_de
    value: 'Referenz auf die handelnde Person (Momentaufnahme zum Zeitpunkt der Verknüpfung).

      '
  description_fr:
    tag: description_fr
    value: 'Référence à la personne agissante (instantané au moment de la mise en
      relation).

      '
description: 'Referenz auf die handelnde Person (Momentaufnahme zum Zeitpunkt der
  Verknüpfung).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Meeting
- Voting
- IndividualVote
- Election
- Attendance
- IndividualAttendance
- Speech
range: PersonReference
inlined: true

```
</details></div>