---
search:
  boost: 5.0
---

# Slot: speeches 


_Ensemble des interventions._




<div data-search-exclude markdown="1">



URI: [ops:speech](https://ch.paf.link/schema/operations/speech)
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
| Plage | [Speech](Speech.md) |
| Domaine de | [Container](Container.md), [Protocol](Protocol.md) |
| URI du slot | [ops:speech](https://ch.paf.link/schema/operations/speech) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: speeches
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Wortmeldungen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des interventions.

      '
description: 'Ensemble des interventions.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:speech
domain_of:
- Container
- Protocol
range: Speech
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>