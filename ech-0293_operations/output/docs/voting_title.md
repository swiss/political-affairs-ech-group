

# Slot: voting_title 


_[en] Title or question being voted on. If no specific subject exists, do not use the business item title._

_[de] Abstimmungstitel bzw. Gegenstand oder Frage. Wenn kein Gegenstand vorhanden ist, sollte nicht der Geschäftstitel verwendet werden._

__





URI: [ops:voting_title](https://ch.paf.link/schema/operations/voting_title)
Alias: voting_title

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |






## Properties

* Range: [MultilingualString](MultilingualString.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:voting_title |
| native | ops:voting_title |




## LinkML Source

<details>
```yaml
name: voting_title
description: '[en] Title or question being voted on. If no specific subject exists,
  do not use the business item title.

  [de] Abstimmungstitel bzw. Gegenstand oder Frage. Wenn kein Gegenstand vorhanden
  ist, sollte nicht der Geschäftstitel verwendet werden.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: voting_title
domain_of:
- Voting
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details>