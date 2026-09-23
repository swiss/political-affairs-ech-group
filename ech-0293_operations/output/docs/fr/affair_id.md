---
search:
  boost: 5.0
---

# Slot: affair_id 


_Identifiant de l'affaire (eCH-0295) à laquelle se rapporte l'enregistrement. Les points administratifs (p. ex. approbation du procès-verbal) n'ont pas d'affaire. Une affaire passe en règle générale par plusieurs points de l'ordre du jour — dans la législation, par exemple, le débat d'entrée en matière, la discussion par article, le vote final et, le cas échéant, la procédure d'élimination des divergences entre les conseils._




<div data-search-exclude markdown="1">



URI: [ops:affair_id](https://ch.paf.link/schema/operations/affair_id)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [Voting](Voting.md) | Un vote sur une question matérielle : l'objet du vote (la question), la procé... |  no  |
| [Election](Election.md) | Une élection par laquelle un organe parlementaire désigne une ou plusieurs pe... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance, tel que planifié à l'avance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [IsAgendaItem](IsAgendaItem.md), [Voting](Voting.md), [Election](Election.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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
description: 'Identifiant de l''affaire (eCH-0295) à laquelle se rapporte l''enregistrement.
  Les points administratifs (p. ex. approbation du procès-verbal) n''ont pas d''affaire.
  Une affaire passe en règle générale par plusieurs points de l''ordre du jour — dans
  la législation, par exemple, le débat d''entrée en matière, la discussion par article,
  le vote final et, le cas échéant, la procédure d''élimination des divergences entre
  les conseils.

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