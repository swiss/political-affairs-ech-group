---
search:
  boost: 5.0
---

# Slot: organization_uid 


_UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch), im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die punktierte Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird hier nicht erfasst._




<div data-search-exclude markdown="1">



URI: [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |
| [Occupation](Occupation.md) | Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Code... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Group](Group.md), [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot-URI | [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
### Wertebeschränkungen

| Eigenschaft | Wert |
| --- | --- |
| Regex Pattern | `^CHE[1-9][0-9]{8}$` |











## Beispiele

| Wert |
| --- |
| CHE106063525 |
| CHE109810537 |





## LinkML-Quelle

<details>
```yaml
name: organization_uid
annotations:
  description_de:
    tag: description_de
    value: 'UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch),
      im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen
      (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die
      punktierte Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird
      hier nicht erfasst.

      '
  description_fr:
    tag: description_fr
    value: 'IDE de l''organisation issu du registre fédéral IDE (uid.admin.ch), dans
      le format d''échange d''eCH-0108 : CHE suivi de neuf chiffres, sans séparateurs
      (p. ex. CHE106063525). Le dernier chiffre est un chiffre de contrôle calculé
      modulo 11. La forme pointée CHE-106.063.525 est la présentation utilisée par
      uid.admin.ch et n''est pas saisie ici.

      '
description: 'UID der Organisation aus dem eidgenössischen UID-Register (uid.admin.ch),
  im Austauschformat von eCH-0108: CHE gefolgt von neun Ziffern, ohne Trennzeichen
  (z.B. CHE106063525). Die letzte Ziffer ist eine Prüfziffer nach Modulo 11. Die punktierte
  Form CHE-106.063.525 ist die Darstellung von uid.admin.ch und wird hier nicht erfasst.

  '
examples:
- value: CHE106063525
- value: CHE109810537
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationUid
domain_of:
- Group
- InterestLink
- Occupation
range: string
pattern: ^CHE[1-9][0-9]{8}$

```
</details></div>