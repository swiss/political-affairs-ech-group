

# Slot: datetime_created 


_[en] The time this record was created._

_[de] Der Zeitpunkt, zu dem dieser Datensatz erstellt wurde._

__





URI: [act:datetime_created](https://ch.paf.link/schema/actors/datetime_created)
Alias: datetime_created

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | [en] A membership relationship between a person and a group |  no  |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |  no  |






## Properties

* Range: [Datetime](Datetime.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:datetime_created |
| native | act:datetime_created |




## LinkML Source

<details>
```yaml
name: datetime_created
description: '[en] The time this record was created.

  [de] Der Zeitpunkt, zu dem dieser Datensatz erstellt wurde.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: datetime_created
domain_of:
- Person
- Group
- Membership
- InterestLink
range: datetime

```
</details>