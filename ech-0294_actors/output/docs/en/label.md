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
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  yes  |
| [Group](Group.md) | A political group, organization, or body (e |  yes  |
| [Gender](Gender.md) | Gender of a person indicating a gender code and temporal validity |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | Electoral district or region associated with a membership |  no  |
| [GroupType](GroupType.md) | Type of group (e |  no  |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  yes  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Person](Person.md), [Group](Group.md), [Gender](Gender.md), [Occupation](Occupation.md), [ElectoralDistrict](ElectoralDistrict.md), [GroupType](GroupType.md), [PersonReference](PersonReference.md), [GroupReference](GroupReference.md) |
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
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:label
domain_of:
- Person
- Group
- Gender
- Occupation
- ElectoralDistrict
- GroupType
- PersonReference
- GroupReference
range: string

```
</details></div>