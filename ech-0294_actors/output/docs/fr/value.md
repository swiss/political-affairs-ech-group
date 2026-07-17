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





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Name](Name.md) | A name with a type (e |  no  |
| [Training](Training.md) | Training or education of a person indicating a type (e |  no  |
| [Contact](Contact.md) | Contact information of a person indicating a type (e |  no  |
| [MultilingualValue](MultilingualValue.md) | A multilingual string with language specification |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Name](Name.md), [Training](Training.md), [Contact](Contact.md), [MultilingualValue](MultilingualValue.md) |
| URI du slot | [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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