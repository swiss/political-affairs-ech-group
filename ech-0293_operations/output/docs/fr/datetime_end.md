---
search:
  boost: 5.0
---

# Slot: datetime_end 


_La date et l'heure auxquelles la séance ou le vote se termine._




<div data-search-exclude markdown="1">



URI: [ops:datetime_end](https://ch.paf.link/schema/operations/datetime_end)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Datetime](Datetime.md) |
| Domaine de | [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: datetime_end
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure auxquelles la séance ou le vote se termine.

      '
description: 'La date et l''heure auxquelles la séance ou le vote se termine.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
- Speech
range: datetime

```
</details></div>