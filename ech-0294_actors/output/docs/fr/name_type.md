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





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Name](Name.md) | A name with a type (e |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [NameTypeEnum](NameTypeEnum.md) |
| Domaine de | [Name](Name.md) |
| URI du slot | [act:nameType](https://ld.ech.ch/schema/0294/actors/nameType) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| PersonFirstName |
| PersonOfficialName |





## Source LinkML

<details>
```yaml
name: name_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ des Namens gemäss eCH-0011 (personNameData).

      '
description: 'Type of name according to eCH-0011 (personNameData).

  '
examples:
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