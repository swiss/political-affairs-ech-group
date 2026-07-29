---
search:
  boost: 5.0
---

# Slot: reason 


_Motif de l'absence ou du retard (texte libre, multilingue)._




<div data-search-exclude markdown="1">



URI: [ops:reason](https://ch.paf.link/schema/operations/reason)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | Constatation individuelle de la présence d'une personne à une séance (rattach... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [MultilingualString](MultilingualString.md) |
| Domaine de | [IndividualAttendance](IndividualAttendance.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: reason
annotations:
  description_de:
    tag: description_de
    value: 'Grund für Abwesenheit oder Verspätung (Freitext, mehrsprachig).

      '
  description_fr:
    tag: description_fr
    value: 'Motif de l''absence ou du retard (texte libre, multilingue).

      '
description: 'Motif de l''absence ou du retard (texte libre, multilingue).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualAttendance
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>