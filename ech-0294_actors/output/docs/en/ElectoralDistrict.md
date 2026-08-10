

## Class: ElectoralDistrict 


_Electoral district or region associated with a membership. The temporal validity is inherited from the enclosing membership._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | For IRI references, LINDAS resources should be used. The IRIs for the different administrative levels of Swiss spatial units are available at: https://ld.admin.ch/country/CHE. Under links in the schema:containsPlace section, the desired level can be selected. Examples for each administrative level: - Country - Switzerland: https://ld.admin.ch/country/CHE - Canton - Aargau: https://ld.admin.ch/canton/19 - District - Brig: https://ld.admin.ch/district/2301 - Municipality - Versoix: https://ld.admin.ch/municipality/6644 Electoral districts that correspond to no official spatial unit, such as districts grouping together neighbourhoods of a municipality, are given an identifier in the namespace of the publishing body instead. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| label | * <br/> [MultilingualValue](MultilingualValue.md) | Name of the electoral district as published by the body responsible for the election, with the language it is published in. Where a district is officially named in several languages, one entry per language is recorded.  |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [electoral_district](electoral_district.md) | range | [ElectoralDistrict](ElectoralDistrict.md) |














### Examples
#### Example ElectoralDistrict: Electoral district without an official spatial unit

```yaml
electoral_district:
  global_uri: https://grosserrat.bs.ch/wahlkreise/kleinbasel
  label:
  - value: Kleinbasel
    language: de

```
#### Example ElectoralDistrict: Canton as electoral district identified via its LINDAS resource

```yaml
electoral_district:
  global_uri: https://ld.admin.ch/canton/12
  label:
  - value: Basel-Stadt
    language: de

```






</div>