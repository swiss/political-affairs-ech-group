---
search:
  boost: 5.0
---

# Slot: function_role 


_Funktion oder Rolle in der Organisation (z.B. Präsident/in, Vizepräsident/in, Mitglied, Delegierter, Geschäftsführer/in, Berater/in) mit der Sprache, in der sie publiziert wird; erfasst wird pro Sprache ein Eintrag._




<div data-search-exclude markdown="1">



URI: [act:functionRole](https://ld.ech.ch/schema/0294/actors/functionRole)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MultilingualValue](MultilingualValue.md) |
| Domäne von | [InterestLink](InterestLink.md) |
| Slot-URI | [act:functionRole](https://ld.ech.ch/schema/0294/actors/functionRole) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

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
description: 'Funktion oder Rolle in der Organisation (z.B. Präsident/in, Vizepräsident/in,
  Mitglied, Delegierter, Geschäftsführer/in, Berater/in) mit der Sprache, in der sie
  publiziert wird; erfasst wird pro Sprache ein Eintrag.

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