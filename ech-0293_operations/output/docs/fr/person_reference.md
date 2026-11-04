---
search:
  boost: 5.0
---

# Slot: person_reference 


_Référence abrégée à une personne selon eCH-0294, retenant ses caractéristiques au moment de la mise en relation._




<div data-search-exclude markdown="1">



URI: [actors:personReference](https://ld.ech.ch/schema/0294/actors/personReference)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | La voix exprimée par un membre lors d'un vote |  yes  |
| [IndividualAttendance](IndividualAttendance.md) | Constatation individuelle de la présence d'une personne à une séance (rattach... |  yes  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  yes  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [PersonReference](PersonReference.md) |
| Domaine de | [IndividualVote](IndividualVote.md), [IndividualAttendance](IndividualAttendance.md), [Speech](Speech.md) |
| URI du slot | [actors:personReference](https://ld.ech.ch/schema/0294/actors/personReference) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: person_reference
annotations:
  description_de:
    tag: description_de
    value: 'Kurzreferenz auf eine Person gemäss eCH-0294, welche deren Merkmale zum
      Zeitpunkt der Verknüpfung festhält.

      '
  description_fr:
    tag: description_fr
    value: 'Référence abrégée à une personne selon eCH-0294, retenant ses caractéristiques
      au moment de la mise en relation.

      '
description: 'Référence abrégée à une personne selon eCH-0294, retenant ses caractéristiques
  au moment de la mise en relation.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: actors:personReference
domain_of:
- IndividualVote
- IndividualAttendance
- Speech
range: PersonReference
inlined: true

```
</details></div>