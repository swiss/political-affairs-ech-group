---
search:
  boost: 5.0
---

# Slot: parent_legislature 


_The legislative body in which the meeting is based._




<div data-search-exclude markdown="1">



URI: [ops:parent_legislature](https://ch.paf.link/schema/operations/parent_legislature)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | A parliamentary session that groups multiple meetings and spans a specific ti... |  no  |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |






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
name: parent_legislature
annotations:
  description_de:
    tag: description_de
    value: 'Der gesetzgebende Körper, auf dem die Sitzung basiert.

      '
  description_fr:
    tag: description_fr
    value: 'La législature dans le cadre de laquelle la séance a lieu.

      '
description: 'The legislative body in which the meeting is based.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>