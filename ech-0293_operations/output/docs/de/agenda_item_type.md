---
search:
  boost: 5.0
---

# Slot: agenda_item_type 


_Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_type](https://ch.paf.link/schema/operations/agenda_item_type)
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
| Wertebereich | [AgendaItemTypeEnum](AgendaItemTypeEnum.md) |
| Domäne von | [AgendaItem](AgendaItem.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| item |





## LinkML-Quelle

<details>
```yaml
name: agenda_item_type
annotations:
  description_de:
    tag: description_de
    value: 'Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen.

      '
  description_fr:
    tag: description_fr
    value: 'Type de point de l''ordre du jour, distinguant les points isolés des groupes
      de points.

      '
description: 'Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen.

  '
examples:
- value: item
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: AgendaItemTypeEnum

```
</details></div>