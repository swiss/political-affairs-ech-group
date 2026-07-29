---
search:
  boost: 5.0
---

# Slot: sessions 


_Collection of session records._




<div data-search-exclude markdown="1">



URI: [ops:session](https://ch.paf.link/schema/operations/session)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Session](Session.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:session](https://ch.paf.link/schema/operations/session) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

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
description: 'Collection of session records.

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