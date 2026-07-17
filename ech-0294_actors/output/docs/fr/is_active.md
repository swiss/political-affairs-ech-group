---
search:
  boost: 5.0
---

# Slot: is_active 


_Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible._

__



<div data-search-exclude markdown="1">



URI: [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |  yes  |
| [HasTemporalValidity](HasTemporalValidity.md) | Une classe mixin qui fournit des slots pour modéliser la validité temporelle ... |  no  |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |  no  |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |
| [Name](Name.md) | Un nom avec un type (p |  no  |
| [Citizenship](Citizenship.md) | Nationalité (également utilisée pour la citoyenneté) d'une personne indiquant... |  no  |
| [Gender](Gender.md) | Sexe d'une personne indiquant un code de sexe et la validité temporelle |  no  |
| [Occupation](Occupation.md) | Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si... |  no  |
| [Training](Training.md) | Formation ou éducation d'une personne indiquant un type (p |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | Circonscription ou région électorale dans laquelle une personne est politique... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Boolean](Boolean.md) |
| Domaine de | [Membership](Membership.md), [HasTemporalValidity](HasTemporalValidity.md) |
| URI du slot | [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: is_active
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn
      diese Information explizit vorhanden ist.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si l''information est actuellement valable. Peut être utile lorsque
      cette information est explicitement disponible.

      '
description: 'Indique si l''information est actuellement valable. Peut être utile
  lorsque cette information est explicitement disponible.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:isCurrent
domain_of:
- Membership
- HasTemporalValidity
range: boolean

```
</details></div>