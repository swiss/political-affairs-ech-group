---
search:
  boost: 5.0
---

# Slot: weight 


_Voting weight of the member; normally 1. Other values arise, for instance, where a member also votes for an absent member (proxy, weight 2), in communal assemblies where legal entities hold several votes, or in historical systems in which different groups of persons had different voting weights._




<div data-search-exclude markdown="1">



URI: [ops:weight](https://ch.paf.link/schema/operations/weight)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | The vote cast by an individual member in a voting |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [IndividualVote](IndividualVote.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: weight
annotations:
  description_de:
    tag: description_de
    value: 'Stimmgewicht des Mitglieds; im Normalfall 1. Andere Werte kommen etwa
      vor, wo ein Mitglied für ein abwesendes Mitglied mitstimmt (Stellvertretung,
      Gewicht 2), an Gemeindeversammlungen, an denen juristische Personen mehrere
      Stimmen haben, oder in historischen Systemen, in denen verschiedene Personengruppen
      unterschiedliches Stimmgewicht hatten.

      '
  description_fr:
    tag: description_fr
    value: 'Poids de la voix du membre ; normalement 1. D''autres valeurs se présentent
      par exemple lorsqu''un membre vote aussi pour un membre absent (représentation,
      poids 2), dans les assemblées communales où des personnes morales disposent
      de plusieurs voix, ou dans des systèmes historiques où différents groupes de
      personnes avaient un poids de voix différent.

      '
description: 'Voting weight of the member; normally 1. Other values arise, for instance,
  where a member also votes for an absent member (proxy, weight 2), in communal assemblies
  where legal entities hold several votes, or in historical systems in which different
  groups of persons had different voting weights.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: integer

```
</details></div>