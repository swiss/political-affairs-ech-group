---
search:
  boost: 5.0
---

# Slot: actor_fullname 


_Full name of the actor/person._




<div data-search-exclude markdown="1">



URI: [ops:actor_fullname](https://ch.paf.link/schema/operations/actor_fullname)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Speech](Speech.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: actor_fullname
annotations:
  description_de:
    tag: description_de
    value: 'Vollständiger Name der Akteurin oder des Akteurs bzw. der Person.

      '
  description_fr:
    tag: description_fr
    value: 'Nom complet de l''actrice ou de l''acteur, respectivement de la personne.

      '
description: 'Full name of the actor/person.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>