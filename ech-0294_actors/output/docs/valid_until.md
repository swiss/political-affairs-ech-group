

# Slot: valid_until 


_[en] End date of validity period._

_[de] Enddatum der Gültigkeitsperiode._

__





URI: [act:validUntil](https://ch.paf.link/schema/actors/validUntil)
Alias: valid_until

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |  no  |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |
| [Membership](Membership.md) | [en] A membership relationship between a person and a group |  no  |
| [Gender](Gender.md) |  |  no  |
| [Occupation](Occupation.md) |  |  no  |
| [Citizenship](Citizenship.md) |  |  no  |
| [Name](Name.md) |  |  no  |
| [Validity](Validity.md) |  |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) |  |  no  |






## Properties

* Range: [Date](Date.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:validUntil |
| native | act:valid_until |




## LinkML Source

<details>
```yaml
name: valid_until
description: '[en] End date of validity period.

  [de] Enddatum der Gültigkeitsperiode.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:validUntil
alias: valid_until
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