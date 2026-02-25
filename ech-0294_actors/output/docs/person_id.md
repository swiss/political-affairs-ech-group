

# Slot: person_id 


_[en] Reference to a person ID._

_[de] Referenz zu einer Personen-ID._

__





URI: [act:person_id](https://ch.paf.link/schema/actors/person_id)
Alias: person_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |  no  |
| [Membership](Membership.md) | [en] A membership relationship between a person and a group |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:person_id |
| native | act:person_id |




## LinkML Source

<details>
```yaml
name: person_id
description: '[en] Reference to a person ID.

  [de] Referenz zu einer Personen-ID.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: person_id
domain_of:
- Membership
- InterestLink
range: string

```
</details>