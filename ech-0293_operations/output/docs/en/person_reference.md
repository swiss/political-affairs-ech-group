---
search:
  boost: 5.0
---

# Slot: person_reference 


_Reference to a person according to eCH-0294 with snapshot data at time of linking._




<div data-search-exclude markdown="1">



URI: [actors:personReference](https://ld.ech.ch/schema/0294/actors/personReference)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | The vote cast by an individual member in a voting |  yes  |
| [IndividualAttendance](IndividualAttendance.md) | Individual attendance record for a specific person at a meeting (linked via t... |  yes  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonReference](PersonReference.md) |
| Domain Of | [IndividualVote](IndividualVote.md), [IndividualAttendance](IndividualAttendance.md), [Speech](Speech.md) |
| Slot URI | [actors:personReference](https://ld.ech.ch/schema/0294/actors/personReference) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

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
description: 'Reference to a person according to eCH-0294 with snapshot data at time
  of linking.

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