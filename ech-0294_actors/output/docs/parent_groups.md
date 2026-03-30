

# Slot: parent_groups 


_[de] Link zu übergeordneten Gruppen._

_[en] Link to parent groups._

__





URI: [act:parentGroup](https://ld.ech.ch/schema/0294/actors/parentGroup)
Alias: parent_groups

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Group](Group.md) |
| Slot URI | [act:parentGroup](https://ld.ech.ch/schema/0294/actors/parentGroup) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:parentGroup |
| native | act:parent_groups |




## LinkML Source

<details>
```yaml
name: parent_groups
description: '[de] Link zu übergeordneten Gruppen.

  [en] Link to parent groups.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:parentGroup
alias: parent_groups
domain_of:
- Group
range: uriorcurie
multivalued: true
inlined: true
inlined_as_list: true

```
</details>