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
Alias: date_created

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
| Slot URI | [mcm:dateCreated](https://ld.ech.ch/schema/0292/meta-common/dateCreated) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:dateCreated |
| native | act:date_created |




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
alias: date_created
domain_of:
- HasCreationModificationDates
range: date

```
</details></div>