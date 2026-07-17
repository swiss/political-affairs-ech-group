---
search:
  boost: 5.0
---

# Slot: date_end_planned 


_The planned end date of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateEndPlanned](https://ld.ech.ch/schema/0292/meta-common/dateEndPlanned)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | A mixin class that provides slots for modeling events or occurrences with tim... |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Date](Date.md) |
| Domaine de | [IsEventWithDuration](IsEventWithDuration.md), [IsProcessStep](IsProcessStep.md) |
| URI du slot | [mcm:dateEndPlanned](https://ld.ech.ch/schema/0292/meta-common/dateEndPlanned) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: date_end_planned
annotations:
  description_de:
    tag: description_de
    value: 'Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

      '
description: 'The planned end date of an event or occurrence with time duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateEndPlanned
domain_of:
- IsEventWithDuration
- IsProcessStep
range: date

```
</details></div>