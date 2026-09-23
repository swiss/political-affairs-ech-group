

## Class: Protocol 


_The minutes of a meeting, recorded after the meeting. A wrapper container bundling the actually handled agenda items (protocol_items), votings, speeches, verbatim text segments and linked documents._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on an agenda item, voting, election, speech or protocol it names the meeting in which the record arose.  |
| protocol_items | * <br/> [ProtocolItem](ProtocolItem.md) | Agenda items as actually recorded in the protocol.  |
| votings | * <br/> [Voting](Voting.md) | Collection of voting records.  |
| elections | * <br/> [Election](Election.md) | Collection of election records.  |
| speeches | * <br/> [Speech](Speech.md) | Collection of speech records.  |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Collection of text segments (e.g. verbatim protocol).  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [protocols](protocols.md) | range | [Protocol](Protocol.md) |
| [Meeting](Meeting.md) | [has_protocol](has_protocol.md) | range | [Protocol](Protocol.md) |
| [Voting](Voting.md) | [parent_protocol](parent_protocol.md) | range | [Protocol](Protocol.md) |
| [Election](Election.md) | [parent_protocol](parent_protocol.md) | range | [Protocol](Protocol.md) |














### Examples
#### Example Protocol: Protocol as an entity in its own right referenced by the meeting

```yaml
protocols:
- global_uri: ops:protokoll_sr_winter25_sitzung_6
  parent_meeting: parl:sr_winter25_sitzung_6
  protocol_items:
  - global_uri: ops:protokollpunkt_69905
    parent_meeting: parl:sr_winter25_sitzung_6
    agenda_item_type: item
    agenda_item_number: '6'
    agenda_item_position: 4
    agenda_item_title:
    - text: >-
        Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich
        durchführen, um die Verzögerungen zu verstehen
      language: de
    affair_id: affairs:24.4471
    datetime_begin_actual: '2025-12-19T09:20:00+01:00'
    landing_page: >-
      https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
    agenda_item_category: agenda_item
    datetime_created: '2026-01-12T00:00:00+01:00'
    datetime_modified: '2026-01-12T00:00:00+01:00'
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'

```






</div>