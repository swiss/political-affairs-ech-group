---
search:
  boost: 5.0
---

# Slot: organization_uid 


_UID of the organization from the federal UID register (uid.admin.ch), in the exchange format of eCH-0108: CHE followed by nine digits, without separators (e.g. CHE106063525). The last digit is a check digit calculated modulo 11. The dotted form CHE-106.063.525 is the presentation used by uid.admin.ch and is not recorded here._




<div data-search-exclude markdown="1">



URI: [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Group](Group.md), [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot URI | [act:organizationUid](https://ld.ech.ch/schema/0294/actors/organizationUid) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^CHE[1-9][0-9]{8}$` |











## Examples

| Value |
| --- |
| CHE106063525 |
| CHE109810537 |





## LinkML Source

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
description: 'UID of the organization from the federal UID register (uid.admin.ch),
  in the exchange format of eCH-0108: CHE followed by nine digits, without separators
  (e.g. CHE106063525). The last digit is a check digit calculated modulo 11. The dotted
  form CHE-106.063.525 is the presentation used by uid.admin.ch and is not recorded
  here.

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