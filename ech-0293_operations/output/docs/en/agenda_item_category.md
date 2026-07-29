---
search:
  boost: 5.0
---

# Slot: agenda_item_category 


_Category for grouped agenda items (e.g., introduction, by department, technical agenda items)._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_category](https://ch.paf.link/schema/operations/agenda_item_category)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AgendaItem](AgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| ANNONCES ET INTERPELLATIONS |
| Budget und Finanzen |
| Gesetzgebung |





## LinkML Source

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
description: 'Category for grouped agenda items (e.g., introduction, by department,
  technical agenda items).

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