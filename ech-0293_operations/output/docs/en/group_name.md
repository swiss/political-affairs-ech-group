---
search:
  boost: 5.0
---

# Slot: group_name 


_Name of the group or body._




<div data-search-exclude markdown="1">



URI: [ops:group_name](https://ch.paf.link/schema/operations/group_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: group_name
annotations:
  description_de:
    tag: description_de
    value: 'Name der Gruppe oder des Gremiums.

      '
  description_fr:
    tag: description_fr
    value: 'Nom du groupe ou de l''organe.

      '
description: 'Name of the group or body.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>