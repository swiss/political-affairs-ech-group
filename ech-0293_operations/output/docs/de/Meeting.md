

## Klasse: Meeting 


_Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sessionssitzung und andere verschiedene Versammlungen verwendet wird._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| body_key | 0..1 <br/> [String](String.md) | Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit (z.B. BE für Bern, CHE für Schweiz).  |
| meeting_type | 0..1 <br/> [MeetingTypeEnum](MeetingTypeEnum.md) | Art der Sitzung, z.B. Session, Kommission, Sessionssitzung, Verschiedenes.  |
| administrative_id | 0..1 <br/> [String](String.md) | Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land.  |
| name | * <br/> [MultilingualString](MultilingualString.md) | Mehrsprachige vollständige Bezeichnung.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing Page oder weiterführende Webadresse, mehrsprachig.  |
| group_name | 0..1 <br/> [String](String.md) | Name der Gruppe oder des Gremiums.  |
| group_id | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf die Gruppe oder das Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| number | 0..1 <br/> [String](String.md) | Laufende Nummer, z.B. innerhalb der Legislatur, der Session oder des Jahres.  |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen.  |
| sequential_number | 0..1 <br/> [Integer](Integer.md) | Laufende Nummer der Sitzung, die zur Sortierung verwendet wird.  |
| position | 0..1 <br/> [String](String.md) | Ganzzahlige Position innerhalb der übergeordneten Reihenfolge.  |
| meeting_abbreviation | 0..1 <br/> [String](String.md) | Kurzbezeichnung der Session oder Sitzung (z.B. „FS24“ für die Frühjahrssession 2024).  |
| actor_name | 0..1 <br/> [String](String.md) | Name des politischen Organs (z.B. Nationalrat).  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| state | 0..1 <br/> [StateEnum](StateEnum.md) | Aktueller Status der Sitzung (geplant, abgesagt, verschoben).  |
| state_name | 0..1 <br/> [String](String.md) | Benutzerdefinierte Zustandsbeschreibung für die Sitzung.  |
| description | 0..1 <br/> [String](String.md) | Beschreibender Text zum Element.  |
| location | 0..1 <br/> [String](String.md) | Ort, an dem die Sitzung stattfindet (physischer Raum, Videokonferenz oder hybrides Format).  |
| parent_meeting | 0..1 <br/> [String](String.md) | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| parent_legislature | 0..1 <br/> [String](String.md) | Der gesetzgebende Körper, auf dem die Sitzung basiert.  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| protocol_ref | 0..1 <br/> [Protocol](Protocol.md) | Das nach der Sitzung erstellte Protokoll dieser Sitzung.  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
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

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [meetings](meetings.md) | range | [Meeting](Meeting.md) |
| [Session](Session.md) | [meetings](meetings.md) | range | [Meeting](Meeting.md) |














### Beispiele
#### Beispiel: Council of States sitting with protocol and speeches

```yaml
global_uri: parl:sr_winter25_sitzung_6
body_key: CHE
meeting_type: session
name:
- text: Sechste Sitzung
  language: de
- text: Sixième séance
  language: fr
url:
- text: https://www.parlament.ch/de/ratsbetrieb/suche-Amtliches-bulletin
  language: de
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/42
  label: Ständerat
  abbreviation:
  - value: SR
    language: de
actor_name: Ständerat
datetime_begin_planned: '2025-12-19T08:15:00+01:00'
datetime_created: '2026-01-12T00:00:00+01:00'
datetime_modified: '2026-01-12T00:00:00+01:00'

```
#### Beispiel: Cantonal parliament sitting with agenda items and votings

```yaml
global_uri: ops:meeting_sg_2025_03_15
body_key: SG
meeting_type: session
name:
- text: Kantonsratssitzung vom 15. März 2025
  language: de
url:
- text: https://www.ratsinfo.sg.ch/sessions/2025-03-15
  language: de
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/265
  label: Kantonsrat St. Gallen
  abbreviation:
  - value: KR
    language: de
actor_name: Kantonsrat St. Gallen
datetime_begin_planned: '2025-03-15T08:00:00Z'
datetime_end_planned: '2025-03-15T18:00:00Z'
datetime_begin_actual: '2025-03-15T08:15:00Z'
datetime_end_actual: '2025-03-15T17:30:00Z'
state: planned
location: Kantonsratssaal, Regierungsgebäude St. Gallen
parent_legislature: ops:legislature_sg_2024_2028
datetime_created: '2025-02-01T10:00:00Z'
datetime_modified: '2025-03-15T17:30:00Z'

```
#### Beispiel: Half-day sitting within a session

```yaml
body_key: BE
global_uri: ops:e7c5d453-848a-430a-b024-1dd2f6873aa6
meeting_type: session
name:
- text: Donnerstag (Nachmittag)
  language: de
url:
- text: >-
    https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
  language: de
- text: >-
    https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
  language: fr
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/253
  label: Grosser Rat Bern
  abbreviation:
  - value: GR
    language: de
actor_name: Grosser Rat Bern
date_begin_planned: '2025-06-05'
date_end_planned: '2025-06-05'
datetime_created: '2025-04-25T11:10:25Z'
datetime_modified: '2025-05-19T01:06:45Z'

```
#### Beispiel: Committee sitting with an attendance list

```yaml
global_uri: ops:meeting_be_committee_wak_2025_05_12
body_key: BE
meeting_type: committee
name:
- text: Sitzung Kommission für Wirtschaft und Abgaben
  language: de
- text: Séance Commission de l'économie et des redevances
  language: fr
url:
- text: https://www.gr.be.ch/kommissionen/wak/2025-05-12
  language: de
actor_id:
  global_uri: actors:committee_wak_be
  label: Kommission für Wirtschaft und Abgaben (WAK)
  abbreviation:
  - value: WAK
    language: de
actor_name: Kommission für Wirtschaft und Abgaben (WAK)
datetime_begin_planned: '2025-05-12T14:00:00Z'
datetime_end_planned: '2025-05-12T17:00:00Z'
datetime_begin_actual: '2025-05-12T14:10:00Z'
datetime_end_actual: '2025-05-12T16:45:00Z'
state: planned
location: Kommissionszimmer 301, Rathaus Bern
parent_legislature: ops:legislature_be_2022_2026
datetime_created: '2025-04-15T09:00:00Z'
datetime_modified: '2025-05-12T16:45:00Z'

```
#### Beispiel: Government sitting with a bilingual designation

```yaml
body_key: BE
global_uri: ops:340dcf932fb044dd8f8c5c943267fbcc
meeting_type: session
name:
- text: Regierungssitzung vom 31. März 2021
  language: de
- text: Séance du gouvernement du 31 mars 2021
  language: fr
url:
- text: >-
    https://www.rr.be.ch/de/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc
  language: de
- text: >-
    https://www.rr.be.ch/fr/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc
  language: fr
actor_id:
  global_uri: actors:rr_be
  label: Regierungsrat Bern
  abbreviation:
  - value: RR
    language: de
actor_name: Regierungsrat Bern
date_begin_planned: '2021-03-31'
date_end_planned: '2021-03-31'
datetime_created: '2024-10-28T01:22:26Z'
datetime_modified: '2024-11-27T20:40:57Z'

```
#### Beispiel: Landsgemeinde as meeting type sitting

```yaml
global_uri: ops:meeting_gl_landsgemeinde_2025
body_key: GL
meeting_type: sitting
name:
- text: Landsgemeinde 2025
  language: de
url:
- text: https://www.landsgemeinde.gl.ch/2025
  language: de
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/258
  label: Landsgemeinde Glarus
  abbreviation:
  - value: LG
    language: de
actor_name: Landsgemeinde Glarus
datetime_begin_planned: '2025-05-04T09:30:00Z'
datetime_end_planned: '2025-05-04T14:00:00Z'
datetime_begin_actual: '2025-05-04T09:30:00Z'
datetime_end_actual: '2025-05-04T13:45:00Z'
state: planned
location: Zaunplatz, Glarus
parent_legislature: ops:legislature_gl_2024_2028
datetime_created: '2025-01-10T12:00:00Z'
datetime_modified: '2025-05-04T13:45:00Z'

```






</div>