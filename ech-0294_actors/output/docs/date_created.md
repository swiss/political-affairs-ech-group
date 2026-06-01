---
search:
  boost: 5.0
---

# Slot: date_created 


_[de] Das Datum, an dem eine Entität erstellt wurde._

_[en] The date when an entity was created._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateCreated](https://ld.ech.ch/schema/0292/meta-common/dateCreated)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Ä... |  no  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group |  no  |
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
description: '[de] Das Datum, an dem eine Entität erstellt wurde.

  [en] The date when an entity was created.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateCreated
domain_of:
- HasCreationModificationDates
range: date

```
</details></div>