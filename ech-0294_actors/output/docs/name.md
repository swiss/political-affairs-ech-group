

# Slot: name 


_[en] Name (can be multilingual)._

_[de] Name (kann mehrsprachig sein)._

__





URI: [act:name](https://ch.paf.link/schema/actors/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |
| [PersonReference](PersonReference.md) | Reference to a person acting in a specific role or function |  no  |
| [GroupReference](GroupReference.md) | Reference to a group acting in a specific role |  no  |






## Properties

* Range: [MultilingualString](MultilingualString.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:name |
| native | act:name |




## LinkML Source

<details>
```yaml
name: name
description: '[en] Name (can be multilingual).

  [de] Name (kann mehrsprachig sein).

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: name
domain_of:
- Group
- PersonReference
- GroupReference
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details>