---
search:
  boost: 5.0
---

# Slot: location 


_Lieu où se tient la séance (salle physique, visioconférence ou format hybride)._




<div data-search-exclude markdown="1">



URI: [ops:location](https://ch.paf.link/schema/operations/location)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| Kantonsratssaal, Regierungsgebäude St. Gallen |
| Kommissionszimmer 301, Rathaus Bern |
| Zaunplatz, Glarus |





## Source LinkML

<details>
```yaml
name: location
annotations:
  description_de:
    tag: description_de
    value: 'Ort, an dem die Sitzung stattfindet (physischer Raum, Videokonferenz oder
      hybrides Format).

      '
  description_fr:
    tag: description_fr
    value: 'Lieu où se tient la séance (salle physique, visioconférence ou format
      hybride).

      '
description: 'Lieu où se tient la séance (salle physique, visioconférence ou format
  hybride).

  '
examples:
- value: Kantonsratssaal, Regierungsgebäude St. Gallen
- value: Kommissionszimmer 301, Rathaus Bern
- value: Zaunplatz, Glarus
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>