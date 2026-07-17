---
search:
  boost: 5.0
---

# Slot: names 


_Namen der Person mit Typ und Wert._

__



<div data-search-exclude markdown="1">



URI: [act:name](https://ld.ech.ch/schema/0294/actors/name)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Name](Name.md) |
| Domäne von | [Person](Person.md) |
| Slot-URI | [act:name](https://ld.ech.ch/schema/0294/actors/name) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: names
annotations:
  description_de:
    tag: description_de
    value: 'Namen der Person mit Typ und Wert.

      '
  description_fr:
    tag: description_fr
    value: 'Noms de la personne avec type et valeur.

      '
description: 'Namen der Person mit Typ und Wert.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:name
domain_of:
- Person
range: Name
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>