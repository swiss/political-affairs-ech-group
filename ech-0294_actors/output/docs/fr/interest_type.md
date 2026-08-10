---
search:
  boost: 5.0
---

# Slot: interest_type 


_Type de lien d'intérêts, suivant les catégories tenues par les registres de publicité (activité professionnelle, siège dans un organe de direction, mandat pour un groupe d'intérêts, fonction dans la sphère publique, appartenance)._




<div data-search-exclude markdown="1">



URI: [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [InterestTypeEnum](InterestTypeEnum.md) |
| Domaine de | [InterestLink](InterestLink.md) |
| URI du slot | [act:interestType](https://ld.ech.ch/schema/0294/actors/interestType) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Requis | Yes |









## Exemples

| Valeur |
| --- |
| governing_body |
| interest_group_mandate |
| professional_activity |





## Source LinkML

<details>
```yaml
name: interest_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der Interessenbindung, den Kategorien der Offenlegungsregister folgend
      (berufliche Tätigkeit, Sitz in einem Führungsgremium, Mandat für eine Interessengruppe,
      Amt in der öffentlichen Hand, Mitgliedschaft).

      '
  description_fr:
    tag: description_fr
    value: 'Type de lien d''intérêts, suivant les catégories tenues par les registres
      de publicité (activité professionnelle, siège dans un organe de direction, mandat
      pour un groupe d''intérêts, fonction dans la sphère publique, appartenance).

      '
description: 'Type de lien d''intérêts, suivant les catégories tenues par les registres
  de publicité (activité professionnelle, siège dans un organe de direction, mandat
  pour un groupe d''intérêts, fonction dans la sphère publique, appartenance).

  '
examples:
- value: governing_body
- value: interest_group_mandate
- value: professional_activity
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:interestType
domain_of:
- InterestLink
range: InterestTypeEnum
required: true

```
</details></div>