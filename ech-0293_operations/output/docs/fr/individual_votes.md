---
search:
  boost: 5.0
---

# Slot: individual_votes 


_Ensemble des voix individuelles._




<div data-search-exclude markdown="1">



URI: [ops:individualVote](https://ch.paf.link/schema/operations/individualVote)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [IndividualVote](IndividualVote.md) |
| Domaine de | [Container](Container.md) |
| URI du slot | [ops:individualVote](https://ch.paf.link/schema/operations/individualVote) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: individual_votes
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Einzelstimmen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des voix individuelles.

      '
description: 'Ensemble des voix individuelles.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:individualVote
domain_of:
- Container
range: IndividualVote
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>