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
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  yes  |
| [IsAgendaItem](IsAgendaItem.md) | Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeic... |  yes  |
| [Protocol](Protocol.md) | Das Protokoll einer Sitzung, nach der Sitzung erstellt und pro Sitzung genau ... |  no  |
| [Resolution](Resolution.md) | Der formale Beschluss zu einem Traktandum, einschliesslich der angewandten Ab... |  no  |
| [Voting](Voting.md) | Eine Abstimmung über eine Sachfrage: der Abstimmungsgegenstand (Frage), das V... |  no  |
| [Election](Election.md) | Eine Wahl, mit der ein parlamentarisches Organ eine oder mehrere Personen für... |  no  |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |  no  |
| [Motion](Motion.md) | Ein formaler Antrag, der während der Beratung gestellt wird, etwa ein Änderun... |  no  |
| [AgendaItem](AgendaItem.md) | Ein vorgängig geplantes Traktandum einer Sitzung |  no  |
| [ProtocolItem](ProtocolItem.md) | Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Work](Work.md) |
| Domäne von | [Legislature](Legislature.md), [Session](Session.md), [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md), [Protocol](Protocol.md), [Resolution](Resolution.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md), [Motion](Motion.md) |
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
- IsAgendaItem
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