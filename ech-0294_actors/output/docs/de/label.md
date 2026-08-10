---
search:
  boost: 5.0
---

# Slot: label 


_Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.)._




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
| [Contact](Contact.md) | Kontaktinformation einer Person mit Angabe eines Typs (z |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | Wahlkreis oder Wahlregion, die einer Mitgliedschaft zugeordnet ist |  yes  |
| [GroupType](GroupType.md) | Art der Gruppe (z |  yes  |
| [PersonReference](PersonReference.md) | Kurzreferenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum... |  yes  |
| [GroupReference](GroupReference.md) | Kurzreferenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Person](Person.md), [Group](Group.md), [Gender](Gender.md), [Occupation](Occupation.md), [Contact](Contact.md), [ElectoralDistrict](ElectoralDistrict.md), [GroupType](GroupType.md), [PersonReference](PersonReference.md), [GroupReference](GroupReference.md) |
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
- Contact
- ElectoralDistrict
- GroupType
- PersonReference
- GroupReference
range: string

```
</details></div>