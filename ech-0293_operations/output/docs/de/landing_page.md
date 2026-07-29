---
search:
  boost: 5.0
---

# Slot: landing_page 


_URL mit weiteren Informationen._




<div data-search-exclude markdown="1">



URI: [ops:landingPage](https://ch.paf.link/schema/operations/landingPage)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Legislature](Legislature.md), [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md) |
| Slot-URI | [ops:landingPage](https://ch.paf.link/schema/operations/landingPage) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: landing_page
annotations:
  description_de:
    tag: description_de
    value: 'URL mit weiteren Informationen.

      '
  description_fr:
    tag: description_fr
    value: 'URL fournissant des informations complémentaires.

      '
description: 'URL mit weiteren Informationen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:landingPage
domain_of:
- Legislature
- Meeting
- AgendaItem
- Voting
- Election
- Speech
range: string

```
</details></div>