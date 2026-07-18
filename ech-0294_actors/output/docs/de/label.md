---
search:
  boost: 5.0
---

# Slot: label 


_Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.)._

__



<div data-search-exclude markdown="1">



URI: [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  yes  |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |  yes  |
| [Gender](Gender.md) | Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen ... |  no  |
| [Occupation](Occupation.md) | Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Code... |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | Wahlkreis oder Wahlregion, die einer Mitgliedschaft zugeordnet ist |  no  |
| [GroupType](GroupType.md) | Art der Gruppe (z |  no  |
| [RoleType](RoleType.md) | Rolle einer Person in einer Mitgliedschaft oder Funktion (z |  yes  |
| [PersonReference](PersonReference.md) | Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikations... |  yes  |
| [GroupReference](GroupReference.md) | Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifikations... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Person](Person.md), [Group](Group.md), [Gender](Gender.md), [Occupation](Occupation.md), [ElectoralDistrict](ElectoralDistrict.md), [GroupType](GroupType.md), [RoleType](RoleType.md), [PersonReference](PersonReference.md), [GroupReference](GroupReference.md) |
| Slot-URI | [mcm:label](https://ld.ech.ch/schema/0292/meta-common/label) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: label
annotations:
  description_de:
    tag: description_de
    value: 'Möglichkeit bei einer strukturierten Information, ein Label zu vergeben
      (bspw. Anzeigename, Anstellung, etc.).

      '
  description_fr:
    tag: description_fr
    value: 'Attribuer un label à une information structurée (par ex. nom d''affichage,
      poste, etc.).

      '
description: 'Möglichkeit bei einer strukturierten Information, ein Label zu vergeben
  (bspw. Anzeigename, Anstellung, etc.).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:label
domain_of:
- Person
- Group
- Gender
- Occupation
- ElectoralDistrict
- GroupType
- RoleType
- PersonReference
- GroupReference
range: string

```
</details></div>