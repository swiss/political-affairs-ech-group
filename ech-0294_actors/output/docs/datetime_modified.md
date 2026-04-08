---
search:
  boost: 5.0
---

# Slot: datetime_modified 


_[de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde._

_[en] The date and time when an entity was last modified._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimeModified](https://ld.ech.ch/schema/0292/meta-common/datetimeModified)
Alias: datetime_modified

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |
| [HasCreationModificationDates](HasCreationModificationDates.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Ä... |  no  |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:datetimeModified |
| native | act:datetime_modified |




## LinkML Source

<details>
```yaml
name: datetime_modified
description: '[de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert
  wurde.

  [en] The date and time when an entity was last modified.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimeModified
alias: datetime_modified
domain_of:
- HasCreationModificationDates
range: datetime

```
</details></div>