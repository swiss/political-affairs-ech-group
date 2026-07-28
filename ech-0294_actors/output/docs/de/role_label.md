---
search:
  boost: 5.0
---

# Slot: role_label 


_Spezifische Rollenbezeichnung. Dieses Feld kann verwendet werden, wenn eine konkrete Rollenbezeichnung benötigt wird, auch wenn in `role_type_enum` bereits ein passender semantischer Wert vorhanden ist; bei `role_type_enum = other` soll diese Bezeichnung angegeben werden._

__



<div data-search-exclude markdown="1">



URI: [act:role_label](https://ld.ech.ch/schema/0294/actors/role_label)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [RoleType](RoleType.md) | Rolle einer Person in einer Mitgliedschaft oder Funktion (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [RoleType](RoleType.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Spezifische Rollenbezeichnung. Dieses Feld kann verwendet werden, wenn
  eine konkrete Rollenbezeichnung benötigt wird, auch wenn in `role_type_enum` bereits
  ein passender semantischer Wert vorhanden ist; bei `role_type_enum = other` soll
  diese Bezeichnung angegeben werden.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
domain_of:
- RoleType
range: string

```
</details></div>