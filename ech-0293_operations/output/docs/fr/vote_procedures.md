---
search:
  boost: 5.0
---

# Slot: vote_procedures 


_Modalités du vote, p. ex. vote secret ou vote ouvert._




<div data-search-exclude markdown="1">



URI: [ops:vote_procedures](https://ch.paf.link/schema/operations/vote_procedures)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Resolution](Resolution.md) | Une décision prise sur un point de l'ordre du jour, y compris les procédures ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Resolution](Resolution.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: vote_procedures
annotations:
  description_de:
    tag: description_de
    value: 'Verfahren für die Abstimmung, wie geheime Abstimmung oder offene Abstimmung.

      '
  description_fr:
    tag: description_fr
    value: 'Modalités du vote, p. ex. vote secret ou vote ouvert.

      '
description: 'Modalités du vote, p. ex. vote secret ou vote ouvert.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Resolution
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>