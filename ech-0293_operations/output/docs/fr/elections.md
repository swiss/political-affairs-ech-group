---
search:
  boost: 5.0
---

# Slot: elections 


_Ensemble des élections._




<div data-search-exclude markdown="1">



URI: [ops:election](https://ch.paf.link/schema/operations/election)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Election](Election.md) |
| Domaine de | [Container](Container.md) |
| URI du slot | [ops:election](https://ch.paf.link/schema/operations/election) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: elections
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Wahlen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des élections.

      '
description: 'Ensemble des élections.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:election
domain_of:
- Container
range: Election
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>