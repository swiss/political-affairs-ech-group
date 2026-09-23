---
search:
  boost: 5.0
---

# Slot: meeting_abbreviation 


_Short designation of the session or meeting (e.g. "FS24" for the 2024 spring session)._




<div data-search-exclude markdown="1">



URI: [ops:meeting_abbreviation](https://ch.paf.link/schema/operations/meeting_abbreviation)
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
name: meeting_abbreviation
annotations:
  description_de:
    tag: description_de
    value: 'Kurzbezeichnung der Session oder Sitzung (z.B. „FS24“ für die Frühjahrssession
      2024).

      '
  description_fr:
    tag: description_fr
    value: 'Désignation abrégée de la session ou de la séance (p. ex. « FS24 » pour
      la session de printemps 2024).

      '
description: 'Short designation of the session or meeting (e.g. "FS24" for the 2024
  spring session).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>