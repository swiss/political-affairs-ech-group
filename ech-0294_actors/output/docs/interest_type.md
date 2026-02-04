

# Slot: interest_type 


_[en] Type of interest link (professional activity, political office, association)._

_[de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein)._

__





URI: [act:interestType](https://ch.paf.link/schema/actors/interestType)
Alias: interest_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |  no  |






## Properties

* Range: [InterestTypeEnum](InterestTypeEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:interestType |
| native | act:interest_type |




## LinkML Source

<details>
```yaml
name: interest_type
description: '[en] Type of interest link (professional activity, political office,
  association).

  [de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein).

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:interestType
alias: interest_type
domain_of:
- InterestLink
range: InterestTypeEnum
required: true

```
</details>