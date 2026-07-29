---
search:
  boost: 5.0
---

# Slot: votings 


_Ensemble des votes._




<div data-search-exclude markdown="1">



URI: [ops:voting](https://ch.paf.link/schema/operations/voting)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |  no  |
| [Protocol](Protocol.md) | Le procès-verbal établi après la séance |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Voting](Voting.md) |
| Domaine de | [Container](Container.md), [Protocol](Protocol.md) |
| URI du slot | [ops:voting](https://ch.paf.link/schema/operations/voting) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: votings
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Abstimmungen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des votes.

      '
description: 'Ensemble des votes.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:voting
domain_of:
- Container
- Protocol
range: Voting
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>