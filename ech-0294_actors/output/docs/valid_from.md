

# Slot: valid_from 


_[en] Start date of validity period._

_[de] Startdatum der Gültigkeitsperiode._

__





URI: [act:validFrom](https://ch.paf.link/schema/actors/validFrom)
Alias: valid_from

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | [en] A membership relationship between a person and a group |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) |  |  no  |
| [Citizenship](Citizenship.md) |  |  no  |
| [Occupation](Occupation.md) |  |  no  |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |  no  |
| [Gender](Gender.md) |  |  no  |
| [Name](Name.md) |  |  no  |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |
| [Validity](Validity.md) |  |  no  |






## Properties

* Range: [Date](Date.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:validFrom |
| native | act:valid_from |




## LinkML Source

<details>
```yaml
name: valid_from
description: '[en] Start date of validity period.

  [de] Startdatum der Gültigkeitsperiode.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:validFrom
alias: valid_from
domain_of:
- Group
- Membership
- InterestLink
- Name
- Validity
- ElectoralDistrict
range: date

```
</details>