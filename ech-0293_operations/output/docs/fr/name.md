---
search:
  boost: 5.0
---

# Slot: name 


_Désignation complète multilingue._




<div data-search-exclude markdown="1">



URI: [ops:name](https://ch.paf.link/schema/operations/name)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |  no  |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [MultilingualString](MultilingualString.md) |
| Domaine de | [Legislature](Legislature.md), [Session](Session.md), [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: name
annotations:
  description_de:
    tag: description_de
    value: 'Mehrsprachige vollständige Bezeichnung.

      '
  description_fr:
    tag: description_fr
    value: 'Désignation complète multilingue.

      '
description: 'Désignation complète multilingue.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Session
- Meeting
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>