---
search:
  boost: 5.0
---

# Slot: trainings 


_Ausbildungen oder Bildungen der Person. Richtlinie: Im Grundsatz nur die höchste Ausbildung angeben._

__



<div data-search-exclude markdown="1">



URI: [act:training](https://ld.ech.ch/schema/0294/actors/training)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Training](Training.md) |
| Domäne von | [Person](Person.md) |
| Slot-URI | [act:training](https://ld.ech.ch/schema/0294/actors/training) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: trainings
annotations:
  description_de:
    tag: description_de
    value: 'Ausbildungen oder Bildungen der Person. Richtlinie: Im Grundsatz nur die
      höchste Ausbildung angeben.

      '
description: 'Ausbildungen oder Bildungen der Person. Richtlinie: Im Grundsatz nur
  die höchste Ausbildung angeben.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:training
domain_of:
- Person
range: Training
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>