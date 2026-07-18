

## Class: ElectoralDistrict 


_Electoral district or region associated with a membership. The temporal validity is inherited from the enclosing membership._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](String.md) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | For IRI references, LINDAS resources should be used. The IRIs for the different administrative levels of Swiss spatial units are available at: ch:country/CHE. Under links in the schema:containsPlace section, the desired level can be selected. Examples for each administrative level: - Country - Switzerland: https://ld.admin.ch/country/CHE - Canton - Aargau: https://ld.admin.ch/canton/19 - District - Brig: https://ld.admin.ch/district/2301 - Municipality - Versoix: https://ld.admin.ch/municipality/6644 <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [electoral_district](electoral_district.md) | range | [ElectoralDistrict](ElectoralDistrict.md) |



















</div>