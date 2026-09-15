---
search:
  boost: 5.0
---

# Slot: parent_agenda_item 


_Identifier of the agenda item this record belongs to. On an agenda item it builds a hierarchy of agenda items; on a voting, election or speech it names the agenda item under which the record was handled._




<div data-search-exclude markdown="1">



URI: [ops:parent_agenda_item](https://ch.paf.link/schema/operations/parent_agenda_item)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AgendaItem](AgendaItem.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

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
description: 'Identifier of the agenda item this record belongs to. On an agenda item
  it builds a hierarchy of agenda items; on a voting, election or speech it names
  the agenda item under which the record was handled.

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