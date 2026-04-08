---
search:
  boost: 5.0
---

# Slot: date_modified 


_[de] Das Datum, an dem eine Entität zuletzt geändert wurde._

_[en] The date when an entity was last modified._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateModified](https://ld.ech.ch/schema/0292/meta-common/dateModified)
Alias: date_modified

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [HasCreationModificationDates](HasCreationModificationDates.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Ä... |  no  |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [HasCreationModificationDates](HasCreationModificationDates.md) |
| Slot URI | [mcm:dateModified](https://ld.ech.ch/schema/0292/meta-common/dateModified) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:dateModified |
| native | act:date_modified |




## LinkML Source

<details>
```yaml
name: date_modified
description: '[de] Das Datum, an dem eine Entität zuletzt geändert wurde.

  [en] The date when an entity was last modified.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateModified
alias: date_modified
domain_of:
- HasCreationModificationDates
range: date

```
</details></div>