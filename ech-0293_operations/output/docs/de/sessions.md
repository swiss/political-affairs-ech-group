---
search:
  boost: 5.0
---

# Slot: sessions 


_Sammlung der Sessionen._




<div data-search-exclude markdown="1">



URI: [ops:session](https://ch.paf.link/schema/operations/session)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Session](Session.md) |
| Domäne von | [Container](Container.md) |
| Slot-URI | [ops:session](https://ch.paf.link/schema/operations/session) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: sessions
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Sessionen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des sessions.

      '
description: 'Sammlung der Sessionen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:session
domain_of:
- Container
range: Session
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>