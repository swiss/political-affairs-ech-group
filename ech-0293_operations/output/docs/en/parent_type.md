---
search:
  boost: 5.0
---

# Slot: parent_type 


_Type of parent object (meeting, agenda, speech, affair)._




<div data-search-exclude markdown="1">



URI: [ops:parent_type](https://ch.paf.link/schema/operations/parent_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Media](Media.md) | Media files or documents (including protocols in PDF/HTML/WORD or links to au... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Media](Media.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: parent_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ des übergeordneten Objekts (Sitzung, Traktandum, Wortmeldung, Geschäft).

      '
  description_fr:
    tag: description_fr
    value: 'Type de l''objet parent (séance, point de l''ordre du jour, intervention,
      affaire).

      '
description: 'Type of parent object (meeting, agenda, speech, affair).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Media
range: string

```
</details></div>