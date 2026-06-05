---
search:
  boost: 5.0
---

# Slot: sessions 

<div data-search-exclude markdown="1">



URI: [tutorial:session](https://ch.paf.link/schema/tutorial/session)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Session](Session.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [tutorial:session](https://ch.paf.link/schema/tutorial/session) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: sessions
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: tutorial:session
domain_of:
- Container
range: Session
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>