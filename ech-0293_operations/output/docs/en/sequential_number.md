---
search:
  boost: 5.0
---

# Slot: sequential_number 


_Sequential number of the meeting, used for ordering._




<div data-search-exclude markdown="1">



URI: [ops:sequential_number](https://ch.paf.link/schema/operations/sequential_number)
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
| Range | [Integer](Integer.md) |
| Domain Of | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: sequential_number
annotations:
  description_de:
    tag: description_de
    value: 'Laufende Nummer der Sitzung, die zur Sortierung verwendet wird.

      '
  description_fr:
    tag: description_fr
    value: 'Numéro séquentiel de la séance, utilisé pour le tri.

      '
description: 'Sequential number of the meeting, used for ordering.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: integer

```
</details></div>