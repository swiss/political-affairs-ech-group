---
search:
  boost: 5.0
---

# Slot: parent_protocol 


_Das Protokoll, in dem die Abstimmung oder Wahl festgehalten ist. Abgestimmt wird im Verlauf der Sitzung; die Abstimmung hängt deshalb am Protokoll und nicht an der vorgängig geplanten Traktandenliste._




<div data-search-exclude markdown="1">



URI: [ops:parentProtocol](https://ch.paf.link/schema/operations/parentProtocol)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Protocol](Protocol.md) |
| Domäne von | [Voting](Voting.md), [Election](Election.md) |
| Slot-URI | [ops:parentProtocol](https://ch.paf.link/schema/operations/parentProtocol) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: parent_protocol
annotations:
  description_de:
    tag: description_de
    value: 'Das Protokoll, in dem die Abstimmung oder Wahl festgehalten ist. Abgestimmt
      wird im Verlauf der Sitzung; die Abstimmung hängt deshalb am Protokoll und nicht
      an der vorgängig geplanten Traktandenliste.

      '
  description_fr:
    tag: description_fr
    value: 'Le procès-verbal dans lequel le vote ou l''élection est consigné. Un vote
      a lieu au cours de la séance et se rattache donc au procès-verbal et non à l''ordre
      du jour planifié à l''avance.

      '
description: 'Das Protokoll, in dem die Abstimmung oder Wahl festgehalten ist. Abgestimmt
  wird im Verlauf der Sitzung; die Abstimmung hängt deshalb am Protokoll und nicht
  an der vorgängig geplanten Traktandenliste.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:parentProtocol
domain_of:
- Voting
- Election
range: Protocol

```
</details></div>