---
search:
  boost: 5.0
---

# Slot: electoral_district 


_Wahlkreis der Mitgliedschaft. Wird angegeben, wo das Mandat in einem Wahlkreis errungen wurde; er wird deshalb an der Mitgliedschaft geführt und nicht an der Person._




<div data-search-exclude markdown="1">



URI: [act:electoralDistrict](https://ld.ech.ch/schema/0294/actors/electoralDistrict)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [ElectoralDistrict](ElectoralDistrict.md) |
| Domäne von | [Membership](Membership.md) |
| Slot-URI | [act:electoralDistrict](https://ld.ech.ch/schema/0294/actors/electoralDistrict) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: electoral_district
annotations:
  description_de:
    tag: description_de
    value: 'Wahlkreis der Mitgliedschaft. Wird angegeben, wo das Mandat in einem Wahlkreis
      errungen wurde; er wird deshalb an der Mitgliedschaft geführt und nicht an der
      Person.

      '
  description_fr:
    tag: description_fr
    value: 'Circonscription électorale de l''affiliation. Indiquée lorsque le mandat
      a été obtenu dans une circonscription ; elle est donc rattachée à l''affiliation
      et non à la personne.

      '
description: 'Wahlkreis der Mitgliedschaft. Wird angegeben, wo das Mandat in einem
  Wahlkreis errungen wurde; er wird deshalb an der Mitgliedschaft geführt und nicht
  an der Person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:electoralDistrict
domain_of:
- Membership
range: ElectoralDistrict
inlined: true

```
</details></div>