---
search:
  boost: 5.0
---

# Slot: tie_breaker 


_Gibt an, ob das Ergebnis bei Stimmengleichheit durch den Stichentscheid der Präsidentin oder des Präsidenten zustande kam._




<div data-search-exclude markdown="1">



URI: [ops:tie_breaker](https://ch.paf.link/schema/operations/tie_breaker)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Eine Abstimmung über eine Sachfrage: der Abstimmungsgegenstand (Frage), das V... |  no  |






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
    value: 'Gibt an, ob das Ergebnis bei Stimmengleichheit durch den Stichentscheid
      der Präsidentin oder des Präsidenten zustande kam.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si le résultat a été obtenu, en cas d''égalité des voix, par la
      voix prépondérante de la présidente ou du président.

      '
description: 'Gibt an, ob das Ergebnis bei Stimmengleichheit durch den Stichentscheid
  der Präsidentin oder des Präsidenten zustande kam.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: boolean

```
</details></div>