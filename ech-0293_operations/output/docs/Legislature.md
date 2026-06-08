

## Class: Legislature 


_[en] Term of office of a parliament as a legislative assembly. Usually lasts four years._

_[de] Amtsdauer eines Parlaments als gesetzgebender Versammlung. Dauert in der Regel vier Jahre._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| administrative_id | 0..1 <br/> [String](String.md) | [en] Administrative ID of the legislative body, such as a municipality, canton, or country. [de] Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land.  |
| name | * <br/> [MultilingualString](MultilingualString.md) | None |
| description | 0..1 <br/> [String](String.md) | None |
| landing_page | 0..1 <br/> [String](String.md) | [en] URL providing further information. [de] URL mit weiteren Informationen.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | [en] Reference to the acting body/organ (lightweight snapshot at time of linking). [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> [Work](Work.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [legislatures](legislatures.md) | range | [Legislature](Legislature.md) |



















</div>