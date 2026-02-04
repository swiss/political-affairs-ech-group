

# Slot: interest_links 


_[en] Collection of interest links._

_[de] Sammlung von Interessenbindungen._

__





URI: [act:interestLink](https://ch.paf.link/schema/actors/interestLink)
Alias: interest_links

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | [en] Root container holding all political actors, groups, and relationships |  no  |






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
| native | act:interest_links |




## LinkML Source

<details>
```yaml
name: interest_links
description: '[en] Collection of interest links.

  [de] Sammlung von Interessenbindungen.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:interestLink
alias: interest_links
domain_of:
- Container
range: InterestLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details>