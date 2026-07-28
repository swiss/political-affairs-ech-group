---
search:
  boost: 5.0
---

# Slot: valid_from 


_La date à partir de laquelle l'information est valable._

__



<div data-search-exclude markdown="1">



URI: [schema:validFrom](http://schema.org/validFrom)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [HasTemporalValidity](HasTemporalValidity.md) | Une classe mixin qui fournit des slots pour modéliser la validité temporelle ... |  no  |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |  no  |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |  no  |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |
| [Name](Name.md) | Un nom avec un type (p |  no  |
| [Citizenship](Citizenship.md) | Nationalité (également utilisée pour la citoyenneté) d'une personne indiquant... |  no  |
| [Gender](Gender.md) | Sexe d'une personne indiquant un code de sexe et la validité temporelle |  no  |
| [Occupation](Occupation.md) | Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si... |  no  |
| [Training](Training.md) | Formation ou éducation d'une personne indiquant un type (p |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Date](Date.md) |
| Domaine de | [HasTemporalValidity](HasTemporalValidity.md) |
| URI du slot | [schema:validFrom](http://schema.org/validFrom) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: valid_from
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, ab dem die Information gültig ist.

      '
  description_fr:
    tag: description_fr
    value: 'La date à partir de laquelle l''information est valable.

      '
description: 'La date à partir de laquelle l''information est valable.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: schema:validFrom
domain_of:
- HasTemporalValidity
range: date

```
</details></div>