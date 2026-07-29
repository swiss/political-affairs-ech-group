---
search:
  boost: 5.0
---

# Slot: speaking_actor_id 


_Der Sprecher oder die Sprecherin bzw. die Departementsvorsteherin oder der Departementsvorsteher für das Traktandum._




<div data-search-exclude markdown="1">



URI: [ops:speaking_actor_id](https://ch.paf.link/schema/operations/speaking_actor_id)
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
name: speaking_actor_id
annotations:
  description_de:
    tag: description_de
    value: 'Der Sprecher oder die Sprecherin bzw. die Departementsvorsteherin oder
      der Departementsvorsteher für das Traktandum.

      '
  description_fr:
    tag: description_fr
    value: 'La ou le porte-parole ou la cheffe ou le chef du département pour le point
      de l''ordre du jour.

      '
description: 'Der Sprecher oder die Sprecherin bzw. die Departementsvorsteherin oder
  der Departementsvorsteher für das Traktandum.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>