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
| [TextSegment](TextSegment.md) | Ein Textsegment wie Querverweise oder Zwischentitel in Sitzungsprotokollen |  no  |
| [Motion](Motion.md) | Ein formeller Antrag, der während der Verhandlungen eingereicht wird |  no  |
| [Media](Media.md) | Mediendateien oder Dokumente (einschliesslich Protokolle in PDF/HTML/WORD ode... |  no  |
| [PersonReference](PersonReference.md) | Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikations... |  no  |
| [GroupReference](GroupReference.md) | Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifikations... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [HasIdentification](HasIdentification.md), [IsProcessStep](IsProcessStep.md) |
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
- IsProcessStep
range: string

```
</details></div>