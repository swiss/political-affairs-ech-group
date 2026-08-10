---
search:
  boost: 5.0
---

# Slot: organization_name 


_Name of the organization or enterprise, with the language it is published in. Bilingual registers state the name in both languages; one entry is recorded per language._




<div data-search-exclude markdown="1">



URI: [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualValue](MultilingualValue.md) |
| Domain Of | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot URI | [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: organization_name
annotations:
  description_de:
    tag: description_de
    value: 'Name der Organisation oder des Unternehmens mit der Sprache, in der er
      publiziert wird. Zweisprachige Register führen den Namen in beiden Sprachen;
      erfasst wird pro Sprache ein Eintrag.

      '
  description_fr:
    tag: description_fr
    value: 'Nom de l''organisation ou de l''entreprise, avec la langue dans laquelle
      il est publié. Les registres bilingues indiquent le nom dans les deux langues
      ; une entrée est saisie par langue.

      '
description: 'Name of the organization or enterprise, with the language it is published
  in. Bilingual registers state the name in both languages; one entry is recorded
  per language.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationName
domain_of:
- InterestLink
- Occupation
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>