---
search:
  boost: 5.0
---

# Slot: group_label 


_Nom de l'organe/du groupe au moment de la liaison._

__



<div data-search-exclude markdown="1">



URI: [mcm:groupLabel](https://ld.ech.ch/schema/0292/meta-common/groupLabel)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [PersonReference](PersonReference.md) | Référence légère à une personne avec les principales données d'identification... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [PersonReference](PersonReference.md) |
| URI du slot | [mcm:groupLabel](https://ld.ech.ch/schema/0292/meta-common/groupLabel) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: group_label
annotations:
  description_de:
    tag: description_de
    value: 'Name des Gremiums zum Zeitpunkt der Verknüpfung.

      '
  description_fr:
    tag: description_fr
    value: 'Nom de l''organe/du groupe au moment de la liaison.

      '
description: 'Nom de l''organe/du groupe au moment de la liaison.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:groupLabel
domain_of:
- PersonReference
range: string

```
</details></div>