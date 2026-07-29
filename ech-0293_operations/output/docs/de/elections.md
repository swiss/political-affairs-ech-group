---
search:
  boost: 5.0
---

# Slot: elections 


_Sammlung der Wahlen._




<div data-search-exclude markdown="1">



URI: [ops:election](https://ch.paf.link/schema/operations/election)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Election](Election.md) |
| Domäne von | [Container](Container.md) |
| Slot-URI | [ops:election](https://ch.paf.link/schema/operations/election) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: elections
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Wahlen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des élections.

      '
description: 'Sammlung der Wahlen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:election
domain_of:
- Container
range: Election
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>