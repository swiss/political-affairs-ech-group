---
search:
  boost: 5.0
---

# Slot: sessions 


_Ensemble des sessions._




<div data-search-exclude markdown="1">



URI: [ops:session](https://ch.paf.link/schema/operations/session)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Session](Session.md) |
| Domaine de | [Container](Container.md) |
| URI du slot | [ops:session](https://ch.paf.link/schema/operations/session) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: sessions
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Sessionen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des sessions.

      '
description: 'Ensemble des sessions.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:session
domain_of:
- Container
range: Session
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>