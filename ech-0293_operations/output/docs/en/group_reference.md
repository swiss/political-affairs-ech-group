---
search:
  boost: 5.0
---

# Slot: group_reference 


_Reference to a group or body according to eCH-0294 with snapshot data at time of linking._




<div data-search-exclude markdown="1">



URI: [actors:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Term of office of a parliament as a legislative assembly |  yes  |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  yes  |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  yes  |
| [Election](Election.md) | An election in which a parliamentary body appoints one or several persons to ... |  yes  |
| [Attendance](Attendance.md) | Aggregated attendance record for a meeting (number of members present, absent... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GroupReference](GroupReference.md) |
| Domain Of | [Legislature](Legislature.md), [Meeting](Meeting.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md) |
| Slot URI | [actors:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: group_reference
annotations:
  description_de:
    tag: description_de
    value: 'Kurzreferenz auf eine Gruppe oder ein Organ gemäss eCH-0294, welche deren
      Merkmale zum Zeitpunkt der Verknüpfung festhält.

      '
  description_fr:
    tag: description_fr
    value: 'Référence abrégée à un groupe ou à un organe selon eCH-0294, retenant
      ses caractéristiques au moment de la mise en relation.

      '
description: 'Reference to a group or body according to eCH-0294 with snapshot data
  at time of linking.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: actors:groupReference
domain_of:
- Legislature
- Meeting
- Voting
- Election
- Attendance
range: GroupReference
inlined: true

```
</details></div>