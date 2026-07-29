---
search:
  boost: 5.0
---

# Slot: individual_votes 


_Sammlung der Einzelstimmen._




<div data-search-exclude markdown="1">



URI: [ops:individualVote](https://ch.paf.link/schema/operations/individualVote)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [IndividualVote](IndividualVote.md) |
| Domäne von | [Container](Container.md) |
| Slot-URI | [ops:individualVote](https://ch.paf.link/schema/operations/individualVote) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: individual_votes
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Einzelstimmen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des voix individuelles.

      '
description: 'Sammlung der Einzelstimmen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:individualVote
domain_of:
- Container
range: IndividualVote
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>