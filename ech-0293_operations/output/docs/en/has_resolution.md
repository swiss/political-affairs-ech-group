---
search:
  boost: 5.0
---

# Slot: has_resolution 


_The formal decision taken on this agenda item, e.g. the adoption of the energy law. The underlying voting with its vote ratio is recorded separately as a Voting._




<div data-search-exclude markdown="1">



URI: [ops:has_resolution](https://ch.paf.link/schema/operations/has_resolution)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | A mixin class that provides the elements of an agenda item: designation, type... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting as planned beforehand |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Resolution](Resolution.md) |
| Domain Of | [IsAgendaItem](IsAgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: has_resolution
annotations:
  description_de:
    tag: description_de
    value: 'Der formale Beschluss zu diesem Traktandum, z.B. die Annahme des Energiegesetzes.
      Die zugrunde liegende Abstimmung mit dem Stimmenverhältnis wird separat als
      Voting erfasst.

      '
  description_fr:
    tag: description_fr
    value: 'La décision formelle prise sur ce point de l''ordre du jour, p. ex. l''adoption
      de la loi sur l''énergie. Le vote sous-jacent avec son rapport de voix est saisi
      séparément comme Voting.

      '
description: 'The formal decision taken on this agenda item, e.g. the adoption of
  the energy law. The underlying voting with its vote ratio is recorded separately
  as a Voting.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: Resolution

```
</details></div>