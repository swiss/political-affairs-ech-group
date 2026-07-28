---
search:
  boost: 5.0
---

# Slot: description 


_Description of the entity._

__



<div data-search-exclude markdown="1">



URI: [act:description](https://ld.ech.ch/schema/0294/actors/description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | A political group, organization, or body (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualValue](MultilingualValue.md) |
| Domain Of | [Group](Group.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: description
annotations:
  description_de:
    tag: description_de
    value: 'Kurze Beschreibung der Gruppierung.

      '
  description_fr:
    tag: description_fr
    value: 'Description de l''entité.

      '
description: 'Description of the entity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
domain_of:
- Group
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>