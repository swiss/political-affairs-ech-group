---
search:
  boost: 5.0
---

# Slot: label_long 


_Assign an extended label to a structured piece of information (e.g., display name with title, position, etc.)._

__



<div data-search-exclude markdown="1">



URI: [mcm:labelLong](https://ld.ech.ch/schema/0292/meta-common/labelLong)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PersonReference](PersonReference.md) |
| Slot URI | [mcm:labelLong](https://ld.ech.ch/schema/0292/meta-common/labelLong) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: label_long
annotations:
  description_de:
    tag: description_de
    value: 'Möglichkeit bei einer strukturierten Information, ein erweitertesLabel
      zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.).

      '
description: 'Assign an extended label to a structured piece of information (e.g.,
  display name with title, position, etc.).

  '
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: mcm:labelLong
domain_of:
- PersonReference
range: string

```
</details></div>