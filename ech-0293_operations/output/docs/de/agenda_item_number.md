---
search:
  boost: 5.0
---

# Slot: agenda_item_number 


_Nummer des Traktandums auf der Traktandenliste, z.B. „2.1“ oder „3“ (Zeichenkette, damit auch römische Ziffern möglich sind)._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_number](https://ch.paf.link/schema/operations/agenda_item_number)
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
name: agenda_item_number
annotations:
  description_de:
    tag: description_de
    value: 'Nummer des Traktandums auf der Traktandenliste, z.B. „2.1“ oder „3“ (Zeichenkette,
      damit auch römische Ziffern möglich sind).

      '
  description_fr:
    tag: description_fr
    value: 'Numéro du point sur l''ordre du jour, p. ex. « 2.1 » ou « 3 » (chaîne
      de caractères, afin de permettre aussi les chiffres romains).

      '
description: 'Nummer des Traktandums auf der Traktandenliste, z.B. „2.1“ oder „3“
  (Zeichenkette, damit auch römische Ziffern möglich sind).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: string

```
</details></div>