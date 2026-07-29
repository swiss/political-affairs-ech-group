---
search:
  boost: 5.0
---

# Slot: result_text 


_Texte libre décrivant le résultat du vote, p. ex. « Accepté par 78 voix »._




<div data-search-exclude markdown="1">



URI: [ops:result_text](https://ch.paf.link/schema/operations/result_text)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Voting](Voting.md), [Election](Election.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25, Auswahl C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern). |
| Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen |
| Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt |





## Source LinkML

<details>
```yaml
name: result_text
annotations:
  description_de:
    tag: description_de
    value: 'Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. „Mit 78
      Stimmen angenommen“.

      '
  description_fr:
    tag: description_fr
    value: 'Texte libre décrivant le résultat du vote, p. ex. « Accepté par 78 voix
      ».

      '
description: 'Texte libre décrivant le résultat du vote, p. ex. « Accepté par 78 voix
  ».

  '
examples:
- value: 'Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25,
    Auswahl C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern).'
- value: Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen
- value: Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: string

```
</details></div>