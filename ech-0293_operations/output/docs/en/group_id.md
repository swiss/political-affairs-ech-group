---
search:
  boost: 5.0
---

# Slot: group_id 


_Reference to the group or body (lightweight snapshot at time of linking)._




<div data-search-exclude markdown="1">



URI: [ops:group_id](https://ch.paf.link/schema/operations/group_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GroupReference](GroupReference.md) |
| Domain Of | [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: group_id
annotations:
  description_de:
    tag: description_de
    value: 'Referenz auf die Gruppe oder das Gremium (Momentaufnahme zum Zeitpunkt
      der Verknüpfung).

      '
  description_fr:
    tag: description_fr
    value: 'Référence au groupe ou à l''organe (instantané au moment de la mise en
      relation).

      '
description: 'Reference to the group or body (lightweight snapshot at time of linking).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: GroupReference
inlined: true

```
</details></div>