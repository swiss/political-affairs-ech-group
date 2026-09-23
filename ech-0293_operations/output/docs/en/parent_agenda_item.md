---
search:
  boost: 5.0
---

# Slot: parent_agenda_item 


_Identifier of the agenda item this record belongs to. On an agenda item it builds a hierarchy of agenda items — e.g. an item group "Gesetzesberatungen" with the sub-items "Energiegesetz (Detailberatung)" and "Energiegesetz (Schlussabstimmung)"; on a speech it names the agenda item under which the speech was given._




<div data-search-exclude markdown="1">



URI: [ops:parent_agenda_item](https://ch.paf.link/schema/operations/parent_agenda_item)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | A mixin class that provides the elements of an agenda item: designation, type... |  no  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting as planned beforehand |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [IsAgendaItem](IsAgendaItem.md), [Speech](Speech.md) |

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
      Traktandum bildet er eine Hierarchie von Traktanden — z.B. eine Traktandengruppe
      „Gesetzesberatungen“ mit den Untertraktanden „Energiegesetz (Detailberatung)“
      und „Energiegesetz (Schlussabstimmung)“; bei einer Wortmeldung bezeichnet er
      das Traktandum, unter dem sie erfolgte.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant du point de l''ordre du jour auquel cet enregistrement se
      rattache. Pour un point de l''ordre du jour, il forme une hiérarchie de points
      — p. ex. un groupe « Délibérations législatives » avec les sous-points « Loi
      sur l''énergie (discussion par article) » et « Loi sur l''énergie (vote final)
      » ; pour une intervention, il désigne le point sous lequel elle a été faite.

      '
description: 'Identifier of the agenda item this record belongs to. On an agenda item
  it builds a hierarchy of agenda items — e.g. an item group "Gesetzesberatungen"
  with the sub-items "Energiegesetz (Detailberatung)" and "Energiegesetz (Schlussabstimmung)";
  on a speech it names the agenda item under which the speech was given.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
- Speech
range: string

```
</details></div>