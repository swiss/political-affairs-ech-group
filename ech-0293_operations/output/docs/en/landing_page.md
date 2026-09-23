---
search:
  boost: 5.0
---

# Slot: landing_page 


_URL providing further information._




<div data-search-exclude markdown="1">



URI: [ops:landingPage](https://ch.paf.link/schema/operations/landingPage)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Term of office of a parliament as a legislative assembly |  no  |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |
| [IsAgendaItem](IsAgendaItem.md) | A mixin class that provides the elements of an agenda item: designation, type... |  no  |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  no  |
| [Election](Election.md) | An election in which a parliamentary body appoints one or several persons to ... |  no  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting as planned beforehand |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Legislature](Legislature.md), [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md) |
| Slot URI | [ops:landingPage](https://ch.paf.link/schema/operations/landingPage) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

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
description: 'URL providing further information.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:landingPage
domain_of:
- Legislature
- Meeting
- IsAgendaItem
- Voting
- Election
- Speech
range: string

```
</details></div>