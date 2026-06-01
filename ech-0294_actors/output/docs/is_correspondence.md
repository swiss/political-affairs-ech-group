---
search:
  boost: 5.0
---

# Slot: is_correspondence 


_Indicates if this is the preferred language._

__



<div data-search-exclude markdown="1">



URI: [act:isCorrespondence](https://ld.ech.ch/schema/0294/actors/isCorrespondence)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LanguageProficiency](LanguageProficiency.md) | Language proficiency of a person indicating the language and whether it is th... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [LanguageProficiency](LanguageProficiency.md) |
| Slot URI | [act:isCorrespondence](https://ld.ech.ch/schema/0294/actors/isCorrespondence) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: is_correspondence
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob es sich um die bevorzugte Sprache handelt.

      '
description: 'Indicates if this is the preferred language.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:isCorrespondence
domain_of:
- LanguageProficiency
range: boolean

```
</details></div>