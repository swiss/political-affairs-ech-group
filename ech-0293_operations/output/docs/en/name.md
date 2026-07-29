---
search:
  boost: 5.0
---

# Slot: name 


_Multilingual full designation._




<div data-search-exclude markdown="1">



URI: [ops:name](https://ch.paf.link/schema/operations/name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | A parliamentary session that groups multiple meetings and spans a specific ti... |  no  |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualString](MultilingualString.md) |
| Domain Of | [Legislature](Legislature.md), [Session](Session.md), [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: name
annotations:
  description_de:
    tag: description_de
    value: 'Mehrsprachige vollständige Bezeichnung.

      '
  description_fr:
    tag: description_fr
    value: 'Désignation complète multilingue.

      '
description: 'Multilingual full designation.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Session
- Meeting
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>