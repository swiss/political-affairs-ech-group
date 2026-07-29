---
search:
  boost: 5.0
---

# Slot: documents 


_List of documents (FRBR Works) linked to the entity._




<div data-search-exclude markdown="1">



URI: [meta:documents](https://ch.paf.link/schema/meta/documents)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | A parliamentary session that groups multiple meetings and spans a specific ti... |  no  |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [Protocol](Protocol.md) | The minutes of a meeting, recorded after the meeting |  no  |
| [Resolution](Resolution.md) | A resolution or decision taken on an agenda item, including voting procedures |  no  |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |
| [Motion](Motion.md) | A formal proposal or motion submitted during proceedings |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Work](Work.md) |
| Domain Of | [Legislature](Legislature.md), [Session](Session.md), [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Protocol](Protocol.md), [Resolution](Resolution.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md), [Motion](Motion.md) |
| Slot URI | [meta:documents](https://ch.paf.link/schema/meta/documents) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

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
description: 'List of documents (FRBR Works) linked to the entity.

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