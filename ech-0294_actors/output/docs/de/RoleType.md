

## Klasse: RoleType 


_Rolle einer Person in einer Mitgliedschaft oder Funktion (z.B. Mitglied, Präsident/in, Stellvertreter/in). Wenn eine Rolle im vorgeschlagenen RoleEnum-Vokabular nicht enthalten ist, kann der Wert 'other' verwendet werden; in diesem Fall soll im Slot `role_label` eine beschreibende Bezeichnung angegeben werden. Die Bezeichnung kann auch verwendet werden, wenn eine spezifische Rollenbezeichnung nötig ist, selbst wenn in `role_type_enum` bereits ein passender semantischer Wert vorhanden ist; bei `role_type_enum = other` soll sie angegeben werden._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| role_type_enum | 0..1 <br/> [RoleEnum](RoleEnum.md) | Rolle der Person in der Mitgliedschaft oder Funktion.  |
| label | 0..1 <br/> [String](String.md) | Spezifische Rollenbezeichnung. Dieses Feld kann verwendet werden, wenn eine konkrete Rollenbezeichnung benötigt wird, auch wenn in `role_type_enum` bereits ein passender semantischer Wert vorhanden ist; bei `role_type_enum = other` soll diese Bezeichnung angegeben werden.  |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [role_type_enum](role_type_enum.md)
- [label](label.md)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [role_type](role_type.md) | range | [RoleType](RoleType.md) |




##### Regeln


- Wenn der Rollentyp 'other' ist, muss eine beschreibende Bezeichnung angegeben werden.

















</div>