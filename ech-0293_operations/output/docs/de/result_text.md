---
search:
  boost: 5.0
---

# Slot: result_text 


_Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. „Mit 78 Stimmen angenommen“._




<div data-search-exclude markdown="1">



URI: [ops:result_text](https://ch.paf.link/schema/operations/result_text)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Voting](Voting.md), [Election](Election.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25, Auswahl C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern). |
| Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen |
| Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt |





## LinkML-Quelle

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
description: 'Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. „Mit
  78 Stimmen angenommen“.

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