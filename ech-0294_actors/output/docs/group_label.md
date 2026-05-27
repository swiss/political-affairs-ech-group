---
search:
  boost: 5.0
---

# Slot: group_label 


_[de] Name des Gremiums zum Zeitpunkt der Verknüpfung._

_[en] Name of the body/group at time of linking._

__



<div data-search-exclude markdown="1">



URI: [act:groupLabel](https://ld.ech.ch/schema/0294/actors/groupLabel)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonReference](PersonReference.md) | [de] Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifika... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PersonReference](PersonReference.md) |
| Slot URI | [act:groupLabel](https://ld.ech.ch/schema/0294/actors/groupLabel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: group_label
description: '[de] Name des Gremiums zum Zeitpunkt der Verknüpfung.

  [en] Name of the body/group at time of linking.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:groupLabel
domain_of:
- PersonReference
range: string

```
</details></div>