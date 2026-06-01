---
search:
  boost: 5.0
---

# Slot: is_active 


_Indicates whether the information is currently valid. Can be useful when this information is explicitly available._

__



<div data-search-exclude markdown="1">



URI: [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasTemporalValidity](HasTemporalValidity.md) | A mixin class that provides slots for modeling a temporal validity of informa... |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Name](Name.md) | A name with a type (e |  no  |
| [Citizenship](Citizenship.md) | Citizenship (also used for Nationality) of a person indicating the country an... |  no  |
| [Gender](Gender.md) | Gender of a person indicating a gender code and temporal validity |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |
| [Training](Training.md) | Training or education of a person indicating a type (e |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | Electoral district or region where a person is politically active; with tempo... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [HasTemporalValidity](HasTemporalValidity.md) |
| Slot URI | [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: is_active
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn
      diese Information explizit vorhanden ist.

      '
description: 'Indicates whether the information is currently valid. Can be useful
  when this information is explicitly available.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:isCurrent
domain_of:
- HasTemporalValidity
range: boolean

```
</details></div>