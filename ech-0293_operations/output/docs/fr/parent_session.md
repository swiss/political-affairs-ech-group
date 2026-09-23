---
search:
  boost: 5.0
---

# Slot: parent_session 


_Identifiant de la session à laquelle la séance appartient._




<div data-search-exclude markdown="1">



URI: [ops:parent_session](https://ch.paf.link/schema/operations/parent_session)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: parent_session
annotations:
  description_de:
    tag: description_de
    value: 'Identifikator der Session, zu der die Sitzung gehört.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la session à laquelle la séance appartient.

      '
description: 'Identifiant de la session à laquelle la séance appartient.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>