---
search:
  boost: 5.0
---

# Slot: state_id 


_Zustands-Identifikator (Verweis auf das Status-Enum oder auf einen eigenen Zustand)._




<div data-search-exclude markdown="1">



URI: [ops:state_id](https://ch.paf.link/schema/operations/state_id)
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
name: state_id
annotations:
  description_de:
    tag: description_de
    value: 'Zustands-Identifikator (Verweis auf das Status-Enum oder auf einen eigenen
      Zustand).

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant d''état (renvoi à l''énumération des états ou à un état propre).

      '
description: 'Zustands-Identifikator (Verweis auf das Status-Enum oder auf einen eigenen
  Zustand).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>