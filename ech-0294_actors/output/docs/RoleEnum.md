# Enum: RoleEnum 




_[en] Roles a person can have within a membership._

_[de] Rollen, die eine Person im Rahmen einer Mitgliedschaft haben kann._

__



URI: [act:RoleEnum](https://ld.ech.ch/schema/0294/actors/RoleEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| member | None | [en] Regular member (default) |
| president | None | [en] President or chair of the group |
| stellvertreter | None | [en] Deputy/vice role (stellvertreter) |
| other | None | [en] Other role; use role_label for a descriptive label |




## Slots

| Name | Description |
| ---  | --- |
| [role_type_enum](role_type_enum.md) | [en] Role of the person in the membership or function |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors






## LinkML Source

<details>
```yaml
name: RoleEnum
description: '[en] Roles a person can have within a membership.

  [de] Rollen, die eine Person im Rahmen einer Mitgliedschaft haben kann.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
permissible_values:
  member:
    text: member
    description: '[en] Regular member (default).

      [de] Gewöhnliches Mitglied (Standard).

      '
  president:
    text: president
    description: '[en] President or chair of the group.

      [de] Präsident oder Vorsitzender der Gruppe.

      '
  stellvertreter:
    text: stellvertreter
    description: '[en] Deputy/vice role (stellvertreter).

      [de] Stellvertreter / Vize.

      '
  other:
    text: other
    description: '[en] Other role; use role_label for a descriptive label.

      [de] Andere Rolle; für eine beschreibende Bezeichnung role_label verwenden.

      '

```
</details>