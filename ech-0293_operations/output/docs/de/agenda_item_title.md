---
search:
  boost: 5.0
---

# Slot: agenda_item_title 


_Titel des Traktandums._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_title](https://ch.paf.link/schema/operations/agenda_item_title)
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
| Wertebereich | [MultilingualString](MultilingualString.md) |
| Domäne von | [AgendaItem](AgendaItem.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: agenda_item_title
annotations:
  description_de:
    tag: description_de
    value: 'Titel des Traktandums.

      '
  description_fr:
    tag: description_fr
    value: 'Titre du point de l''ordre du jour.

      '
description: 'Titel des Traktandums.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>