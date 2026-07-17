---
search:
  boost: 5.0
---

# Slot: date_modified 


_The date when an entity was last modified._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateModified](https://ld.ech.ch/schema/0292/meta-common/dateModified)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | A mixin class that provides slots for modeling creation and modification date... |  no  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Date](Date.md) |
| Domaine de | [HasCreationModificationDates](HasCreationModificationDates.md) |
| URI du slot | [mcm:dateModified](https://ld.ech.ch/schema/0292/meta-common/dateModified) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: date_modified
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, an dem eine Entität zuletzt geändert wurde.

      '
description: 'The date when an entity was last modified.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateModified
domain_of:
- HasCreationModificationDates
range: date

```
</details></div>