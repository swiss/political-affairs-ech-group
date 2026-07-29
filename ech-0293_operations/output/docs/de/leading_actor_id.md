---
search:
  boost: 5.0
---

# Slot: leading_actor_id 


_Das federführende Departement für das Traktandum._




<div data-search-exclude markdown="1">



URI: [ops:leading_actor_id](https://ch.paf.link/schema/operations/leading_actor_id)
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
name: leading_actor_id
annotations:
  description_de:
    tag: description_de
    value: 'Das federführende Departement für das Traktandum.

      '
  description_fr:
    tag: description_fr
    value: 'Le département responsable du point de l''ordre du jour.

      '
description: 'Das federführende Departement für das Traktandum.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>