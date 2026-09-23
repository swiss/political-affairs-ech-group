---
search:
  boost: 5.0
---

# Slot: weight 


_Stimmgewicht des Mitglieds; im Normalfall 1. Andere Werte kommen etwa vor, wo ein Mitglied für ein abwesendes Mitglied mitstimmt (Stellvertretung, Gewicht 2), an Gemeindeversammlungen, an denen juristische Personen mehrere Stimmen haben, oder in historischen Systemen, in denen verschiedene Personengruppen unterschiedliches Stimmgewicht hatten._




<div data-search-exclude markdown="1">



URI: [ops:weight](https://ch.paf.link/schema/operations/weight)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | Die Stimme, die ein einzelnes Mitglied in einer Abstimmung abgibt |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Integer](Integer.md) |
| Domäne von | [IndividualVote](IndividualVote.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: weight
annotations:
  description_de:
    tag: description_de
    value: 'Stimmgewicht des Mitglieds; im Normalfall 1. Andere Werte kommen etwa
      vor, wo ein Mitglied für ein abwesendes Mitglied mitstimmt (Stellvertretung,
      Gewicht 2), an Gemeindeversammlungen, an denen juristische Personen mehrere
      Stimmen haben, oder in historischen Systemen, in denen verschiedene Personengruppen
      unterschiedliches Stimmgewicht hatten.

      '
  description_fr:
    tag: description_fr
    value: 'Poids de la voix du membre ; normalement 1. D''autres valeurs se présentent
      par exemple lorsqu''un membre vote aussi pour un membre absent (représentation,
      poids 2), dans les assemblées communales où des personnes morales disposent
      de plusieurs voix, ou dans des systèmes historiques où différents groupes de
      personnes avaient un poids de voix différent.

      '
description: 'Stimmgewicht des Mitglieds; im Normalfall 1. Andere Werte kommen etwa
  vor, wo ein Mitglied für ein abwesendes Mitglied mitstimmt (Stellvertretung, Gewicht
  2), an Gemeindeversammlungen, an denen juristische Personen mehrere Stimmen haben,
  oder in historischen Systemen, in denen verschiedene Personengruppen unterschiedliches
  Stimmgewicht hatten.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: integer

```
</details></div>