---
search:
  boost: 5.0
---

# Slot: organization_name 


_Nom de l'organisation ou de l'entreprise, avec la langue dans laquelle il est publié. Les registres bilingues indiquent le nom dans les deux langues ; une entrée est saisie par langue._




<div data-search-exclude markdown="1">



URI: [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |
| [Occupation](Occupation.md) | Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [MultilingualValue](MultilingualValue.md) |
| Domaine de | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| URI du slot | [act:organizationName](https://ld.ech.ch/schema/0294/actors/organizationName) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: organization_name
annotations:
  description_de:
    tag: description_de
    value: 'Name der Organisation oder des Unternehmens mit der Sprache, in der er
      publiziert wird. Zweisprachige Register führen den Namen in beiden Sprachen;
      erfasst wird pro Sprache ein Eintrag.

      '
  description_fr:
    tag: description_fr
    value: 'Nom de l''organisation ou de l''entreprise, avec la langue dans laquelle
      il est publié. Les registres bilingues indiquent le nom dans les deux langues
      ; une entrée est saisie par langue.

      '
description: 'Nom de l''organisation ou de l''entreprise, avec la langue dans laquelle
  il est publié. Les registres bilingues indiquent le nom dans les deux langues ;
  une entrée est saisie par langue.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationName
domain_of:
- InterestLink
- Occupation
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>