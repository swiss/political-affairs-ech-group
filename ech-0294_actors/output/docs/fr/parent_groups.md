---
search:
  boost: 5.0
---

# Slot: parent_groups 


_Référence aux groupes supérieurs sous forme de GroupReference, c'est-à-dire indiquée au moyen de leur local_id ou de leur global_uri. Seule une véritable relation de subordination y a sa place : le parti faîtier d'un parti cantonal, la hiérarchie au sein de l'exécutif, une sous-commission rattachée à sa commission ou un groupe parlementaire rattaché à son parlement. (parentGroup est généralement utilisé au sein d'un même group_type, mais les liens intertypes sont autorisés, p. ex. groupe parlementaire → parlement.) Les partis qui portent un groupe parlementaire ne lui sont pas supérieurs et ne sont donc pas indiqués ici._




<div data-search-exclude markdown="1">



URI: [act:parentGroup](https://ld.ech.ch/schema/0294/actors/parentGroup)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [GroupReference](GroupReference.md) |
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
description: 'Référence aux groupes supérieurs sous forme de GroupReference, c''est-à-dire
  indiquée au moyen de leur local_id ou de leur global_uri. Seule une véritable relation
  de subordination y a sa place : le parti faîtier d''un parti cantonal, la hiérarchie
  au sein de l''exécutif, une sous-commission rattachée à sa commission ou un groupe
  parlementaire rattaché à son parlement. (parentGroup est généralement utilisé au
  sein d''un même group_type, mais les liens intertypes sont autorisés, p. ex. groupe
  parlementaire → parlement.) Les partis qui portent un groupe parlementaire ne lui
  sont pas supérieurs et ne sont donc pas indiqués ici.

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