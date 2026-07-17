---
search:
  boost: 5.0
---

# Slot: local_id 


_Local identifier. For example, a UUID from the council information system._

__



<div data-search-exclude markdown="1">



URI: [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | A mixin class that provides slots for the identification of an entity |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |
| [Container](Container.md) | Container for political actors, groups, and relationships |  no  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  no  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [HasIdentification](HasIdentification.md), [IsProcessStep](IsProcessStep.md) |
| Slot URI | [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: local_id
annotations:
  description_de:
    tag: description_de
    value: 'Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant local. Par exemple, un UUID issu du système d''information
      du conseil.

      '
description: 'Local identifier. For example, a UUID from the council information system.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:localId
domain_of:
- HasIdentification
- IsProcessStep
range: string

```
</details></div>