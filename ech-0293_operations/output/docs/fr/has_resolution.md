---
search:
  boost: 5.0
---

# Slot: has_resolution 


_La décision formelle prise sur ce point de l'ordre du jour, p. ex. l'adoption de la loi sur l'énergie. Le vote sous-jacent avec son rapport de voix est saisi séparément comme Voting._




<div data-search-exclude markdown="1">



URI: [ops:has_resolution](https://ch.paf.link/schema/operations/has_resolution)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance, tel que planifié à l'avance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Resolution](Resolution.md) |
| Domaine de | [IsAgendaItem](IsAgendaItem.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: has_resolution
annotations:
  description_de:
    tag: description_de
    value: 'Der formale Beschluss zu diesem Traktandum, z.B. die Annahme des Energiegesetzes.
      Die zugrunde liegende Abstimmung mit dem Stimmenverhältnis wird separat als
      Voting erfasst.

      '
  description_fr:
    tag: description_fr
    value: 'La décision formelle prise sur ce point de l''ordre du jour, p. ex. l''adoption
      de la loi sur l''énergie. Le vote sous-jacent avec son rapport de voix est saisi
      séparément comme Voting.

      '
description: 'La décision formelle prise sur ce point de l''ordre du jour, p. ex.
  l''adoption de la loi sur l''énergie. Le vote sous-jacent avec son rapport de voix
  est saisi séparément comme Voting.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: Resolution

```
</details></div>