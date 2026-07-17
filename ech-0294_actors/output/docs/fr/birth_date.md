---
search:
  boost: 5.0
---

# Slot: birth_date 


_Exact date of birth if available and public. This field has precedence over the field `birthYear`._

__



<div data-search-exclude markdown="1">



URI: [schema:birthDate](http://schema.org/birthDate)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Date](Date.md) |
| Domaine de | [Person](Person.md) |
| URI du slot | [schema:birthDate](http://schema.org/birthDate) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| 1964-07-12 |





## Source LinkML

<details>
```yaml
name: birth_date
annotations:
  description_de:
    tag: description_de
    value: 'Genaues Geburtsdatum, sofern verfügbar und öffentlich. Dieses Feld hat
      Vorrang vor dem Feld `birthYear`.

      '
description: 'Exact date of birth if available and public. This field has precedence
  over the field `birthYear`.

  '
examples:
- value: '1964-07-12'
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: schema:birthDate
domain_of:
- Person
range: date

```
</details></div>