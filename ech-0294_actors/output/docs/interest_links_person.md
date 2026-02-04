

# Slot: interest_links_person 


_[en] Interest links of the person._

_[de] Interessenbindungen der Person._

__





URI: [act:interestLink](https://ch.paf.link/schema/actors/interestLink)
Alias: interest_links_person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |






## Properties

* Range: [InterestLink](InterestLink.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:interestLink |
| native | act:interest_links_person |




## LinkML Source

<details>
```yaml
name: interest_links_person
description: '[en] Interest links of the person.

  [de] Interessenbindungen der Person.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:interestLink
alias: interest_links_person
domain_of:
- Person
range: InterestLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details>