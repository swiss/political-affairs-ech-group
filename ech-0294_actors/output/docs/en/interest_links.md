---
search:
  boost: 5.0
---

# Slot: interest_links 


_Collection of interest links._

__



<div data-search-exclude markdown="1">



URI: [act:interestLink](https://ld.ech.ch/schema/0294/actors/interestLink)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for political actors, groups, and relationships |  no  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






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












## LinkML Source

<details>
```yaml
name: interest_links
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung von Interessenbindungen.

      '
  description_fr:
    tag: description_fr
    value: 'Collection de liens d''intérêts.

      '
description: 'Collection of interest links.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:interestLink
domain_of:
- Container
- Person
range: InterestLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>