---
search:
  boost: 5.0
---

# Slot: is_native 


_Indicates if this is the native language._

__



<div data-search-exclude markdown="1">



URI: [act:isNative](https://ld.ech.ch/schema/0294/actors/isNative)
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
| Slot URI | [act:isNative](https://ld.ech.ch/schema/0294/actors/isNative) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: is_native
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob es sich um die Muttersprache handelt.

      '
  description_fr:
    tag: description_fr
    value: 'Indique s''il s''agit de la langue maternelle.

      '
description: 'Indicates if this is the native language.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:isNative
domain_of:
- LanguageProficiency
range: boolean

```
</details></div>