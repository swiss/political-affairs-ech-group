

# Slot: is_paid 


_[de] Gibt an, ob die Position bezahlt ist._

_[en] Indicates if the position is paid._

__





URI: [act:isPaid](https://ld.ech.ch/schema/0294/actors/isPaid)
Alias: is_paid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Occupation](Occupation.md) | [de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19... |  no  |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot URI | [act:isPaid](https://ld.ech.ch/schema/0294/actors/isPaid) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:isPaid |
| native | act:is_paid |




## LinkML Source

<details>
```yaml
name: is_paid
description: '[de] Gibt an, ob die Position bezahlt ist.

  [en] Indicates if the position is paid.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:isPaid
alias: is_paid
domain_of:
- InterestLink
- Occupation
range: boolean

```
</details>