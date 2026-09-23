---
search:
  boost: 5.0
---

# Slot: has_resolution 


_Der formale Beschluss zu diesem Traktandum, z.B. die Annahme des Energiegesetzes. Die zugrunde liegende Abstimmung mit dem Stimmenverhältnis wird separat als Voting erfasst._




<div data-search-exclude markdown="1">



URI: [ops:has_resolution](https://ch.paf.link/schema/operations/has_resolution)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |  no  |
| [AgendaItem](AgendaItem.md) | Ein vorgängig geplantes Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Resolution](Resolution.md) |
| Domäne von | [IsAgendaItem](IsAgendaItem.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Der formale Beschluss zu diesem Traktandum, z.B. die Annahme des Energiegesetzes.
  Die zugrunde liegende Abstimmung mit dem Stimmenverhältnis wird separat als Voting
  erfasst.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: Resolution

```
</details></div>