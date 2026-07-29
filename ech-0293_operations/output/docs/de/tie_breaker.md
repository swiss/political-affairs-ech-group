---
search:
  boost: 5.0
---

# Slot: tie_breaker 


_Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde._




<div data-search-exclude markdown="1">



URI: [ops:tie_breaker](https://ch.paf.link/schema/operations/tie_breaker)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Boolean](Boolean.md) |
| Domäne von | [Voting](Voting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: tie_breaker
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si une voix prépondérante a été utilisée lors du vote.

      '
description: 'Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: boolean

```
</details></div>