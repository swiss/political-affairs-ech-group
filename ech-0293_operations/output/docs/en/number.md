---
search:
  boost: 5.0
---

# Slot: number 


_Number of the session or meeting as designated by the body, e.g. within the legislature, the session or the year. As a string it also allows roman numerals. Numbering practices vary widely, which is why number, sequential_number, position and meeting_abbreviation are available side by side._




<div data-search-exclude markdown="1">



URI: [ops:number](https://ch.paf.link/schema/operations/number)
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
name: number
annotations:
  description_de:
    tag: description_de
    value: 'Nummer der Session oder Sitzung, wie sie das Organ vergibt, z.B. innerhalb
      der Legislatur, der Session oder des Jahres. Als Zeichenkette erlaubt sie auch
      römische Ziffern. Nummeriert wird sehr unterschiedlich, weshalb number, sequential_number,
      position und meeting_abbreviation nebeneinander zur Verfügung stehen.

      '
  description_fr:
    tag: description_fr
    value: 'Numéro de la session ou de la séance tel qu''attribué par l''organe, p.
      ex. au sein de la législature, de la session ou de l''année. En tant que chaîne
      de caractères, il admet aussi les chiffres romains. Les pratiques de numérotation
      variant fortement, number, sequential_number, position et meeting_abbreviation
      sont disponibles côte à côte.

      '
description: 'Number of the session or meeting as designated by the body, e.g. within
  the legislature, the session or the year. As a string it also allows roman numerals.
  Numbering practices vary widely, which is why number, sequential_number, position
  and meeting_abbreviation are available side by side.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>