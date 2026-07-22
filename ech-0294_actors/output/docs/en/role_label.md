---
search:
  boost: 5.0
---

# Slot: role_label 


_Specific role label. Use this when a specific role name is needed, even if a fitting semantic value exists in `role_type_enum`; provide this label when `role_type_enum` is set to 'other'._

__



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
| Range | [String](String.md) |
| Domain Of | [RoleType](RoleType.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












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
      other` soll diese Bezeichnung angegeben werden.

      '
  description_fr:
    tag: description_fr
    value: 'Libellé de rôle spécifique. À utiliser lorsqu''un nom de rôle spécifique
      est nécessaire, même s''il existe une valeur sémantique appropriée dans `role_type_enum`
      ; fournir ce libellé lorsque « role_type_enum » est réglé sur « other ».

      '
description: 'Specific role label. Use this when a specific role name is needed, even
  if a fitting semantic value exists in `role_type_enum`; provide this label when
  `role_type_enum` is set to ''other''.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
domain_of:
- RoleType
range: string

```
</details></div>