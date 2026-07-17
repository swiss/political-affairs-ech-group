---
search:
  boost: 5.0
---

# Slot: parent_groups 


_Übergeordnete Gruppe. Zum Beispiel die Mutterpartei zu Kantonalparteien, oder zur Beschreibung der Hierarchie in der Exekutive. Auch zur Verknüpfung von Subkommissionen mit Kommissionen oder Fraktionen mit Parlament und Partei. (parentGroup wird typischerweise im selben group_type verwendet, typenübergreifende Verknüpfungen sind aber erlaubt, z.B. Fraktion → Parlament und Fraktion → Partei.)_

__



<div data-search-exclude markdown="1">



URI: [act:parentGroup](https://ld.ech.ch/schema/0294/actors/parentGroup)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Uriorcurie](Uriorcurie.md) |
| Domäne von | [Group](Group.md) |
| Slot-URI | [act:parentGroup](https://ld.ech.ch/schema/0294/actors/parentGroup) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

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
  description_fr:
    tag: description_fr
    value: 'Lien vers les groupes parents. Par exemple, le parti faîtier pour les
      partis cantonaux, ou pour décrire la hiérarchie au sein de l''exécutif. Utilisé
      également pour rattacher des sous-commissions à des commissions, ou des groupes
      parlementaires à la fois à leur parlement et à leur parti. (parentGroup est
      généralement utilisé au sein d''un même group_type, mais les liens intertypes
      sont autorisés, p. ex. groupe parlementaire → parlement et groupe parlementaire
      → parti.)

      '
description: 'Übergeordnete Gruppe. Zum Beispiel die Mutterpartei zu Kantonalparteien,
  oder zur Beschreibung der Hierarchie in der Exekutive. Auch zur Verknüpfung von
  Subkommissionen mit Kommissionen oder Fraktionen mit Parlament und Partei. (parentGroup
  wird typischerweise im selben group_type verwendet, typenübergreifende Verknüpfungen
  sind aber erlaubt, z.B. Fraktion → Parlament und Fraktion → Partei.)

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