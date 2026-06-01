---
search:
  boost: 5.0
---

# Slot: global_uri 


_[de] Eine eindeutige, global gültige URI für die Entität._

_[en] A unique, globally valid URI for the entity._

__



<div data-search-exclude markdown="1">



URI: [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | [de] Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Ve... |  no  |
| [Container](Container.md) | Container for political actors, groups, and relationships |  no  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  no  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [IsProcessStep](IsProcessStep.md) | [de] Eine Mixin-Klasse für einen einzelnen Schritt in einem |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [HasIdentification](HasIdentification.md) |
| Slot URI | [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |














## LinkML Source

<details>
```yaml
name: global_uri
description: '[de] Eine eindeutige, global gültige URI für die Entität.

  [en] A unique, globally valid URI for the entity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:globalURI
identifier: true
domain_of:
- HasIdentification
range: uriorcurie
required: true

```
</details></div>