---
search:
  boost: 5.0
---

# Slot: votings 


_Sammlung der Abstimmungen._




<div data-search-exclude markdown="1">



URI: [ops:voting](https://ch.paf.link/schema/operations/voting)
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
| Wertebereich | [Voting](Voting.md) |
| Domäne von | [Container](Container.md), [Protocol](Protocol.md) |
| Slot-URI | [ops:voting](https://ch.paf.link/schema/operations/voting) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: votings
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Abstimmungen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des votes.

      '
description: 'Sammlung der Abstimmungen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:voting
domain_of:
- Container
- Protocol
range: Voting
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>