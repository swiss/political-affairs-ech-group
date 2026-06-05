---
search:
  boost: 5.0
---

# Slot: group_label 


_Name of the body/group at time of linking._

__



<div data-search-exclude markdown="1">



URI: [mcm:groupLabel](https://ld.ech.ch/schema/0292/meta-common/groupLabel)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PersonReference](PersonReference.md) |
| Slot URI | [mcm:groupLabel](https://ld.ech.ch/schema/0292/meta-common/groupLabel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_de | Name des Gremiums zum Zeitpunkt der Verknüpfung.
 |




### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:groupLabel |
| native | tutorial:group_label |




## LinkML Source

<details>
```yaml
name: group_label
annotations:
  description_de:
    tag: description_de
    value: 'Name des Gremiums zum Zeitpunkt der Verknüpfung.

      '
description: 'Name of the body/group at time of linking.

  '
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: mcm:groupLabel
domain_of:
- PersonReference
range: string

```
</details></div>