---
search:
  boost: 5.0
---

# Slot: works 


_Les documents (FRBR Works) contenus dans le conteneur._




<div data-search-exclude markdown="1">



URI: [meta:works](https://ch.paf.link/schema/meta/works)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [WorkContainer](WorkContainer.md) | Conteneur pour les documents (FRBR Works) de ce schéma |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Work](Work.md) |
| Domaine de | [WorkContainer](WorkContainer.md) |
| URI du slot | [meta:works](https://ch.paf.link/schema/meta/works) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: works
annotations:
  description_de:
    tag: description_de
    value: 'Die im Container enthaltenen Dokumente (FRBR Works).

      '
  description_fr:
    tag: description_fr
    value: 'Les documents (FRBR Works) contenus dans le conteneur.

      '
description: 'Les documents (FRBR Works) contenus dans le conteneur.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:works
domain_of:
- WorkContainer
range: Work
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>