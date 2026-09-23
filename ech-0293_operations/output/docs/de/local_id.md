---
search:
  boost: 5.0
---

# Slot: local_id 


_Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem._




<div data-search-exclude markdown="1">



URI: [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügu... |  no  |
| [IsProcessStep](IsProcessStep.md) | Eine Mixin-Klasse für einen einzelnen Schritt in einem |  no  |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |  no  |
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
| [TextSegment](TextSegment.md) | Ein Textsegment wie Querverweise oder Zwischentitel |  no  |
| [Motion](Motion.md) | Ein formaler Antrag, der während der Beratung gestellt wird, etwa ein Änderun... |  no  |
| [Media](Media.md) | Mediendateien oder Dokumente (einschliesslich Protokolle in PDF/HTML/WORD ode... |  no  |
| [HasReferenceIdentification](HasReferenceIdentification.md) | Eine Mixin-Klasse, welche die Slots bereitstellt, mit denen eine Referenz die... |  no  |
| [PersonReference](PersonReference.md) | Kurzreferenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum... |  no  |
| [GroupReference](GroupReference.md) | Kurzreferenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [HasIdentification](HasIdentification.md), [HasReferenceIdentification](HasReferenceIdentification.md), [IsProcessStep](IsProcessStep.md) |
| Slot-URI | [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: local_id
annotations:
  description_de:
    tag: description_de
    value: 'Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant local. Par exemple, un UUID issu du système d''information
      du conseil.

      '
description: 'Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:localId
domain_of:
- HasIdentification
- HasReferenceIdentification
- IsProcessStep
range: string

```
</details></div>