---
search:
  boost: 5.0
---

# Slot: person_reference 


_Référence à une personne avec des données instantanées au moment de la mise en relation._

__



<div data-search-exclude markdown="1">



URI: [act:personReference](https://ld.ech.ch/schema/0294/actors/personReference)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |  no  |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [PersonReference](PersonReference.md) |
| Domaine de | [Membership](Membership.md), [InterestLink](InterestLink.md) |
| URI du slot | [act:personReference](https://ld.ech.ch/schema/0294/actors/personReference) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: person_reference
annotations:
  description_de:
    tag: description_de
    value: 'Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.

      '
  description_fr:
    tag: description_fr
    value: 'Référence à une personne avec des données instantanées au moment de la
      mise en relation.

      '
description: 'Référence à une personne avec des données instantanées au moment de
  la mise en relation.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:personReference
domain_of:
- Membership
- InterestLink
range: PersonReference
inlined: true

```
</details></div>