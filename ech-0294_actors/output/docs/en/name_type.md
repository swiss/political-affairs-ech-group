---
search:
  boost: 5.0
---

# Slot: name_type 


_Type of name according to eCH-0011 (personNameData)._

__



<div data-search-exclude markdown="1">



URI: [act:nameType](https://ld.ech.ch/schema/0294/actors/nameType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Name](Name.md) | A name with a type (e |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NameTypeEnum](NameTypeEnum.md) |
| Domain Of | [Name](Name.md) |
| Slot URI | [act:nameType](https://ld.ech.ch/schema/0294/actors/nameType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| PersonCallFirstName |
| PersonFirstName |
| PersonOfficialName |





## LinkML Source

<details>
```yaml
name: name_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ des Namens gemäss eCH-0011 (personNameData).

      '
  description_fr:
    tag: description_fr
    value: 'Type de nom selon eCH-0011 (personNameData).

      '
description: 'Type of name according to eCH-0011 (personNameData).

  '
examples:
- value: PersonCallFirstName
- value: PersonFirstName
- value: PersonOfficialName
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:nameType
domain_of:
- Name
range: NameTypeEnum

```
</details></div>