

## Klasse: Legislature 


_Amtsdauer eines Parlaments als gesetzgebender Versammlung. Dauert in der Regel vier Jahre._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| spatial | 0..1 <br/> [String](String.md) | Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer, Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234, Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23, Bund: https://ld.admin.ch/country/CHE.  |
| administrative_id | 0..1 <br/> [String](String.md) | Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land.  |
| name | * <br/> [MultilingualString](MultilingualString.md) | Mehrsprachige vollständige Bezeichnung.  |
| description | 0..1 <br/> [String](String.md) | Beschreibender Text zum Element.  |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf das handelnde Organ/Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [legislatures](legislatures.md) | range | [Legislature](Legislature.md) |














### Beispiele
#### Beispiel Legislature: Completed federal legislature

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
#### Beispiel Legislature: Ongoing cantonal legislature with a five-year term

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
#### Beispiel Legislature: Cantonal legislature with a four-year term

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