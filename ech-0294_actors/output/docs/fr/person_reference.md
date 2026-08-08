---
search:
  boost: 5.0
---

# Slot: person_reference 


_Référence abrégée à une personne, retenant ses caractéristiques au moment de la mise en relation._




<div data-search-exclude markdown="1">



URI: [act:personReference](https://ld.ech.ch/schema/0294/actors/personReference)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |  yes  |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  yes  |






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
    value: 'Kurzreferenz auf eine Person, welche deren Merkmale zum Zeitpunkt der
      Verknüpfung festhält.

      '
  description_fr:
    tag: description_fr
    value: 'Référence abrégée à une personne, retenant ses caractéristiques au moment
      de la mise en relation.

      '
description: 'Référence abrégée à une personne, retenant ses caractéristiques au moment
  de la mise en relation.

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