---
search:
  boost: 5.0
---

# Slot: parent_groups 


_Reference to the parent groups as a GroupReference, i.e. stated by their local_id or their global_uri. Only genuine super-/subordination belongs here: the parent party of a cantonal party, the hierarchy within the executive, a sub-commission under its commission, or a parliamentary group under its parliament. (parentGroup is typically used within the same group_type, but cross-type links are permitted, e.g. parliamentary group → parliament.) The parties carrying a parliamentary group are not a superordinate group of it and are therefore not stated here._




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
| Range | [GroupReference](GroupReference.md) |
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
    value: 'Verweis auf die übergeordneten Gruppen als GroupReference, also angegeben
      über deren local_id oder deren global_uri. Hierher gehört nur eine echte Über-/Unterordnung:
      die Mutterpartei einer Kantonalpartei, die Hierarchie in der Exekutive, eine
      Subkommission unter ihrer Kommission oder eine Fraktion unter ihrem Parlament.
      (parentGroup wird typischerweise im selben group_type verwendet, typenübergreifende
      Verknüpfungen sind aber erlaubt, z.B. Fraktion → Parlament.) Die eine Fraktion
      tragenden Parteien sind ihr nicht übergeordnet und werden hier deshalb nicht
      angegeben.

      '
  description_fr:
    tag: description_fr
    value: 'Référence aux groupes supérieurs sous forme de GroupReference, c''est-à-dire
      indiquée au moyen de leur local_id ou de leur global_uri. Seule une véritable
      relation de subordination y a sa place : le parti faîtier d''un parti cantonal,
      la hiérarchie au sein de l''exécutif, une sous-commission rattachée à sa commission
      ou un groupe parlementaire rattaché à son parlement. (parentGroup est généralement
      utilisé au sein d''un même group_type, mais les liens intertypes sont autorisés,
      p. ex. groupe parlementaire → parlement.) Les partis qui portent un groupe parlementaire
      ne lui sont pas supérieurs et ne sont donc pas indiqués ici.

      '
description: 'Reference to the parent groups as a GroupReference, i.e. stated by their
  local_id or their global_uri. Only genuine super-/subordination belongs here: the
  parent party of a cantonal party, the hierarchy within the executive, a sub-commission
  under its commission, or a parliamentary group under its parliament. (parentGroup
  is typically used within the same group_type, but cross-type links are permitted,
  e.g. parliamentary group → parliament.) The parties carrying a parliamentary group
  are not a superordinate group of it and are therefore not stated here.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:parentGroup
domain_of:
- Group
range: GroupReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>