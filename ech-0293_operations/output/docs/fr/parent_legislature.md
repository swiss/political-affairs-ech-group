---
search:
  boost: 5.0
---

# Slot: parent_legislature 


_La législature dans le cadre de laquelle la séance a lieu._




<div data-search-exclude markdown="1">



URI: [ops:parent_legislature](https://ch.paf.link/schema/operations/parent_legislature)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: parent_legislature
annotations:
  description_de:
    tag: description_de
    value: 'Der gesetzgebende Körper, auf dem die Sitzung basiert.

      '
  description_fr:
    tag: description_fr
    value: 'La législature dans le cadre de laquelle la séance a lieu.

      '
description: 'La législature dans le cadre de laquelle la séance a lieu.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>