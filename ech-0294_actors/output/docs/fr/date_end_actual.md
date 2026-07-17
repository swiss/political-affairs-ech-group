---
search:
  boost: 5.0
---

# Slot: date_end_actual 


_La date de fin effective d'un événement ou d'une occurrence avec durée._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateEndActual](https://ld.ech.ch/schema/0292/meta-common/dateEndActual)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | Une classe mixin qui fournit des slots pour modéliser des événements ou occur... |  no  |
| [IsProcessStep](IsProcessStep.md) | Une classe mixin pour une étape unique dans un processus |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Date](Date.md) |
| Domaine de | [IsEventWithDuration](IsEventWithDuration.md), [IsProcessStep](IsProcessStep.md) |
| URI du slot | [mcm:dateEndActual](https://ld.ech.ch/schema/0292/meta-common/dateEndActual) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: date_end_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

      '
  description_fr:
    tag: description_fr
    value: 'La date de fin effective d''un événement ou d''une occurrence avec durée.

      '
description: 'La date de fin effective d''un événement ou d''une occurrence avec durée.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateEndActual
domain_of:
- IsEventWithDuration
- IsProcessStep
range: date

```
</details></div>