---
search:
  boost: 5.0
---

# Slot: state_name 


_Abweichende, freitextliche Statusbezeichnung, wo die Status-Aufzählung nicht genügt._




<div data-search-exclude markdown="1">



URI: [ops:state_name](https://ch.paf.link/schema/operations/state_name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  yes  |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |  no  |
| [AgendaItem](AgendaItem.md) | Ein vorgängig geplantes Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: state_name
annotations:
  description_de:
    tag: description_de
    value: 'Abweichende, freitextliche Statusbezeichnung, wo die Status-Aufzählung
      nicht genügt.

      '
  description_fr:
    tag: description_fr
    value: 'Désignation de statut divergente, en texte libre, là où l''énumération
      des statuts ne suffit pas.

      '
description: 'Abweichende, freitextliche Statusbezeichnung, wo die Status-Aufzählung
  nicht genügt.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- IsAgendaItem
range: string

```
</details></div>