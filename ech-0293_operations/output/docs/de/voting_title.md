---
search:
  boost: 5.0
---

# Slot: voting_title 


_Abstimmungstitel bzw. Gegenstand oder Frage. Wenn kein Gegenstand vorhanden ist, sollte nicht der Geschäftstitel verwendet werden._




<div data-search-exclude markdown="1">



URI: [ops:voting_title](https://ch.paf.link/schema/operations/voting_title)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MultilingualString](MultilingualString.md) |
| Domäne von | [Voting](Voting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: voting_title
annotations:
  description_de:
    tag: description_de
    value: 'Abstimmungstitel bzw. Gegenstand oder Frage. Wenn kein Gegenstand vorhanden
      ist, sollte nicht der Geschäftstitel verwendet werden.

      '
  description_fr:
    tag: description_fr
    value: 'Titre du vote, objet ou question soumise au vote. En l''absence d''objet
      propre, il ne faut pas reprendre le titre de l''affaire.

      '
description: 'Abstimmungstitel bzw. Gegenstand oder Frage. Wenn kein Gegenstand vorhanden
  ist, sollte nicht der Geschäftstitel verwendet werden.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>