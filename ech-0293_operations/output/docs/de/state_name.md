---
search:
  boost: 5.0
---

# Slot: state_name 


_Benutzerdefinierte Zustandsbeschreibung für die Sitzung._




<div data-search-exclude markdown="1">



URI: [ops:state_name](https://ch.paf.link/schema/operations/state_name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Meeting](Meeting.md), [AgendaItem](AgendaItem.md) |

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
    value: 'Benutzerdefinierte Zustandsbeschreibung für die Sitzung.

      '
  description_fr:
    tag: description_fr
    value: 'Description personnalisée de l''état de la séance.

      '
description: 'Benutzerdefinierte Zustandsbeschreibung für die Sitzung.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- AgendaItem
range: string

```
</details></div>