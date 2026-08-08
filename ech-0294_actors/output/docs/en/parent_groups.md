---
search:
  boost: 5.0
---

# Slot: parent_groups 


_Reference to the parent groups as a GroupReference, i.e. stated by their local_id or their global_uri. For example, the parent party for cantonal parties, or to describe the hierarchy in the executive. Also used to link sub-commissions to commissions, or factions to both their parliament and their party. (parentGroup is typically used within the same group_type, but cross-type links are permitted, e.g., faction → parliament and faction → party.)_




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
      über deren local_id oder deren global_uri. Zum Beispiel die Mutterpartei zu
      Kantonalparteien, oder zur Beschreibung der Hierarchie in der Exekutive. Auch
      zur Verknüpfung von Subkommissionen mit Kommissionen oder Fraktionen mit Parlament
      und Partei. (parentGroup wird typischerweise im selben group_type verwendet,
      typenübergreifende Verknüpfungen sind aber erlaubt, z.B. Fraktion → Parlament
      und Fraktion → Partei.)

      '
  description_fr:
    tag: description_fr
    value: 'Référence aux groupes supérieurs sous forme de GroupReference, c''est-à-dire
      indiquée au moyen de leur local_id ou de leur global_uri. Par exemple, le parti
      faîtier pour les partis cantonaux, ou pour décrire la hiérarchie au sein de
      l''exécutif. Utilisé également pour rattacher des sous-commissions à des commissions,
      ou des groupes parlementaires à la fois à leur parlement et à leur parti. (parentGroup
      est généralement utilisé au sein d''un même group_type, mais les liens intertypes
      sont autorisés, p. ex. groupe parlementaire → parlement et groupe parlementaire
      → parti.)

      '
description: 'Reference to the parent groups as a GroupReference, i.e. stated by their
  local_id or their global_uri. For example, the parent party for cantonal parties,
  or to describe the hierarchy in the executive. Also used to link sub-commissions
  to commissions, or factions to both their parliament and their party. (parentGroup
  is typically used within the same group_type, but cross-type links are permitted,
  e.g., faction → parliament and faction → party.)

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