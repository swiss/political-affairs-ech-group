

## Klasse: Session 


_Eine Session: eine zusammenhängende Sitzungsperiode innerhalb einer Legislaturperiode. Sie fasst ihre Sitzungen zusammen (meetings) und kann auch direkt Traktanden führen (agenda_items). Die Session ist die einzige der drei zeitlichen Ebenen, auf die verzichtet werden kann: Föderaleinheiten ohne formale Sessionen lassen sie weg und hängen ihre Sitzungen direkt an die Legislaturperiode (parent_legislature). Session und Sitzung können auch zusammenfallen — eine eintägige Sitzung eines Kantonsparlaments oder eine Landsgemeinde wird als Session mit einer einzigen Sitzung abgebildet oder als Session, die ihre Traktanden direkt und ohne Sitzung führt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| spatial | 0..1 <br/> [String](String.md) | Räumliche Referenz auf eine LINDAS-Ressource (BFS-Gemeindenummer, BFS-Kantonsnummer, Bezirk oder Land). Formate: Gemeinde: https://ld.admin.ch/municipality/1234, Bezirk: https://ld.admin.ch/district/2301, Kanton: https://ld.admin.ch/canton/23, Bund: https://ld.admin.ch/country/CHE.  |
| name | * <br/> [MultilingualString](MultilingualString.md) | Mehrsprachige vollständige Bezeichnung.  |
| number | 0..1 <br/> [String](String.md) | Nummer der Session oder Sitzung, wie sie das Organ vergibt, z.B. innerhalb der Legislatur, der Session oder des Jahres. Als Zeichenkette erlaubt sie auch römische Ziffern. Nummeriert wird sehr unterschiedlich, weshalb number, sequential_number, position und meeting_abbreviation nebeneinander zur Verfügung stehen.  |
| sequential_number | 0..1 <br/> [Integer](Integer.md) | Laufende Nummer der Session oder Sitzung als Ganzzahl, die zur Sortierung verwendet wird.  |
| position | 0..1 <br/> [String](String.md) | Ganzzahlige Position innerhalb der übergeordneten Reihenfolge, z.B. einer Session innerhalb der Legislaturperiode.  |
| meeting_abbreviation | 0..1 <br/> [String](String.md) | Kurzbezeichnung der Session oder Sitzung (z.B. „FS24“ für die Frühjahrssession 2024).  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing Page oder weiterführende Webadresse, mehrsprachig.  |
| parent_legislature | 0..1 <br/> [String](String.md) | Identifikator der Legislaturperiode, zu der die Session oder Sitzung gehört. Eine Sitzung, die zu einer Session gehört, ist über die Session (parent_session) der Legislaturperiode zugeordnet; eine Sitzung ohne Session — etwa eine Kommissionssitzung oder eine Sitzung in einer Föderaleinheit ohne formale Sessionen — verweist direkt auf die Legislaturperiode.  |
| meetings | * <br/> [Meeting](Meeting.md) | Sammlung der Sitzungen.  |
| agenda_items | * <br/> [AgendaItem](AgendaItem.md) | Für diese Sitzung oder Session geplante Traktanden, eingebettet als Liste. Bei einer Sitzung bilden sie deren Traktandenliste. Bei einer Session enthalten sie Traktanden, die direkt auf Ebene der Session geplant sind — wo eine Föderaleinheit die Session nicht in einzelne Sitzungen gliedert (z.B. eine Landsgemeinde oder eine eintägige Sitzung eines Kantonsparlaments) oder für Traktanden, die (noch) keiner bestimmten Sitzung zugeordnet sind, wie in einem Sessionsprogramm. Das Gegenstück nach der Sitzung sind die im Protokoll festgehaltenen Traktanden (Protocol.protocol_items).  |
| joint_debates | * <br/> [JointDebate](JointDebate.md) | An diesem Eintrag angehängte gemeinsame Beratungen: bei einem Traktandum die Beratungen, in denen es zusammen mit anderen Traktanden behandelt wird; bei einer Sitzung oder Session die darin geführten gemeinsamen Beratungen.  |
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
| [Container](Container.md) | [sessions](sessions.md) | range | [Session](Session.md) |














### Beispiele
#### Beispiel Session: One-day sitting period of a cantonal parliament

```yaml
sessions:
- global_uri: ops:session_gl_landrat_2025_02_26
  spatial: https://ld.admin.ch/canton/8
  name:
  - text: Sitzung des Landrates vom 26.02.2025
    language: de
  url:
  - text: https://www.gl.ch/parlament/landrat/landratsprotokolle-ab-30-juni-2010.html/239
    language: de
  date_begin_planned: '2025-02-26'
  date_end_planned: '2025-02-26'
  datetime_modified: '2025-04-25T13:40:34Z'
  datetime_created: '2025-04-23T22:58:39Z'

```
#### Beispiel Session: Landsgemeinde as a sitting period

```yaml
sessions:
- global_uri: ops:session_gl_landsgemeinde_2025_05_04
  spatial: https://ld.admin.ch/canton/8
  name:
  - text: Landsgemeinde vom 04. Mai 2025
    language: de
  url:
  - text: https://www.landsgemeinde.gl.ch/landsgemeinde/2025-05-04
    language: de
  date_begin_planned: '2025-05-04'
  date_end_planned: '2025-05-04'
  agenda_items:
  - global_uri: ops:agenda_item_gl_landsgemeinde_2025_01
    agenda_item_type: item
    agenda_item_number: '1'
    agenda_item_position: 1
    agenda_item_title:
    - text: Eröffnung der Landsgemeinde
      language: de
  datetime_modified: '2025-04-25T13:40:34Z'
  datetime_created: '2025-04-23T22:58:39Z'

```
#### Beispiel Session: Federal session with a trilingual designation

```yaml
sessions:
- global_uri: ops:session_5207
  spatial: https://ld.admin.ch/country/CHE
  name:
  - text: Frühjahrssession 2025
    language: de
  - text: Session de printemps 2025
    language: fr
  - text: Sessione primaverile 2025
    language: it
  url:
  - text: https://www.parlament.ch/de/ratsbetrieb/sessionen/fruehjahr-2025
    language: de
  - text: https://www.parlament.ch/fr/ratsbetrieb/sessionen/fruehjahr-2025
    language: fr
  - text: https://www.parlament.ch/it/ratsbetrieb/sessionen/fruehjahr-2025
    language: it
  date_begin_planned: '2025-03-03'
  date_end_planned: '2025-03-21'
  parent_legislature: ops:legislature_51
  datetime_modified: '2025-04-24T00:19:37Z'
  datetime_created: '2025-03-20T14:27:09Z'

```
#### Beispiel Session: Cantonal session with a bilingual designation

```yaml
sessions:
- global_uri: ops:session_be_summer_2025
  spatial: https://ld.admin.ch/canton/2
  name:
  - text: Sommersession 2025
    language: de
  - text: Session d'été 2025
    language: fr
  url:
  - text: >-
      https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
    language: de
  - text: >-
      https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
    language: fr
  date_begin_planned: '2025-06-02'
  date_end_planned: '2025-06-12'
  datetime_modified: '2025-05-19T01:06:44Z'
  datetime_created: '2025-04-25T11:10:24Z'

```






</div>