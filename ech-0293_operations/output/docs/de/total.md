---
search:
  boost: 5.0
---

# Slot: total 


_Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen._




<div data-search-exclude markdown="1">



URI: [ops:total](https://ch.paf.link/schema/operations/total)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Eine Abstimmung über eine Sachfrage: der Abstimmungsgegenstand (Frage), das V... |  no  |
| [Election](Election.md) | Eine Wahl, mit der ein parlamentarisches Organ eine oder mehrere Personen für... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Integer](Integer.md) |
| Domäne von | [Voting](Voting.md), [Election](Election.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: total
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de voix, sans les absents ni la voix de la présidence.

      '
description: 'Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: integer

```
</details></div>