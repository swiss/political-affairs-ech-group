---
search:
  boost: 5.0
---

# Slot: agenda_items 


_Agenda items planned for this meeting or session, embedded as a list. On a meeting they form the agenda of the sitting. On a session they hold agenda items planned directly at the level of the session — where a federal unit does not break the session down into individual meetings (e.g. a Landsgemeinde or a one-day sitting of a cantonal parliament), or for items not (yet) assigned to a specific meeting, as in a session programme. The counterpart after the sitting are the items recorded in the protocol (Protocol.protocol_items)._




<div data-search-exclude markdown="1">



URI: [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | A session: a contiguous period of sittings within a legislature |  no  |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AgendaItem](AgendaItem.md) |
| Domain Of | [Session](Session.md), [Meeting](Meeting.md) |
| Slot URI | [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: agenda_items
annotations:
  description_de:
    tag: description_de
    value: 'Für diese Sitzung oder Session geplante Traktanden, eingebettet als Liste.
      Bei einer Sitzung bilden sie deren Traktandenliste. Bei einer Session enthalten
      sie Traktanden, die direkt auf Ebene der Session geplant sind — wo eine Föderaleinheit
      die Session nicht in einzelne Sitzungen gliedert (z.B. eine Landsgemeinde oder
      eine eintägige Sitzung eines Kantonsparlaments) oder für Traktanden, die (noch)
      keiner bestimmten Sitzung zugeordnet sind, wie in einem Sessionsprogramm. Das
      Gegenstück nach der Sitzung sind die im Protokoll festgehaltenen Traktanden
      (Protocol.protocol_items).

      '
  description_fr:
    tag: description_fr
    value: 'Points de l''ordre du jour planifiés pour cette séance ou cette session,
      imbriqués sous forme de liste. Pour une séance, ils forment son ordre du jour.
      Pour une session, ils contiennent les points planifiés directement au niveau
      de la session — lorsqu''une unité fédérale ne subdivise pas la session en séances
      (p. ex. une Landsgemeinde ou une séance d''un jour d''un parlement cantonal),
      ou pour des points qui ne sont pas (encore) attribués à une séance déterminée,
      comme dans un programme de session. Leur pendant après la séance sont les points
      consignés au procès-verbal (Protocol.protocol_items).

      '
description: 'Agenda items planned for this meeting or session, embedded as a list.
  On a meeting they form the agenda of the sitting. On a session they hold agenda
  items planned directly at the level of the session — where a federal unit does not
  break the session down into individual meetings (e.g. a Landsgemeinde or a one-day
  sitting of a cantonal parliament), or for items not (yet) assigned to a specific
  meeting, as in a session programme. The counterpart after the sitting are the items
  recorded in the protocol (Protocol.protocol_items).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:agendaItem
domain_of:
- Session
- Meeting
range: AgendaItem
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>