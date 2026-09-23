---
search:
  boost: 5.0
---

# Slot: agenda_item_category 


_Free categorisation of the agenda item by content or grouping, e.g. "Gesetzgebung", "Budget und Finanzen", "Interpellationen und Anfragen", "Wahlen", by department, or introductory and technical items. The categorisation is not standardised and may vary between federal units._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_category](https://ch.paf.link/schema/operations/agenda_item_category)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | A mixin class that provides the elements of an agenda item: designation, type... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting as planned beforehand |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [IsAgendaItem](IsAgendaItem.md) |

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
    value: 'Freie Kategorisierung des Traktandums nach Inhalt oder Gruppierung, z.B.
      „Gesetzgebung“, „Budget und Finanzen“, „Interpellationen und Anfragen“, „Wahlen“,
      nach Departement oder einleitende und technische Traktanden. Die Kategorisierung
      ist nicht standardisiert und kann je nach Föderaleinheit variieren.

      '
  description_fr:
    tag: description_fr
    value: 'Catégorisation libre du point selon son contenu ou son regroupement, p.
      ex. « Législation », « Budget et finances », « Interpellations et questions
      », « Élections », par département, ou points introductifs et techniques. La
      catégorisation n''est pas standardisée et peut varier selon l''unité fédérale.

      '
description: 'Free categorisation of the agenda item by content or grouping, e.g.
  "Gesetzgebung", "Budget und Finanzen", "Interpellationen und Anfragen", "Wahlen",
  by department, or introductory and technical items. The categorisation is not standardised
  and may vary between federal units.

  '
examples:
- value: ANNONCES ET INTERPELLATIONS
- value: Budget und Finanzen
- value: Gesetzgebung
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: string

```
</details></div>