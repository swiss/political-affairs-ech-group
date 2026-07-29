---
search:
  boost: 5.0
---

# Slot: has_resolution 


_Die Resolution oder Entscheidung zu diesem Traktandum._




<div data-search-exclude markdown="1">



URI: [ops:has_resolution](https://ch.paf.link/schema/operations/has_resolution)
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
| Wertebereich | [Resolution](Resolution.md) |
| Domäne von | [AgendaItem](AgendaItem.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: has_resolution
annotations:
  description_de:
    tag: description_de
    value: 'Die Resolution oder Entscheidung zu diesem Traktandum.

      '
  description_fr:
    tag: description_fr
    value: 'La décision prise sur ce point de l''ordre du jour.

      '
description: 'Die Resolution oder Entscheidung zu diesem Traktandum.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: Resolution

```
</details></div>