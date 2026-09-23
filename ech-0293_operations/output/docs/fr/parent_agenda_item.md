---
search:
  boost: 5.0
---

# Slot: parent_agenda_item 


_Identifiant du point de l'ordre du jour auquel cet enregistrement se rattache. Pour un point de l'ordre du jour, il construit une hiérarchie de points ; pour un vote, une élection ou une intervention, il désigne le point sous lequel l'enregistrement a été traité._




<div data-search-exclude markdown="1">



URI: [ops:parent_agenda_item](https://ch.paf.link/schema/operations/parent_agenda_item)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [AgendaItem](AgendaItem.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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
description: 'Identifiant du point de l''ordre du jour auquel cet enregistrement se
  rattache. Pour un point de l''ordre du jour, il construit une hiérarchie de points
  ; pour un vote, une élection ou une intervention, il désigne le point sous lequel
  l''enregistrement a été traité.

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