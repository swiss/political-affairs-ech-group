---
search:
  boost: 5.0
---

# Slot: sequential_number 


_Sequential number of the session or meeting as an integer, used for ordering._




<div data-search-exclude markdown="1">



URI: [ops:sequential_number](https://ch.paf.link/schema/operations/sequential_number)
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
    value: 'Laufende Nummer der Session oder Sitzung als Ganzzahl, die zur Sortierung
      verwendet wird.

      '
  description_fr:
    tag: description_fr
    value: 'Numéro d''ordre de la session ou de la séance sous forme de nombre entier,
      utilisé pour le tri.

      '
description: 'Sequential number of the session or meeting as an integer, used for
  ordering.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: integer

```
</details></div>