---
search:
  boost: 5.0
---

# Slot: value 


_La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc._




<div data-search-exclude markdown="1">



URI: [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [MultilingualValue](MultilingualValue.md) | Une chaîne de caractères multilingue avec indication de la langue |  yes  |
| [MultilingualUri](MultilingualUri.md) | Une URI accompagnée de la langue de la ressource vers laquelle elle renvoie |  yes  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [MultilingualValue](MultilingualValue.md), [MultilingualUri](MultilingualUri.md) |
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
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:value
domain_of:
- MultilingualValue
- MultilingualUri
range: string

```
</details></div>