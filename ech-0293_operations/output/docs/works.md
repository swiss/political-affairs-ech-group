---
search:
  boost: 5.0
---

# Slot: works 

<div data-search-exclude markdown="1">



URI: [meta:works](https://ch.paf.link/schema/meta/works)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkContainer](WorkContainer.md) |  |  no  |






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