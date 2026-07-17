---
search:
  boost: 5.0
---

# Slot: citizenships 


_Staatsbürgerschaften der Person._

__



<div data-search-exclude markdown="1">



URI: [act:citizenship](https://ld.ech.ch/schema/0294/actors/citizenship)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Citizenship](Citizenship.md) |
| Domäne von | [Person](Person.md) |
| Slot-URI | [act:citizenship](https://ld.ech.ch/schema/0294/actors/citizenship) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: citizenships
annotations:
  description_de:
    tag: description_de
    value: 'Staatsbürgerschaften der Person.

      '
  description_fr:
    tag: description_fr
    value: 'Nationalités de la personne.

      '
description: 'Staatsbürgerschaften der Person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:citizenship
domain_of:
- Person
range: Citizenship
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>