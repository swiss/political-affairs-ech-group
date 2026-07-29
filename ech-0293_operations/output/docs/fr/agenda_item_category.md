---
search:
  boost: 5.0
---

# Slot: agenda_item_category 


_Catégorie pour les points de l'ordre du jour regroupés (p. ex. introduction, par département, points techniques)._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_category](https://ch.paf.link/schema/operations/agenda_item_category)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [AgendaItem](AgendaItem.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| ANNONCES ET INTERPELLATIONS |
| Budget und Finanzen |
| Gesetzgebung |





## Source LinkML

<details>
```yaml
name: agenda_item_category
annotations:
  description_de:
    tag: description_de
    value: 'Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement,
      technische Traktanden).

      '
  description_fr:
    tag: description_fr
    value: 'Catégorie pour les points de l''ordre du jour regroupés (p. ex. introduction,
      par département, points techniques).

      '
description: 'Catégorie pour les points de l''ordre du jour regroupés (p. ex. introduction,
  par département, points techniques).

  '
examples:
- value: ANNONCES ET INTERPELLATIONS
- value: Budget und Finanzen
- value: Gesetzgebung
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>