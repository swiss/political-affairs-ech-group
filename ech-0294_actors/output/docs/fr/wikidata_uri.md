---
search:
  boost: 5.0
---

# Slot: wikidata_uri 


_A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland._

__



<div data-search-exclude markdown="1">



URI: [mcm:wikidataUri](https://ld.ech.ch/schema/0292/meta-common/wikidataUri)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | A mixin class that provides slots for the identification of an entity |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |
| [Container](Container.md) | Container for political actors, groups, and relationships |  no  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  no  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Uriorcurie](Uriorcurie.md) |
| Domaine de | [HasIdentification](HasIdentification.md), [IsProcessStep](IsProcessStep.md) |
| URI du slot | [mcm:wikidataUri](https://ld.ech.ch/schema/0292/meta-common/wikidataUri) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: wikidata_uri
annotations:
  description_de:
    tag: description_de
    value: 'Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39
      für die Schweiz.

      '
description: 'A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39
  for Switzerland.

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