

# Slot: interest_type 


_[de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein)._

_[en] Type of interest link (professional activity, political office, association)._

__





URI: [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType)
Alias: interest_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InterestTypeEnum](InterestTypeEnum.md) |
| Domain Of | [InterestLink](InterestLink.md) |
| Slot URI | [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:interestType |
| native | act:interest_type |




## LinkML Source

<details>
```yaml
name: interest_type
description: '[de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter,
  Verein).

  [en] Type of interest link (professional activity, political office, association).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:interestType
alias: interest_type
domain_of:
- InterestLink
range: InterestTypeEnum
required: true

```
</details>