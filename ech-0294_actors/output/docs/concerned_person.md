---
search:
  boost: 5.0
---

# Slot: concerned_person 


_[de] Link zu einer Person, auf die sich die Zugehörigkeit bezieht._

_[en] Link to a person that the affiliation concerns._

__



<div data-search-exclude markdown="1">



URI: [act:concernedPerson](https://ld.ech.ch/schema/0294/actors/concernedPerson)
Alias: concerned_person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](Person.md) |
| Domain Of | [Membership](Membership.md), [InterestLink](InterestLink.md) |
| Slot URI | [act:concernedPerson](https://ld.ech.ch/schema/0294/actors/concernedPerson) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:concernedPerson |
| native | act:concerned_person |




## LinkML Source

<details>
```yaml
name: concerned_person
description: '[de] Link zu einer Person, auf die sich die Zugehörigkeit bezieht.

  [en] Link to a person that the affiliation concerns.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:concernedPerson
alias: concerned_person
domain_of:
- Membership
- InterestLink
range: Person

```
</details></div>