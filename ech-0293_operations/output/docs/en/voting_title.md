---
search:
  boost: 5.0
---

# Slot: voting_title 


_Title or question being voted on. If no specific subject exists, do not use the business item title._




<div data-search-exclude markdown="1">



URI: [ops:voting_title](https://ch.paf.link/schema/operations/voting_title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualString](MultilingualString.md) |
| Domain Of | [Voting](Voting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: voting_title
annotations:
  description_de:
    tag: description_de
    value: 'Abstimmungstitel bzw. Gegenstand oder Frage. Wenn kein Gegenstand vorhanden
      ist, sollte nicht der Geschäftstitel verwendet werden.

      '
  description_fr:
    tag: description_fr
    value: 'Titre du vote, objet ou question soumise au vote. En l''absence d''objet
      propre, il ne faut pas reprendre le titre de l''affaire.

      '
description: 'Title or question being voted on. If no specific subject exists, do
  not use the business item title.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>