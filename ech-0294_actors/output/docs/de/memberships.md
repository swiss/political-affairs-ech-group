---
search:
  boost: 5.0
---

# Slot: memberships 


_Sammlung von Mitgliedschaften._

__



<div data-search-exclude markdown="1">



URI: [act:membership](https://ld.ech.ch/schema/0294/actors/membership)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für politische Akteure, Gruppen und Beziehungen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Membership](Membership.md) |
| Domäne von | [Container](Container.md) |
| Slot-URI | [act:membership](https://ld.ech.ch/schema/0294/actors/membership) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: memberships
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung von Mitgliedschaften.

      '
description: 'Sammlung von Mitgliedschaften.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:membership
domain_of:
- Container
range: Membership
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>