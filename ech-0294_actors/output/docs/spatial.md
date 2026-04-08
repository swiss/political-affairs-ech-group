---
search:
  boost: 5.0
---

# Slot: spatial 


_[de] Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer, z.B. ld.admin.ch/municipality/1234, ld.admin.ch/canton/23)._

_[en] Spatial reference (fos-municipality number, fos-canton number, e.g., ld.admin.ch/municipality/1234, ld.admin.ch/canton/23)._

__



<div data-search-exclude markdown="1">



URI: [act:spatial](https://ld.ech.ch/schema/0294/actors/spatial)
Alias: spatial

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Group](Group.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:spatial |
| native | act:spatial |




## LinkML Source

<details>
```yaml
name: spatial
description: '[de] Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer, z.B.
  ld.admin.ch/municipality/1234, ld.admin.ch/canton/23).

  [en] Spatial reference (fos-municipality number, fos-canton number, e.g., ld.admin.ch/municipality/1234,
  ld.admin.ch/canton/23).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
alias: spatial
domain_of:
- Group
range: string

```
</details></div>