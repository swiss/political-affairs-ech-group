---
search:
  boost: 5.0
---

# Slot: parent_agenda_item 


_Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf._




<div data-search-exclude markdown="1">



URI: [ops:parent_agenda_item](https://ch.paf.link/schema/operations/parent_agenda_item)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |  no  |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
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












## LinkML-Quelle

<details>
```yaml
name: parent_agenda_item
annotations:
  description_de:
    tag: description_de
    value: 'Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf.

      '
  description_fr:
    tag: description_fr
    value: 'Au besoin, ce slot permet de construire une hiérarchie de points de l''ordre
      du jour.

      '
description: 'Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: string

```
</details></div>