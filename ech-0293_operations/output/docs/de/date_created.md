---
search:
  boost: 5.0
---

# Slot: date_created 


_Das Datum, an dem eine Entität erstellt wurde._




<div data-search-exclude markdown="1">



URI: [mcm:dateCreated](https://ld.ech.ch/schema/0292/meta-common/dateCreated)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderu... |  no  |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |  no  |
| [Session](Session.md) | Eine Session: eine zusammenhängende Sitzungsperiode innerhalb einer Legislatu... |  no  |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |
| [AgendaItem](AgendaItem.md) | Ein vorgängig geplantes Traktandum einer Sitzung |  no  |
| [Protocol](Protocol.md) | Das Protokoll einer Sitzung, nach der Sitzung erstellt und pro Sitzung genau ... |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |
| [Voting](Voting.md) | Eine Abstimmung über eine Sachfrage: der Abstimmungsgegenstand (Frage), das V... |  no  |
| [IndividualVote](IndividualVote.md) | Die Stimme, die ein einzelnes Mitglied in einer Abstimmung abgibt |  no  |
| [Election](Election.md) | Eine Wahl, mit der ein parlamentarisches Organ eine oder mehrere Personen für... |  no  |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |  no  |
| [IndividualAttendance](IndividualAttendance.md) | Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft üb... |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Date](Date.md) |
| Domäne von | [HasCreationModificationDates](HasCreationModificationDates.md) |
| Slot-URI | [mcm:dateCreated](https://ld.ech.ch/schema/0292/meta-common/dateCreated) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: date_created
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, an dem eine Entität erstellt wurde.

      '
  description_fr:
    tag: description_fr
    value: 'La date à laquelle une entité a été créée.

      '
description: 'Das Datum, an dem eine Entität erstellt wurde.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:dateCreated
domain_of:
- HasCreationModificationDates
range: date

```
</details></div>