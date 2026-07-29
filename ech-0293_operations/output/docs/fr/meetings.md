---
search:
  boost: 5.0
---

# Slot: meetings 


_Ensemble des séances._




<div data-search-exclude markdown="1">



URI: [ops:meeting](https://ch.paf.link/schema/operations/meeting)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |  no  |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Meeting](Meeting.md) |
| Domaine de | [Container](Container.md), [Session](Session.md) |
| URI du slot | [ops:meeting](https://ch.paf.link/schema/operations/meeting) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: meetings
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Sitzungen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des séances.

      '
description: 'Ensemble des séances.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:meeting
domain_of:
- Container
- Session
range: Meeting
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>