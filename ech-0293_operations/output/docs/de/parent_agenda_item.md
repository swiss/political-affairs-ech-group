---
search:
  boost: 5.0
---

# Slot: parent_agenda_item 


_Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem Traktandum baut er eine Hierarchie von Traktanden auf, bei Abstimmung, Wahl oder Wortmeldung bezeichnet er das Traktandum, unter dem der Eintrag behandelt wurde._




<div data-search-exclude markdown="1">



URI: [ops:parent_agenda_item](https://ch.paf.link/schema/operations/parent_agenda_item)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [AgendaItem](AgendaItem.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: parent_agenda_item
annotations:
  description_de:
    tag: description_de
    value: 'Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem
      Traktandum baut er eine Hierarchie von Traktanden auf, bei Abstimmung, Wahl
      oder Wortmeldung bezeichnet er das Traktandum, unter dem der Eintrag behandelt
      wurde.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant du point de l''ordre du jour auquel cet enregistrement se
      rattache. Pour un point de l''ordre du jour, il construit une hiérarchie de
      points ; pour un vote, une élection ou une intervention, il désigne le point
      sous lequel l''enregistrement a été traité.

      '
description: 'Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem
  Traktandum baut er eine Hierarchie von Traktanden auf, bei Abstimmung, Wahl oder
  Wortmeldung bezeichnet er das Traktandum, unter dem der Eintrag behandelt wurde.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
- Voting
- Election
- Speech
range: string

```
</details></div>