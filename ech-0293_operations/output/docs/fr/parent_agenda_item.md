---
search:
  boost: 5.0
---

# Slot: parent_agenda_item 


_Identifiant du point de l'ordre du jour auquel cet enregistrement se rattache. Pour un point de l'ordre du jour, il forme une hiérarchie de points — p. ex. un groupe « Délibérations législatives » avec les sous-points « Loi sur l'énergie (discussion par article) » et « Loi sur l'énergie (vote final) » ; pour une intervention, il désigne le point sous lequel elle a été faite._




<div data-search-exclude markdown="1">



URI: [ops:parent_agenda_item](https://ch.paf.link/schema/operations/parent_agenda_item)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance, tel que planifié à l'avance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [IsAgendaItem](IsAgendaItem.md), [Speech](Speech.md) |

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
description: 'Identifiant du point de l''ordre du jour auquel cet enregistrement se
  rattache. Pour un point de l''ordre du jour, il forme une hiérarchie de points —
  p. ex. un groupe « Délibérations législatives » avec les sous-points « Loi sur l''énergie
  (discussion par article) » et « Loi sur l''énergie (vote final) » ; pour une intervention,
  il désigne le point sous lequel elle a été faite.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
- Speech
range: string

```
</details></div>