

## Class: Protocol 


_[en] The minutes of a meeting, recorded after the meeting. A wrapper container_

_     bundling the actually handled agenda items (protocol_items), votings,_

_     speeches, verbatim text segments and linked documents._

_[de] Das nach der Sitzung erstellte Protokoll. Ein Wrapper-Container, der die_

_     tatsächlich behandelten Traktanden (protocol_items), Abstimmungen, Wortmeldungen,_

_     Wortlaut-Textsegmente und verknüpfte Dokumente bündelt._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](String.md) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| protocol_items | * <br/> [ProtocolItem](ProtocolItem.md) | [en] Agenda items as actually recorded in the protocol. [de] Traktanden, wie sie im Protokoll tatsächlich festgehalten wurden.  |
| votings | * <br/> [Voting](Voting.md) | Collection of voting records |
| speeches | * <br/> [Speech](Speech.md) | Collection of speech records |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Collection of text segments (e.g. verbatim protocol) |
| documents | * <br/> [Work](Work.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [protocols](protocols.md) | range | [Protocol](Protocol.md) |
| [Meeting](Meeting.md) | [protocol_ref](protocol_ref.md) | range | [Protocol](Protocol.md) |



















</div>