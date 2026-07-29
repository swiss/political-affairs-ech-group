---
search:
  boost: 5.0
---

# Slot: datetime_end_actual 


_La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée._




<div data-search-exclude markdown="1">



URI: [mcm:datetimeEndActual](https://ld.ech.ch/schema/0292/meta-common/datetimeEndActual)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | Une classe mixin qui fournit des slots pour modéliser des événements ou occur... |  no  |
| [IsProcessStep](IsProcessStep.md) | Une classe mixin pour une étape unique dans un processus |  no  |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |  no  |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Datetime](Datetime.md) |
| Domaine de | [IsEventWithDuration](IsEventWithDuration.md), [IsProcessStep](IsProcessStep.md) |
| URI du slot | [mcm:datetimeEndActual](https://ld.ech.ch/schema/0292/meta-common/datetimeEndActual) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: datetime_end_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
      mit Zeitdauer.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure de fin effectives d''un événement ou d''une occurrence
      avec durée.

      '
description: 'La date et l''heure de fin effectives d''un événement ou d''une occurrence
  avec durée.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:datetimeEndActual
domain_of:
- IsEventWithDuration
- IsProcessStep
range: datetime

```
</details></div>