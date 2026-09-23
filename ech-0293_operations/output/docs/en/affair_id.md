---
search:
  boost: 5.0
---

# Slot: affair_id 


_Identifier of the affair (eCH-0295) the record refers to. Administrative agenda items (e.g. approval of the minutes) have no affair. An affair usually runs through several agenda items — in legislation, for instance, the debate on entering into the matter, the detailed deliberation, the final vote and, where applicable, the procedure for resolving differences between the chambers._




<div data-search-exclude markdown="1">



URI: [ops:affair_id](https://ch.paf.link/schema/operations/affair_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | A mixin class that provides the elements of an agenda item: designation, type... |  no  |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  no  |
| [Election](Election.md) | An election in which a parliamentary body appoints one or several persons to ... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting as planned beforehand |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [IsAgendaItem](IsAgendaItem.md), [Voting](Voting.md), [Election](Election.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: affair_id
annotations:
  description_de:
    tag: description_de
    value: 'Identifikator des Geschäfts (eCH-0295), auf das sich der Eintrag bezieht.
      Administrative Traktanden (z.B. Genehmigung des Protokolls) haben kein Geschäft.
      Ein Geschäft durchläuft in der Regel mehrere Traktanden — in der Gesetzgebung
      etwa Eintretensdebatte, Detailberatung, Schlussabstimmung und gegebenenfalls
      die Differenzbereinigung zwischen den Räten.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de l''affaire (eCH-0295) à laquelle se rapporte l''enregistrement.
      Les points administratifs (p. ex. approbation du procès-verbal) n''ont pas d''affaire.
      Une affaire passe en règle générale par plusieurs points de l''ordre du jour
      — dans la législation, par exemple, le débat d''entrée en matière, la discussion
      par article, le vote final et, le cas échéant, la procédure d''élimination des
      divergences entre les conseils.

      '
description: 'Identifier of the affair (eCH-0295) the record refers to. Administrative
  agenda items (e.g. approval of the minutes) have no affair. An affair usually runs
  through several agenda items — in legislation, for instance, the debate on entering
  into the matter, the detailed deliberation, the final vote and, where applicable,
  the procedure for resolving differences between the chambers.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
- Voting
- Election
range: string

```
</details></div>