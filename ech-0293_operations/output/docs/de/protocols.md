---
search:
  boost: 5.0
---

# Slot: protocols 


_Sammlung der Protokolle._




<div data-search-exclude markdown="1">



URI: [ops:protocol](https://ch.paf.link/schema/operations/protocol)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Protocol](Protocol.md) |
| Domäne von | [Container](Container.md) |
| Slot-URI | [ops:protocol](https://ch.paf.link/schema/operations/protocol) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: protocols
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Protokolle.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des procès-verbaux.

      '
description: 'Sammlung der Protokolle.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:protocol
domain_of:
- Container
range: Protocol
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>