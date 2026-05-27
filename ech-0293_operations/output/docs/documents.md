---
search:
  boost: 5.0
---

# Slot: documents 


_[de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind._

_[en] List of documents (FRBR Works) linked to the entity._

__



<div data-search-exclude markdown="1">



URI: [meta:documents](https://ch.paf.link/schema/meta/documents)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Resolution](Resolution.md) | [en] A resolutionor decision taken on an agenda item, including voting proced... |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Work](Work.md) |
| Domain Of | [Legislature](Legislature.md), [Session](Session.md), [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Resolution](Resolution.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md), [Motion](Motion.md) |
| Slot URI | [meta:documents](https://ch.paf.link/schema/meta/documents) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | meta:documents |
| native | ops:documents |




## LinkML Source

<details>
```yaml
name: documents
description: '[de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft
  sind.

  [en] List of documents (FRBR Works) linked to the entity.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:documents
domain_of:
- Legislature
- Session
- Meeting
- AgendaItem
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