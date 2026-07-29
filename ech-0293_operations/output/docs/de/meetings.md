---
search:
  boost: 5.0
---

# Slot: meetings 


_Sammlung der Sitzungen._




<div data-search-exclude markdown="1">



URI: [ops:meeting](https://ch.paf.link/schema/operations/meeting)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |  no  |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Meeting](Meeting.md) |
| Domäne von | [Container](Container.md), [Session](Session.md) |
| Slot-URI | [ops:meeting](https://ch.paf.link/schema/operations/meeting) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: meetings
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Sitzungen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des séances.

      '
description: 'Sammlung der Sitzungen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:meeting
domain_of:
- Container
- Session
range: Meeting
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>