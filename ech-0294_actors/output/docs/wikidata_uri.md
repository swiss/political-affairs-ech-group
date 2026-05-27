---
search:
  boost: 5.0
---

# Slot: wikidata_uri 


_[de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz._

_[en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland._

__



<div data-search-exclude markdown="1">



URI: [mcm:wikidataUri](https://ld.ech.ch/schema/0292/meta-common/wikidataUri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | [de] Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Ve... |  no  |
| [Container](Container.md) | [de] Container für politische Akteure, Gruppen und Beziehungen |  no  |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [PersonReference](PersonReference.md) | [de] Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifika... |  no  |
| [GroupReference](GroupReference.md) | [de] Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifika... |  no  |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |
| [IsProcessStep](IsProcessStep.md) | [de] Eine Mixin-Klasse für einen einzelnen Schritt in einem |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [HasIdentification](HasIdentification.md) |
| Slot URI | [mcm:wikidataUri](https://ld.ech.ch/schema/0292/meta-common/wikidataUri) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: wikidata_uri
description: '[de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39
  für die Schweiz.

  [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39
  for Switzerland.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:wikidataUri
domain_of:
- HasIdentification
range: uriorcurie

```
</details></div>