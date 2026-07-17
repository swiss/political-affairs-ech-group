---
search:
  boost: 5.0
---

# Slot: group_reference 


_Référence à un groupe avec des données instantanées au moment de la mise en relation._

__



<div data-search-exclude markdown="1">



URI: [act:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [GroupReference](GroupReference.md) |
| Domaine de | [Membership](Membership.md) |
| URI du slot | [act:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: group_reference
annotations:
  description_de:
    tag: description_de
    value: 'Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.

      '
  description_fr:
    tag: description_fr
    value: 'Référence à un groupe avec des données instantanées au moment de la mise
      en relation.

      '
description: 'Référence à un groupe avec des données instantanées au moment de la
  mise en relation.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:groupReference
domain_of:
- Membership
range: GroupReference
inlined: true

```
</details></div>