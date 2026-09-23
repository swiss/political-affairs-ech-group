---
search:
  boost: 5.0
---

# Slot: tie_breaker 


_Indique si le résultat a été obtenu, en cas d'égalité des voix, par la voix prépondérante de la présidente ou du président._




<div data-search-exclude markdown="1">



URI: [ops:tie_breaker](https://ch.paf.link/schema/operations/tie_breaker)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Un vote sur une question matérielle : l'objet du vote (la question), la procé... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Boolean](Boolean.md) |
| Domaine de | [Voting](Voting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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
description: 'Indique si le résultat a été obtenu, en cas d''égalité des voix, par
  la voix prépondérante de la présidente ou du président.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: boolean

```
</details></div>