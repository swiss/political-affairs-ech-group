---
search:
  boost: 5.0
---

# Slot: is_active 


_Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist._

__



<div data-search-exclude markdown="1">



URI: [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |  yes  |
| [HasTemporalValidity](HasTemporalValidity.md) | Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit... |  no  |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |
| [Name](Name.md) | Ein Name mit einem Typ (z |  no  |
| [Citizenship](Citizenship.md) | Staatsangehörigkeit (wird auch für Nationalität verwendet) einer Person unter... |  no  |
| [Gender](Gender.md) | Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen ... |  no  |
| [Occupation](Occupation.md) | Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Code... |  no  |
| [Training](Training.md) | Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit zeitli... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Boolean](Boolean.md) |
| Domäne von | [Membership](Membership.md), [HasTemporalValidity](HasTemporalValidity.md) |
| Slot-URI | [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: is_active
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn
      diese Information explizit vorhanden ist.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si l''information est actuellement valable. Peut être utile lorsque
      cette information est explicitement disponible.

      '
description: 'Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein,
  wenn diese Information explizit vorhanden ist.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:isCurrent
domain_of:
- Membership
- HasTemporalValidity
range: boolean

```
</details></div>