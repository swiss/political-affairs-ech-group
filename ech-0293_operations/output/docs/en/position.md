---
search:
  boost: 5.0
---

# Slot: position 


_Integer position within the superordinate sequence, e.g. of a session within the legislature._




<div data-search-exclude markdown="1">



URI: [ops:position](https://ch.paf.link/schema/operations/position)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | A session: a contiguous period of sittings within a legislature |  no  |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: position
annotations:
  description_de:
    tag: description_de
    value: 'Ganzzahlige Position innerhalb der übergeordneten Reihenfolge, z.B. einer
      Session innerhalb der Legislaturperiode.

      '
  description_fr:
    tag: description_fr
    value: 'Position entière au sein de la séquence supérieure, p. ex. d''une session
      au sein de la législature.

      '
description: 'Integer position within the superordinate sequence, e.g. of a session
  within the legislature.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>