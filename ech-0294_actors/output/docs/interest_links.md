---
search:
  boost: 5.0
---

# Slot: interest_links 


_[de] Sammlung von Interessenbindungen._

_[en] Collection of interest links.range: InterestLink_

__



<div data-search-exclude markdown="1">



URI: [act:interestLink](https://ld.ech.ch/schema/0294/actors/interestLink)
Alias: interest_links

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |
| [Container](Container.md) | [de] Container für politische Akteure, Gruppen und Beziehungen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InterestLink](InterestLink.md) |
| Domain Of | [Container](Container.md), [Person](Person.md) |
| Slot URI | [act:interestLink](https://ld.ech.ch/schema/0294/actors/interestLink) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:interestLink |
| native | act:interest_links |




## LinkML Source

<details>
```yaml
name: interest_links
description: '[de] Sammlung von Interessenbindungen.

  [en] Collection of interest links.range: InterestLink

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:interestLink
alias: interest_links
domain_of:
- Container
- Person
range: InterestLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>