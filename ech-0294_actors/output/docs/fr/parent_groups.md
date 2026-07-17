---
search:
  boost: 5.0
---

# Slot: parent_groups 


_Link to parent groups. For example, the parent party for cantonal parties, or to describe the hierarchy in the executive. Also used to link sub-commissions to commissions, or factions to both their parliament and their party. (parentGroup is typically used within the same group_type, but cross-type links are permitted, e.g., faction → parliament and faction → party.)_

__



<div data-search-exclude markdown="1">



URI: [act:parentGroup](https://ld.ech.ch/schema/0294/actors/parentGroup)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Group](Group.md) | A political group, organization, or body (e |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Uriorcurie](Uriorcurie.md) |
| Domaine de | [Group](Group.md) |
| URI du slot | [act:parentGroup](https://ld.ech.ch/schema/0294/actors/parentGroup) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: parent_groups
annotations:
  description_de:
    tag: description_de
    value: 'Übergeordnete Gruppe. Zum Beispiel die Mutterpartei zu Kantonalparteien,
      oder zur Beschreibung der Hierarchie in der Exekutive. Auch zur Verknüpfung
      von Subkommissionen mit Kommissionen oder Fraktionen mit Parlament und Partei.
      (parentGroup wird typischerweise im selben group_type verwendet, typenübergreifende
      Verknüpfungen sind aber erlaubt, z.B. Fraktion → Parlament und Fraktion → Partei.)

      '
description: 'Link to parent groups. For example, the parent party for cantonal parties,
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
range: uriorcurie
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>