---
search:
  boost: 5.0
---

# Slot: datetime_begin_actual 


_La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimeBeginActual](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginActual)
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
| Plage | [Datetime](Datetime.md) |
| Domaine de | [IsEventWithDuration](IsEventWithDuration.md), [IsProcessStep](IsProcessStep.md) |
| URI du slot | [mcm:datetimeBeginActual](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginActual) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: datetime_begin_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
      mit Zeitdauer.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure de début effectives d''un événement ou d''une occurrence
      avec durée.

      '
description: 'La date et l''heure de début effectives d''un événement ou d''une occurrence
  avec durée.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimeBeginActual
domain_of:
- IsEventWithDuration
- IsProcessStep
range: datetime

```
</details></div>