---
search:
  boost: 5.0
---

# Slot: parent_session 


_Identifier of the session to which the meeting belongs._




<div data-search-exclude markdown="1">



URI: [ops:parent_session](https://ch.paf.link/schema/operations/parent_session)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: parent_session
annotations:
  description_de:
    tag: description_de
    value: 'Identifikator der Session, zu der die Sitzung gehört.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la session à laquelle la séance appartient.

      '
description: 'Identifier of the session to which the meeting belongs.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: string

```
</details></div>