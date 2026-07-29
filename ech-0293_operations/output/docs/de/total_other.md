---
search:
  boost: 5.0
---

# Slot: total_other 


_Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B. 5 Knöpfe in Zürich)._




<div data-search-exclude markdown="1">



URI: [ops:total_other](https://ch.paf.link/schema/operations/total_other)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [TotalOther](TotalOther.md) |
| Domäne von | [Voting](Voting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: total_other
annotations:
  description_de:
    tag: description_de
    value: 'Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B.
      5 Knöpfe in Zürich).

      '
  description_fr:
    tag: description_fr
    value: 'Utilisé lorsque plusieurs options sont soumises au vote (p. ex. 5 boutons
      à Zurich).

      '
description: 'Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden
  (z.B. 5 Knöpfe in Zürich).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: TotalOther
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>