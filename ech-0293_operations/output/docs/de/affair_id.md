---
search:
  boost: 5.0
---

# Slot: affair_id 


_Die Verbindung zu den Geschäften des Traktandums._




<div data-search-exclude markdown="1">



URI: [ops:affair_id](https://ch.paf.link/schema/operations/affair_id)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [AgendaItem](AgendaItem.md), [Voting](Voting.md), [Election](Election.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: affair_id
annotations:
  description_de:
    tag: description_de
    value: 'Die Verbindung zu den Geschäften des Traktandums.

      '
  description_fr:
    tag: description_fr
    value: 'Le lien vers les affaires rattachées au point de l''ordre du jour.

      '
description: 'Die Verbindung zu den Geschäften des Traktandums.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
- Voting
- Election
range: string

```
</details></div>