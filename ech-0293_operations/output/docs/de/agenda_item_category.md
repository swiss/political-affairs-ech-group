---
search:
  boost: 5.0
---

# Slot: agenda_item_category 


_Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden)._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_category](https://ch.paf.link/schema/operations/agenda_item_category)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [AgendaItem](AgendaItem.md) |

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
    value: 'Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement,
      technische Traktanden).

      '
  description_fr:
    tag: description_fr
    value: 'Catégorie pour les points de l''ordre du jour regroupés (p. ex. introduction,
      par département, points techniques).

      '
description: 'Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement,
  technische Traktanden).

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