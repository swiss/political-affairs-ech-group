---
search:
  boost: 5.0
---

# Slot: works 


_The documents (FRBR Works) contained in the container._




<div data-search-exclude markdown="1">



URI: [meta:works](https://ch.paf.link/schema/meta/works)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkContainer](WorkContainer.md) | Container for the documents (FRBR Works) of this schema |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Work](Work.md) |
| Domain Of | [WorkContainer](WorkContainer.md) |
| Slot URI | [meta:works](https://ch.paf.link/schema/meta/works) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

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
description: 'The documents (FRBR Works) contained in the container.

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