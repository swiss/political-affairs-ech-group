

## Class: Legislature 


_Term of office of a parliament as a legislative assembly. Usually lasts four years._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| spatial | 0..1 <br/> [String](String.md) | Spatial reference to a LINDAS resource (fos-municipality number, fos-canton number, district, or country). Formats: municipality: https://ld.admin.ch/municipality/1234, district: https://ld.admin.ch/district/2301, canton: https://ld.admin.ch/canton/23, country: https://ld.admin.ch/country/CHE.  |
| administrative_id | 0..1 <br/> [String](String.md) | Administrative ID of the legislative body, such as a municipality, canton, or country.  |
| name | * <br/> [MultilingualString](MultilingualString.md) | Multilingual full designation.  |
| description | 0..1 <br/> [String](String.md) | Descriptive text of the element.  |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |
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

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [legislatures](legislatures.md) | range | [Legislature](Legislature.md) |














### Examples
#### Example Legislature: Completed federal legislature

```yaml
legislatures:
- global_uri: ops:legislature_51
  wikidata_uri: http://www.wikidata.org/entity/Q71712404
  spatial: https://ld.admin.ch/country/CHE
  name:
  - text: 51. Legislaturperiode
    language: de
  - text: 51e législature
    language: fr
  - text: 51ª legislatura
    language: it
  description: >-
    Amtsdauer der am 20. Oktober 2019 gewählten Bundesversammlung; sie endete am Vortag
    der konstituierenden Sitzung der 52. Legislaturperiode vom 4. Dezember 2023.
  landing_page: https://www.parlament.ch/de/ratsbetrieb/sessionen
  actor_id:
    global_uri: actors:bundesversammlung
    label: Bundesversammlung
    abbreviation:
    - value: BV
      language: de
  date_begin_actual: '2019-12-02'
  date_end_actual: '2023-12-03'
  datetime_created: '2019-12-02T09:00:00+01:00'
  datetime_modified: '2023-12-04T08:30:00+01:00'

```
#### Example Legislature: Ongoing cantonal legislature with a five-year term

```yaml
legislatures:
- global_uri: ops:legislature_vd_2022_2027
  wikidata_uri: http://www.wikidata.org/entity/Q131627357
  spatial: https://ld.admin.ch/canton/22
  name:
  - text: Législature 2022-2027
    language: fr
  description: Le Grand Conseil vaudois est élu pour cinq ans.
  landing_page: https://www.vd.ch/gc
  actor_id:
    global_uri: actors:gc_vd
    label: Grand Conseil du canton de Vaud
    abbreviation:
    - value: GC
      language: fr
  date_begin_actual: '2022-07-01'
  date_end_planned: '2027-06-30'
  datetime_created: '2022-05-10T14:00:00+02:00'
  datetime_modified: '2025-01-08T11:20:00+01:00'

```
#### Example Legislature: Cantonal legislature with a four-year term

```yaml
legislatures:
- global_uri: ops:legislature_be_2022_2026
  local_id: GR-BE-2022-2026
  spatial: https://ld.admin.ch/canton/2
  name:
  - text: Legislatur 2022–2026
    language: de
  - text: Législature 2022-2026
    language: fr
  landing_page: https://www.gr.be.ch/de/start/grosser-rat.html
  actor_id:
    global_uri: actors:gr_be
    label: Grosser Rat Bern
    abbreviation:
    - value: GR
      language: de
  date_begin_planned: '2022-06-01'
  date_end_planned: '2026-05-31'
  date_begin_actual: '2022-06-01'
  date_end_actual: '2026-05-31'
  datetime_created: '2022-04-01T10:15:00+02:00'
  datetime_modified: '2026-06-01T07:00:00+02:00'

```






</div>