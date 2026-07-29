---
search:
  boost: 5.0
---

# Slot: documents 


_Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind._




<div data-search-exclude markdown="1">



URI: [meta:documents](https://ch.paf.link/schema/meta/documents)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |  no  |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |  no  |
| [Protocol](Protocol.md) | Das nach der Sitzung erstellte Protokoll |  no  |
| [Resolution](Resolution.md) | Eine Resolution oder Entscheidung zu einem Traktandum, einschliesslich Abstim... |  no  |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |
| [Motion](Motion.md) | Ein formeller Antrag, der während der Verhandlungen eingereicht wird |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Work](Work.md) |
| Domäne von | [Legislature](Legislature.md), [Session](Session.md), [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Protocol](Protocol.md), [Resolution](Resolution.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md), [Motion](Motion.md) |
| Slot-URI | [meta:documents](https://ch.paf.link/schema/meta/documents) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: documents
annotations:
  description_de:
    tag: description_de
    value: 'Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.

      '
  description_fr:
    tag: description_fr
    value: 'Liste des documents (FRBR Works) liés à l''entité.

      '
description: 'Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:documents
domain_of:
- Legislature
- Session
- Meeting
- AgendaItem
- Protocol
- Resolution
- Voting
- Election
- Speech
- Motion
range: Work
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>