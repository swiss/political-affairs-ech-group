---
search:
  boost: 5.0
---

# Slot: url 


_Landing page or further web address, multilingual._




<div data-search-exclude markdown="1">



URI: [ops:url](https://ch.paf.link/schema/operations/url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | A parliamentary session that groups multiple meetings and spans a specific ti... |  no  |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [Media](Media.md) | Media files or documents (including protocols in PDF/HTML/WORD or links to au... |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualString](MultilingualString.md) |
| Domain Of | [Session](Session.md), [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Media](Media.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: url
annotations:
  description_de:
    tag: description_de
    value: 'Landing Page oder weiterführende Webadresse, mehrsprachig.

      '
  description_fr:
    tag: description_fr
    value: 'Page d''accueil ou adresse web complémentaire, multilingue.

      '
description: 'Landing page or further web address, multilingual.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
- AgendaItem
- Media
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>