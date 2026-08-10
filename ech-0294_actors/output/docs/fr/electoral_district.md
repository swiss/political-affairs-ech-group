---
search:
  boost: 5.0
---

# Slot: electoral_district 


_Circonscription électorale de l'affiliation. Indiquée lorsque le mandat a été obtenu dans une circonscription ; elle est donc rattachée à l'affiliation et non à la personne._




<div data-search-exclude markdown="1">



URI: [act:electoralDistrict](https://ld.ech.ch/schema/0294/actors/electoralDistrict)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [ElectoralDistrict](ElectoralDistrict.md) |
| Domaine de | [Membership](Membership.md) |
| URI du slot | [act:electoralDistrict](https://ld.ech.ch/schema/0294/actors/electoralDistrict) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: electoral_district
annotations:
  description_de:
    tag: description_de
    value: 'Wahlkreis der Mitgliedschaft. Wird angegeben, wo das Mandat in einem Wahlkreis
      errungen wurde; er wird deshalb an der Mitgliedschaft geführt und nicht an der
      Person.

      '
  description_fr:
    tag: description_fr
    value: 'Circonscription électorale de l''affiliation. Indiquée lorsque le mandat
      a été obtenu dans une circonscription ; elle est donc rattachée à l''affiliation
      et non à la personne.

      '
description: 'Circonscription électorale de l''affiliation. Indiquée lorsque le mandat
  a été obtenu dans une circonscription ; elle est donc rattachée à l''affiliation
  et non à la personne.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:electoralDistrict
domain_of:
- Membership
range: ElectoralDistrict
inlined: true

```
</details></div>