---
search:
  boost: 5.0
---

# Slot: electoral_district 


_Link to the electoral district._

__



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
    value: 'Link zum Wahlbezirk.

      '
  description_fr:
    tag: description_fr
    value: 'Lien vers la circonscription électorale.

      '
description: 'Link to the electoral district.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:electoralDistrict
domain_of:
- Membership
range: ElectoralDistrict

```
</details></div>