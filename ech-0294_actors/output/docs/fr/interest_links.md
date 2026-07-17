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





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Container](Container.md) | Container for political actors, groups, and relationships |  no  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [InterestLink](InterestLink.md) |
| Domaine de | [Container](Container.md), [Person](Person.md) |
| URI du slot | [act:interestLink](https://ld.ech.ch/schema/0294/actors/interestLink) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: interest_links
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung von Interessenbindungen.

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