---
search:
  boost: 5.0
---

# Slot: function_role 


_Fonction ou rôle dans l'organisation (p. ex. président/e, vice-président/e, membre, délégué, directeur/directrice, conseiller/ère), avec la langue dans laquelle elle est publiée ; une entrée est saisie par langue._




<div data-search-exclude markdown="1">



URI: [act:functionRole](https://ld.ech.ch/schema/0294/actors/functionRole)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [MultilingualValue](MultilingualValue.md) |
| Domaine de | [InterestLink](InterestLink.md) |
| URI du slot | [act:functionRole](https://ld.ech.ch/schema/0294/actors/functionRole) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: function_role
annotations:
  description_de:
    tag: description_de
    value: 'Funktion oder Rolle in der Organisation (z.B. Präsident/in, Vizepräsident/in,
      Mitglied, Delegierter, Geschäftsführer/in, Berater/in) mit der Sprache, in der
      sie publiziert wird; erfasst wird pro Sprache ein Eintrag.

      '
  description_fr:
    tag: description_fr
    value: 'Fonction ou rôle dans l''organisation (p. ex. président/e, vice-président/e,
      membre, délégué, directeur/directrice, conseiller/ère), avec la langue dans
      laquelle elle est publiée ; une entrée est saisie par langue.

      '
description: 'Fonction ou rôle dans l''organisation (p. ex. président/e, vice-président/e,
  membre, délégué, directeur/directrice, conseiller/ère), avec la langue dans laquelle
  elle est publiée ; une entrée est saisie par langue.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:functionRole
domain_of:
- InterestLink
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>