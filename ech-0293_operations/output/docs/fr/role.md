---
search:
  boost: 5.0
---

# Slot: role 


_Rôle de la personne (p. ex. rapporteuse ou rapporteur de commission)._




<div data-search-exclude markdown="1">



URI: [ops:role](https://ch.paf.link/schema/operations/role)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Speech](Speech.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| speaker |





## Source LinkML

<details>
```yaml
name: role
annotations:
  description_de:
    tag: description_de
    value: 'Rolle der Person (z.B. Kommissionssprecherin oder Kommissionssprecher).

      '
  description_fr:
    tag: description_fr
    value: 'Rôle de la personne (p. ex. rapporteuse ou rapporteur de commission).

      '
description: 'Rôle de la personne (p. ex. rapporteuse ou rapporteur de commission).

  '
examples:
- value: speaker
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>