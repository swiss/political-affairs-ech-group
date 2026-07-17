---
search:
  boost: 5.0
---

# Slot: date_modified 


_Das Datum, an dem eine Entität zuletzt geändert wurde._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateModified](https://ld.ech.ch/schema/0292/meta-common/dateModified)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderu... |  no  |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |  no  |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Date](Date.md) |
| Domäne von | [HasCreationModificationDates](HasCreationModificationDates.md) |
| Slot-URI | [mcm:dateModified](https://ld.ech.ch/schema/0292/meta-common/dateModified) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: date_modified
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, an dem eine Entität zuletzt geändert wurde.

      '
  description_fr:
    tag: description_fr
    value: 'La date à laquelle une entité a été modifiée pour la dernière fois.

      '
description: 'Das Datum, an dem eine Entität zuletzt geändert wurde.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateModified
domain_of:
- HasCreationModificationDates
range: date

```
</details></div>