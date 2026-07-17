---
search:
  boost: 5.0
---

# Slot: date_created 


_The date when an entity was created._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateCreated](https://ld.ech.ch/schema/0292/meta-common/dateCreated)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | A mixin class that provides slots for modeling creation and modification date... |  no  |
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
| Slot-URI | [mcm:dateCreated](https://ld.ech.ch/schema/0292/meta-common/dateCreated) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: date_created
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, an dem eine Entität erstellt wurde.

      '
description: 'The date when an entity was created.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateCreated
domain_of:
- HasCreationModificationDates
range: date

```
</details></div>