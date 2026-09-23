---
search:
  boost: 5.0
---

# Slot: majority_count 


_Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind._




<div data-search-exclude markdown="1">



URI: [ops:majority_count](https://ch.paf.link/schema/operations/majority_count)
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
name: majority_count
annotations:
  description_de:
    tag: description_de
    value: 'Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich
      sind.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre de voix requis pour atteindre le seuil de majorité déterminant.

      '
description: 'Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich
  sind.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: integer

```
</details></div>