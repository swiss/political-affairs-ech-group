---
search:
  boost: 5.0
---

# Slot: date_actual 


_La date effective d'un événement ou d'une occurrence instantané (sans durée)._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateActual](https://ld.ech.ch/schema/0292/meta-common/dateActual)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | Une classe mixin qui fournit des slots pour modéliser des événements ou occur... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Date](Date.md) |
| Domaine de | [IsInstantaneousEvent](IsInstantaneousEvent.md) |
| URI du slot | [mcm:dateActual](https://ld.ech.ch/schema/0292/meta-common/dateActual) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: date_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommnissen
      (ohne Zeitdauer).

      '
  description_fr:
    tag: description_fr
    value: 'La date effective d''un événement ou d''une occurrence instantané (sans
      durée).

      '
description: 'La date effective d''un événement ou d''une occurrence instantané (sans
  durée).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:dateActual
domain_of:
- IsInstantaneousEvent
range: date

```
</details></div>