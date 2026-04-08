---
search:
  boost: 5.0
---

# Slot: local_id 


_[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem._

_[en] Local identifier. For example, a UUID from the council information system._

__



<div data-search-exclude markdown="1">



URI: [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId)
Alias: local_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | [de] Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Ve... |  no  |
| [Container](Container.md) | [de] Container für politische Akteure, Gruppen und Beziehungen |  no  |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [HasIdentification](HasIdentification.md) |
| Slot URI | [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:localId |
| native | act:local_id |




## LinkML Source

<details>
```yaml
name: local_id
description: '[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

  [en] Local identifier. For example, a UUID from the council information system.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:localId
alias: local_id
domain_of:
- HasIdentification
range: string

```
</details></div>