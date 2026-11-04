---
search:
  boost: 5.0
---

# Slot: actor_name 


_Name of the political body in plain text (e.g., Nationalrat), in addition to the reference `group_reference`._




<div data-search-exclude markdown="1">



URI: [ops:actor_name](https://ch.paf.link/schema/operations/actor_name)
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
name: actor_name
annotations:
  description_de:
    tag: description_de
    value: 'Name des politischen Organs im Klartext (z.B. Nationalrat), zusätzlich
      zur Referenz `group_reference`.

      '
  description_fr:
    tag: description_fr
    value: 'Nom de l''organe politique en clair (p. ex. Conseil national), en complément
      de la référence `group_reference`.

      '
description: 'Name of the political body in plain text (e.g., Nationalrat), in addition
  to the reference `group_reference`.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>