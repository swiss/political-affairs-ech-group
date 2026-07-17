---
search:
  boost: 5.0
---

# Slot: value 


_The value of an information besides other attributes such as type, language, etc._

__



<div data-search-exclude markdown="1">



URI: [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Name](Name.md) | A name with a type (e |  no  |
| [Training](Training.md) | Training or education of a person indicating a type (e |  no  |
| [Contact](Contact.md) | Contact information of a person indicating a type (e |  no  |
| [MultilingualValue](MultilingualValue.md) | A multilingual string with language specification |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Name](Name.md), [Training](Training.md), [Contact](Contact.md), [MultilingualValue](MultilingualValue.md) |
| Slot URI | [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: value
annotations:
  description_de:
    tag: description_de
    value: 'Der eigentliche Wert einer Information neben weiteren attributen wie Typ,
      Sprache, etc.

      '
description: 'The value of an information besides other attributes such as type, language,
  etc.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:value
domain_of:
- Name
- Training
- Contact
- MultilingualValue
range: string

```
</details></div>