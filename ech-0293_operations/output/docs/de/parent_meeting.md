---
search:
  boost: 5.0
---

# Slot: parent_meeting 


_Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung bezeichnet er die übergeordnete Sitzung, bei Abstimmung, Wahl, Wortmeldung, Anwesenheitsliste oder Protokoll die Sitzung, in der der Eintrag entstanden ist. Traktanden führen ihn nicht: Sie sind in ihre Sitzung eingebettet._




<div data-search-exclude markdown="1">



URI: [ops:parent_meeting](https://ch.paf.link/schema/operations/parent_meeting)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |
| [Protocol](Protocol.md) | Das Protokoll einer Sitzung, nach der Sitzung erstellt und pro Sitzung genau ... |  no  |
| [Voting](Voting.md) | Eine Abstimmung über eine Sachfrage: der Abstimmungsgegenstand (Frage), das V... |  no  |
| [Election](Election.md) | Eine Wahl, mit der ein parlamentarisches Organ eine oder mehrere Personen für... |  no  |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Meeting](Meeting.md), [Protocol](Protocol.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md), [Speech](Speech.md) |

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
    value: 'Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung
      bezeichnet er die übergeordnete Sitzung, bei Abstimmung, Wahl, Wortmeldung,
      Anwesenheitsliste oder Protokoll die Sitzung, in der der Eintrag entstanden
      ist. Traktanden führen ihn nicht: Sie sind in ihre Sitzung eingebettet.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la séance à laquelle cet enregistrement se rattache. Pour
      une séance, il désigne la séance supérieure ; pour un vote, une élection, une
      intervention, une liste de présence ou un procès-verbal, la séance au cours
      de laquelle l''enregistrement est né. Les points de l''ordre du jour ne le portent
      pas : ils sont imbriqués dans leur séance.

      '
description: 'Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung
  bezeichnet er die übergeordnete Sitzung, bei Abstimmung, Wahl, Wortmeldung, Anwesenheitsliste
  oder Protokoll die Sitzung, in der der Eintrag entstanden ist. Traktanden führen
  ihn nicht: Sie sind in ihre Sitzung eingebettet.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- Protocol
- Voting
- Election
- Attendance
- Speech
range: string

```
</details></div>