---
search:
  boost: 5.0
---

# Slot: protocols 


_Collection of protocol records._




<div data-search-exclude markdown="1">



URI: [ops:protocol](https://ch.paf.link/schema/operations/protocol)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Protocol](Protocol.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:protocol](https://ch.paf.link/schema/operations/protocol) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: protocols
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Protokolle.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des procès-verbaux.

      '
description: 'Collection of protocol records.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:protocol
domain_of:
- Container
range: Protocol
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>