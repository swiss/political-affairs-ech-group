---
search:
  boost: 5.0
---

# Slot: label 


_Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.)._

__



<div data-search-exclude markdown="1">



URI: [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |  yes  |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |  yes  |
| [Gender](Gender.md) | Sexe d'une personne indiquant un code de sexe et la validité temporelle |  no  |
| [Occupation](Occupation.md) | Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si... |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | Circonscription ou région électorale associée à une affiliation |  no  |
| [GroupType](GroupType.md) | Type de groupe (p |  no  |
| [RoleType](RoleType.md) | Rôle d'une personne dans une affiliation ou une fonction (p |  yes  |
| [PersonReference](PersonReference.md) | Référence légère à une personne avec les principales données d'identification... |  yes  |
| [GroupReference](GroupReference.md) | Référence légère à un groupe avec les principales données d'identification au... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Person](Person.md), [Group](Group.md), [Gender](Gender.md), [Occupation](Occupation.md), [ElectoralDistrict](ElectoralDistrict.md), [GroupType](GroupType.md), [RoleType](RoleType.md), [PersonReference](PersonReference.md), [GroupReference](GroupReference.md) |
| URI du slot | [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: label
annotations:
  description_de:
    tag: description_de
    value: 'Möglichkeit bei einer strukturierten Information, ein Label zu vergeben
      (bspw. Anzeigename, Anstellung, etc.).

      '
  description_fr:
    tag: description_fr
    value: 'Attribuer un label à une information structurée (par ex. nom d''affichage,
      poste, etc.).

      '
description: 'Attribuer un label à une information structurée (par ex. nom d''affichage,
  poste, etc.).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:label
domain_of:
- Person
- Group
- Gender
- Occupation
- ElectoralDistrict
- GroupType
- RoleType
- PersonReference
- GroupReference
range: string

```
</details></div>