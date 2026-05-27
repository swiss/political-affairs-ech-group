---
search:
  boost: 5.0
---

# Slot: person_reference 


_[de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung._

_[en] Reference to a person with snapshot data at time of linking._

__



<div data-search-exclude markdown="1">



URI: [act:personReference](https://ld.ech.ch/schema/0294/actors/personReference)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonReference](PersonReference.md) |
| Domain Of | [Membership](Membership.md), [InterestLink](InterestLink.md) |
| Slot URI | [act:personReference](https://ld.ech.ch/schema/0294/actors/personReference) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: person_reference
description: '[de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.

  [en] Reference to a person with snapshot data at time of linking.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:personReference
domain_of:
- Membership
- InterestLink
range: PersonReference
inlined: true

```
</details></div>