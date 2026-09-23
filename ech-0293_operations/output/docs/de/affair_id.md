---
search:
  boost: 5.0
---

# Slot: affair_id 


_Identifikator des Geschäfts (eCH-0295), auf das sich der Eintrag bezieht. Administrative Traktanden (z.B. Genehmigung des Protokolls) haben kein Geschäft. Ein Geschäft durchläuft in der Regel mehrere Traktanden — in der Gesetzgebung etwa Eintretensdebatte, Detailberatung, Schlussabstimmung und gegebenenfalls die Differenzbereinigung zwischen den Räten._




<div data-search-exclude markdown="1">



URI: [ops:affair_id](https://ch.paf.link/schema/operations/affair_id)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |  no  |
| [Voting](Voting.md) | Eine Abstimmung über eine Sachfrage: der Abstimmungsgegenstand (Frage), das V... |  no  |
| [Election](Election.md) | Eine Wahl, mit der ein parlamentarisches Organ eine oder mehrere Personen für... |  no  |
| [AgendaItem](AgendaItem.md) | Ein vorgängig geplantes Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [IsAgendaItem](IsAgendaItem.md), [Voting](Voting.md), [Election](Election.md) |

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
description: 'Identifikator des Geschäfts (eCH-0295), auf das sich der Eintrag bezieht.
  Administrative Traktanden (z.B. Genehmigung des Protokolls) haben kein Geschäft.
  Ein Geschäft durchläuft in der Regel mehrere Traktanden — in der Gesetzgebung etwa
  Eintretensdebatte, Detailberatung, Schlussabstimmung und gegebenenfalls die Differenzbereinigung
  zwischen den Räten.

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