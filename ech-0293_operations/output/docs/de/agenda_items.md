---
search:
  boost: 5.0
---

# Slot: agenda_items 


_Für diese Sitzung oder Session geplante Traktanden, eingebettet als Liste. Bei einer Sitzung bilden sie deren Traktandenliste. Bei einer Session enthalten sie Traktanden, die direkt auf Ebene der Session geplant sind — wo eine Föderaleinheit die Session nicht in einzelne Sitzungen gliedert (z.B. eine Landsgemeinde oder eine eintägige Sitzung eines Kantonsparlaments) oder für Traktanden, die (noch) keiner bestimmten Sitzung zugeordnet sind, wie in einem Sessionsprogramm. Das Gegenstück nach der Sitzung sind die im Protokoll festgehaltenen Traktanden (Protocol.protocol_items)._




<div data-search-exclude markdown="1">



URI: [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Session: eine zusammenhängende Sitzungsperiode innerhalb einer Legislatu... |  no  |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [AgendaItem](AgendaItem.md) |
| Domäne von | [Session](Session.md), [Meeting](Meeting.md) |
| Slot-URI | [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

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
description: 'Für diese Sitzung oder Session geplante Traktanden, eingebettet als
  Liste. Bei einer Sitzung bilden sie deren Traktandenliste. Bei einer Session enthalten
  sie Traktanden, die direkt auf Ebene der Session geplant sind — wo eine Föderaleinheit
  die Session nicht in einzelne Sitzungen gliedert (z.B. eine Landsgemeinde oder eine
  eintägige Sitzung eines Kantonsparlaments) oder für Traktanden, die (noch) keiner
  bestimmten Sitzung zugeordnet sind, wie in einem Sessionsprogramm. Das Gegenstück
  nach der Sitzung sind die im Protokoll festgehaltenen Traktanden (Protocol.protocol_items).

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