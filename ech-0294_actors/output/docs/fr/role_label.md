---
search:
  boost: 5.0
---

# Slot: role_label 


_Libellé de rôle spécifique. À utiliser lorsqu'un nom de rôle spécifique est nécessaire, même s'il existe une valeur sémantique appropriée dans `role_type_enum` ; fournir ce libellé lorsque « role_type_enum » est réglé sur « other ». La désignation est saisie avec la langue dans laquelle elle est publiée ; lorsqu'elle est publiée en plusieurs langues, une entrée est saisie par langue._




<div data-search-exclude markdown="1">



URI: [act:role_label](https://ld.ech.ch/schema/0294/actors/role_label)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [RoleType](RoleType.md) | Rôle d'une personne dans une affiliation ou une fonction (p |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [MultilingualValue](MultilingualValue.md) |
| Domaine de | [RoleType](RoleType.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: role_label
annotations:
  description_de:
    tag: description_de
    value: 'Spezifische Rollenbezeichnung. Dieses Feld kann verwendet werden, wenn
      eine konkrete Rollenbezeichnung benötigt wird, auch wenn in `role_type_enum`
      bereits ein passender semantischer Wert vorhanden ist; bei `role_type_enum =
      other` soll diese Bezeichnung angegeben werden. Die Bezeichnung wird mit der
      Sprache erfasst, in der sie publiziert wird; wird sie in mehreren Sprachen publiziert,
      wird pro Sprache ein Eintrag erfasst.

      '
  description_fr:
    tag: description_fr
    value: 'Libellé de rôle spécifique. À utiliser lorsqu''un nom de rôle spécifique
      est nécessaire, même s''il existe une valeur sémantique appropriée dans `role_type_enum`
      ; fournir ce libellé lorsque « role_type_enum » est réglé sur « other ». La
      désignation est saisie avec la langue dans laquelle elle est publiée ; lorsqu''elle
      est publiée en plusieurs langues, une entrée est saisie par langue.

      '
description: 'Libellé de rôle spécifique. À utiliser lorsqu''un nom de rôle spécifique
  est nécessaire, même s''il existe une valeur sémantique appropriée dans `role_type_enum`
  ; fournir ce libellé lorsque « role_type_enum » est réglé sur « other ». La désignation
  est saisie avec la langue dans laquelle elle est publiée ; lorsqu''elle est publiée
  en plusieurs langues, une entrée est saisie par langue.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
domain_of:
- RoleType
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>