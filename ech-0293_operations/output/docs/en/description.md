---
search:
  boost: 5.0
---

# Slot: description 


_Descriptive text of the element._




<div data-search-exclude markdown="1">



URI: [ops:description](https://ch.paf.link/schema/operations/description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Term of office of a parliament as a legislative assembly |  no  |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |
| [Motion](Motion.md) | A formal proposal or motion submitted during proceedings |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Legislature](Legislature.md), [Meeting](Meeting.md), [Motion](Motion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: description
annotations:
  description_de:
    tag: description_de
    value: 'Beschreibender Text zum Element.

      '
  description_fr:
    tag: description_fr
    value: 'Texte descriptif de l''élément.

      '
description: 'Descriptive text of the element.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Meeting
- Motion
range: string

```
</details></div>