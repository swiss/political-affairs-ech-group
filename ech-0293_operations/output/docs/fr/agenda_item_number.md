---
search:
  boost: 5.0
---

# Slot: agenda_item_number 


_Numéro du point sur l'ordre du jour, p. ex. « 2.1 » ou « 3 » (chaîne de caractères, afin de permettre aussi les chiffres romains)._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_number](https://ch.paf.link/schema/operations/agenda_item_number)
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
name: agenda_item_number
annotations:
  description_de:
    tag: description_de
    value: 'Nummer des Traktandums auf der Traktandenliste, z.B. „2.1“ oder „3“ (Zeichenkette,
      damit auch römische Ziffern möglich sind).

      '
  description_fr:
    tag: description_fr
    value: 'Numéro du point sur l''ordre du jour, p. ex. « 2.1 » ou « 3 » (chaîne
      de caractères, afin de permettre aussi les chiffres romains).

      '
description: 'Numéro du point sur l''ordre du jour, p. ex. « 2.1 » ou « 3 » (chaîne
  de caractères, afin de permettre aussi les chiffres romains).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: string

```
</details></div>