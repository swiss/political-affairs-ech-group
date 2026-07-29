---
search:
  boost: 5.0
---

# Slot: agenda_item_number 


_Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern)._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_number](https://ch.paf.link/schema/operations/agenda_item_number)
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












## LinkML-Quelle

<details>
```yaml
name: agenda_item_number
annotations:
  description_de:
    tag: description_de
    value: 'Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern).

      '
  description_fr:
    tag: description_fr
    value: 'Numéro d''ordre du point de l''ordre du jour (type chaîne, afin de permettre
      les chiffres romains).

      '
description: 'Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>