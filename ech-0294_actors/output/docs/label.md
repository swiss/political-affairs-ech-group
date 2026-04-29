---
search:
  boost: 5.0
---

# Slot: label 


_[de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.)._

_[en] Option to assign a label to a structured piece of information (e.g., display name, position, etc.)._

__



<div data-search-exclude markdown="1">



URI: [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label)
Alias: label

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RoleType](RoleType.md) | [de] Rolle einer Person in einer Mitgliedschaft oder Funktion (z |  no  |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [GroupType](GroupType.md) | [de] Art der Gruppe (z |  no  |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |
| [Occupation](Occupation.md) | [de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Person](Person.md), [Group](Group.md), [Occupation](Occupation.md), [GroupType](GroupType.md), [RoleType](RoleType.md) |
| Slot URI | [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:label |
| native | act:label |




## LinkML Source

<details>
```yaml
name: label
description: '[de] Möglichkeit bei einer strukturierten Information, ein Label zu
  vergeben (bspw. Anzeigename, Anstellung, etc.).

  [en] Option to assign a label to a structured piece of information (e.g., display
  name, position, etc.).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:label
alias: label
domain_of:
- Person
- Group
- Occupation
- GroupType
- RoleType
range: string

```
</details></div>