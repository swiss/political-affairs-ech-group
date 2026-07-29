---
search:
  boost: 5.0
---

# Slot: actor_name 


_Name of the political body (e.g., Nationalrat)._




<div data-search-exclude markdown="1">



URI: [ops:actor_name](https://ch.paf.link/schema/operations/actor_name)
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
name: actor_name
annotations:
  description_de:
    tag: description_de
    value: 'Name des politischen Organs (z.B. Nationalrat).

      '
  description_fr:
    tag: description_fr
    value: 'Nom de l''organe politique (p. ex. Conseil national).

      '
description: 'Name of the political body (e.g., Nationalrat).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>