---
search:
  boost: 5.0
---

# Slot: speeches 


_Sammlung der Wortmeldungen._




<div data-search-exclude markdown="1">



URI: [ops:speech](https://ch.paf.link/schema/operations/speech)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |  no  |
| [Protocol](Protocol.md) | Das nach der Sitzung erstellte Protokoll |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Speech](Speech.md) |
| Domäne von | [Container](Container.md), [Protocol](Protocol.md) |
| Slot-URI | [ops:speech](https://ch.paf.link/schema/operations/speech) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: speeches
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Wortmeldungen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des interventions.

      '
description: 'Sammlung der Wortmeldungen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:speech
domain_of:
- Container
- Protocol
range: Speech
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>