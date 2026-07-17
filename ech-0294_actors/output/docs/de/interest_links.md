---
search:
  boost: 5.0
---

# Slot: interest_links 


_Sammlung von Interessenbindungen._

__



<div data-search-exclude markdown="1">



URI: [act:interestLink](https://ld.ech.ch/schema/0294/actors/interestLink)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für politische Akteure, Gruppen und Beziehungen |  no  |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [InterestLink](InterestLink.md) |
| Domäne von | [Container](Container.md), [Person](Person.md) |
| Slot-URI | [act:interestLink](https://ld.ech.ch/schema/0294/actors/interestLink) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: interest_links
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung von Interessenbindungen.

      '
description: 'Sammlung von Interessenbindungen.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:interestLink
domain_of:
- Container
- Person
range: InterestLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>