

## Class: Group 


_A political group, organization, or body (e.g., party, committee, parliament, department)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| group_type | 0..1 <br/> [GroupType](GroupType.md) | Type of group (e.g., party, commission, parliament, or similar). The exact naming and description of the group is provided via `label`.  |
| label | 0..1 <br/> [String](String.md) | Option to assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abbreviation (can be multilingual).  |
| description | * <br/> [MultilingualValue](MultilingualValue.md) | Description of the entity.  |
| landing_page | 0..1 <br/> [Uri](Uri.md) | Website providing further information.  |
| parent_groups | * <br/> [Uriorcurie](Uriorcurie.md) | Link to parent groups. For example, the parent party for cantonal parties, or to describe the hierarchy in the executive. Also used to link sub-commissions to commissions, or factions to both their parliament and their party. (parentGroup is typically used within the same group_type, but cross-type links are permitted, e.g., faction → parliament and faction → party.)  |
| spatial | 0..1 <br/> [String](String.md) | Spatial reference (fos-municipality number, fos-canton number, or country). Formats: municipality: ld.admin.ch/municipality/1234, canton: ld.admin.ch/canton/23, country: ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](Contact.md) | Contact information (email, website, social media). Guideline: email is quasi-mandatory and should always be provided where available.  |
| addresses | * <br/> [Address](Address.md) | Addresses with type (private, business, local).  |
| statutes_url | 0..1 <br/> [String](String.md) | URL to party statutes (PDF or webpage; optional for parties).  |
| party_color | 0..1 <br/> [String](String.md) | Party color as hexadecimal value (optional for parties, e.g., "#FF0000").  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [groups](groups.md) | range | [Group](Group.md) |



















</div>