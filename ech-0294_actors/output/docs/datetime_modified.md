---
search:
  boost: 5.0
---

# Slot: datetime_modified 


_The date and time when an entity was last modified._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimeModified](https://ld.ech.ch/schema/0292/meta-common/datetimeModified)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | A mixin class that provides slots for modeling creation and modification date... |  no  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [HasCreationModificationDates](HasCreationModificationDates.md) |
| Slot URI | [mcm:datetimeModified](https://ld.ech.ch/schema/0292/meta-common/datetimeModified) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: datetime_modified
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.

      '
description: 'The date and time when an entity was last modified.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimeModified
domain_of:
- HasCreationModificationDates
range: datetime

```
</details></div>