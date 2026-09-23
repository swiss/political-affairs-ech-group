---
search:
  boost: 5.0
---

# Slot: state_id 


_Identifiant d'état du point (renvoi à une énumération des états ou à un état propre), p. ex. pending (pas encore traité), in_progress (en délibération), completed (traité), postponed (renvoyé à une séance ultérieure) ou withdrawn (retiré)._




<div data-search-exclude markdown="1">



URI: [ops:state_id](https://ch.paf.link/schema/operations/state_id)
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
| Plage | [String](String.md) |
| Domaine de | [IsAgendaItem](IsAgendaItem.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: state_id
annotations:
  description_de:
    tag: description_de
    value: 'Zustands-Identifikator des Traktandums (Verweis auf ein Status-Enum oder
      auf einen eigenen Zustand), z.B. pending (noch nicht behandelt), in_progress
      (in Beratung), completed (abgeschlossen), postponed (auf eine spätere Sitzung
      vertagt) oder withdrawn (zurückgezogen).

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant d''état du point (renvoi à une énumération des états ou à
      un état propre), p. ex. pending (pas encore traité), in_progress (en délibération),
      completed (traité), postponed (renvoyé à une séance ultérieure) ou withdrawn
      (retiré).

      '
description: 'Identifiant d''état du point (renvoi à une énumération des états ou
  à un état propre), p. ex. pending (pas encore traité), in_progress (en délibération),
  completed (traité), postponed (renvoyé à une séance ultérieure) ou withdrawn (retiré).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: string

```
</details></div>