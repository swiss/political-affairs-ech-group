

# Slot: datetime_updated 


_[en] The last time this record was updated._

_[de] Der Zeitpunkt, zu dem dieser Datensatz zuletzt aktualisiert wurde._

__





URI: [act:datetime_updated](https://ch.paf.link/schema/actors/datetime_updated)
Alias: datetime_updated

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |  no  |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |
| [Membership](Membership.md) | [en] A membership relationship between a person and a group |  no  |






## Properties

* Range: [Datetime](Datetime.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:datetime_updated |
| native | act:datetime_updated |




## LinkML Source

<details>
```yaml
name: datetime_updated
description: '[en] The last time this record was updated.

  [de] Der Zeitpunkt, zu dem dieser Datensatz zuletzt aktualisiert wurde.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: datetime_updated
domain_of:
- Person
- Group
- Membership
- InterestLink
range: datetime

```
</details>