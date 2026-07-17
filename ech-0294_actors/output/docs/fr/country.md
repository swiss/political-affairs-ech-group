---
search:
  boost: 5.0
---

# Slot: country 


_ISO 3166-1 alpha-2 country code._

__



<div data-search-exclude markdown="1">



URI: [act:country](https://ld.ech.ch/schema/0294/actors/country)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Citizenship](Citizenship.md) | Citizenship (also used for Nationality) of a person indicating the country an... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Citizenship](Citizenship.md) |
| URI du slot | [act:country](https://ld.ech.ch/schema/0294/actors/country) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
### Contraintes de valeur

| Propriété | Valeur |
| --- | --- |
| Regex Pattern | `^[A-Z]{2}$` |











## Exemples

| Valeur |
| --- |
| CH |





## Source LinkML

<details>
```yaml
name: country
annotations:
  description_de:
    tag: description_de
    value: 'ISO 3166-1 alpha-2 Ländercode.

      '
description: 'ISO 3166-1 alpha-2 country code.

  '
examples:
- value: CH
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:country
domain_of:
- Citizenship
range: string
pattern: ^[A-Z]{2}$

```
</details></div>