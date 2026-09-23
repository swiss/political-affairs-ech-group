---
search:
  boost: 5.0
---

# Slot: parent_legislature 


_Identifier of the legislature to which the session belongs._




<div data-search-exclude markdown="1">



URI: [ops:parent_legislature](https://ch.paf.link/schema/operations/parent_legislature)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | A parliamentary session that groups multiple meetings and spans a specific ti... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Session](Session.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: parent_legislature
annotations:
  description_de:
    tag: description_de
    value: 'Identifikator der Legislaturperiode, zu der die Session gehört.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la législature à laquelle la session appartient.

      '
description: 'Identifier of the legislature to which the session belongs.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
range: string

```
</details></div>