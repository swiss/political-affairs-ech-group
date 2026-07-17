---
search:
  boost: 5.0
---

# Slot: persons 


_Sammlung von Personen._

__



<div data-search-exclude markdown="1">



URI: [act:person](https://ld.ech.ch/schema/0294/actors/person)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für politische Akteure, Gruppen und Beziehungen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Person](Person.md) |
| Domäne von | [Container](Container.md) |
| Slot-URI | [act:person](https://ld.ech.ch/schema/0294/actors/person) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: persons
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung von Personen.

      '
  description_fr:
    tag: description_fr
    value: 'Collection de personnes.

      '
description: 'Sammlung von Personen.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:person
domain_of:
- Container
range: Person
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>