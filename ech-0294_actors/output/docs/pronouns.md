

# Slot: pronouns 


_[de] Von der Person verwendete Pronomen._

_[en] Pronouns used by the person._

__





URI: [act:pronouns](https://ld.ech.ch/schema/0294/actors/pronouns)
Alias: pronouns

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gender](Gender.md) | [de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitli... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Gender](Gender.md) |
| Slot URI | [act:pronouns](https://ld.ech.ch/schema/0294/actors/pronouns) |

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
| self | act:pronouns |
| native | act:pronouns |




## LinkML Source

<details>
```yaml
name: pronouns
description: '[de] Von der Person verwendete Pronomen.

  [en] Pronouns used by the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:pronouns
alias: pronouns
domain_of:
- Gender
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details>