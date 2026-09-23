---
search:
  boost: 5.0
---

# Slot: agenda_item_category 


_Freie Kategorisierung des Traktandums nach Inhalt oder Gruppierung, z.B. „Gesetzgebung“, „Budget und Finanzen“, „Interpellationen und Anfragen“, „Wahlen“, nach Departement oder einleitende und technische Traktanden. Die Kategorisierung ist nicht standardisiert und kann je nach Föderaleinheit variieren._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_category](https://ch.paf.link/schema/operations/agenda_item_category)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |  no  |
| [AgendaItem](AgendaItem.md) | Ein vorgängig geplantes Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [IsAgendaItem](IsAgendaItem.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| ANNONCES ET INTERPELLATIONS |
| Budget und Finanzen |
| Gesetzgebung |





## LinkML-Quelle

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
description: 'Freie Kategorisierung des Traktandums nach Inhalt oder Gruppierung,
  z.B. „Gesetzgebung“, „Budget und Finanzen“, „Interpellationen und Anfragen“, „Wahlen“,
  nach Departement oder einleitende und technische Traktanden. Die Kategorisierung
  ist nicht standardisiert und kann je nach Föderaleinheit variieren.

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