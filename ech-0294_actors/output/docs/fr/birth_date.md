---
search:
  boost: 5.0
---

# Slot: birth_date 


_Date de naissance exacte si disponible et publique. Ce champ prime sur le champ `birthYear`._

__



<div data-search-exclude markdown="1">



URI: [schema:birthDate](http://schema.org/birthDate)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |  no  |






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
  description_fr:
    tag: description_fr
    value: 'Date de naissance exacte si disponible et publique. Ce champ prime sur
      le champ `birthYear`.

      '
description: 'Date de naissance exacte si disponible et publique. Ce champ prime sur
  le champ `birthYear`.

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