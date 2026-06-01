---
search:
  boost: 5.0
---

# Slot: parent_groups 


_Link to parent groups._

__



<div data-search-exclude markdown="1">



URI: [act:parentGroup](https://ld.ech.ch/schema/0294/actors/parentGroup)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | A political group, organization, or body (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Group](Group.md) |
| Slot URI | [act:parentGroup](https://ld.ech.ch/schema/0294/actors/parentGroup) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: parent_groups
annotations:
  description_de:
    tag: description_de
    value: 'Übergeordneten Gruppe. Zum Beispiel die Mutterpartei, zu Kantonalenparteien.
      Oder zur Beschreibung der Hierarchie in Exekutive. Verknüpfung von Subkommissionen
      mit Kommissionen. (parentGroup wird immer im selben group_type verwendet.)

      '
description: 'Link to parent groups.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:parentGroup
domain_of:
- Group
range: uriorcurie
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>