---
search:
  boost: 5.0
---

# Slot: weight 


_Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B. in Fällen, in denen eine Person mehrere Stimmen hat)._




<div data-search-exclude markdown="1">



URI: [ops:weight](https://ch.paf.link/schema/operations/weight)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens |  no  |






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
    value: 'Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B.
      in Fällen, in denen eine Person mehrere Stimmen hat).

      '
  description_fr:
    tag: description_fr
    value: 'Le nombre de voix dont dispose la personne, le cas échéant (p. ex. lorsqu''une
      personne détient plusieurs voix).

      '
description: 'Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B.
  in Fällen, in denen eine Person mehrere Stimmen hat).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: integer

```
</details></div>