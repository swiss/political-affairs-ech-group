---
search:
  boost: 5.0
---

# Slot: date_created 


_The date when an entity was created._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateCreated](https://ld.ech.ch/schema/0292/meta-common/dateCreated)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | A mixin class that provides slots for modeling creation and modification date... |  no  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [HasCreationModificationDates](HasCreationModificationDates.md) |
| Slot URI | [mcm:dateCreated](https://ld.ech.ch/schema/0292/meta-common/dateCreated) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: date_created
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, an dem eine Entität erstellt wurde.

      '
  description_fr:
    tag: description_fr
    value: 'La date à laquelle une entité a été créée.

      '
description: 'The date when an entity was created.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateCreated
domain_of:
- HasCreationModificationDates
range: date

```
</details></div>