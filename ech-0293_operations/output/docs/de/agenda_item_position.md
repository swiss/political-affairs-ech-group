---
search:
  boost: 5.0
---

# Slot: agenda_item_position 


_Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_position](https://ch.paf.link/schema/operations/agenda_item_position)
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
| Wertebereich | [Integer](Integer.md) |
| Domäne von | [AgendaItem](AgendaItem.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: agenda_item_position
annotations:
  description_de:
    tag: description_de
    value: 'Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge.

      '
  description_fr:
    tag: description_fr
    value: 'Position (nombre entier) du point de l''ordre du jour dans le déroulement
      de la séance.

      '
description: 'Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: integer

```
</details></div>