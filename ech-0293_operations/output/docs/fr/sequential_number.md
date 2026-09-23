---
search:
  boost: 5.0
---

# Slot: sequential_number 


_Numéro d'ordre de la session ou de la séance sous forme de nombre entier, utilisé pour le tri._




<div data-search-exclude markdown="1">



URI: [ops:sequential_number](https://ch.paf.link/schema/operations/sequential_number)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Session](Session.md) | Une session : une période de séances continue au sein d'une législature |  no  |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Integer](Integer.md) |
| Domaine de | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: sequential_number
annotations:
  description_de:
    tag: description_de
    value: 'Laufende Nummer der Session oder Sitzung als Ganzzahl, die zur Sortierung
      verwendet wird.

      '
  description_fr:
    tag: description_fr
    value: 'Numéro d''ordre de la session ou de la séance sous forme de nombre entier,
      utilisé pour le tri.

      '
description: 'Numéro d''ordre de la session ou de la séance sous forme de nombre entier,
  utilisé pour le tri.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: integer

```
</details></div>