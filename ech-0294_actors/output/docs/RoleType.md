

## Class: RoleType 


_[de] Rolle einer Person in einer Mitgliedschaft oder Funktion (z.B. Mitglied, Präsident, Stellvertreter)._

_[en] Role of a person in a membership or function (e.g., member, president, deputy)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| role_type_enum | 0..1 <br/> [RoleEnum](RoleEnum.md) | [en] Role of the person in the membership or function. [de] Rolle der Person in der Mitgliedschaft oder Funktion.  |
| label | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.). [en] Option to assign a label to a structured piece of information (e.g., display name, position, etc.).  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PersonReference](PersonReference.md) | [role_type](role_type.md) | range | [RoleType](RoleType.md) |
| [Membership](Membership.md) | [role_type](role_type.md) | range | [RoleType](RoleType.md) |



















</div>