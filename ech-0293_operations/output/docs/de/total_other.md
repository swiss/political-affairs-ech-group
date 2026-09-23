---
search:
  boost: 5.0
---

# Slot: total_other 


_Stimmenzahlen für die Optionen einer Auswahlabstimmung, ein Eintrag pro Option; tritt an die Stelle von total_count_yes, total_count_no und total_count_abstention (siehe TotalOther)._




<div data-search-exclude markdown="1">



URI: [ops:total_other](https://ch.paf.link/schema/operations/total_other)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Eine Abstimmung über eine Sachfrage: der Abstimmungsgegenstand (Frage), das V... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [TotalOther](TotalOther.md) |
| Domäne von | [Voting](Voting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: total_other
annotations:
  description_de:
    tag: description_de
    value: 'Stimmenzahlen für die Optionen einer Auswahlabstimmung, ein Eintrag pro
      Option; tritt an die Stelle von total_count_yes, total_count_no und total_count_abstention
      (siehe TotalOther).

      '
  description_fr:
    tag: description_fr
    value: 'Nombres de voix pour les options d''un vote à choix multiple, une entrée
      par option ; remplace total_count_yes, total_count_no et total_count_abstention
      (voir TotalOther).

      '
description: 'Stimmenzahlen für die Optionen einer Auswahlabstimmung, ein Eintrag
  pro Option; tritt an die Stelle von total_count_yes, total_count_no und total_count_abstention
  (siehe TotalOther).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: TotalOther
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>