---
search:
  boost: 5.0
---

# Slot: individual_attendances 


_Ensemble des constatations individuelles de présence._




<div data-search-exclude markdown="1">



URI: [ops:individualAttendance](https://ch.paf.link/schema/operations/individualAttendance)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [IndividualAttendance](IndividualAttendance.md) |
| Domaine de | [Container](Container.md) |
| URI du slot | [ops:individualAttendance](https://ch.paf.link/schema/operations/individualAttendance) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: individual_attendances
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der einzelnen Anwesenheitsfeststellungen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des constatations individuelles de présence.

      '
description: 'Ensemble des constatations individuelles de présence.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:individualAttendance
domain_of:
- Container
range: IndividualAttendance
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>