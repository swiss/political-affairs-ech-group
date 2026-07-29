---
search:
  boost: 5.0
---

# Slot: datetime_begin 


_Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt._




<div data-search-exclude markdown="1">



URI: [ops:datetime_begin](https://ch.paf.link/schema/operations/datetime_begin)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Datetime](Datetime.md) |
| Domäne von | [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md), [Speech](Speech.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: datetime_begin
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure auxquelles la séance ou le vote commence.

      '
description: 'Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
- Attendance
- Speech
range: datetime

```
</details></div>