---
search:
  boost: 5.0
---

# Slot: speeches 


_Collection of speech records_



<div data-search-exclude markdown="1">



URI: [ops:speech](https://ch.paf.link/schema/operations/speech)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |
| [Protocol](Protocol.md) | [en] The minutes of a meeting, recorded after the meeting |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Speech](Speech.md) |
| Domain Of | [Container](Container.md), [Protocol](Protocol.md) |
| Slot URI | [ops:speech](https://ch.paf.link/schema/operations/speech) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: speeches
description: Collection of speech records
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