

# Slot: is_active 


_[de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist._

_[en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available._

__





URI: [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent)
Alias: is_active

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasTemporalValidity](HasTemporalValidity.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gülti... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [HasTemporalValidity](HasTemporalValidity.md) |
| Slot URI | [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:isCurrent |
| native | ops:is_active |




## LinkML Source

<details>
```yaml
name: is_active
description: '[de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein,
  wenn diese Information explizit vorhanden ist.

  [en] Indicates whether the information is currently valid. Can be useful when this
  information is explicitly available.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:isCurrent
alias: is_active
domain_of:
- HasTemporalValidity
range: boolean

```
</details>