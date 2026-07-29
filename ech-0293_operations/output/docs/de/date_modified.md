---
search:
  boost: 5.0
---

# Slot: date_modified 


_Das Datum, an dem eine Entität zuletzt geändert wurde._




<div data-search-exclude markdown="1">



URI: [mcm:dateModified](https://ld.ech.ch/schema/0292/meta-common/dateModified)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderu... |  no  |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |  no  |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [Protocol](Protocol.md) | Das nach der Sitzung erstellte Protokoll |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [IndividualVote](IndividualVote.md) | Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |  no  |
| [IndividualAttendance](IndividualAttendance.md) | Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft üb... |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Date](Date.md) |
| Domäne von | [HasCreationModificationDates](HasCreationModificationDates.md) |
| Slot-URI | [mcm:dateModified](https://ld.ech.ch/schema/0292/meta-common/dateModified) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: date_modified
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, an dem eine Entität zuletzt geändert wurde.

      '
  description_fr:
    tag: description_fr
    value: 'La date à laquelle une entité a été modifiée pour la dernière fois.

      '
description: 'Das Datum, an dem eine Entität zuletzt geändert wurde.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:dateModified
domain_of:
- HasCreationModificationDates
range: date

```
</details></div>