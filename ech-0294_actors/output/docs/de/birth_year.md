---
search:
  boost: 5.0
---

# Slot: birth_year 


_Geburtsjahr. Nur zu verwenden, wenn kein vollständiges `birthDate` vorhanden ist._

__



<div data-search-exclude markdown="1">



URI: [act:birthYear](https://ld.ech.ch/schema/0294/actors/birthYear)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Integer](Integer.md) |
| Domäne von | [Person](Person.md) |
| Slot-URI | [act:birthYear](https://ld.ech.ch/schema/0294/actors/birthYear) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| 1964 |





## LinkML-Quelle

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
description: 'Geburtsjahr. Nur zu verwenden, wenn kein vollständiges `birthDate` vorhanden
  ist.

  '
examples:
- value: '1964'
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:birthYear
domain_of:
- Person
range: integer

```
</details></div>