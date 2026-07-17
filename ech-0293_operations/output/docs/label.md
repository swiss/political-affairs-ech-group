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
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  yes  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TotalOther](TotalOther.md), [PersonReference](PersonReference.md), [GroupReference](GroupReference.md) |
| Slot URI | [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












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
  description_fr:
    tag: description_fr
    value: 'Attribuer un label à une information structurée (par ex. nom d''affichage,
      poste, etc.).

      '
description: 'Assign a label to a structured piece of information (e.g., display name,
  position, etc.).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:label
domain_of:
- TotalOther
- PersonReference
- GroupReference
range: string

```
</details></div>