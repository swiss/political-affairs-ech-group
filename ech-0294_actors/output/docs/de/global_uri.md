---
search:
  boost: 5.0
---

# Slot: global_uri 


_Eine eindeutige, global gültige URI für die Entität._

__



<div data-search-exclude markdown="1">



URI: [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügu... |  no  |
| [IsProcessStep](IsProcessStep.md) | Eine Mixin-Klasse für einen einzelnen Schritt in einem |  no  |
| [Container](Container.md) | Container für politische Akteure, Gruppen und Beziehungen |  no  |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |  no  |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | Wahlkreis oder Wahlregion, die einer Mitgliedschaft zugeordnet ist |  yes  |
| [PersonReference](PersonReference.md) | Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikations... |  no  |
| [GroupReference](GroupReference.md) | Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifikations... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Uriorcurie](Uriorcurie.md) |
| Domäne von | [HasIdentification](HasIdentification.md), [IsProcessStep](IsProcessStep.md) |
| Slot-URI | [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Erforderlich | Yes |
### Slot-Eigenschaften

| Eigenschaft | Wert |
| --- | --- |
| Identifikator | Yes |














## LinkML-Quelle

<details>
```yaml
name: global_uri
annotations:
  description_de:
    tag: description_de
    value: 'Eine eindeutige, global gültige URI für die Entität.

      '
  description_fr:
    tag: description_fr
    value: 'Une URI unique et globalement valide pour l''entité.

      '
description: 'Eine eindeutige, global gültige URI für die Entität.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:globalURI
identifier: true
domain_of:
- HasIdentification
- IsProcessStep
range: uriorcurie
required: true

```
</details></div>