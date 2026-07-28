---
search:
  boost: 5.0
---

# Slot: organization_uid 


_UID der Organisation (Format eCH-0097: CHE-XXX.XXX.XXX) aus dem eidgenössischen UID-Register (uid.admin.ch)._




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
| Regex Pattern | `^CHE-\d{3}\.\d{3}\.\d{3}$` |











## Beispiele

| Wert |
| --- |
| CHE-106.063.525 |
| CHE-109.810.537 |





## LinkML-Quelle

<details>
```yaml
name: organization_uid
annotations:
  description_de:
    tag: description_de
    value: 'UID der Organisation (Format eCH-0097: CHE-XXX.XXX.XXX) aus dem eidgenössischen
      UID-Register (uid.admin.ch).

      '
  description_fr:
    tag: description_fr
    value: 'IDE de l''organisation (format eCH-0097 : CHE-XXX.XXX.XXX) issu du registre
      fédéral IDE (uid.admin.ch).

      '
description: 'UID der Organisation (Format eCH-0097: CHE-XXX.XXX.XXX) aus dem eidgenössischen
  UID-Register (uid.admin.ch).

  '
examples:
- value: CHE-106.063.525
- value: CHE-109.810.537
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:organizationUid
domain_of:
- Group
- InterestLink
- Occupation
range: string
pattern: ^CHE-\d{3}\.\d{3}\.\d{3}$

```
</details></div>