

# Slot: id 


_[en] Unique identifier (preferably Wikidata-ID or URI)._

_[de] Eindeutiger Identifikator (vorzugsweise Wikidata-ID oder URI)._

__





URI: [dcterm:identifier](http://purl.org/dc/terms/identifier)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | [en] Root container holding all political actors, groups, and relationships |  no  |
| [InterestLink](InterestLink.md) | [en] An interest link (conflict of interest, political financing) of a person... |  no  |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |
| [GroupReference](GroupReference.md) | Reference to a group acting in a specific role |  no  |
| [Membership](Membership.md) | [en] A membership relationship between a person and a group |  no  |
| [PersonReference](PersonReference.md) | Reference to a person acting in a specific role or function |  no  |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterm:identifier |
| native | act:id |




## LinkML Source

<details>
```yaml
name: id
description: '[en] Unique identifier (preferably Wikidata-ID or URI).

  [de] Eindeutiger Identifikator (vorzugsweise Wikidata-ID oder URI).

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: dcterm:identifier
identifier: true
alias: id
domain_of:
- Container
- Person
- Group
- Membership
- InterestLink
- PersonReference
- GroupReference
range: string
required: true

```
</details>