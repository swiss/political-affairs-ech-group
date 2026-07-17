---
search:
  boost: 5.0
---

# Slot: value 


_La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc._

__



<div data-search-exclude markdown="1">



URI: [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Name](Name.md) | Un nom avec un type (p |  yes  |
| [Training](Training.md) | Formation ou éducation d'une personne indiquant un type (p |  no  |
| [Contact](Contact.md) | Informations de contact d'une personne indiquant un type (p |  yes  |
| [MultilingualValue](MultilingualValue.md) | Une chaîne de caractères multilingue avec indication de la langue |  yes  |






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
  description_fr:
    tag: description_fr
    value: 'La valeur proprement dite d''une information, en plus d''autres attributs
      tels que le type, la langue, etc.

      '
description: 'La valeur proprement dite d''une information, en plus d''autres attributs
  tels que le type, la langue, etc.

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