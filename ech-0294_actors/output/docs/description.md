

# Slot: description 


_[de] Beschreibung der Entität._

_[en] Description of the entity._

__





URI: [act:description](https://ld.ech.ch/schema/0294/actors/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualValue](MultilingualValue.md) |
| Domain Of | [Group](Group.md) |

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
| self | act:description |
| native | act:description |




## LinkML Source

<details>
```yaml
name: description
description: '[de] Beschreibung der Entität.

  [en] Description of the entity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
alias: description
domain_of:
- Group
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details>