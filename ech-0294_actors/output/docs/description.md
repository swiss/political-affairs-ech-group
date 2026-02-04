

# Slot: description 


_[en] Description of the entity._

_[de] Beschreibung der Entität._

__





URI: [act:description](https://ch.paf.link/schema/actors/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |






## Properties

* Range: [MultilingualString](MultilingualString.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:description |
| native | act:description |




## LinkML Source

<details>
```yaml
name: description
description: '[en] Description of the entity.

  [de] Beschreibung der Entität.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: description
domain_of:
- Group
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details>