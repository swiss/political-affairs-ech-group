---
search:
  boost: 5.0
---

# Slot: label 


_Assign a label to a structured piece of information (e.g., display name, position, etc.)._

__



<div data-search-exclude markdown="1">



URI: [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TotalOther](TotalOther.md) | [en] Additional vote counts when multiple options are presented (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TotalOther](TotalOther.md) |
| Slot URI | [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_de | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).
 |




### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:label |
| native | ops:label |




## LinkML Source

<details>
```yaml
name: label
annotations:
  description_de:
    tag: description_de
    value: 'Möglichkeit bei einer strukturierten Information, ein Label zu vergeben
      (bspw. Anzeigename, Anstellung, etc.).

      '
description: 'Assign a label to a structured piece of information (e.g., display name,
  position, etc.).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:label
domain_of:
- TotalOther
range: string

```
</details></div>