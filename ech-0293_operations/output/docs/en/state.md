---
search:
  boost: 5.0
---

# Slot: state 


_Whether the meeting takes place as planned at all (planned, canceled, postponed). A diverging, free-text designation goes into `state_name`._




<div data-search-exclude markdown="1">



URI: [ops:state](https://ch.paf.link/schema/operations/state)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StateEnum](StateEnum.md) |
| Domain Of | [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| planned |





## LinkML Source

<details>
```yaml
name: state
annotations:
  description_de:
    tag: description_de
    value: 'Ob die Sitzung überhaupt wie vorgesehen stattfindet (geplant, abgesagt,
      verschoben). Eine abweichende, freitextliche Bezeichnung nimmt `state_name`
      auf.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si la séance a lieu comme prévu (planifiée, annulée, reportée).
      Une désignation divergente, en texte libre, est reprise dans `state_name`.

      '
description: 'Whether the meeting takes place as planned at all (planned, canceled,
  postponed). A diverging, free-text designation goes into `state_name`.

  '
examples:
- value: planned
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: StateEnum

```
</details></div>