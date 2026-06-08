---
search:
  boost: 5.0
---

# Slot: text_segments 


_Collection of text segments (e.g. verbatim protocol)_



<div data-search-exclude markdown="1">



URI: [ops:textSegment](https://ch.paf.link/schema/operations/textSegment)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protocol](Protocol.md) | [en] The minutes of a meeting, recorded after the meeting |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TextSegment](TextSegment.md) |
| Domain Of | [Protocol](Protocol.md) |
| Slot URI | [ops:textSegment](https://ch.paf.link/schema/operations/textSegment) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: text_segments
description: Collection of text segments (e.g. verbatim protocol)
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:textSegment
domain_of:
- Protocol
range: TextSegment
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>