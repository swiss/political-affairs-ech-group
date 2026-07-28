

## Class: RoleType 


_Role of a person in a membership or function (e.g., member, president, deputy). If a role is not listed in the proposed RoleEnum vocabulary, the value 'other' can be used, and a descriptive label should be provided in the `role_label` slot. The label can also be used when a specific name is needed, even if a fitting semantic value exists in `role_type_enum`; it should be provided when `role_type_enum` is set to 'other'._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| role_type_enum | 0..1 <br/> [RoleEnum](RoleEnum.md) | Role of the person in the membership or function.  |
| role_label | 0..1 <br/> [String](String.md) | Specific role label. Use this when a specific role name is needed, even if a fitting semantic value exists in `role_type_enum`; provide this label when `role_type_enum` is set to 'other'.  |

##### Constraints


At least one of the following must be set:

- [role_type_enum](role_type_enum.md)
- [role_label](role_label.md)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [role_type](role_type.md) | range | [RoleType](RoleType.md) |




##### Rules


- If the role type is 'other', a descriptive label must be provided.

















</div>