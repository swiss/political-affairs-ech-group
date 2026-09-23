---
search:
  boost: 5.0
---

# Slot: state_id 


_Zustands-Identifikator des Traktandums (Verweis auf ein Status-Enum oder auf einen eigenen Zustand), z.B. pending (noch nicht behandelt), in_progress (in Beratung), completed (abgeschlossen), postponed (auf eine spätere Sitzung vertagt) oder withdrawn (zurückgezogen)._




<div data-search-exclude markdown="1">



URI: [ops:state_id](https://ch.paf.link/schema/operations/state_id)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |  no  |
| [AgendaItem](AgendaItem.md) | Ein vorgängig geplantes Traktandum einer Sitzung |  no  |
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
name: state_id
annotations:
  description_de:
    tag: description_de
    value: 'Zustands-Identifikator des Traktandums (Verweis auf ein Status-Enum oder
      auf einen eigenen Zustand), z.B. pending (noch nicht behandelt), in_progress
      (in Beratung), completed (abgeschlossen), postponed (auf eine spätere Sitzung
      vertagt) oder withdrawn (zurückgezogen).

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant d''état du point (renvoi à une énumération des états ou à
      un état propre), p. ex. pending (pas encore traité), in_progress (en délibération),
      completed (traité), postponed (renvoyé à une séance ultérieure) ou withdrawn
      (retiré).

      '
description: 'Zustands-Identifikator des Traktandums (Verweis auf ein Status-Enum
  oder auf einen eigenen Zustand), z.B. pending (noch nicht behandelt), in_progress
  (in Beratung), completed (abgeschlossen), postponed (auf eine spätere Sitzung vertagt)
  oder withdrawn (zurückgezogen).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: string

```
</details></div>