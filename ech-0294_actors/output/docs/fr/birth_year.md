---
search:
  boost: 5.0
---

# Slot: birth_year 


_Année de naissance. À utiliser uniquement lorsqu'aucune `birthDate` complète n'est disponible._

__



<div data-search-exclude markdown="1">



URI: [act:birthYear](https://ld.ech.ch/schema/0294/actors/birthYear)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Integer](Integer.md) |
| Domaine de | [Person](Person.md) |
| URI du slot | [act:birthYear](https://ld.ech.ch/schema/0294/actors/birthYear) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| 1964 |
| 1965 |
| 1981 |





## Source LinkML

<details>
```yaml
name: birth_year
annotations:
  description_de:
    tag: description_de
    value: 'Geburtsjahr. Nur zu verwenden, wenn kein vollständiges `birthDate` vorhanden
      ist.

      '
  description_fr:
    tag: description_fr
    value: 'Année de naissance. À utiliser uniquement lorsqu''aucune `birthDate` complète
      n''est disponible.

      '
description: 'Année de naissance. À utiliser uniquement lorsqu''aucune `birthDate`
  complète n''est disponible.

  '
examples:
- value: '1964'
- value: '1965'
- value: '1981'
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:birthYear
domain_of:
- Person
range: integer

```
</details></div>