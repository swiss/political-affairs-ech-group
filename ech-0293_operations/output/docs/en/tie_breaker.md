---
search:
  boost: 5.0
---

# Slot: tie_breaker 


_Indicates whether the result was decided by the casting vote of the presiding member in case of a tie._




<div data-search-exclude markdown="1">



URI: [ops:tie_breaker](https://ch.paf.link/schema/operations/tie_breaker)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Voting](Voting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: tie_breaker
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob das Ergebnis bei Stimmengleichheit durch den Stichentscheid
      der Präsidentin oder des Präsidenten zustande kam.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si le résultat a été obtenu, en cas d''égalité des voix, par la
      voix prépondérante de la présidente ou du président.

      '
description: 'Indicates whether the result was decided by the casting vote of the
  presiding member in case of a tie.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: boolean

```
</details></div>