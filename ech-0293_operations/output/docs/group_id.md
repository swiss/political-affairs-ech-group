---
search:
  boost: 5.0
---

# Slot: group_id 


_[en] Reference to the group or body (lightweight snapshot at time of linking)._

_[de] Referenz auf die Gruppe oder das Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung)._

__



<div data-search-exclude markdown="1">



URI: [ops:group_id](https://ch.paf.link/schema/operations/group_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






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
description: '[en] Reference to the group or body (lightweight snapshot at time of
  linking).

  [de] Referenz auf die Gruppe oder das Gremium (leichtgewichtiger Snapshot zum Zeitpunkt
  der Verknüpfung).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: GroupReference
inlined: true

```
</details></div>