---
search:
  boost: 5.0
---

# Slot: occupations 


_Berufe oder Tätigkeiten der Person._

__



<div data-search-exclude markdown="1">



URI: [act:occupation](https://ld.ech.ch/schema/0294/actors/occupation)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Occupation](Occupation.md) |
| Domäne von | [Person](Person.md) |
| Slot-URI | [act:occupation](https://ld.ech.ch/schema/0294/actors/occupation) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: occupations
annotations:
  description_de:
    tag: description_de
    value: 'Berufe oder Tätigkeiten der Person.

      '
description: 'Berufe oder Tätigkeiten der Person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:occupation
domain_of:
- Person
range: Occupation
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>