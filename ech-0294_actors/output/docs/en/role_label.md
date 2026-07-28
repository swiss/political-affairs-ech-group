---
search:
  boost: 5.0
---

# Slot: role_label 


_Specific role label. Use this when a specific role name is needed, even if a fitting semantic value exists in `role_type_enum`; provide this label when `role_type_enum` is set to 'other'. The designation is recorded with the language it is published in; where it is published in several languages, one entry per language is recorded._




<div data-search-exclude markdown="1">



URI: [act:role_label](https://ld.ech.ch/schema/0294/actors/role_label)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RoleType](RoleType.md) | Role of a person in a membership or function (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualValue](MultilingualValue.md) |
| Domain Of | [RoleType](RoleType.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

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
description: 'Specific role label. Use this when a specific role name is needed, even
  if a fitting semantic value exists in `role_type_enum`; provide this label when
  `role_type_enum` is set to ''other''. The designation is recorded with the language
  it is published in; where it is published in several languages, one entry per language
  is recorded.

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