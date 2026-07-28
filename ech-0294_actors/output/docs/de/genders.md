---
search:
  boost: 5.0
---

# Slot: genders 


_Geschlecht der Person._

__



<div data-search-exclude markdown="1">



URI: [act:gender](https://ld.ech.ch/schema/0294/actors/gender)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Gender](Gender.md) |
| Domäne von | [Person](Person.md) |
| Slot-URI | [act:gender](https://ld.ech.ch/schema/0294/actors/gender) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: genders
annotations:
  description_de:
    tag: description_de
    value: 'Geschlecht der Person.

      '
  description_fr:
    tag: description_fr
    value: 'Sexe de la personne.

      '
description: 'Geschlecht der Person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:gender
domain_of:
- Person
range: Gender
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>