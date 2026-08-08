---
search:
  boost: 5.0
---

# Slot: organization_uid 


_IDE de l'organisation issu du registre fédéral IDE (uid.admin.ch), dans le format d'échange d'eCH-0108 : CHE suivi de neuf chiffres, sans séparateurs (p. ex. CHE106063525). Le dernier chiffre est un chiffre de contrôle calculé modulo 11. La forme pointée CHE-106.063.525 est la présentation utilisée par uid.admin.ch et n'est pas saisie ici._




<div data-search-exclude markdown="1">



URI: [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |  no  |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |
| [Occupation](Occupation.md) | Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Group](Group.md), [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| URI du slot | [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
### Contraintes de valeur

| Propriété | Valeur |
| --- | --- |
| Regex Pattern | `^CHE[1-9][0-9]{8}$` |











## Exemples

| Valeur |
| --- |
| CHE106063525 |
| CHE109810537 |





## Source LinkML

<details>
```yaml
name: organization_uid
annotations:
  description_de:
    tag: description_de
    value: 'UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch),
      im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen
      (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die
      punktierte Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird
      hier nicht erfasst.

      '
  description_fr:
    tag: description_fr
    value: 'IDE de l''organisation issu du registre fédéral IDE (uid.admin.ch), dans
      le format d''échange d''eCH-0108 : CHE suivi de neuf chiffres, sans séparateurs
      (p. ex. CHE106063525). Le dernier chiffre est un chiffre de contrôle calculé
      modulo 11. La forme pointée CHE-106.063.525 est la présentation utilisée par
      uid.admin.ch et n''est pas saisie ici.

      '
description: 'IDE de l''organisation issu du registre fédéral IDE (uid.admin.ch),
  dans le format d''échange d''eCH-0108 : CHE suivi de neuf chiffres, sans séparateurs
  (p. ex. CHE106063525). Le dernier chiffre est un chiffre de contrôle calculé modulo
  11. La forme pointée CHE-106.063.525 est la présentation utilisée par uid.admin.ch
  et n''est pas saisie ici.

  '
examples:
- value: CHE106063525
- value: CHE109810537
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationUid
domain_of:
- Group
- InterestLink
- Occupation
range: string
pattern: ^CHE[1-9][0-9]{8}$

```
</details></div>