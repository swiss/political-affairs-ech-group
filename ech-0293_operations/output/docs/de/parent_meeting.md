---
search:
  boost: 5.0
---

# Slot: parent_meeting 


_Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert._




<div data-search-exclude markdown="1">



URI: [ops:parent_meeting](https://ch.paf.link/schema/operations/parent_meeting)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [Protocol](Protocol.md) | Das nach der Sitzung erstellte Protokoll |  no  |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Protocol](Protocol.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: parent_meeting
annotations:
  description_de:
    tag: description_de
    value: 'Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la séance liée qui regroupe la séance courante.

      '
description: 'Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- AgendaItem
- Protocol
- Voting
- Election
- Attendance
range: string

```
</details></div>