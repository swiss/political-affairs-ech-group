---
search:
  boost: 5.0
---

# Slot: group_name 


_Name of the group or body in plain text, in addition to the reference `group_id`._




<div data-search-exclude markdown="1">



URI: [ops:group_name](https://ch.paf.link/schema/operations/group_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |






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
    value: 'Name der Gruppe oder des Gremiums im Klartext, zusätzlich zur Referenz
      `group_id`.

      '
  description_fr:
    tag: description_fr
    value: 'Nom du groupe ou de l''organe en clair, en complément de la référence
      `group_id`.

      '
description: 'Name of the group or body in plain text, in addition to the reference
  `group_id`.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>