---
search:
  boost: 5.0
---

# Slot: agenda_item_position 


_Ganzzahlige Position des Traktandums im Sitzungsablauf, massgebend für Sortierung und Darstellung._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_position](https://ch.paf.link/schema/operations/agenda_item_position)
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
| Wertebereich | [Integer](Integer.md) |
| Domäne von | [IsAgendaItem](IsAgendaItem.md) |

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
    value: 'Ganzzahlige Position des Traktandums im Sitzungsablauf, massgebend für
      Sortierung und Darstellung.

      '
  description_fr:
    tag: description_fr
    value: 'Position entière du point dans le déroulement de la séance, déterminante
      pour le tri et l''affichage.

      '
description: 'Ganzzahlige Position des Traktandums im Sitzungsablauf, massgebend für
  Sortierung und Darstellung.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: integer

```
</details></div>