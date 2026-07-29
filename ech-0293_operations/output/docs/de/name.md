---
search:
  boost: 5.0
---

# Slot: name 


_Mehrsprachige vollständige Bezeichnung._




<div data-search-exclude markdown="1">



URI: [ops:name](https://ch.paf.link/schema/operations/name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |  no  |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MultilingualString](MultilingualString.md) |
| Domäne von | [Legislature](Legislature.md), [Session](Session.md), [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: name
annotations:
  description_de:
    tag: description_de
    value: 'Mehrsprachige vollständige Bezeichnung.

      '
  description_fr:
    tag: description_fr
    value: 'Désignation complète multilingue.

      '
description: 'Mehrsprachige vollständige Bezeichnung.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Session
- Meeting
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>