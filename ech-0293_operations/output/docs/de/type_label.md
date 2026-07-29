---
search:
  boost: 5.0
---

# Slot: type_label 


_Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen._




<div data-search-exclude markdown="1">



URI: [ops:type_label](https://ch.paf.link/schema/operations/type_label)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Resolution](Resolution.md) | Eine Resolution oder Entscheidung zu einem Traktandum, einschliesslich Abstim... |  no  |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [IndividualVote](IndividualVote.md) | Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Resolution](Resolution.md), [Voting](Voting.md), [IndividualVote](IndividualVote.md), [Election](Election.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: type_label
annotations:
  description_de:
    tag: description_de
    value: 'Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.

      '
  description_fr:
    tag: description_fr
    value: 'Libellé de type personnalisé lorsque les valeurs de type standard ne s''appliquent
      pas.

      '
description: 'Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Resolution
- Voting
- IndividualVote
- Election
range: string

```
</details></div>