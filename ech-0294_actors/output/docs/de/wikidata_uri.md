---
search:
  boost: 5.0
---

# Slot: wikidata_uri 


_Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz._

__



<div data-search-exclude markdown="1">



URI: [mcm:wikidataUri](https://ld.ech.ch/schema/0292/meta-common/wikidataUri)
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
| [PersonReference](PersonReference.md) | Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikations... |  no  |
| [GroupReference](GroupReference.md) | Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifikations... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Uriorcurie](Uriorcurie.md) |
| Domäne von | [HasIdentification](HasIdentification.md), [IsProcessStep](IsProcessStep.md) |
| Slot-URI | [mcm:wikidataUri](https://ld.ech.ch/schema/0292/meta-common/wikidataUri) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: wikidata_uri
annotations:
  description_de:
    tag: description_de
    value: 'Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39
      für die Schweiz.

      '
  description_fr:
    tag: description_fr
    value: 'Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39
      pour la Suisse.

      '
description: 'Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39
  für die Schweiz.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:wikidataUri
domain_of:
- HasIdentification
- IsProcessStep
range: uriorcurie

```
</details></div>