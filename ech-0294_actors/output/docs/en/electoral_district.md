---
search:
  boost: 5.0
---

# Slot: electoral_district 


_Electoral district of the membership. Stated where the mandate was won in an electoral district; it is therefore recorded on the membership and not on the person._




<div data-search-exclude markdown="1">



URI: [act:electoralDistrict](https://ld.ech.ch/schema/0294/actors/electoralDistrict)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ElectoralDistrict](ElectoralDistrict.md) |
| Domain Of | [Membership](Membership.md) |
| Slot URI | [act:electoralDistrict](https://ld.ech.ch/schema/0294/actors/electoralDistrict) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: electoral_district
annotations:
  description_de:
    tag: description_de
    value: 'Wahlkreis der Mitgliedschaft. Wird angegeben, wo das Mandat in einem Wahlkreis
      errungen wurde; er wird deshalb an der Mitgliedschaft geführt und nicht an der
      Person.

      '
  description_fr:
    tag: description_fr
    value: 'Circonscription électorale de l''affiliation. Indiquée lorsque le mandat
      a été obtenu dans une circonscription ; elle est donc rattachée à l''affiliation
      et non à la personne.

      '
description: 'Electoral district of the membership. Stated where the mandate was won
  in an electoral district; it is therefore recorded on the membership and not on
  the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:electoralDistrict
domain_of:
- Membership
range: ElectoralDistrict
inlined: true

```
</details></div>