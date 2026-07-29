---
search:
  boost: 5.0
---

# Slot: location 


_Place where the meeting is held (physical room, video conference or hybrid format)._




<div data-search-exclude markdown="1">



URI: [ops:location](https://ch.paf.link/schema/operations/location)
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









## Examples

| Value |
| --- |
| Kantonsratssaal, Regierungsgebäude St. Gallen |
| Kommissionszimmer 301, Rathaus Bern |
| Zaunplatz, Glarus |





## LinkML Source

<details>
```yaml
name: location
annotations:
  description_de:
    tag: description_de
    value: 'Ort, an dem die Sitzung stattfindet (physischer Raum, Videokonferenz oder
      hybrides Format).

      '
  description_fr:
    tag: description_fr
    value: 'Lieu où se tient la séance (salle physique, visioconférence ou format
      hybride).

      '
description: 'Place where the meeting is held (physical room, video conference or
  hybrid format).

  '
examples:
- value: Kantonsratssaal, Regierungsgebäude St. Gallen
- value: Kommissionszimmer 301, Rathaus Bern
- value: Zaunplatz, Glarus
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>