---
search:
  boost: 5.0
---

# Slot: datetime_end 


_Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet._




<div data-search-exclude markdown="1">



URI: [ops:datetime_end](https://ch.paf.link/schema/operations/datetime_end)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Datetime](Datetime.md) |
| Domäne von | [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: datetime_end
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure auxquelles la séance ou le vote se termine.

      '
description: 'Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
- Speech
range: datetime

```
</details></div>