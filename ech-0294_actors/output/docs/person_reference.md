---
search:
  boost: 5.0
---

# Slot: person_reference 


_Reference to a person with snapshot data at time of linking._

__



<div data-search-exclude markdown="1">



URI: [act:personReference](https://ld.ech.ch/schema/0294/actors/personReference)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | A membership relationship between a person and a group |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






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
annotations:
  description_de:
    tag: description_de
    value: 'Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.

      '
description: 'Reference to a person with snapshot data at time of linking.

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