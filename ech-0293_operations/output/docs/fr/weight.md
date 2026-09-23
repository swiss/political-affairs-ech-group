---
search:
  boost: 5.0
---

# Slot: weight 


_Poids de la voix du membre ; normalement 1. D'autres valeurs se présentent par exemple lorsqu'un membre vote aussi pour un membre absent (représentation, poids 2), dans les assemblées communales où des personnes morales disposent de plusieurs voix, ou dans des systèmes historiques où différents groupes de personnes avaient un poids de voix différent._




<div data-search-exclude markdown="1">



URI: [ops:weight](https://ch.paf.link/schema/operations/weight)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | La voix exprimée par un membre lors d'un vote |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Integer](Integer.md) |
| Domaine de | [IndividualVote](IndividualVote.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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
description: 'Poids de la voix du membre ; normalement 1. D''autres valeurs se présentent
  par exemple lorsqu''un membre vote aussi pour un membre absent (représentation,
  poids 2), dans les assemblées communales où des personnes morales disposent de plusieurs
  voix, ou dans des systèmes historiques où différents groupes de personnes avaient
  un poids de voix différent.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: integer

```
</details></div>