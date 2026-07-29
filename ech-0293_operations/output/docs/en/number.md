---
search:
  boost: 5.0
---

# Slot: number 


_Sequential number, e.g. within the legislature, the session or the year._




<div data-search-exclude markdown="1">



URI: [ops:number](https://ch.paf.link/schema/operations/number)
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
name: number
annotations:
  description_de:
    tag: description_de
    value: 'Laufende Nummer, z.B. innerhalb der Legislatur, der Session oder des Jahres.

      '
  description_fr:
    tag: description_fr
    value: 'Numéro courant, p. ex. au sein de la législature, de la session ou de
      l''année.

      '
description: 'Sequential number, e.g. within the legislature, the session or the year.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>