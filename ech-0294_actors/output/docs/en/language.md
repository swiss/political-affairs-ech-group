---
search:
  boost: 5.0
---

# Slot: language 


_Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en")._

__



<div data-search-exclude markdown="1">



URI: [mcm:language](https://ld.ech.ch/schema/0292/meta-common/language)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LanguageProficiency](LanguageProficiency.md) | Language proficiency of a person indicating the language and whether it is th... |  no  |
| [MultilingualValue](MultilingualValue.md) | A multilingual string with language specification |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [LanguageProficiency](LanguageProficiency.md), [MultilingualValue](MultilingualValue.md) |
| Slot URI | [mcm:language](https://ld.ech.ch/schema/0292/meta-common/language) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[a-z]{2}$` |














## LinkML Source

<details>
```yaml
name: language
annotations:
  description_de:
    tag: description_de
    value: 'Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z.B. "de", "fr",
      "it", "en").

      '
  description_fr:
    tag: description_fr
    value: 'Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. «
      de », « fr », « it », « en »).

      '
description: 'Language code in ISO 639-1 format (two lowercase letters, e.g. "de",
  "fr", "it", "en").

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:language
domain_of:
- LanguageProficiency
- MultilingualValue
range: string
pattern: ^[a-z]{2}$

```
</details></div>