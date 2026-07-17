---
title: "eCH-xxxx Öffentlicher Ratsbetrieb"
lang: de
toc: false
---

| **Name**              | **Öffentlicher Ratsbetrieb**                                                                                               |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------|
| **eCH-Nummer**        | eCH-0293                                                                                                                   |
| **Kategorie**         | Entwurf                                                                                                                    |
| **Reifegrad**         |                                                                                                                            |
| **Version**           | 0.1                                                                                                                        |
| **Status**            |                                                                                                                            |
| **Beschluss am**      |                                                                                                                            |
| **Ausgabedatum**      |                                                                                                                            |
| **Ersetzt Version**   | 0.0                                                                                                                        |
| **Voraussetzungen**   | ?                                                                                                                          |
| **Beilagen**          | -                                                                                                                          |
| **Sprachen**          | English (Original)                                                                                                         |
| **Autoren**           | Fachgruppe politische Geschäfte: Nicole Aeby, David Imseng, Jonas Schärer, Lena Mina Friedrich, Manuel Weingartner, Orhan Saeedi, Michel Moret, Laurens Abu-Talib |
| **Herausgeber / Vertrieb** | Verein eCH, Räffelstr. 20, 8045                                                                                       |


# Zusammenfassung

Der Standard eCH-0293 definiert ein gemeinsames Datenmodell für die Erfassung und Publikation von Informationen zum öffentlichen Ratsbetrieb in der Schweiz. Er deckt die zeitliche Organisation parlamentarischer Arbeit (Legislaturperioden, Sessionen), die Strukturierung von Sitzungen und Traktanden, Abstimmungen und Wahlen, Einzelstimmen, Anwesenheitslisten sowie Wortmeldungen und Resolutionen ab.

Dieser Standard richtet sich an Parlamentsdienste, Softwareanbieter von Parlamentsverwaltungssystemen, Datennutzer für Analysen und Visualisierungen sowie Open-Data-Plattformen.

eCH-0293 ist Teil einer Familie von Standards für politische Daten und arbeitet eng mit eCH-0294 (Actors), eCH-0295 (Affairs), eCH-0296 (Laws) und eCH-0297 (Consultations) zusammen.

# Table of Contents

< manually insert TOC here >

# Note

This document uses a gender-neutral formulation when referring to persons. This is based on the [guidelines](https://www.bk.admin.ch/bk/de/home/dokumentation/sprachen/hilfsmittel-textredaktion/leitfaden-zum-geschlechtergerechten-formulieren.html) (German) of the Federal Chancellery. Depending on the situation, paired forms (citizens), gender-abstract forms (insured person), gender-neutral forms (insured person) or paraphrases with-out personal reference are used. The generic masculine (citizen) is not permitted. Full forms are used in continuous texts, i.e. in texts consisting of formulated sentences. Short forms can be used in abbreviated text passages, namely in tables. The short form is used with a slash but without an ellipsis (referent). Gender asterisks and similar spellings are not used.

# Einleitung

## Kontext: Öffentlicher Ratsbetrieb

Auf Bundes-, Kantons- und Gemeindeebene tagen Räte und Versammlungen, beraten über politische Geschäfte, fassen Beschlüsse und kontrollieren die Exekutive.

## Zusammenhang mit anderen eCH-Standards

eCH-0293 ist Teil eines Ökosystems von Standards für politische Daten:

### eCH-0294: Politische Akteure (Actors)
Definiert Personen, Organe und Gruppen im politischen Kontext. eCH-0293 referenziert diese Akteure über `actor_id` (z.B. welches Parlament, welche Person hat abgestimmt).

### eCH-0295: Parlamentarische Geschäfte (Affairs)
Beschreibt den Lebenszyklus politischer Geschäfte. AgendaItems in eCH-0293 verweisen über `affair_id` auf die zugehörigen Geschäfte.

### eCH-0296: Erlasse und Gesetzestexte (Laws)
Erfasst die Resultate des parlamentarischen Prozesses - die verabschiedeten Gesetze und Erlasse.

### eCH-0297: Öffentliche Konsultationen (Consultations)
Strukturiert Vernehmlassungsverfahren, die oft Ausgangspunkt für parlamentarische Geschäfte sind.

ToDo: Christian

# Zeitliche Organisation des Ratsbetriebs

Der parlamentarische Betrieb ist zeitlich auf drei Ebenen organisiert: Legislaturperioden bilden den langfristigen Rahmen, Sessions strukturieren die Arbeit innerhalb einer Legislature, und Meetings sind die konkreten Sitzungen, in denen Geschäfte beraten werden. Diese Hierarchie ermöglicht sowohl langfristige Planung als auch flexible Anpassung an aktuelle Erfordernisse.

## Legislature (Legislaturperiode)

### Begriff und Bedeutung

Eine Legislaturperiode bezeichnet den Zeitraum, für den ein Parlament gewählt wird und in seiner aktuellen Zusammensetzung tätig ist. Sie bildet die oberste zeitliche Gliederungseinheit des parlamentarischen Betriebs und markiert den Rahmen für die legislative Arbeit eines Parlaments.

In der Schweiz variiert die Dauer von Legislaturperioden je nach Föderalebene:

- **Bundesebene**: 4 Jahre (Nationalrat und Ständerat)
- **Kantone**: Meist 4 Jahre, in einigen Kantonen auch 5 Jahre
- **Gemeinden**: Unterschiedlich, häufig 4 Jahre

### Struktur und Hierarchie

Die Legislaturperiode steht hierarchisch über den Sessions (Sessionen) und Meetings (Sitzungen):

```
Legislature (Legislaturperiode)
  └─ Sessions (z.B. Frühjahrssession, Herbstsession)
      └─ Meetings (einzelne Sitzungen)
          └─ Agenda Items (Traktanden)
```

### Parlamentarischer Kontext

Jede Legislature ist einem spezifischen parlamentarischen Organ zugeordnet, identifiziert durch:

- **actor_id**: Verweis auf das Parlament als politischen Akteur (z.B. Nationalrat, Kantonsrat) gemäss eCH-0294 Actors
- **administrative_id**: Verwaltungs-ID der gesetzgebenden Körperschaft (z.B. Gemeinde, Kanton, Land)

### Zeitliche Einordnung

Eine Legislaturperiode wird über das Mixin `IsEventWithDuration` charakterisiert. Die wichtigsten Datumsfelder sind:

- **date_begin_planned** / **date_begin_actual**: Geplanter bzw. tatsächlicher Beginn der Legislaturperiode (meist nach Wahlen)
- **date_end_planned** / **date_end_actual**: Geplantes bzw. tatsächliches Ende der Legislaturperiode (vor den nächsten Wahlen)

Bei Bedarf gibt es analoge `datetime_*`-Varianten mit Uhrzeit.

Beispiel Bundesebene: Die 51. Legislaturperiode des Schweizer Parlaments dauerte vom 5. Dezember 2019 bis zum 4. Dezember 2023.

### Identifikation

Über das Mixin `HasIdentification` stehen `local_id`, `global_uri` und `wikidata_uri` zur Verfügung. Der `global_uri` ist Pflicht und dient als eindeutiger Identifikator.

### Verlinkte Dokumente

Über den Slot **documents** können relevante Dokumente (z.B. Mitgliederverzeichnisse der Legislatur, Geschäftsverzeichnisse) als FRBR-Works verknüpft werden.



## Class: Legislature 


_[en] Term of office of a parliament as a legislative assembly. Usually lasts four years._

_[de] Amtsdauer eines Parlaments als gesetzgebender Versammlung. Dauert in der Regel vier Jahre._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| administrative_id | 0..1 <br/> [String](#String) | [en] Administrative ID of the legislative body, such as a municipality, canton, or country. [de] Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land.  |
| name | * <br/> [MultilingualString](#MultilingualString) | None |
| description | 0..1 <br/> [String](#String) | None |
| landing_page | 0..1 <br/> [String](#String) | [en] URL providing further information. [de] URL mit weiteren Informationen.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | [en] Reference to the acting body/organ (lightweight snapshot at time of linking). [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> [Date](#Date) | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> [Datetime](#Datetime) | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> [Date](#Date) | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> [Datetime](#Datetime) | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> [Date](#Date) | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> [Datetime](#Datetime) | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> [Date](#Date) | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> [Datetime](#Datetime) | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [legislatures](#legislatures) | range | [Legislature](#Legislature) |



















</div>

## Session (Sitzungsperiode)

### Begriff und Bedeutung

Eine Session bezeichnet eine zusammenhängende Sitzungsperiode eines Parlaments, in der mehrere Meetings (Sitzungen) stattfinden. Sie bildet die mittlere zeitliche Gliederungseinheit zwischen der Legislaturperiode und den einzelnen Sitzungen.

### Unterscheidung: Session vs. Meeting

Diese Unterscheidung ist wichtig für das Verständnis des Standards:

- **Session**: Eine Sitzungsperiode, die sich typischerweise über mehrere Tage oder Wochen erstreckt
- **Meeting**: Eine einzelne Sitzung innerhalb einer Session

#### Beispiel Bundesebene
```
Legislature (51. Legislaturperiode)
  └─ Session (Frühjahrssession 2024)
      ├─ Meeting (Nationalratssitzung 4. März 2024)
      ├─ Meeting (Ständeratssitzung 4. März 2024)
      ├─ Meeting (Nationalratssitzung 5. März 2024)
      └─ ...
```

### Zuordnung zu Organen

Eine Session bezieht sich auf das politische Organ, das die Sessionen als Reihe von Sitzungen organisiert. Beispiele:

- **Parlament**: Sessions eines Kantonsrats oder der Bundesversammlung
- **Kommissionen**: Sitzungsperioden parlamentarischer Kommissionen
- **Gemeinsame Gremien**: Z.B. Sessions der Vereinigten Bundesversammlung

Über **body_key** kann das Organ (z.B. "NR" für Nationalrat, "SR" für Ständerat) als Schlüssel hinterlegt werden. Über **parent_legislature** wird die Session der zugehörigen Legislaturperiode zugeordnet.

### Identifikation und Nummerierung

Sessions werden üblicherweise nummeriert. Folgende Slots stehen zur Verfügung — sie sind kompatibel mit der entsprechenden Modellierung bei Meeting:

- **number**: Laufende Nummer (z.B. innerhalb der Legislature oder des Jahres)
- **sequential_number**: Laufende Nummer als String (auch römische Ziffern möglich)
- **position**: Ganzzahlige Position
- **abbreviation**: Kurze Bezeichnung (z.B. "FS24" für Frühjahrssession 2024)
- **name**: Mehrsprachige vollständige Bezeichnung

Über das Mixin `HasIdentification` stehen zusätzlich `local_id`, `global_uri` und `wikidata_uri` zur Verfügung.

### Zeitliche Attribute

Sessions nutzen das Mixin `IsEventWithDuration` und bieten damit dieselben Datumsfelder wie Legislatures und Meetings:

- **date_begin_planned** / **datetime_begin_planned**: Geplanter Beginn der Session
- **date_begin_actual** / **datetime_begin_actual**: Tatsächlicher Beginn
- **date_end_planned** / **datetime_end_planned**: Geplantes Ende der Session
- **date_end_actual** / **datetime_end_actual**: Tatsächliches Ende

### Verknüpfungen

- **meetings**: Liste der Sitzungen innerhalb der Session
- **documents**: Verknüpfte FRBR-Works (z.B. Sessionsprogramm, Sessionsvorschau)
- **url**: Landing Page der Session

### Flexibilität im Standard

Der Standard ist bewusst flexibel gestaltet, um verschiedene Organisationsformen abzubilden. Föderaleinheiten ohne formale Sessions können diese Entität optional nutzen oder direkt auf Meetings referenzieren.



## Class: Session 


_[en] A parliamentary session that groups multiple meetings and spans a specific time period._

_[de] Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen bestimmten Zeitraum erstreckt._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| body_key | 0..1 <br/> [String](#String) | [en] Key identifying the political body or jurisdiction (e.g., BE for Bern, CHE for Switzerland). [de] Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit (z.B. BE für Bern, CHE für Schweiz).  |
| name | * <br/> [MultilingualString](#MultilingualString) | None |
| number | 0..1 <br/> [String](#String) | None |
| sequential_number | 0..1 <br/> [Integer](#Integer) | [en] Sequential number of the meeting, used for ordering. [de] Laufende Nummer der Sitzung, die zur Sortierung verwendet wird.  |
| position | 0..1 <br/> [String](#String) | None |
| meeting_abbreviation | 0..1 <br/> [String](#String) | None |
| url | * <br/> [MultilingualString](#MultilingualString) | None |
| parent_legislature | 0..1 <br/> [String](#String) | [en] The legislative body in which the meeting is based. [de] Der gesetzgebende Körper, auf dem die Sitzung basiert.  |
| meetings | * <br/> [Meeting](#Meeting) | None |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> [Date](#Date) | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> [Datetime](#Datetime) | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> [Date](#Date) | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> [Datetime](#Datetime) | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> [Date](#Date) | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> [Datetime](#Datetime) | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> [Date](#Date) | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> [Datetime](#Datetime) | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [sessions](#sessions) | range | [Session](#Session) |














### Examples
#### Example: Session-session_session_be_summer_2025

```yaml
global_uri: ops:session_be_summer_2025
body_key: BE
name:
- text: Sommersession 2025
  language: de
- text: Session d'été 2025
  language: fr
url:
- text: https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
  language: de
- text: https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
  language: fr
date_begin_planned: '2025-06-02'
date_end_planned: '2025-06-12'
datetime_modified: '2025-05-19T01:06:44Z'
datetime_created: '2025-04-25T11:10:24Z'

```
#### Example: Session-session_session_gl_landsgemeinde_2025_05_04

```yaml
global_uri: ops:session_gl_landsgemeinde_2025_05_04
body_key: GL
name:
- text: Landsgemeinde vom 04. Mai 2025
  language: de
url:
- text: https://www.landsgemeinde.gl.ch/landsgemeinde/2025-05-04
  language: de
date_begin_planned: '2025-05-04'
date_end_planned: '2025-05-04'
datetime_modified: '2025-04-25T13:40:34Z'
datetime_created: '2025-04-23T22:58:39Z'

```
#### Example: Session-session_session_5207

```yaml
global_uri: ops:session_5207
body_key: CHE
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
#### Example: Session-session_session_gl_landrat_2025_02_26

```yaml
global_uri: ops:session_gl_landrat_2025_02_26
body_key: GL
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






</div>

## Meeting (Einzelne Sitzung)

### Begriff und Bedeutung

Ein Meeting bezeichnet eine einzelne Sitzung eines parlamentarischen Organs. Dies ist die konkrete Veranstaltung, bei der sich die Mitglieder eines Parlaments, einer Kommission oder eines anderen Gremiums versammeln, um Geschäfte zu beraten und Beschlüsse zu fassen.

### Arten von Meetings

Der Standard unterscheidet verschiedene Meeting-Typen über das Feld **meeting_type** (Enum `MeetingTypeEnum`):

#### session
Plenarsitzungen des gesamten Parlaments oder einer Kammer

**Beispiele:**
- Nationalratssitzung während der Herbstsession
- Sitzung des Kantonsrats
- Sitzung der Vereinigten Bundesversammlung

#### committee
Sitzungen parlamentarischer Kommissionen

**Beispiele:**
- Sitzung der Kommission für Wirtschaft und Abgaben (WAK)
- Geschäftsprüfungskommission (GPK)
- Aussenpolitische Kommission (APK)

#### sitting
Spezielle Sitzungsformen

**Beispiele:**
- Landsgemeinden (in den Kantonen Glarus und Appenzell Innerrhoden)
- Bürgergemeindeversammlungen
- Gemeindeversammlungen

#### various
Andere Sitzungsformen, die nicht in die obigen Kategorien fallen

### Hierarchie und Struktur

Ein Meeting ist Teil einer Session (wenn verwendet) und enthält mehrere Agenda Items (Traktanden):

```
Session (Frühjahrssession 2024)
  └─ Meeting (Nationalratssitzung, 4. März 2024, 08:00)
      ├─ AgendaItem (Traktandum 1: Begrüssung)
      ├─ AgendaItem (Traktandum 2: Gesetzesberatung)
      └─ AgendaItem (Traktandum 3: Abstimmungen)
```

### Zeitliche Planung vs. Realität

Über das Mixin `IsEventWithDuration` unterscheidet das Meeting zwischen geplanten und tatsächlichen Zeitpunkten:

#### Geplante Daten
- **date_begin_planned** / **datetime_begin_planned**: Geplanter Beginn
- **date_end_planned** / **datetime_end_planned**: Geplantes Ende

#### Tatsächliche Daten
- **date_begin_actual** / **datetime_begin_actual**: Tatsächlicher Beginn
- **date_end_actual** / **datetime_end_actual**: Tatsächliches Ende

Diese Unterscheidung ist wichtig, da:
- Sitzungen sich verzögern können
- Traktanden vorgezogen oder verschoben werden
- Sitzungen früher als geplant enden können

**Anwendungsfall:** Eine für 14:00 geplante Sitzung beginnt aufgrund von Verzögerungen erst um 14:25 und endet statt um 18:00 bereits um 17:30.

### Sitzungsstatus

Das Feld **state** (Enum `StateEnum`) erfasst den aktuellen Status eines Meetings:

- **planned**: Die Sitzung ist geplant und wird wie vorgesehen stattfinden
- **canceled**: Die Sitzung wurde abgesagt
- **postponed**: Die Sitzung wurde verschoben

Über **state_name** kann eine abweichende, freitextliche Statusbeschreibung ergänzt werden.

Dieser Status ist wichtig für:
- Aktuelle Informationen an Parlamentsmitglieder und Öffentlichkeit
- Historische Nachvollziehbarkeit von Planungsänderungen
- Automatische Benachrichtigungen bei Änderungen

### Identifikation und Nummerierung

Meetings werden identifiziert durch:

- **local_id** / **global_uri** / **wikidata_uri** (via Mixin `HasIdentification`)
- **number**: Laufende Nummer (z.B. "5" für die 5. Sitzung einer Session)
- **sequential_number**: Laufende Nummer als String (auch römische Ziffern möglich)
- **position**: Ganzzahlige Position innerhalb der Session
- **abbreviation**: Kurze Bezeichnung (z.B. "NR-24-05")
- **name**: Mehrsprachige vollständige Bezeichnung

### Ort der Sitzung

Das Feld **location** erfasst den Sitzungsort:

- Physischer Ort: "Bundeshaus, Nationalratssaal"
- Virtuelle Sitzungen: "Videokonferenz via [Plattform]"
- Hybride Formate: "Bundeshaus und Videokonferenz"

### Zuordnung zu Organen

Das zuständige Organ wird über **actor_id** (gemäss eCH-0294 Actors) referenziert. Über **actor_name** kann zusätzlich der Name des Organs für schnellen Zugriff festgehalten werden, über **body_key** ein kurzer Schlüssel (z.B. "NR", "SR"). Über **administrative_id** kann die Verwaltungsebene angegeben werden, **group_name** und **group_id** ergänzen Gruppierungen wo nötig.

- Plenarsitzungen: Verweis auf das gesamte Parlament
- Kommissionssitzungen: Verweis auf die spezifische Kommission
- Gemeinsame Sitzungen: Verweis auf das gemeinsame Gremium

### Hierarchische Verknüpfungen

- **parent_meeting**: Falls ein Meeting Teil eines übergeordneten Meetings ist
- **parent_legislature**: Die Legislatur, in deren Rahmen das Meeting stattfindet

### Beziehungen zu anderen Entitäten

Ein Meeting verbindet verschiedene Elemente des parlamentarischen Betriebs:

- **Agenda Items**: Die behandelten Traktanden
- **Votings**: Abstimmungen während der Sitzung
- **Elections**: Wahlen während der Sitzung
- **Speeches**: Wortmeldungen und Voten
- **Attendance**: Anwesenheitslisten (über `Attendance.parent_meeting`)
- **documents**: Verknüpfte FRBR-Works (Protokolle, Sitzungsunterlagen, Tagblatt etc.)



## Class: Meeting 


_[en] A general meeting class used for Sessions, Comittee Meetings, individual session Sittings and other various Meetings._

_[de] Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sessionssitzung und andere verschiedene Versammlungen verwendet wird._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| body_key | 0..1 <br/> [String](#String) | [en] Key identifying the political body or jurisdiction (e.g., BE for Bern, CHE for Switzerland). [de] Schlüssel zur Identifizierung des politischen Organs oder der Gerichtsbarkeit (z.B. BE für Bern, CHE für Schweiz).  |
| meeting_type | 0..1 <br/> [MeetingTypeEnum](#MeetingTypeEnum) | Type of the meeting, e.g. session, committee, sitting, various |
| administrative_id | 0..1 <br/> [String](#String) | [en] Administrative ID of the legislative body, such as a municipality, canton, or country. [de] Verwaltungs-ID des gesetzgebenden Körpers, wie z.B. Gemeinde, Kanton oder Land.  |
| name | * <br/> [MultilingualString](#MultilingualString) | None |
| url | * <br/> [MultilingualString](#MultilingualString) | None |
| group_name | 0..1 <br/> [String](#String) | Name of the group or body |
| group_id | 0..1 <br/> [GroupReference](#GroupReference) | [en] Reference to the group or body (lightweight snapshot at time of linking). [de] Referenz auf die Gruppe oder das Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| number | 0..1 <br/> [String](#String) | None |
| landing_page | 0..1 <br/> [String](#String) | [en] URL providing further information. [de] URL mit weiteren Informationen.  |
| sequential_number | 0..1 <br/> [Integer](#Integer) | [en] Sequential number of the meeting, used for ordering. [de] Laufende Nummer der Sitzung, die zur Sortierung verwendet wird.  |
| position | 0..1 <br/> [String](#String) | None |
| meeting_abbreviation | 0..1 <br/> [String](#String) | None |
| actor_name | 0..1 <br/> [String](#String) | [en] Name of the political body (e.g., Nationalrat). [de] Name des politischen Organs (z.B. Nationalrat).  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | [en] Reference to the acting body/organ (lightweight snapshot at time of linking). [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| state | 0..1 <br/> [StateEnum](#StateEnum) | None |
| state_name | 0..1 <br/> [String](#String) | [en] Custom state description for the meeting. [de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung.  |
| description | 0..1 <br/> [String](#String) | None |
| location | 0..1 <br/> [String](#String) | None |
| parent_meeting | 0..1 <br/> [String](#String) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| parent_legislature | 0..1 <br/> [String](#String) | [en] The legislative body in which the meeting is based. [de] Der gesetzgebende Körper, auf dem die Sitzung basiert.  |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| protocol_ref | 0..1 <br/> [Protocol](#Protocol) | [en] The protocol (minutes) of this meeting, recorded after the meeting. [de] Das nach der Sitzung erstellte Protokoll dieser Sitzung.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> [Date](#Date) | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> [Datetime](#Datetime) | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> [Date](#Date) | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> [Datetime](#Datetime) | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> [Date](#Date) | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> [Datetime](#Datetime) | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> [Date](#Date) | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> [Datetime](#Datetime) | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [meetings](#meetings) | range | [Meeting](#Meeting) |
| [Session](#Session) | [meetings](#meetings) | range | [Meeting](#Meeting) |














### Examples
#### Example: Meeting-meeting_340dcf932fb044dd8f8c5c943267fbcc

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
- text: https://www.rr.be.ch/de/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc
  language: de
- text: https://www.rr.be.ch/fr/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc
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
#### Example: Meeting-meeting_sr_winter25_Sitzung6_sr_winter25_sitzung_6

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
#### Example: Meeting-meeting_complete_meeting_gl_landsgemeinde_2025

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
#### Example: Meeting-meeting_e7c5d453-848a-430a-b024-1dd2f6873aa6

```yaml
body_key: BE
global_uri: ops:e7c5d453-848a-430a-b024-1dd2f6873aa6
meeting_type: session
name:
- text: Donnerstag (Nachmittag)
  language: de
url:
- text: https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
  language: de
- text: https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8
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
#### Example: Meeting-meeting_complete_meeting_sg_2025_03_15

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
#### Example: Meeting-meeting_complete_meeting_be_committee_wak_2025_05_12

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






</div>

## Enum: MeetingTypeEnum 




_Type of the meeting_



<div data-search-exclude markdown="1">

URI: [ops:MeetingTypeEnum](https://ch.paf.link/schema/operations/MeetingTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| session |  None |
| | [ops:enum/meeting_type/session](ops:enum/meeting_type/session) |
| committee |  None |
| | [ops:enum/meeting_type/committee](ops:enum/meeting_type/committee) |
| sitting |  None |
| | [ops:enum/meeting_type/sitting](ops:enum/meeting_type/sitting) |
| various |  None |
| | [ops:enum/meeting_type/various](ops:enum/meeting_type/various) |







</div>

## Enum: StateEnum 




_State of the meeting_



<div data-search-exclude markdown="1">

URI: [ops:StateEnum](https://ch.paf.link/schema/operations/StateEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| planned |  None |
| | [ops:enum/state/planned](ops:enum/state/planned) |
| canceled |  None |
| | [ops:enum/state/canceled](ops:enum/state/canceled) |
| postponed |  None |
| | [ops:enum/state/postponed](ops:enum/state/postponed) |







</div>

# Anwesenheit und Wortmeldungen

Neben den formalen Entscheidungen dokumentiert der Standard auch die Teilnahme an Sitzungen und die geführten Debatten. Anwesenheitslisten erfassen wer an einer Sitzung teilgenommen hat, während Wortmeldungen die parlamentarische Debatte mit Text- und Medienaufzeichnungen festhalten.

## Attendance (Anwesenheit)

## Begriff und Bedeutung

Die Attendance (Anwesenheit) erfasst, welche Mitglieder eines parlamentarischen Organs bei einer Sitzung anwesend, abwesend oder entschuldigt waren. Sie dient der Dokumentation der Teilnahme und ist Voraussetzung für die Beschlussfähigkeit (Quorum).

## Zweiebenen-Struktur

Der Standard unterscheidet zwischen zwei Ebenen der Anwesenheitserfassung:

### 1. Attendance (Aggregierte Ebene)
Zusammenfassung der Anwesenheit für ein Meeting:
- Gesamtzahl Anwesende
- Gesamtzahl Abwesende (entschuldigt/unentschuldigt)
- Beschlussfähigkeit

### 2. IndividualAttendance (Individuelle Ebene)
Detaillierte Erfassung für jede einzelne Person:
- Wer war anwesend?
- Wer war abwesend?
- War die Abwesenheit entschuldigt?

```
Meeting (Nationalratssitzung 4. März 2024)
  └─ Attendance (Aggregierte Anwesenheit)
      ├─ IndividualAttendance (Person A: anwesend)
      ├─ IndividualAttendance (Person B: entschuldigt)
      ├─ IndividualAttendance (Person C: abwesend)
      └─ ...
```

## Attendance (Aggregierte Ebene)

### Zuordnung zu Meeting und Organ

- **parent_meeting**: Verweis auf die spezifische Sitzung, zu der die Anwesenheitsliste gehört
- **actor_id**: Verweis auf das Organ (Parlament, Kommission) gemäss eCH-0294 Actors
- **datetime_begin**: Zeitpunkt der Anwesenheitserfassung

### Aggregierte Zahlen

- **total_count**: Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen, z.B. 200 für Nationalrat, 46 für Ständerat)
- **total_present**: Anzahl anwesender Mitglieder
- **total_excused**: Anzahl entschuldigter Mitglieder
- **total_absent**: Anzahl unentschuldigt abwesender Mitglieder

**Beispiel:**
- Total: 200
- Anwesend: 185
- Entschuldigt: 12
- Abwesend: 3

### Beschlussfähigkeit

Die Beschlussfähigkeit (Quorum) ergibt sich aus dem Verhältnis von `total_present` zu `total_count` und den jeweiligen Quorum-Regeln des Gremiums. Sie wird daher nicht als eigenes Feld gespeichert, sondern bei Bedarf datenseitig berechnet.

## IndividualAttendance (Individuelle Ebene)

### Verknüpfung

- **parent_attendance**: Verweis auf das übergeordnete `Attendance`-Aggregat (das wiederum am Meeting hängt). So wird die individuelle Erfassung sauber dem Meeting zugeordnet.
- **actor_id**: Verweis auf die Person gemäss eCH-0294 Actors

### Anwesenheitstyp

Das Feld **attendance_type** (Enum `AttendanceTypeEnum`) erfasst die Art der Anwesenheit:

- **present**: Persönlich anwesend
- **remote**: Per Fernzugriff (z.B. Videokonferenz) anwesend
- **substitute**: Stellvertretung — eine andere Person hat in der Vertretung teilgenommen

> Die Modellierung der Stellvertretung (z.B. wer hat wen vertreten, mit welchem Stimmrecht) wird in [Issue #24](https://github.com/swiss/political-affairs-ech-group/issues/24) weiter ausgearbeitet.
>
> Eine zweite Status-Achse `present` / `excused` / `absent` ("ob anwesend") parallel zur bestehenden Achse "wie anwesend" ist als Erweiterung in Diskussion.

### Grund

Das Feld **reason** (mehrsprachig) kann den Grund für Abwesenheit oder Verspätung als Freitext erfassen.

## Unterschied: Attendance vs. IndividualVote

Wichtige Abgrenzung:

| Aspekt | Attendance | IndividualVote |
|--------|------------|----------------|
| Erfasst | Anwesenheit bei Sitzung | Stimmabgabe bei Abstimmung |
| Zeitpunkt | Beginn/während Sitzung | Zeitpunkt der Abstimmung |
| Granularität | Pro Meeting | Pro Voting |

**Beispiel:** Eine Person kann bei der Sitzung anwesend sein (Attendance: present), aber bei einer spezifischen Abstimmung als absent erfasst werden (IndividualVote: absent), weil sie in diesem Moment kurz den Raum verlassen hat.

## Verwendungszwecke

Die Attendance-Entitäten ermöglichen:

1. **Dokumentation**: Nachvollziehbare Erfassung der Teilnahme
2. **Quorum-Prüfung**: Sicherstellung der Beschlussfähigkeit
3. **Transparenz**: Öffentliche Information über Anwesenheit
4. **Rechenschaft**: Kontrolle der Pflichtenerfüllung
5. **Statistik**: Auswertung von Anwesenheitsquoten
6. **Administration**: Berechnung von Entschädigungen und Spesen



## Class: Attendance 


_[en] Aggregated attendance record for a meeting (number of members present, absent, excused)._

_[de] Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, Entschuldigte)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](#String) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| datetime_begin | 0..1 <br/> [Datetime](#Datetime) | [en] The date and time when the meeting or voting begins. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | [en] Reference to the acting body/organ (lightweight snapshot at time of linking). [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| total_count | 0..1 <br/> [Integer](#Integer) | [en] Total number of members of the body (reference value for quorum calculations). [de] Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen).  |
| total_present | 0..1 <br/> [Integer](#Integer) | Total number of members present |
| total_absent | 0..1 <br/> [Integer](#Integer) | [en] Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list. [de] Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total_excused | 0..1 <br/> [Integer](#Integer) | Total number of excused absences |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [attendances](#attendances) | range | [Attendance](#Attendance) |
| [IndividualAttendance](#IndividualAttendance) | [parent_attendance](#parent_attendance) | range | [Attendance](#Attendance) |



















</div>



## Class: IndividualAttendance 


_[en] Individual attendance record for a specific person at a meeting (linked via the parent Attendance aggregate)._

_[de] Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft über das übergeordnete Attendance-Aggregat)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_attendance | 0..1 <br/> [Attendance](#Attendance) | [en] The Attendance aggregate this individual attendance record belongs to. [de] Das Attendance-Aggregat, zu dem dieser einzelne Anwesenheits-Eintrag gehört.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | [en] Reference to the acting person (lightweight snapshot at time of linking). [de] Referenz auf die handelnde Person (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| attendance_type | 0..1 <br/> [AttendanceTypeEnum](#AttendanceTypeEnum) | Type of individual attendance |
| reason | * <br/> [MultilingualString](#MultilingualString) | [en] Reason for absence or lateness (free-text, multilingual). [de] Grund für Abwesenheit oder Verspätung (Freitext, mehrsprachig).  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [individual_attendances](#individual_attendances) | range | [IndividualAttendance](#IndividualAttendance) |



















</div>

## Enum: AttendanceTypeEnum 




_[en] Type of individual attendance._

_[de] Art der individuellen Anwesenheit._

__



<div data-search-exclude markdown="1">

URI: [ops:AttendanceTypeEnum](https://ch.paf.link/schema/operations/AttendanceTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| remote |  [en] Remote participation [de] Teilnahme per Fernzugriff  |
| | [ops:enum/attendance_type/remote](ops:enum/attendance_type/remote) |
| substitute |  [en] Substitute (Stellvertretung) [de] Stellvertretung  |
| | [ops:enum/attendance_type/substitute](ops:enum/attendance_type/substitute) |
| present |  [en] Present in person [de] Persönlich anwesend  |
| | [ops:enum/attendance_type/present](ops:enum/attendance_type/present) |







</div>


ToDo: Michel

# Tagesordnung (Traktandenliste), Protokoll und Beschlüsse

Die Tagesordnung einer Sitzung wird durch Traktanden strukturiert. Die Traktanden gelten als Planung einer Sitzung und bleiben nach Beginn der Sitzung in den Daten nicht mehr geändert. Anschliessend werden die gleichen Datenelemente genutzt um das Protkoll und die enthaltenen Beschlüsse fest zu halten. 

Im Falle dass es Änderungen der Traktanden während einer Sitzung gibt, werden diese im Protokoll erfasst, und damit die Traktandenliste der nächsten Sitzung angepasst.

## AgendaItem (Traktandum)

### Zweck der Entität

AgendaItem strukturiert die Tagesordnung einer Sitzung und verbindet die zeitliche Organisation (Meeting) mit den inhaltlichen Geschäften (Affairs aus eCH-0295). Es ist die zentrale Entität zur Abbildung des Sitzungsablaufs.

### Hierarchie und Struktur

Agenda Items können hierarchisch organisiert sein, um die Struktur komplexer Tagesordnungen abzubilden:

```
Meeting (Sitzung vom 4. März 2024)
  ├─ AgendaItem 1: Mitteilungen und Begrüssung
  ├─ AgendaItem 2: Gesetzesberatungen
  │   ├─ AgendaItem 2.1: Energiegesetz (Detailberatung)
  │   ├─ AgendaItem 2.2: Energiegesetz (Schlussabstimmung)
  │   └─ AgendaItem 2.3: Gesundheitsgesetz (Eintretensdebatte)
  └─ AgendaItem 3: Verschiedenes
```

Die Hierarchie wird über das Feld **parent_agenda_item** abgebildet, das auf das übergeordnete Traktandum verweist.

### Identifikation und Nummerierung

- **id**: Eindeutiger Identifikator
- **number**: Traktandennummer auf der Tagesordnung (z.B. "2.1", "3")
- **position**: Sortierreihenfolge (für die Darstellung)
- **title**: Titel des Traktandums

### Typen von Agenda Items

Das Feld **agenda_item_type** unterscheidet verschiedene Arten:

- **item**: Ein reguläres Traktandum mit Beratung und ggf. Abstimmung
- **item_group**: Eine Gruppe von Traktanden (z.B. "Gesetzesberatungen")
- **note**: Informative Einträge ohne Abstimmung (z.B. "Mitteilungen")

### Beziehung zu parlamentarischen Geschäften

Das Feld **affairs** verweist auf die zugehörigen parlamentarischen Geschäfte gemäss eCH-0295. Ein Traktandum kann sich auf mehrere Geschäfte beziehen:

- **Einzelnes Geschäft**: Ein Traktandum behandelt eine spezifische Vorlage
- **Mehrere Geschäfte**: Ein Traktandum fasst zusammenhängende Geschäfte zusammen
- **Kein Geschäft**: Administrative Traktanden (z.B. "Genehmigung des Protokolls")

**Beispiel:** Das Traktandum "Energiegesetz - Schlussabstimmung" verweist auf das Geschäft "23.XXX Energiegesetz" in eCH-0295.

### Zeitliche Planung

- **date_time**: Geplanter Zeitpunkt der Behandlung
- **date_time_actual**: Tatsächlicher Zeitpunkt der Behandlung

Diese Unterscheidung ist wichtig, da:
- Die Tagesordnung im Voraus festgelegt wird
- Der tatsächliche Ablauf davon abweichen kann
- Traktanden vorgezogen, verschoben oder vertagt werden können

### Status und Ergebnis

#### Status
Das Feld **status** zeigt den Bearbeitungsstand:
- "pending": Noch nicht behandelt
- "in_progress": Aktuell in Beratung
- "completed": Behandlung abgeschlossen
- "postponed": Vertagt auf eine spätere Sitzung
- "withdrawn": Zurückgezogen

#### Ergebnis
Das Feld **result** erfasst das Ergebnis der Behandlung:
- "accepted": Angenommen
- "rejected": Abgelehnt
- "referred": Zurückgewiesen (z.B. an Kommission)
- "noted": Zur Kenntnis genommen
- "no_decision": Keine Beschlussfassung

### Kategorisierung

Das Feld **category** erlaubt die Gruppierung nach inhaltlichen Kriterien:
- "Gesetzgebung"
- "Budget und Finanzen"
- "Interpellationen und Anfragen"
- "Wahlen"
- "Diverses"

Diese Kategorisierung ist nicht standardisiert und kann je nach Föderaleinheit variieren.

### Resolutionen zu Traktanden

Das Feld **resolution** verweist auf die Resolution(en), die zu diesem Traktandum gefasst wurde(n). Eine Resolution dokumentiert den formalen Beschluss:

```
AgendaItem: "Energiegesetz - Schlussabstimmung"
  └─ Resolution: "Annahme des Energiegesetzes mit 120 zu 75 Stimmen bei 5 Enthaltungen"
      └─ Voting: Details der Abstimmung
```

### Beschreibung und URL

- **description**: Ausführliche Beschreibung des Traktandums
- **url**: Array von mehrsprachigen URLs zu Sitzungsunterlagen:
  - Botschaften und Berichte
  - Anträge
  - Änderungsanträge
  - Abstimmungsergebnisse

### Besonderheiten verschiedener Verfahren

#### Gesetzgebungsverfahren
Ein Geschäft durchläuft mehrere Traktanden:
1. Eintretensdebatte
2. Detailberatung
3. Schlussabstimmung
4. Ggf. Differenzbereinigung zwischen den Räten

#### Interpellationen und Anfragen
- Einreichung als Traktandum
- Antwort der Regierung
- Ggf. Diskussion

#### Wahlen
- Wahlvorschlag als Traktandum
- Durchführung der Wahl
- Verkündung des Ergebnisses

### Verknüpfung mit anderen Entitäten

Ein AgendaItem ist das zentrale Bindeglied zwischen:

- **Meeting**: Die Sitzung, in der es behandelt wird
- **Affairs** (eCH-0295): Die inhaltlichen Geschäfte
- **Resolution**: Der formale Beschluss
- **Voting**: Die Abstimmung(en) zum Traktandum
- **Speech**: Voten und Wortmeldungen zum Traktandum

### Anwendungsbeispiele

...

### Verwendungszwecke

1. Strukturierung des Sitzungsablaufs und Tagesordnung
2. Verknüpfung zwischen Meetings und Affairs (eCH-0295)
3. Dokumentation von Status und Ergebnis pro Traktandum
4. Grundlage für Sitzungsprotokolle und Publikationen



## Class: AgendaItem 


_[en] An agenda item of a meeting._

_[de] Ein Traktandum einer Sitzung._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](#String) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | [en] Type of agenda item, distinguishing individual items from groups. [de] Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen.  |
| agenda_item_number | 0..1 <br/> [String](#String) | [en] Sequential number of the agenda item (string type to support roman numerals). [de] Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern).  |
| agenda_item_position | 0..1 <br/> [Integer](#Integer) | [en] Integer position of the agenda item in the meeting sequence. [de] Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge.  |
| leading_actor_id | 0..1 <br/> [String](#String) | [en] The leading department for the agenda item. [de] Das federführende Departement für den Tagesordnungspunkt.  |
| speaking_actor_id | 0..1 <br/> [String](#String) | [en] The speaker or head of the department for the agenda item. [de] Der Sprecher oder Departementsvorsteher für den Tagesordnungspunkt.  |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | [en] Title of the agenda item. [de] Titel des Traktandums.  |
| affair_id | 0..1 <br/> [String](#String) | [en] The connection to the affairs (business items) of the agenda item. [de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts.  |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | [en] Subtitle or detailed description of the agenda item. [de] Untertitel oder ausführliche Beschreibung des Traktandums.  |
| state_id | 0..1 <br/> [String](#String) | State identifier (reference to state enum or custom state) |
| state_name | 0..1 <br/> [String](#String) | [en] Custom state description for the meeting. [de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung.  |
| landing_page | 0..1 <br/> [String](#String) | [en] URL providing further information. [de] URL mit weiteren Informationen.  |
| url | * <br/> [MultilingualString](#MultilingualString) | None |
| agenda_item_category | 0..1 <br/> [String](#String) | [en] Category for grouped agenda items (e.g., introduction, by department, technical agenda items). [de] Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden).  |
| parent_agenda_item | 0..1 <br/> [String](#String) | [en] If needed, this slot builds a hierarchy of agenda items. [de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten auf.  |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | [en] The resolutionor decision taken on this agenda item. [de] Die Resolution oder Entscheidung zu diesem Traktandum.  |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> [Date](#Date) | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> [Datetime](#Datetime) | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> [Date](#Date) | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> [Datetime](#Datetime) | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> [Date](#Date) | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> [Datetime](#Datetime) | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> [Date](#Date) | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> [Datetime](#Datetime) | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [agenda_items](#agenda_items) | range | [AgendaItem](#AgendaItem) |
| [JointDebate](#JointDebate) | [agenda_items](#agenda_items) | range | [AgendaItem](#AgendaItem) |














### Examples
#### Example: AgendaItem-meeting_complete_agenda_item_be_2025_042

```yaml
global_uri: ops:agenda_item_be_2025_042
parent_meeting: ops:meeting_be_committee_wak_2025_05_12
agenda_item_type: item
agenda_item_number: '4.2'
agenda_item_position: 42
agenda_item_title:
- text: Steuergesetz - Detailberatung Art. 5
  language: de
- text: Loi fiscale - Délibération détaillée art. 5
  language: fr
agenda_item_description:
- text: Beratung von Änderungsanträgen zu Artikel 5 des Steuergesetzes
  language: de
- text: Délibération sur les propositions de modification de l'article 5 de la loi
    fiscale
  language: fr
agenda_item_category: Gesetzgebung
state_id: completed
datetime_begin_planned: '2025-05-12T15:00:00Z'
datetime_begin_actual: '2025-05-12T15:15:00Z'
affair_id: affairs:be_2024_089_steuergesetz
datetime_created: '2025-04-15T09:00:00Z'
datetime_modified: '2025-05-12T15:20:00Z'

```
#### Example: AgendaItem-meeting_item_2025_05_20-23

```yaml
global_uri: ops:2025_05_20-23
parent_meeting: ops:meeting_lausanne_2025_05_20
agenda_item_type: item
datetime_begin_planned: '2025-05-20T00:00:00Z'
agenda_item_position: 23
agenda_item_number: '23'
agenda_item_title:
- text: 'Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : « Interpellation
    urgente de Kulmiye Yusuf et crts – Solidarité sans frontières, Lausanne en faveur
    du respect du droit international et de la protection des populations civiles
    à Gaza »'
  language: fr
state_id: not_treated
agenda_item_category: ANNONCES ET INTERPELLATIONS
affair_id: affairs:INT25/027
url:
- text: https://www.lausanne.ch/apps/agir/affaire/6c/049b6c612fe2428f9be66ea39522ac6c.htm
  language: fr
datetime_created: '2025-06-07T23:50:18Z'
datetime_modified: '2025-06-07T23:50:18Z'

```
#### Example: AgendaItem-meeting_item_06fb582b753c416d8fdb05fa13873545

```yaml
global_uri: ops:06fb582b753c416d8fdb05fa13873545
parent_meeting: ops:meeting_2011_11_23
agenda_item_type: item
datetime_begin_planned: '2011-11-23T00:00:00Z'
agenda_item_position: 2
agenda_item_title:
- text: Interpellation Peter Mark betr. elektronische Datenerfassung durch Mitarbeiter
    im Werkhof – Versuchsphase
  language: de
datetime_created: '2025-03-21T23:15:19Z'
datetime_modified: '2025-03-21T23:15:19Z'

```
#### Example: AgendaItem-meeting_item_2023_10_03-52

```yaml
global_uri: ops:2023_10_03-52
parent_meeting: ops:meeting_lausanne_2023_10_03
agenda_item_type: item
datetime_begin_planned: '2023-10-03T00:00:00Z'
agenda_item_position: 52
agenda_item_number: '52'
agenda_item_title:
- text: 'Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité commerciale
    » (FIM)'
  language: fr
state_id: postponed
agenda_item_category: RAPPORTS
affair_id: affairs:POS22/029
url:
- text: https://www.lausanne.ch/apps/agir/affaire/81/b7157ea2a4994086b65cf176768c6381.htm
  language: fr
datetime_created: '2025-02-08T12:33:10Z'
datetime_modified: '2025-02-08T12:33:10Z'

```
#### Example: AgendaItem-meeting_item_0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a

```yaml
global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
parent_meeting: ops:meeting_luzern_2025_01_28
agenda_item_type: item
datetime_begin_planned: '2025-01-28T00:00:00Z'
agenda_item_position: 29
agenda_item_number: '29'
agenda_item_title:
- text: Postulat Widmer Reichlin Gisela und Mit. über Massnahmen zur Erfüllung des
    Sonderschulkonkordats und zur gezielten Behebung des Fachkräftemangels im Bereich
    schulische Heilpädagogik / Bildungs- und Kulturdepartement
  language: de
agenda_item_category: voting
url:
- text: https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
  language: de
affair_id: affairs:2024P_125
datetime_created: '2025-01-29T06:59:41Z'
datetime_modified: '2025-01-29T06:59:41Z'

```
#### Example: AgendaItem-meeting_item_16155798_4

```yaml
global_uri: ops:16155798_4
parent_meeting: ops:meeting_schaffhausen_2025_03_31_b
agenda_item_type: item
datetime_begin_planned: '2025-03-31T00:00:00Z'
agenda_item_position: 3
agenda_item_number: '3'
agenda_item_title:
- text: 'Volksmotion Nr. 2024/1 von Sandro Mamedow und Livia Schraff (Erstunterzeichnende)
    sowie weitere 150 Mitunterzeichnende vom 22. März 2024 mit dem Titel: «Für eine
    Stimme der Studierenden im Hochschulrat der Pädagogischen Hochschule Schaffhausen
    (PHSH)»'
  language: de
agenda_item_category: Traktanden
affair_id: affairs:MOT_2024_1
datetime_created: '2025-05-02T11:23:49Z'
datetime_modified: '2025-05-02T11:23:49Z'

```
#### Example: AgendaItem-meeting_complete_agenda_item_sg_2025_015

```yaml
global_uri: ops:agenda_item_sg_2025_015
parent_meeting: ops:meeting_sg_2025_03_15
agenda_item_type: item
agenda_item_number: '15'
agenda_item_position: 15
agenda_item_title:
- text: Energiegesetz - Schlussabstimmung
  language: de
agenda_item_description:
- text: Schlussabstimmung über das revidierte Energiegesetz des Kantons St. Gallen
  language: de
agenda_item_category: Gesetzgebung
state_id: completed
datetime_begin_planned: '2025-03-15T14:00:00Z'
datetime_begin_actual: '2025-03-15T14:30:00Z'
affair_id: affairs:sg_2024_123_energiegesetz
datetime_created: '2025-02-01T10:00:00Z'
datetime_modified: '2025-03-15T14:35:00Z'

```
#### Example: AgendaItem-meeting_item_87b69a72919445a493a061d9b0daeba3

```yaml
global_uri: ops:87b69a72919445a493a061d9b0daeba3
parent_meeting: ops:meeting_be_2025_06_02
agenda_item_type: item
datetime_begin_planned: '2025-06-02T00:00:00Z'
agenda_item_title:
- text: Differenzierte Anpassung des Gehalts von Lehrpersonen ohne Lehrdiplom
  language: de
affair_id: affairs:2025.GRPARL.81
datetime_created: '2025-04-25T11:10:35Z'
datetime_modified: '2025-04-25T11:10:35Z'

```
#### Example: AgendaItem-meeting_sr_winter25_Sitzung6_69905

```yaml
global_uri: ops:69905
parent_meeting: parl:sr_winter25_sitzung_6
agenda_item_type: item
datetime_begin_planned: '2025-12-19T09:15:00+01:00'
datetime_begin_actual: '2025-12-19T09:20:00+01:00'
agenda_item_number: '6'
agenda_item_position: 4
agenda_item_title:
- text: Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich
    durchführen, um die Verzögerungen zu verstehen
  language: de
affair_id: affairs:24.4471
landing_page: https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
agenda_item_category: agenda_item
datetime_created: '2026-01-12T00:00:00+01:00'
datetime_modified: '2026-01-12T00:00:00+01:00'

```
#### Example: AgendaItem-meeting_complete_agenda_item_zh_budget_2026

```yaml
global_uri: ops:agenda_item_zh_budget_2026
parent_meeting: ops:meeting_zh_2025_11_20
agenda_item_type: item
agenda_item_number: '8'
agenda_item_position: 8
agenda_item_title:
- text: Budget 2026
  language: de
agenda_item_description:
- text: Beratung und Beschlussfassung über das Kantonsbudget für das Jahr 2026
  language: de
agenda_item_category: Budget und Finanzen
state_id: completed
datetime_begin_planned: '2025-11-20T16:00:00Z'
datetime_begin_actual: '2025-11-20T16:45:00Z'
affair_id: affairs:zh_2025_budget_2026
datetime_created: '2025-10-01T08:00:00Z'
datetime_modified: '2025-11-20T16:50:00Z'

```
#### Example: AgendaItem-meeting_item_fa732e0e-7e5f-4d45-994a-fc74720c0781

```yaml
global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
parent_meeting: ops:meeting_luzern_2025_01_28_b
agenda_item_type: item
datetime_begin_planned: '2025-01-28T00:00:00Z'
agenda_item_position: 14
agenda_item_number: '14'
agenda_item_title:
- text: Postulat Stadelmann Karin Andrea und Mit. über die Überprüfung und Anpassung
    der Kriterien zum früheren Eintritt von Kindern in die Basisstufe (den freiwilligen
    Kindergarten) / Bildungs- und Kulturdepartement
  language: de
agenda_item_category: voting
url:
- text: https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=fa732e0e-7e5f-4d45-994a-fc74720c0781
  language: de
affair_id: affairs:2023P_102
datetime_created: '2025-01-29T06:59:41Z'
datetime_modified: '2025-01-29T06:59:41Z'

```
#### Example: AgendaItem-meeting_item_16155798_3

```yaml
global_uri: ops:16155798_3
parent_meeting: ops:meeting_schaffhausen_2025_03_31
agenda_item_type: item
datetime_begin_planned: '2025-03-31T00:00:00Z'
agenda_item_position: 2
agenda_item_number: '2'
agenda_item_title:
- text: Motion Nr. 2023/9 von Rainer Schmidig vom 18. Dezember 2023 betreffend zeitgemässe
    Abzüge in den Art. 35 und 37 des Gesetzes über die direkten Steuern
  language: de
agenda_item_category: Traktanden
affair_id: affairs:MOT_2023_9
datetime_created: '2025-05-02T11:23:49Z'
datetime_modified: '2025-05-02T11:23:49Z'

```
#### Example: AgendaItem-meeting_item_49_253

```yaml
global_uri: ops:49_253
parent_meeting: ops:meeting_2025_03_31
agenda_item_type: item
datetime_begin_planned: '2025-03-31T00:00:00Z'
agenda_item_position: 2
agenda_item_number: '2'
agenda_item_title:
- text: Programmvereinbarungen 2024
  language: de
datetime_created: '2025-03-29T01:07:14Z'
datetime_modified: '2025-03-29T01:07:14Z'

```
#### Example: AgendaItem-meeting_item_7b3545e4-57dc-3901-aaa8-4020da6ab0c6

```yaml
global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
parent_meeting: ops:meeting_vaud_2008_04_30
agenda_item_type: item
datetime_begin_planned: '2008-04-30T00:00:00Z'
agenda_item_position: 7
agenda_item_number: '7'
agenda_item_title:
- text: Révision partielle de sept ordonnances fédérales relatives aux produits chimiques
  language: fr
agenda_item_description:
- text: 'Le Conseil d''Etat approuve le projet de révision partielle de sept ordonnances
    fédérales relatives aux produits chimiques. Il salue la volonté des autorités
    fédérales d''introduire dans la législation fédérale les modifications nécessaires
    découlant des nouveaux règlements européens, afin d''éliminer des entraves au
    commerce et d''augmenter la sécurité d''évaluation des produits chimiques.

    '
  language: fr
url:
- text: https://www.vd.ch/actualites/decisions-du-conseil-detat/seance-du-conseil-detat/seance/265632#7b3545e4-57dc-3901-aaa8-4020da6ab0c6
  language: fr
datetime_created: '2024-12-06T10:50:04Z'
datetime_modified: '2024-12-06T10:50:04Z'

```
#### Example: AgendaItem-meeting_item_cea750a5bd7b420fa4da1c914f801384

```yaml
global_uri: ops:cea750a5bd7b420fa4da1c914f801384
parent_meeting: ops:meeting_bern_2022_03_17
agenda_item_type: item
datetime_begin_planned: '2022-03-17T17:00:00Z'
agenda_item_position: 29
agenda_item_number: '8'
agenda_item_title:
- text: 'Interpellation Fraktion GB/JA! (Katharina Gallizzi, GB): Welche Konsequenzen
    haben die Klimaziele für das Gasnetz in Bern?'
  language: de
affair_id: affairs:2020.SR.000007
url:
- text: https://stadtrat.bern.ch/de/sitzungen/detail.php?gid=000d6cf5f0bc4d89a5171e0123cfbff5#cea750a5bd7b420fa4da1c914f801384
  language: de
datetime_created: '2025-01-17T21:25:52Z'
datetime_modified: '2025-01-17T21:25:52Z'

```
#### Example: AgendaItem-meeting_item_21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de

```yaml
global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
parent_meeting: ops:meeting_bern_rr_2025_04_02
agenda_item_type: item
datetime_begin_planned: '2025-04-02T00:00:00Z'
agenda_item_title:
- text: 'Petition «Gleichberechtigung für Tagesfamilien: Gleich hohe Betreuungsgutscheine
    für alle Anbieter im Kanton Bern». Regierungsrätliches Antwortschreiben'
  language: de
affair_id: affairs:2025.STA.622
url:
- text: https://www.rr.be.ch/de/start/beschluesse/suche/geschaeftsdetail.html?guid=21c50b86d21b4b4baeb1a76738ff82a3
  language: de
datetime_created: '2025-04-25T11:11:40Z'
datetime_modified: '2025-04-25T11:11:40Z'

```






</div>

## Enum: AgendaItemTypeEnum 




_[en] Type of agenda item, distinguishing individual items from grouped items._

_[de] Art des Traktandums, unterscheidet einzelne von gruppierten Traktanden._

__



<div data-search-exclude markdown="1">

URI: [ops:AgendaItemTypeEnum](https://ch.paf.link/schema/operations/AgendaItemTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| item |  [en] Individual agenda item (Traktandum) [de] Einzelnes Traktandum  |
| | [ops:enum/agenda_item_type/item](ops:enum/agenda_item_type/item) |
| group |  [en] Group of agenda items (Traktandengruppe) [de] Traktandengruppe  |
| | [ops:enum/agenda_item_type/group](ops:enum/agenda_item_type/group) |







</div>

## Protokoll (Protocol)

### Zweck der Entität

Während die Traktanden die **Planung** einer Sitzung abbilden, hält das Protokoll den **tatsächlichen Verlauf** nach der Sitzung fest. `Protocol` ist ein Wrapper-Container, der pro Sitzung (`Meeting`) genau einmal geführt wird und die effektiv behandelten Traktanden (`protocol_items`), Abstimmungen, Wortmeldungen sowie Wortlaut-Textsegmente und Dokumente bündelt.

```
Meeting
  ├─ agenda_items   (vorher: geplante Traktanden)
  └─ protocol_ref   (nachher: Niederschrift)
        ├─ protocol_items  → ProtocolItem (wie AgendaItem)
        ├─ votings
        ├─ speeches
        ├─ text_segments
        └─ documents
```



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
| parent_meeting | 0..1 <br/> [String](#String) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| protocol_items | * <br/> [ProtocolItem](#ProtocolItem) | [en] Agenda items as actually recorded in the protocol. [de] Traktanden, wie sie im Protokoll tatsächlich festgehalten wurden.  |
| votings | * <br/> [Voting](#Voting) | Collection of voting records |
| speeches | * <br/> [Speech](#Speech) | Collection of speech records |
| text_segments | * <br/> [TextSegment](#TextSegment) | Collection of text segments (e.g. verbatim protocol) |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [protocols](#protocols) | range | [Protocol](#Protocol) |
| [Meeting](#Meeting) | [protocol_ref](#protocol_ref) | range | [Protocol](#Protocol) |



















</div>

### ProtocolItem (protokolliertes Traktandum)

`ProtocolItem` erbt sämtliche Felder von `AgendaItem` (`is_a: AgendaItem`) und bildet ein Traktandum so ab, wie es im Protokoll tatsächlich festgehalten wurde.



## Class: ProtocolItem 


_[en] An agenda item as actually recorded in the protocol._

_[de] Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](#String) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert. <br/><br/>Inheritance: [AgendaItem](#en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert. <br/><br/>Inheritance: [AgendaItem) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | [en] Type of agenda item, distinguishing individual items from groups. [de] Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen. <br/><br/>Inheritance: [AgendaItem](#en] Type of agenda item, distinguishing individual items from groups. [de] Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen. <br/><br/>Inheritance: [AgendaItem) |
| agenda_item_number | 0..1 <br/> [String](#String) | [en] Sequential number of the agenda item (string type to support roman numerals). [de] Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern). <br/><br/>Inheritance: [AgendaItem](#en] Sequential number of the agenda item (string type to support roman numerals). [de] Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern). <br/><br/>Inheritance: [AgendaItem) |
| agenda_item_position | 0..1 <br/> [Integer](#Integer) | [en] Integer position of the agenda item in the meeting sequence. [de] Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge. <br/><br/>Inheritance: [AgendaItem](#en] Integer position of the agenda item in the meeting sequence. [de] Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge. <br/><br/>Inheritance: [AgendaItem) |
| leading_actor_id | 0..1 <br/> [String](#String) | [en] The leading department for the agenda item. [de] Das federführende Departement für den Tagesordnungspunkt. <br/><br/>Inheritance: [AgendaItem](#en] The leading department for the agenda item. [de] Das federführende Departement für den Tagesordnungspunkt. <br/><br/>Inheritance: [AgendaItem) |
| speaking_actor_id | 0..1 <br/> [String](#String) | [en] The speaker or head of the department for the agenda item. [de] Der Sprecher oder Departementsvorsteher für den Tagesordnungspunkt. <br/><br/>Inheritance: [AgendaItem](#en] The speaker or head of the department for the agenda item. [de] Der Sprecher oder Departementsvorsteher für den Tagesordnungspunkt. <br/><br/>Inheritance: [AgendaItem) |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | [en] Title of the agenda item. [de] Titel des Traktandums. <br/><br/>Inheritance: [AgendaItem](#en] Title of the agenda item. [de] Titel des Traktandums. <br/><br/>Inheritance: [AgendaItem) |
| affair_id | 0..1 <br/> [String](#String) | [en] The connection to the affairs (business items) of the agenda item. [de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts. <br/><br/>Inheritance: [AgendaItem](#en] The connection to the affairs (business items) of the agenda item. [de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts. <br/><br/>Inheritance: [AgendaItem) |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | [en] Subtitle or detailed description of the agenda item. [de] Untertitel oder ausführliche Beschreibung des Traktandums. <br/><br/>Inheritance: [AgendaItem](#en] Subtitle or detailed description of the agenda item. [de] Untertitel oder ausführliche Beschreibung des Traktandums. <br/><br/>Inheritance: [AgendaItem) |
| state_id | 0..1 <br/> [String](#String) | State identifier (reference to state enum or custom state)<br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| state_name | 0..1 <br/> [String](#String) | [en] Custom state description for the meeting. [de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung. <br/><br/>Inheritance: [AgendaItem](#en] Custom state description for the meeting. [de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung. <br/><br/>Inheritance: [AgendaItem) |
| landing_page | 0..1 <br/> [String](#String) | [en] URL providing further information. [de] URL mit weiteren Informationen. <br/><br/>Inheritance: [AgendaItem](#en] URL providing further information. [de] URL mit weiteren Informationen. <br/><br/>Inheritance: [AgendaItem) |
| url | * <br/> [MultilingualString](#MultilingualString) | None<br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| agenda_item_category | 0..1 <br/> [String](#String) | [en] Category for grouped agenda items (e.g., introduction, by department, technical agenda items). [de] Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden). <br/><br/>Inheritance: [AgendaItem](#en] Category for grouped agenda items (e.g., introduction, by department, technical agenda items). [de] Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden). <br/><br/>Inheritance: [AgendaItem) |
| parent_agenda_item | 0..1 <br/> [String](#String) | [en] If needed, this slot builds a hierarchy of agenda items. [de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten auf. <br/><br/>Inheritance: [AgendaItem](#en] If needed, this slot builds a hierarchy of agenda items. [de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten auf. <br/><br/>Inheritance: [AgendaItem) |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | [en] The resolutionor decision taken on this agenda item. [de] Die Resolution oder Entscheidung zu diesem Traktandum. <br/><br/>Inheritance: [AgendaItem](#en] The resolutionor decision taken on this agenda item. [de] Die Resolution oder Entscheidung zu diesem Traktandum. <br/><br/>Inheritance: [AgendaItem) |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity. <br/><br/>Inheritance: [AgendaItem](#de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity. <br/><br/>Inheritance: [AgendaItem) |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_begin_actual | 0..1 <br/> [Date](#Date) | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> [Datetime](#Datetime) | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> [Date](#Date) | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> [Datetime](#Datetime) | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> [Date](#Date) | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> [Datetime](#Datetime) | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> [Date](#Date) | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> [Datetime](#Datetime) | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](#Protocol) | [protocol_items](#protocol_items) | range | [ProtocolItem](#ProtocolItem) |



















</div>

## Gemeinsame Beratung (JointDebate)

### Zweck der Entität

`JointDebate` fasst mehrere Traktanden zusammen, die gemeinsam beraten werden – etwa inhaltlich zusammenhängende Geschäfte, die in einer einzigen Debatte behandelt werden.



## Class: JointDebate 


_[en] Agenda Items which are debated together._

_[de] Traktanden die gemeinsam behandelt werden._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | None |






















</div>

## Resolution (Beschluss)

### Zweck der Entität

Die Resolution-Entität erfasst den formalen Beschluss zu einem Traktandum. Sie dokumentiert **was** entschieden wurde, während Voting dokumentiert **wie** (mit welchem Verfahren und Stimmenverhältnis) entschieden wurde.

### Beziehung zu AgendaItem und Voting

```
AgendaItem (Energiegesetz - Schlussabstimmung)
  ├─ Resolution (Annahme des Energiegesetzes)
  └─ Voting (120 Ja, 75 Nein, 5 Enthaltungen)
```

Ein AgendaItem kann mehrere Resolutions haben (z.B. bei mehreren Abstimmungen zum selben Traktandum). Jede Resolution referenziert typischerweise ein Voting, das die Abstimmungsdetails enthält.

### Typen von Resolutionen

Das **resolution_type**-Feld verwendet ein kontrolliertes Vokabular:

#### accepted
Das Traktandum wurde angenommen

**Anwendung:**
- Gesetzesvorlagen wurden angenommen
- Anträge wurden gutgeheissen
- Beschlüsse wurden gefasst

#### rejected
Das Traktandum wurde abgelehnt

**Anwendung:**
- Gesetzesvorlagen wurden abgelehnt
- Anträge wurden abgewiesen
- Ablehnungsbeschlüsse

#### referred_back
Rückweisung an ein anderes Gremium

**Anwendung:**
- Rückweisung an Kommission zur Überarbeitung
- Rückweisung an Regierung
- Zurück an andere Kammer (in Zweikammersystemen)

#### noted
Zur Kenntnis genommen

**Anwendung:**
- Berichte ohne Abstimmung
- Mitteilungen
- Informative Traktanden

#### postponed
Vertagt auf später

**Anwendung:**
- Aufschub der Behandlung
- Noch nicht entscheidungsreif
- Weitere Abklärungen nötig

#### withdrawn
Zurückgezogen

**Anwendung:**
- Antragsteller zieht Vorlage zurück
- Geschäft wird nicht weiterverfolgt

#### amended
Mit Änderungen angenommen

**Anwendung:**
- Gesetz mit Amendments angenommen
- Modifizierte Fassung beschlossen
- Kompromisslösung

#### no_decision
Kein Beschluss gefasst

**Anwendung:**
- Keine Mehrheit für irgendeinen Antrag
- Patt-Situation ohne Stichentscheid
- Nicht beschlussfähig

### Designentscheid: Warum separate Resolution-Entität?

**Alternative wäre gewesen:** Resolution-Typ direkt im AgendaItem speichern.

**Gründe für separate Entität:**

1. **Mehrere Beschlüsse pro Traktandum**: Ein Traktandum kann mehrere Beschlüsse haben (z.B. erst Änderungsantrag, dann Gesamtabstimmung)

2. **Strukturierte Verknüpfung zu Votings**: Klare 1:1-Beziehung zwischen Resolution und Voting

3. **Mehrsprachige Beschlusstexte**: Resolution kann ausführliche Beschlusstexte in mehreren Sprachen enthalten

4. **Zeitliche Flexibilität**: Resolution kann zeitlich vom AgendaItem getrennt erfasst werden

### Beschlusstext

- **title**: Kurze Zusammenfassung des Beschlusses
- **description**: Ausführlicher Beschlusstext

**Beispiel:**
- title: "Annahme Energiegesetz"
- description: "Der Nationalrat nimmt das Bundesgesetz über die Energiewende in der Fassung der Kommission mit 120 zu 75 Stimmen bei 5 Enthaltungen an."

### Verknüpfung zur Abstimmung

Das Feld **voting_id** verweist auf das zugehörige Voting, das die Abstimmungsdetails enthält:

- Stimmenverhältnis
- Abstimmungsverfahren
- Einzelstimmen (bei namentlichen Abstimmungen)

**Nicht alle Resolutions haben ein Voting:**
- "Zur Kenntnis genommen" erfolgt oft ohne formale Abstimmung
- Stille Annahmen
- Administrativbeschlüsse

### Zeitstempel

- **datetime_created**: Zeitpunkt des Beschlusses
- **datetime_modified**: Letzte Änderung (z.B. bei Korrekturen)

### URLs und Dokumentation

Das Feld **url** kann auf weiterführende Dokumente verweisen:
- Detaillierte Beschlusstexte
- Begründungen
- Rechtliche Grundlagen

### Anwendungsfälle in verschiedenen Kontexten

#### Gesetzgebungsverfahren
Mehrere Resolutions zu verschiedenen Phasen:
1. Resolution "Eintreten" (accepted/rejected)
2. Resolution zu Artikel 1 (accepted/amended)
3. Resolution zu Artikel 2 (accepted)
4. Resolution Gesamtabstimmung (accepted/rejected)

#### Differenzbereinigung (Zweikammersystem)
- Resolution "Zustimmung zur Fassung des Erstrats"
- Resolution "Festhalten an eigener Fassung"
- Resolution "Annahme Kompromissvorschlag"

#### Kommissionsarbeit
- Resolution "Rückweisung an Kommission mit Zusatzauftrag"
- Resolution "Annahme Kommissionsbericht"

### Technische Überlegungen

#### Granularität
Die Granularität der Resolution-Erfassung variiert:
- **Detailliert**: Jede Einzelabstimmung erhält eigene Resolution
- **Aggregiert**: Nur finaler Beschluss wird erfasst

Der Standard erlaubt beide Ansätze.

#### Mehrsprachigkeit
Bei mehrsprachigen Parlamenten (CH, BE, etc.) müssen Beschlusstexte in allen Amtssprachen erfasst werden. Dies erfolgt über MultilingualString-Arrays in title und description.

### Verwendungszwecke

1. **Offizielle Dokumentation**: Was wurde entschieden?
2. **Rechtliche Verbindlichkeit**: Formaler Beschlussnachweis
3. **Öffentliche Information**: Verständliche Zusammenfassung komplexer Abstimmungen
4. **Geschäftsführung**: Nachverfolgung von Beschlüssen und deren Umsetzung
5. **Statistische Auswertung**: Annahme-/Ablehnungsquoten



## Class: Resolution 


_[en] A resolutionor decision taken on an agenda item, including voting procedures._

_[de] Eine Resolution oder Entscheidung zu einem Traktandum, einschließlich Abstimmungsverfahren._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](#ResolutionTypeEnum) | [en] Type of resolutiontaken on the agenda item. [de] Art der Resolution zum Traktandum.  |
| type_label | 0..1 <br/> [String](#String) | [en] Custom type label when standard type values don't apply. [de] Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| vote_procedures | * <br/> [String](#String) | [en] Procedures for voting, such as secret ballot or open vote. [de] Verfahren für die Abstimmung, wie geheime Abstimmung oder offene Abstimmung.  |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [resolutions](#resolutions) | range | [Resolution](#Resolution) |
| [AgendaItem](#AgendaItem) | [has_resolution](#has_resolution) | range | [Resolution](#Resolution) |
| [ProtocolItem](#ProtocolItem) | [has_resolution](#has_resolution) | range | [Resolution](#Resolution) |



















</div>

## Enum: ResolutionTypeEnum 




_[en] Type of resolutiontaken on an agenda item._

_[de] Art der Resolution zu einem Traktandum._

__



<div data-search-exclude markdown="1">

URI: [ops:ResolutionTypeEnum](https://ch.paf.link/schema/operations/ResolutionTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| accepted |  [en] Accepted (Annahme) [de] Annahme  |
| | [ops:enum/resolution_type/accepted](ops:enum/resolution_type/accepted) |
| rejected |  [en] Rejected (Ablehnung) [de] Ablehnung  |
| | [ops:enum/resolution_type/rejected](ops:enum/resolution_type/rejected) |
| noted |  [en] Noted (Kenntnisnahme) [de] Kenntnisnahme  |
| | [ops:enum/resolution_type/noted](ops:enum/resolution_type/noted) |
| accepted_point_by_point |  [en] Accepted point by point (Punktweise Annahme) [de] Punktweise Annahme  |
| | [ops:enum/resolution_type/accepted_point_by_point](ops:enum/resolution_type/accepted_point_by_point) |
| accepted_with_postulate |  [en] Accepted with postulate (Annahme mit Postulat) [de] Annahme mit Postulat  |
| | [ops:enum/resolution_type/accepted_with_postulate](ops:enum/resolution_type/accepted_with_postulate) |
| orally_settled |  [en] Orally settled (Mündlich erledigt) [de] Mündlich erledigt  |
| | [ops:enum/resolution_type/orally_settled](ops:enum/resolution_type/orally_settled) |
| nearly_unanimous |  [en] Nearly unanimous (Beinahe einstimmig) [de] Beinahe einstimmig  |
| | [ops:enum/resolution_type/nearly_unanimous](ops:enum/resolution_type/nearly_unanimous) |
| other |  [en] Other resolutiontype not covered by standard categories [de] Andere Resolution, nicht durch Standardkategorien abgedeckt  |
| | [ops:enum/resolution_type/other](ops:enum/resolution_type/other) |







</div>

## Motion (Anträge)

### Zweck

Erfasst Anträge, die während der Sitzung gestellt werden (Änderungsanträge, Verfahrensanträge, etc.).

### Struktur

- **motion_type**: Art des Antrags
  - **amendment**: Änderungsantrag zu Gesetzestext
  - **procedural**: Verfahrensantrag (z.B. Schluss der Debatte)
  - **referral**: Rückweisungsantrag
  - **other**: Sonstige Anträge
- **title**: Kurztitel des Antrags
- **description**: Vollständiger Antragstext
- **proposer_person_id**: Antragsteller/in
- **seconder_person_id**: Mitstimmende (falls erforderlich)
- **result**: Ergebnis (accepted, rejected, withdrawn)

### Designentscheid

**Warum eigene Entität statt nur in AgendaItem?**
- Ein Traktandum kann mehrere Anträge enthalten
- Anträge haben eigene Lifecycle (gestellt, unterstützt, abgestimmt)
- Strukturierte Erfassung von Antragsteller und Unterstützern
- Separate Abstimmungen pro Antrag möglich

### Anwendung

Verknüpft mit AgendaItem und optional mit Voting:

```
AgendaItem (Energiegesetz - Art. 15)
  ├─ Motion (Änderungsantrag Person A)
  │   └─ Voting (Abstimmung über Änderungsantrag)
  ├─ Motion (Änderungsantrag Person B)
  │   └─ Voting (Abstimmung über Änderungsantrag)
  └─ Voting (Abstimmung über Artikel in Gesamtheit)
```



## Class: Motion 


_[en] A formal proposal or motion submitted during proceedings._

_[de] Ein formeller Antrag, der während der Verhandlungen eingereicht wird._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| title | 0..1 <br/> [String](#String) | None |
| description | 0..1 <br/> [String](#String) | None |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |






















</div>

ToDo: Nicole

# Abstimmungen und Wahlen

Parlamentarische Beschlussfassungen erfolgen entweder durch Abstimmungen über Sachfragen oder durch Wahlen von Personen. Der Standard unterscheidet diese beiden Mechanismen klar und erfasst bei offenen Verfahren zudem das individuelle Stimm- und Wahlverhalten jedes Parlamentsmitglieds. Parlamentspräsidentinnen oder Parlamentspräsidenten nehmen an Abstimmungen grundsätzlich nicht teil; sie stimmen nur bei Wahlen mit. Bei Abstimmungen mit Stimmengleichstand fällen sie den Stichentscheid. 

## Voting (Abstimmung)

## Zweck der Entität

"Voting" erfasst den Abstimmungsprozess und das Ergebnis einer formalen Entscheidung im Parlament. Die Entität dokumentiert sowohl den Abstimmungsgegenstand (Frage), als auch das Verfahren (wie wurde abgestimmt) und das Resultat (mit welchem Stimmenverhältnis).

## Arten von Abstimmungen

Der Standard unterscheidet verschiedene Abstimmungstypen über das Feld **voting_type**:

### intermediate
Zwischenabstimmungen während der Beratung.

**Beispiele:**
- Abstimmung über Eintreten auf ein Geschäft
- Abstimmung über einen Antrag
- Gegenüberstellung von zwei Anträgen, die sich gegenseitig ausschliessen oder sich auf denselben Textabschnitt beziehen
- Eventualabstimmung wenn zu einem Abstimmungsgegenstand mehr als zwei Anträge vorliegen
- Abstimmung über einen einzelnen Artikel eines Gesetzes
- Gesamtabstimmung nach der ersten Lesung eines Erlasses, der in zwei Lesungen beraten wird

### final
Die abschliessende Abstimmung über die gesamte Vorlage

**Beispiele:**
- Schlussabstimmung nach der letzten Lesung eines Erlasses
- Gesamtabstimmung über einen Beschluss
- Annahme oder Ablehnung einer Vorlage in ihrer Gesamtheit
- Punktweise Abstimmung über einen Vorstoss

### casting
Stichentscheid des/der Vorsitzenden bei Stimmengleichheit. Vorsitzende nehmen an Abstimmungen nicht teil, haben bei Stimmengleichheit jedoch den Stichentscheid. Bei geheimer Abstimmung gilt bei Stimmengleichheit der Antrag des vorberatenden Ratsorgans als angenommen. 

### secret
Geheime Stimmabgabe bei Abstimmungen und Wahlen

**Anwendung:**
- Wahl von Personen
- Abstimmung über besonders heikles Sachgeschäft wie Gnadengesuch oder Aufhebung der Immunität
- Abstimmung nach geheimer Beratung
- Geheime Abstimmung auf Antrag 

## Struktur einer Abstimmung

Eine Abstimmung ist immer einer Sitzungsphase und/oder einer Sitzung, einem Traktandum (Agenda-Item) und einem Geschäft mit Geschäftstitel und mit Geschäftsnummer zugeordnet. Sie umfasst den Abstimmungstyp, den Abstimmungsgegenstand (Frage), das Ergebnis und – bei nicht geheimer Abstimmung – die Einzelstimmen der Mitglieder. 
Sie kann entweder:

```
AgendaItem (15) Geschäft (Energiegesetz - Art. 15)
  └─ Voting (Zwischenabstimmung über Art. 15)
      ├─ IndividualVote (Person A: Ja)
      ├─ IndividualVote (Person B: Nein)
      └─ IndividualVote (Person C: Ja)
```


Beispiel Auswahl:
3 Optionen: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
5 Optionen: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=23f01ba9b3f3410cb9cfb85f32f3dfe0

## Abstimmungsverfahren

Das Feld **procedure** beschreibt die Art der Durchführung:

### Open procedures (Offene Abstimmungen)
- **show_of_hands**: Handzeichen (traditionell)
- **standing**: Aufstehen (seltener)
- **electronic**: Elektronische Abstimmung (häufig auf Bundesebene und Kantonsebene)
- **roll_call**: Namentliche Abstimmung mit Namensaufruf
- **remote_voting**: Externe Stimmabgabe bei Krisen (Einzelne Ratsmitglieder geben ihre Stimme dem Parlamentspräsidium im Vorfeld des Sitzungstags bekannt. Die extern abgegebenen Stimmen werden gleichzeitig mit der im Rat laufenden Abstimmung erfasst.
- **circulation_voting**: Zirkulationsverfahren bei Krisen (Das Parlamentspräsidium führt die Abstimmung im Zirkulationsverfahren durch und informiert über das Ergebnis)
- **virtual_voting**: Stimmabgabe an virtuellen Sitzungen in Krisenfällen.

### Secret procedures (Geheime Abstimmungen)
- **secret_ballot**: Geheime Wahl mit Stimmzetteln
- **electronic_secret**: Elektronische geheime Abstimmung

Die Wahl des Verfahrens beeinflusst, ob Einzelstimmen erfasst werden können:
- Offene Verfahren: Einzelstimmen dokumentierbar
- Geheime Verfahren: Nur Gesamtergebnis verfügbar


## Abstimmungsergebnis

Das Ergebnis wird auf zwei Arten erfasst:

### Detaillierte Zahlen
- **total_count_yes**: Anzahl Ja-Stimmen
- **total_count_no**: Anzahl Nein-Stimmen
- **total_count_abstention**: Anzahl Enthaltungen
- **total_other**: Stimmenzahlen für zusätzliche Optionen, wenn nicht nur Ja/Nein/Enthaltung zur Auswahl stehen (siehe Abschnitt "Mehrfachoptionen")
- **total_absent**: Anzahl Abwesende (die nicht abstimmen konnten)
- **total**: Gesamtzahl der abstimmenden Mitglieder (ohne Abwesende und Präsidiumsstimme)
- **majority_count**: Anzahl Stimmen, die für die erforderliche Mehrheit nötig waren

### Gesamtergebnis
Das Ergebnis wird als Freitext im Feld **result_text** beschrieben (z.B. "Mit 120 zu 75 Stimmen bei 5 Enthaltungen angenommen"). Die kategorische Entscheidung (angenommen / abgelehnt / Kenntnisnahme usw.) wird nicht auf der Abstimmung selbst, sondern über die Klasse **Resolution** (Slot **resolution_type**) zum Traktandum festgehalten. Bei Stimmengleichheit wird ein allfälliger Stichentscheid des Präsidiums über eine eigene Abstimmung (`voting_type: tie_breaker_president`) bzw. eine neue Abstimmung modelliert.

**Beispiel** (Schlussabstimmung, einfache Ja/Nein-Abstimmung):
- total_count_yes: 120
- total_count_no: 75
- total_count_abstention: 5
- total_absent: 0
- total: 200
- result_text: "Mit 120 zu 75 Stimmen bei 5 Enthaltungen angenommen"
- Resolution.resolution_type: accepted

<!-- TODO: weitere komplexere Beispiele ergänzen — Ordnungsantrag, Wiederholung einer Abstimmung. (Cup-/Mehrfachabstimmung und Stichentscheid sind abgedeckt.) -->

### Mehrfachoptionen (Auswahlabstimmungen / "gleichgerichtete Anträge")

Nicht jede Abstimmung kennt nur Ja, Nein und Enthaltung. Liegen zu derselben Sachfrage mehrere gleichgerichtete Anträge vor, stimmen die Mitglieder über mehr als zwei Varianten gleichzeitig ab (in Zürich umgangssprachlich "Cup-Abstimmung", technisch über mehrere Abstimmungsknöpfe). Die obsiegende Variante ist diejenige mit den meisten Stimmen.

Solche Verfahren werden wie folgt abgebildet:

- **voting_type** = `other`, ergänzt durch ein sprechendes **type_label** (z.B. "Gleichgerichtete Anträge (Mehrfachauswahl)").
- Die Standardfelder **total_count_yes / total_count_no / total_count_abstention** bleiben leer, da die Optionen nicht Ja/Nein/Enthaltung entsprechen.
- Jede Auswahloption erhält stattdessen einen Eintrag in **total_other** (Liste von `TotalOther` mit **count** und **label**). So lassen sich beliebig viele Optionen mit ihrer jeweiligen Stimmenzahl erfassen.
- Auf Ebene der Einzelstimme wird **individual_vote_type** = `other` gesetzt und die gewählte Option über **type_label** (z.B. "Auswahl A") festgehalten; abwesende Mitglieder erhalten `not_voted`.
- Als **majority_type** wird `other` verwendet, da nicht eine fixe Schwelle, sondern die relative Mehrheit unter den Optionen entscheidet.

**Beispiel** (Gemeinderat der Stadt Zürich, 86. Sitzung vom 28.02.2024, Geschäft 2023/361 "Wohnhaus Magnusstrasse 27, Netto-Zusatzkredit") — gleichgerichtete Anträge mit vier Auswahloptionen:

| Option | Stimmen |
|--------|---------|
| Auswahl A (obsiegend) | 75 |
| Auswahl B | 25 |
| Auswahl C | 12 |
| Auswahl D | 0 |
| Abwesend | 13 |

- Total abgegeben: 112 (von 125 Mitgliedern)
- Ergebnis: Auswahl A angenommen (relative Mehrheit)

Die vollständige Modellierung dieses Falls findet sich in `data_voting.yaml` (`ops:voting_zh_gr_2024_2023_361`).

## Mehrheitstypen

Das Feld **majority_type** definiert die erforderliche Mehrheit:

### simple
Einfache Mehrheit (mehr Ja als Nein)

**Anwendung:**
- Standardfall für die meisten Beschlüsse
- Enthaltungen zählen nicht mit

**Beispiel:** 100 Ja, 80 Nein, 20 Enthaltungen → Angenommen

### absolute
Absolute Mehrheit (mehr als die Hälfte aller Mitglieder)

**Anwendung:**
- Wahlen
- Verfassungsänderungen in einigen Kantonen
- Besonders wichtige Beschlüsse

**Beispiel:** Bei 200 Mitgliedern sind mindestens 101 Ja-Stimmen erforderlich

### two_thirds
Zweidrittelmehrheit

**Anwendung:**
- Dringlichkeitsklauseln auf Bundesebene
- Verfassungsänderungen in einigen Kantonen
- Aufhebung der Immunität

**Beispiel:** Bei 200 Mitgliedern sind mindestens 134 Ja-Stimmen erforderlich

### qualified
Qualifizierte Mehrheit (andere Schwellenwerte)

**Anwendung:**
- Spezielle Anforderungen in einzelnen Kantonen oder Gemeinden
- Das konkrete Quorum wird in **majority_threshold** angegeben

## Schwellenwert

Das Feld **majority_threshold** gibt bei qualifizierten Mehrheiten den genauen Schwellenwert an (z.B. 0.6 für 60%).

## Quorum

Das Feld **quorum** definiert die Mindestanzahl anwesender Mitglieder für die Beschlussfähigkeit:

**Beispiel:** Ein Parlament mit 200 Mitgliedern ist beschlussfähig, wenn mindestens 100 Mitglieder anwesend sind (quorum: 100).

## Namentliche Abstimmungen
Das Feld **named_vote** zeigt an, ob es sich um eine namentliche Abstimmung handelt: 

- **true**: Die Einzelstimmen werden erfasst und publiziert
- **false**: Nur das Gesamtergebnis wird erfasst

Namentliche Abstimmungen sind wichtig für:
- Transparenz des Abstimmungsverhaltens
- Analyse von Abstimmungsmustern
- Rechenschaftspflicht gegenüber Wählerinnen

## Beziehung zu Einzelstimmen

Bei namentlichen Abstimmungen verweist die Voting-Entität auf die einzelnen IndividualVote-Entitäten:

```
Voting
  ├─ IndividualVote (Person A)
  ├─ IndividualVote (Person B)
  └─ ...
```

**Beispiel:** Namensliste in Akkordeon https://www.tagblatt.gr.be.ch/shareparl?agendaItemUid=e65d81c90d1d43deb19ef078f7e363f3&segmentType=vote&unitName=default&scroll=true&autoplay=false 


## Beschreibung und Dokumentation

- **description**: Beschreibung worüber abgestimmt wurde (Abstimmungsgegenstand, Abstimmungsfrage)
- **url**: Mehrsprachige URLs zu Abstimmungsdetails

## Zeitstempel

- **datetime_created**: Zeitpunkt der Durchführung der Abstimmung
- **datetime_modified**: Letzte Aktualisierung (z.B. bei Korrekturen des Abstimmungsprotkolls)




## Class: Voting 


_[en] A voting procedure with individual votes and results._

_[de] Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| datetime_begin | 0..1 <br/> [Datetime](#Datetime) | [en] The date and time when the meeting or voting begins. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> [Datetime](#Datetime) | [en] The date and time when the meeting or voting ends. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| voting_type | 0..1 <br/> [VotingTypeEnum](#VotingTypeEnum) | [en] Type of voting procedure (preliminary, final, secret, etc.). [de] Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc.).  |
| type_label | 0..1 <br/> [String](#String) | [en] Custom type label when standard type values don't apply. [de] Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| voting_title | * <br/> [MultilingualString](#MultilingualString) | [en] Title or question being voted on. If no specific subject exists, do not use the business item title. [de] Abstimmungstitel bzw. Gegenstand oder Frage. Wenn kein Gegenstand vorhanden ist, sollte nicht der Geschäftstitel verwendet werden.  |
| optional | 0..1 <br/> [Boolean](#Boolean) | [en] Indicates if the meeting or voting is optional. [de] Gibt an, ob die Sitzung oder Abstimmung optional ist.  |
| landing_page | 0..1 <br/> [String](#String) | [en] URL providing further information. [de] URL mit weiteren Informationen.  |
| label_yes | 0..1 <br/> [String](#String) | [en] Meaning of a 'yes' vote. [de] Bedeutung einer 'Ja'-Stimme.  |
| label_no | 0..1 <br/> [String](#String) | [en] Meaning of a 'no' vote. [de] Bedeutung einer 'Nein'-Stimme.  |
| label_abstention | 0..1 <br/> [String](#String) | [en] Meaning of an 'abstention' vote. [de] Bedeutung einer Enthaltungsstimme.  |
| tie_breaker | 0..1 <br/> [Boolean](#Boolean) | [en] Indicates if a tie-breaker was used in the voting. [de] Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde.  |
| total_count_yes | 0..1 <br/> [Integer](#Integer) | [en] Total number of 'yes' votes. [de] Gesamtzahl der 'Ja'-Stimmen.  |
| total_count_no | 0..1 <br/> [Integer](#Integer) | [en] Total number of 'no' votes. [de] Gesamtzahl der 'Nein'-Stimmen.  |
| total_count_abstention | 0..1 <br/> [Integer](#Integer) | [en] Total number of abstentions. [de] Gesamtzahl der Enthaltungen.  |
| total_other | * <br/> [TotalOther](#TotalOther) | [en] Used when multiple options are presented for voting (e.g., 5 buttons in Zurich). [de] Wird verwendet, wenn mehrere Optionen zur Abstimmung gestellt werden (z.B. 5 Knöpfe in Zürich).  |
| total_absent | 0..1 <br/> [Integer](#Integer) | [en] Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list. [de] Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total | 0..1 <br/> [Integer](#Integer) | [en] Total number of votes, excluding absent and president's vote. [de] Gesamtzahl der Stimmen, ohne abwesende und Präsidentenstimmen.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | [en] Type of majority required for the vote (absolute, two-thirds, etc.). [de] Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.).  |
| majority_count | 0..1 <br/> [Integer](#Integer) | [en] Number of votes required for the relevant majority threshold. [de] Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind.  |
| result_text | 0..1 <br/> [String](#String) | [en] Free text describing the outcome of the vote, e.g., "Accepted with 78 votes". [de] Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. "Mit 78 Stimmen angenommen".  |
| parent_meeting | 0..1 <br/> [String](#String) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| parent_agenda_item | 0..1 <br/> [String](#String) | [en] If needed, this slot builds a hierarchy of agenda items. [de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten auf.  |
| affair_id | 0..1 <br/> [String](#String) | [en] The connection to the affairs (business items) of the agenda item. [de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | [en] Reference to the acting body/organ (lightweight snapshot at time of linking). [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [votings](#votings) | range | [Voting](#Voting) |
| [Protocol](#Protocol) | [votings](#votings) | range | [Voting](#Voting) |
| [IndividualVote](#IndividualVote) | [parent_voting](#parent_voting) | range | [Voting](#Voting) |














### Examples
#### Example: Voting-voting_voting_be_2025_042

```yaml
global_uri: ops:voting_be_2025_042
voting_title:
- text: Änderungsantrag Art. 5 Abs. 2
  language: de
- text: Proposition de modification art. 5 al. 2
  language: fr
voting_type: preliminary_vote
datetime_begin: '2025-06-05T10:15:00Z'
datetime_end: '2025-06-05T10:17:00Z'
total_count_yes: 45
total_count_no: 87
total_count_abstention: 8
total_absent: 10
total: 150
majority_type: absolute
majority_count: 76
result_text: Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt
parent_agenda_item: ops:agenda_item_be_2025_042
parent_meeting: ops:meeting_be_2025_06_05
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/253
  label: Grosser Rat Bern
  abbreviation:
  - value: GR
    language: de
datetime_created: '2025-06-05T10:15:00Z'
datetime_modified: '2025-06-05T10:15:00Z'

```
#### Example: Voting-voting_voting_zh_gr_2024_2023_361

```yaml
global_uri: ops:voting_zh_gr_2024_2023_361
voting_title:
- text: Liegenschaften Stadt Zürich, Wohnhaus Magnusstrasse 27, Gesamtinstandsetzung,
    Grundrissanpassung, Netto-Zusatzkredit (Geschäft 2023/361)
  language: de
voting_type: other
type_label: Gleichgerichtete Anträge (Mehrfachauswahl)
datetime_begin: '2024-02-28T00:00:00Z'
datetime_end: '2024-02-28T00:00:00Z'
landing_page: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
total_other:
- count: 75
  label: Auswahl A (siegreich)
- count: 25
  label: Auswahl B
- count: 12
  label: Auswahl C
- count: 0
  label: Auswahl D
total_absent: 13
total: 112
majority_type: other
result_text: 'Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B:
  25, Auswahl C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern).'
parent_agenda_item: ops:agenda_item_zh_gr_2024_2023_361
parent_meeting: ops:meeting_zh_gr_2024_02_28
affair_id: 2023/361
actor_id:
  global_uri: https://www.gemeinderat-zuerich.ch/
  label: Gemeinderat der Stadt Zürich
  abbreviation:
  - value: GR
    language: de
datetime_created: '2024-02-28T00:00:00Z'
datetime_modified: '2024-02-28T00:00:00Z'

```
#### Example: Voting-voting_voting_sg_2025_001

```yaml
global_uri: ops:voting_sg_2025_001
voting_title:
- text: Schlussabstimmung Energiegesetz
  language: de
voting_type: final_vote
datetime_begin: '2025-03-15T14:30:00Z'
datetime_end: '2025-03-15T14:35:00Z'
total_count_yes: 78
total_count_no: 42
total_count_abstention: 5
total_absent: 3
total: 128
majority_type: absolute
majority_count: 65
result_text: Mit 78 zu 42 Stimmen bei 5 Enthaltungen angenommen
parent_agenda_item: ops:agenda_item_sg_2025_015
parent_meeting: ops:meeting_sg_2025_03_15
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/265
  label: Kantonsrat St. Gallen
  abbreviation:
  - value: KR
    language: de
datetime_created: '2025-03-15T14:30:00Z'
datetime_modified: '2025-03-15T14:35:00Z'

```
#### Example: Voting-voting_voting_zh_budget_2026

```yaml
global_uri: ops:voting_zh_budget_2026
voting_title:
- text: Budgetbeschluss 2026
  language: de
voting_type: final_vote
datetime_begin: '2025-11-20T16:45:00Z'
datetime_end: '2025-11-20T16:50:00Z'
total_count_yes: 105
total_count_no: 70
total_count_abstention: 5
total_absent: 0
total: 180
majority_type: absolute
majority_count: 91
result_text: Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen
parent_agenda_item: ops:agenda_item_zh_budget_2026
parent_meeting: ops:meeting_zh_2025_11_20
actor_id:
  global_uri: https://api.openparldata.ch/v1/bodies/275
  label: Kantonsrat Zürich
  abbreviation:
  - value: KR
    language: de
datetime_created: '2025-11-20T16:45:00Z'
datetime_modified: '2025-11-20T16:50:00Z'

```






</div>

## Enum: VotingTypeEnum 




_[en] Type of voting procedure._

_[de] Art des Abstimmungsverfahrens._

__



<div data-search-exclude markdown="1">

URI: [ops:VotingTypeEnum](https://ch.paf.link/schema/operations/VotingTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| preliminary_vote |  [en] Preliminary vote (Zwischenabstimmung) [de] Zwischenabstimmung  |
| | [ops:enum/voting_type/preliminary_vote](ops:enum/voting_type/preliminary_vote) |
| final_vote |  [en] Final vote (Schlussabstimmung) [de] Schlussabstimmung  |
| | [ops:enum/voting_type/final_vote](ops:enum/voting_type/final_vote) |
| tie_breaker_president |  [en] President's tie-breaking vote (Stichentscheid Präsidium) [de] Stichentscheid Präsidium  |
| | [ops:enum/voting_type/tie_breaker_president](ops:enum/voting_type/tie_breaker_president) |
| secret_vote |  [en] Secret ballot (Geheime Wahl/Abstimmung) [de] Geheime Wahl/Abstimmung  |
| | [ops:enum/voting_type/secret_vote](ops:enum/voting_type/secret_vote) |
| other |  [en] Other voting type [de] Andere Abstimmungsart  |
| | [ops:enum/voting_type/other](ops:enum/voting_type/other) |







</div>

## Enum: MajorityTypeEnum 




_Type of majority required for the vote_



<div data-search-exclude markdown="1">

URI: [ops:MajorityTypeEnum](https://ch.paf.link/schema/operations/MajorityTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| absolute |  None |
| | [ops:enum/majority_type/absolute](ops:enum/majority_type/absolute) |
| two_thirds |  None |
| | [ops:enum/majority_type/two_thirds](ops:enum/majority_type/two_thirds) |
| other |  None |
| | [ops:enum/majority_type/other](ops:enum/majority_type/other) |







</div>

## Individual Vote (Einzelstimme)

## Zweck der Entität

IndividualVote erfasst das Stimmverhalten einzelner Parlamentsmitglieder bei namentlichen Abstimmungen. Die Entität wird nur erstellt, wenn eine Abstimmung nicht geheim durchgeführt wird (Voting.is_nominal = true).

## Beziehung zur Abstimmung

Jede Individual Vote ist Teil eines übergeordneten Votings (Abstimmung):

```
Voting (Schlussabstimmung Energiegesetz)
  ├─ IndividualVote (Nationalrätin Anna Müller: Ja)
  ├─ IndividualVote (Nationalrat Beat Schweizer: Nein)
  ├─ IndividualVote (Nationalrätin Carla Rossi: Enthaltung)
  └─ ...
```

## Identifikation der Person

Die stimmende Person wird über das Feld **person_id** referenziert. Diese ID entspricht einer Person gemäss eCH-0294 Actors Standard.

Zusätzlich können weitere Identifikationsdaten erfasst werden:
- **person_name**: Name der Person (für schnellen Zugriff)
- **person_number**: Interne Nummer (z.B. Mandatsnummer)
- **person_political_group**: Fraktionszugehörigkeit
- **person_party**: Parteizugehörigkeit

## Arten von Stimmen

TODO: Aufführen mit dem Umgang von "Anderen", Stimmen für möglichkeiten welche nicht Ja, Nein, Enthaltung umfassen.

Das Feld **vote** erfasst die Art der Stimmabgabe:

### yes
Ja-Stimme (Zustimmung)

**Bedeutung:** Die Person stimmt der Vorlage/dem Antrag zu.

### no
Nein-Stimme (Ablehnung)

**Bedeutung:** Die Person lehnt die Vorlage/den Antrag ab.

### abstention
Enthaltung

**Bedeutung:** Die Person nimmt an der Abstimmung teil, enthält sich aber der Stimme. Bei elektronischer Stimmabgabe drückt sie den Knopf "Enthaltung". 

## Stimmgewicht

Das Feld **weight** erfasst das Stimmgewicht:

- **Standardfall**: 1.0 (eine Stimme)
- **Spezialfälle**: Andere Werte möglich

### Anwendungsfälle für abweichendes Stimmgewicht

1. **Stellvertretung**: In einigen Systemen kann eine Person für eine abwesende Person mitstimmen (weight: 2.0)
3. **Gemeindeversammlungen**: In speziellen Fällen können juristische Personen mehrere Stimmen haben
4. **Historische Systeme**: Früher hatten in einigen Kantonen verschiedene Personengruppen unterschiedliches Stimmgewicht

## Gruppenzugehörigkeit

Das Feld **group_id** erfasst die Fraktionszugehörigkeit zum Zeitpunkt der Abstimmung:

**Nutzen:**
- Analyse des Abstimmungsverhaltens nach Fraktionen
- Ermittlung der Parteidisziplin
- Identifikation von Koalitionen

**Beispiel:** Bei einer Abstimmung über das Energiegesetz stimmen 90% der SP-Fraktion mit Ja, 80% der SVP-Fraktion mit Nein.

## Position und Reihenfolge

Das Feld **position** definiert die Gruppierung und Sortierreihenfolge bei der Darstellung:

**Anwendung:**
- Alphabetische Sortierung nach Nachname
- Sortierung nach Fraktion
- Sortierung nach Stimmabgabe (erst Ja, dann Nein, dann Enthaltungen)
- Gruppierung nach Fraktion, innerhalb der Fraktion nach Ja, Nein, Enthaltungen und innerhalb der Untergruppe alphabetisch sortiert

## Beschreibung und Kontext

Das Feld **description** kann zusätzliche Informationen erfassen:

**Beispiele:**
- "Enthaltung wegen Interessenkonflikt (Verwaltungsrat Energieunternehmen)"
- "Abwesend wegen Krankheit"

## Zeitstempel

- **datetime_created**: Erste Publikation
- **datetime_modified**: Letzte Aktualisierung (z.B. bei Korrekturen der Publikation)

## Anwesenheit vs. Stimmabgabe

Wichtiger Unterschied:

- **Attendance** (andere Entität): Erfasst die generelle Anwesenheit bei einer Sitzung
- **IndividualVote**: Erfasst die spezifische Stimmabgabe bei einer Abstimmung

Eine Person kann bei einer Sitzung anwesend sein (Attendance), aber bei einzelnen Abstimmungen mit "absent" oder "did_not_vote" erfasst werden (z.B. wenn sie kurz den Raum verlässt).

## Namentliche vs. geheime Abstimmungen

IndividualVote-Entitäten werden nur bei namentlichen (offenen) Abstimmungen erfasst:

- **Namentliche Abstimmung**: Jede Stimme wird erfasst und ist öffentlich
- **Geheime Abstimmung**: Nur das Gesamtergebnis wird erfasst, keine IndividualVotes



## Class: IndividualVote 


_[en] An individual vote cast by a member during a voting procedure._

_[de] Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_voting | 0..1 <br/> [Voting](#Voting) | [en] The ID of the voting associated with the individual vote. [de] Die ID der Abstimmung, die mit der Einzelstimme verbunden ist.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | [en] Reference to the acting person (lightweight snapshot at time of linking). [de] Referenz auf die handelnde Person (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| seat_nr | 0..1 <br/> [String](#String) | [en] The seat number of the individual vote, if applicable. [de] Die Sitznummer der Einzelstimme, falls zutreffend.  |
| weight | 0..1 <br/> [Integer](#Integer) | [en] The number of votes held by the individual, if applicable (e.g., in cases where a person has multiple votes). [de] Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B. in Fällen, in denen eine Person mehrere Stimmen hat).  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](#IndividualVoteTypeEnum) | [en] Type of vote cast (yes, no, abstention, no vote, etc.). [de] Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc.).  |
| type_label | 0..1 <br/> [String](#String) | [en] Custom type label when standard type values don't apply. [de] Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [individual_votes](#individual_votes) | range | [IndividualVote](#IndividualVote) |














### Examples
#### Example: IndividualVote-voting_vote_zh_gr_2024_2023_361_abs1

```yaml
global_uri: ops:vote_zh_gr_2024_2023_361_abs1
parent_voting: ops:voting_zh_gr_2024_2023_361
actor_id:
  global_uri: https://www.gemeinderat-zuerich.ch/personen/4
  label: Abwesendes Mitglied
seat_nr: '103'
individual_vote_type: not_voted
datetime_created: '2024-02-28T00:00:00Z'

```
#### Example: IndividualVote-voting_vote_zh_budget_2026_person_102

```yaml
global_uri: ops:vote_zh_budget_2026_person_102
parent_voting: ops:voting_zh_budget_2026
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/25208
  label: Jean-Daniel Strub
seat_nr: '2'
individual_vote_type: 'no'
datetime_created: '2025-11-20T16:45:00Z'

```
#### Example: IndividualVote-voting_vote_sg_2025_001_person_789

```yaml
global_uri: ops:vote_sg_2025_001_person_789
parent_voting: ops:voting_sg_2025_001
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/27233
  label: Thomas Ammann
seat_nr: '3'
individual_vote_type: abstention
datetime_created: '2025-03-15T14:30:00Z'

```
#### Example: IndividualVote-voting_vote_zh_gr_2024_2023_361_b1

```yaml
global_uri: ops:vote_zh_gr_2024_2023_361_b1
parent_voting: ops:voting_zh_gr_2024_2023_361
actor_id:
  global_uri: https://www.gemeinderat-zuerich.ch/personen/2
  label: Mitglied Auswahl B
seat_nr: '47'
individual_vote_type: other
type_label: Auswahl B
datetime_created: '2024-02-28T00:00:00Z'

```
#### Example: IndividualVote-voting_vote_zh_gr_2024_2023_361_a1

```yaml
global_uri: ops:vote_zh_gr_2024_2023_361_a1
parent_voting: ops:voting_zh_gr_2024_2023_361
actor_id:
  global_uri: https://www.gemeinderat-zuerich.ch/personen/1
  label: Mitglied Auswahl A
seat_nr: '12'
individual_vote_type: other
type_label: Auswahl A
datetime_created: '2024-02-28T00:00:00Z'

```
#### Example: IndividualVote-voting_vote_zh_budget_2026_person_101

```yaml
global_uri: ops:vote_zh_budget_2026_person_101
parent_voting: ops:voting_zh_budget_2026
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/27237
  label: Thomas Wolf
seat_nr: '1'
individual_vote_type: 'yes'
datetime_created: '2025-11-20T16:45:00Z'

```
#### Example: IndividualVote-voting_vote_sg_2025_001_person_321

```yaml
global_uri: ops:vote_sg_2025_001_person_321
parent_voting: ops:voting_sg_2025_001
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/25177
  label: Ruedi Thomann
seat_nr: '4'
individual_vote_type: not_voted
datetime_created: '2025-03-15T14:30:00Z'

```
#### Example: IndividualVote-voting_vote_sg_2025_001_person_123

```yaml
global_uri: ops:vote_sg_2025_001_person_123
parent_voting: ops:voting_sg_2025_001
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/27235
  label: Paul Schlegel
seat_nr: '1'
individual_vote_type: 'yes'
datetime_created: '2025-03-15T14:30:00Z'

```
#### Example: IndividualVote-voting_vote_sg_2025_001_person_456

```yaml
global_uri: ops:vote_sg_2025_001_person_456
parent_voting: ops:voting_sg_2025_001
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/27234
  label: Andreas Eggenberger
seat_nr: '2'
individual_vote_type: 'no'
datetime_created: '2025-03-15T14:30:00Z'

```
#### Example: IndividualVote-voting_vote_zh_gr_2024_2023_361_c1

```yaml
global_uri: ops:vote_zh_gr_2024_2023_361_c1
parent_voting: ops:voting_zh_gr_2024_2023_361
actor_id:
  global_uri: https://www.gemeinderat-zuerich.ch/personen/3
  label: Mitglied Auswahl C
seat_nr: '88'
individual_vote_type: other
type_label: Auswahl C
datetime_created: '2024-02-28T00:00:00Z'

```






</div>

## Enum: IndividualVoteTypeEnum 




_[en] Type of individual vote cast by a member._

_[de] Art der Einzelstimme eines Mitglieds._

__



<div data-search-exclude markdown="1">

URI: [ops:IndividualVoteTypeEnum](https://ch.paf.link/schema/operations/IndividualVoteTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| yes |  [en] Vote in favor (yes) [de] Ja-Stimme  |
| | [ops:enum/individual_vote_type/yes](ops:enum/individual_vote_type/yes) |
| no |  [en] Vote against (no) [de] Nein-Stimme  |
| | [ops:enum/individual_vote_type/no](ops:enum/individual_vote_type/no) |
| abstention |  [en] Abstention [de] Enthaltung  |
| | [ops:enum/individual_vote_type/abstention](ops:enum/individual_vote_type/abstention) |
| not_voted |  [en] Not Voted [de] Nicht abgestimmt  |
| | [ops:enum/individual_vote_type/not_voted](ops:enum/individual_vote_type/not_voted) |
| tie_breaker |  [en] Tie-breaking vote, TODO english [de] Stichentscheid, meist durch Präsidium  |
| | [ops:enum/individual_vote_type/tie_breaker](ops:enum/individual_vote_type/tie_breaker) |
| other |  [en] Other vote type [de] Andere Stimmabgabe  |
| | [ops:enum/individual_vote_type/other](ops:enum/individual_vote_type/other) |







</div>

## Election (Wahl)

## Begriff und Bedeutung

Eine Election (Wahl) bezeichnet die Bestimmung einer oder mehrerer Personen für ein Amt oder eine Funktion durch ein parlamentarisches Organ. Im Gegensatz zu Abstimmungen (Votings), bei denen über Sachfragen entschieden wird, geht es bei Wahlen um Personenentscheidungen.

## Unterschied: Wahl vs. Abstimmung

| Kriterium | Election (Wahl) | Voting (Abstimmung) |
|-----------|-----------------|---------------------|
| Gegenstand | Personen | Sachfragen, Vorlagen |
| Ergebnis | Gewählte Person(en) | Angenommen/Abgelehnt |
| Verfahren | Oft geheim | Oft offen |
| Mehrheit | Meist absolut | Meist einfach |

## Arten von Wahlen

Der Standard unterscheidet verschiedene Wahltypen über das Feld **election_type**:

### open
Offene Wahl

**Charakteristik:**
- Stimmabgabe ist öffentlich sichtbar
- Jedes Mitglied gibt seine Stimme offen ab
- Nachvollziehbar, wer wen gewählt hat

**Anwendung:**
- Wenn Transparenz gewünscht ist
- Bei unumstrittenen Wahlen
- In kleineren Gremien

### secret
Geheime Wahl

**Charakteristik:**
- Stimmabgabe ist anonym
- Wahlzettel oder elektronisches Geheimwahlsystem
- Nicht nachvollziehbar, wer wen gewählt hat

**Anwendung:**
- Personenwahlen (Standard)
- Wenn freie, unbeeinflusste Entscheidung gewährleistet werden soll
- Gesetzlich oft vorgeschrieben

**Beispiele auf Bundesebene:**
- Wahl des Bundesrats
- Wahl der Bundesrichter
- Wahl der Kommissionspräsidien

**Beispiele auf Kantonsebene:**
- Wahl der Parlamentspräsidentin oder des Parlamentspräsidenten
- Wahl der Regierungspräsidentin oder des Regierungspräsidenten
- Wahl der Präsidentinnen und Präsidenten der obersten kantonalen Gerichte
- Wahl der Richterinnen und Richter
- Wahl er Staatsschreiberin oder des Staatsschreibers
- Wahl der Kommissionspräsidentinnen oder der Kommissionspräsidenten
- Wahl idien
- Wahl der Kommissions

### tacit
Stille Wahl

**Charakteristik:**
- Keine formale Abstimmung erforderlich
- Wahl erfolgt durch Akklamation oder Konsens
- Nur wenn keine Gegenstimmen erhoben werden

**Anwendung:**
- Bei Einstimmigkeit
- Unumstrittene Wahlen
- Wiederwahlen ohne Gegenkandidaten

**Beispiel:** Wiederwahl eines Kommissionspräsidenten ohne Gegenkandidatur

## Zuordnung zu Traktanden

Jede Wahl ist einem AgendaItem zugeordnet:

```
AgendaItem (Wahl des Bundesrats)
  └─ Election (Wahl für Departement XY)
      ├─ Kandidat A: 120 Stimmen
      ├─ Kandidat B: 75 Stimmen
      └─ Leere Stimmzettel: 5
```

## Beschreibung und Titel

- **title**: Titel der Wahl (z.B. "Wahl Kommissionspräsidium WAK")
- **description**: Ausführliche Beschreibung, Kontext, besondere Umstände

## Wahlergebnis

Das Feld **result** erfasst das Ergebnis:

- **elected**: Person(en) gewählt
- **not_elected**: Keine Person gewählt (z.B. bei absoluter Mehrheit nicht erreicht)
- **deferred**: Wahl verschoben
- **withdrawn**: Wahl zurückgezogen

## Gewählte Person(en)

Das Feld **elected_person_id** enthält die ID(s) der gewählten Person(en) gemäss eCH-0294 Actors.

Bei Mehrfachwahlen (z.B. Wahl mehrerer Kommissionsmitglieder gleichzeitig) können mehrere IDs erfasst werden.

## Stimmenverteilung

Bei offenen Wahlen oder nach Publikation der Ergebnisse:

- **total_votes**: Gesamtzahl abgegebener Stimmen
- **valid_votes**: Gültige Stimmen
- **invalid_votes**: Ungültige Stimmen
- **blank_votes**: Leere Stimmzettel

Zusätzlich Details pro Kandidat (über separate Entitäten oder als strukturierte Daten).

## Wahlverfahren

Das Feld **procedure** beschreibt das konkrete Verfahren:

- **written_ballot**: Schriftliche Wahl mit Stimmzetteln
- **electronic**: Elektronische Wahl
- **show_of_hands**: Handzeichen (bei offenen Wahlen)
- **acclamation**: Akklamation (bei stillen Wahlen)

## Mehrheitsverhältnisse

Das Feld **majority_type** definiert die erforderliche Mehrheit:

### absolute
Absolute Mehrheit (mehr als die Hälfte der Stimmenden)

**Anwendung:**
- Bundesratswahl
- Wahl von Kommissionspräsidien
- Standardfall bei Personenwahlen

**Beispiel:** Bei 200 abgegebenen Stimmen sind mindestens 101 Stimmen erforderlich

**Besonderheit:** Wenn im ersten Wahlgang niemand die absolute Mehrheit erreicht, folgt meist ein zweiter Wahlgang, in dem die einfache Mehrheit genügt.

### simple
Einfache Mehrheit (mehr Stimmen als andere Kandidaten)

**Anwendung:**
- Zweiter Wahlgang nach erfolglosem ersten Wahlgang
- Einige Kommissionswahlen

### qualified
Qualifizierte Mehrheit

**Anwendung:**
- Seltener bei Wahlen
- Spezielle Funktionen mit erhöhten Anforderungen

## Wahlgänge

Bei Wahlen mit absoluter Mehrheit im ersten Wahlgang:

```
1. Wahlgang (absolute Mehrheit erforderlich)
   └─ Kein Kandidat erreicht absolute Mehrheit

2. Wahlgang (einfache Mehrheit genügt)
   └─ Kandidat A gewählt
```

Jeder Wahlgang wird als separate Election-Entität erfasst, verbunden über das gemeinsame AgendaItem.

## Zeitstempel

- **datetime_created**: Zeitpunkt der Durchführung
- **datetime_modified**: Letzte Aktualisierung

## URL und Dokumentation

- **url**: Mehrsprachige URLs zu Wahlunterlagen:
  - Kandidatenprofile
  - Wahlresultate
  - Protokolle

## Besonderheiten verschiedener Wahlen

### Bundesratswahl
- Geheime Wahl
- Absolute Mehrheit erforderlich (im 1. Wahlgang)
- Durch die Vereinigte Bundesversammlung

### Bundesrichterwahl
- Geheime Wahl
- Proporzprinzip (Berücksichtigung von Parteien, Landesteilen, Geschlechtern)

### Kommissionspräsidien
- Wahl durch das jeweilige Parlament
- Oft weniger öffentlich

### Kantons- und Gemeindeebene
- Grosse Vielfalt an Wahlverfahren
- Teilweise Volkswahl statt parlamentarische Wahl
- Unterschiedliche Mehrheitserfordernisse

## Transparenz und Geheimhaltung

Spannungsfeld:
- **Wahlgeheimnis**: Schutz der individuellen Wahlentscheidung
- **Transparenz**: Öffentliches Interesse am Wahlergebnis

Bei geheimen Wahlen:
- Nur Gesamtergebnis wird publiziert
- Keine IndividualVote-Entitäten
- Schutz der Wahlfreiheit

Bei offenen Wahlen:
- Individuelle Stimmabgaben können erfasst werden
- Höhere Transparenz
- Potenzielle soziale Druckeffekte



## Class: Election 


_[en] An election procedure for selecting persons to positions._

_[de] Ein Wahlverfahren zur Wahl von Personen in Positionen._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| datetime_begin | 0..1 <br/> [Datetime](#Datetime) | [en] The date and time when the meeting or voting begins. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> [Datetime](#Datetime) | [en] The date and time when the meeting or voting ends. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](#ElectionTypeEnum) | Type of election procedure |
| type_label | 0..1 <br/> [String](#String) | [en] Custom type label when standard type values don't apply. [de] Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| title | 0..1 <br/> [String](#String) | None |
| landing_page | 0..1 <br/> [String](#String) | [en] URL providing further information. [de] URL mit weiteren Informationen.  |
| total_absent | 0..1 <br/> [Integer](#Integer) | [en] Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list. [de] Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total | 0..1 <br/> [Integer](#Integer) | [en] Total number of votes, excluding absent and president's vote. [de] Gesamtzahl der Stimmen, ohne abwesende und Präsidentenstimmen.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | [en] Type of majority required for the vote (absolute, two-thirds, etc.). [de] Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.).  |
| majority_count | 0..1 <br/> [Integer](#Integer) | [en] Number of votes required for the relevant majority threshold. [de] Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind.  |
| result_text | 0..1 <br/> [String](#String) | [en] Free text describing the outcome of the vote, e.g., "Accepted with 78 votes". [de] Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. "Mit 78 Stimmen angenommen".  |
| parent_meeting | 0..1 <br/> [String](#String) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| parent_agenda_item | 0..1 <br/> [String](#String) | [en] If needed, this slot builds a hierarchy of agenda items. [de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten auf.  |
| affair_id | 0..1 <br/> [String](#String) | [en] The connection to the affairs (business items) of the agenda item. [de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | [en] Reference to the acting body/organ (lightweight snapshot at time of linking). [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [elections](#elections) | range | [Election](#Election) |



















</div>

## Enum: ElectionTypeEnum 




_[en] Type of election procedure._

_[de] Art des Wahlverfahrens._

__



<div data-search-exclude markdown="1">

URI: [ops:ElectionTypeEnum](https://ch.paf.link/schema/operations/ElectionTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| secret |  [en] Secret election (Geheime Wahl) [de] Geheime Wahl  |
| | [ops:enum/election_type/secret](ops:enum/election_type/secret) |
| open |  [en] Open election (Offene Wahl) [de] Offene Wahl  |
| | [ops:enum/election_type/open](ops:enum/election_type/open) |
| silent |  [en] Silent election without opponent (Stille Wahl ohne Gegenkandidat) [de] Stille Wahl ohne Gegenkandidat  |
| | [ops:enum/election_type/silent](ops:enum/election_type/silent) |







</div>

ToDo: David


Debatte

* -> Video Aufzeichnung -> Worttransskript
*   -> Wortprotokol -> Text to Timestamp -> Text beinhaltet die Timestamps -> Textdokument (mit oder ohne definition vom Format (spantypen))
*   -> Aufbereitetes Proktoll -> AgendaItem to Timestamp

## Speech (Wortmeldung, Votum)

## Begriff und Bedeutung

Eine Speech (Wortmeldung, Votum) bezeichnet einen mündlichen Beitrag einer Person während einer parlamentarischen Sitzung. Sie ist das zentrale Instrument der politischen Debatte und Meinungsäusserung im Parlament.

## Arten von Speeches

Parlamentarische Wortmeldungen haben verschiedene Formen:

### Hauptvoten
- Ausführliche Stellungnahmen zu einem Geschäft
- Begründung von Anträgen
- Darlegung der Fraktionsmeinung

### Kurzinterventionen
- Kurze Wortmeldungen
- Zwischenfragen
- Richtigstellungen

### Fraktionserklärungen
- Offizielle Stellungnahme einer Fraktion
- Vorgetragen durch Fraktionssprecher/in

### Regierungsvoten
- Stellungnahmen von Regierungsmitgliedern
- Beantwortung von Fragen
- Verteidigung von Vorlagen

## Struktur und Zuordnung

Eine Speech ist immer einem bestimmten Kontext zugeordnet:

```
Meeting (Sitzung)
  └─ AgendaItem (Traktandum)
      └─ Speech (Wortmeldung Person A)
          ├─ TextSegment (Transkription)
          ├─ Media (Audio-Aufzeichnung)
          └─ Media (Video-Aufzeichnung)
```

### Zuordnungsfelder

- **meeting_id**: Die Sitzung, in der die Wortmeldung erfolgte
- **agenda_item_id**: Das Traktandum, zu dem gesprochen wurde
- **person_id**: Die sprechende Person (gemäss eCH-0294 Actors)

## Identifikation der Sprechenden

- **person_id**: Eindeutige Identifikation der Person
- **person_name**: Name für schnellen Zugriff
- **role**: Rolle der Person (z.B. "Fraktionspräsident/in", "Berichterstatter/in", "Bundesrat/Bundesrätin")

## Zeitliche Erfassung

- **start_time**: Beginn der Wortmeldung
- **end_time**: Ende der Wortmeldung
- **duration**: Dauer in Sekunden (berechnet oder erfasst)

Diese Zeitangaben ermöglichen:
- Genaue Referenzierung in Audio-/Video-Aufzeichnungen
- Analyse der Redezeit pro Person/Fraktion
- Kontrolle der Einhaltung von Zeitlimiten

## Sprache der Wortmeldung

Das Feld **language** erfasst die Sprache, in der gesprochen wurde:

- **de**: Deutsch
- **fr**: Französisch
- **it**: Italienisch
- **rm**: Rätoromanisch
- **en**: Englisch

## Textdokumente

Das Feld **text_segments** verweist auf TextSegment-Entitäten, die den gesprochenen Text enthalten.

### Verschiedene Textversionen

#### Rohtranskript
- Wörtliche Niederschrift
- Unbearbeitet, mit Füllwörtern
- Direkt nach der Sitzung verfügbar

#### Bearbeitetes Transkript
- Redaktionell überarbeitet
- Grammatikalisch korrigiert
- Offizielle Protokollversion

#### Übersetzungen
- In andere Landessprachen
- Für internationale Publikationen

### TextSegment-Struktur

Jedes TextSegment kann enthalten:
- **text**: Der eigentliche Text
- **language**: Sprache des Texts
- **version**: Art der Version (raw, edited, translated)
- **format**: Format (plain, markdown, HTML)

## Multimedia-Aufzeichnungen

Das Feld **media** verweist auf Media-Entitäten mit Audio- und Video-Aufzeichnungen.

### Audio-Aufzeichnungen
- Originalton der Wortmeldung
- Format: MP3, WAV, etc.
- Technische Metadaten (Qualität, Bitrate)

### Video-Aufzeichnungen
- Visuelle Aufzeichnung (bei Plenarsitzungen)
- Format: MP4, WebM, etc.
- Verschiedene Auflösungen

### Livestreaming
- Echtzeit-Übertragung
- URL zum Stream
- Archivierung nach der Sitzung

## Titel und Beschreibung

- **title**: Kurzer Titel (z.B. "Votum zur Energiepolitik")
- **description**: Zusammenfassung oder Kontext der Wortmeldung

## Typ der Wortmeldung

Das Feld **speech_type** kann verschiedene Arten unterscheiden:

- **statement**: Stellungnahme
- **question**: Frage
- **response**: Antwort (z.B. Regierung auf Frage)
- **procedural**: Verfahrensantrag
- **declaration**: Erklärung



## Class: Speech 


_[en] A speech or statement made during a meeting (also called Votum or speaker segment)._

_[de] Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| language | 0..1 <br/> [String](#String) | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |
| start | 0..1 <br/> [String](#String) | Start indicator or position |
| datetime_begin | 0..1 <br/> [Datetime](#Datetime) | [en] The date and time when the meeting or voting begins. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> [Datetime](#Datetime) | [en] The date and time when the meeting or voting ends. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| actor_fullname | 0..1 <br/> [String](#String) | Full name of the actor/person |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | [en] Reference to the acting person (lightweight snapshot at time of linking). [de] Referenz auf die handelnde Person (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| role | 0..1 <br/> [String](#String) | Role of the person (e.g., commission speaker) |
| text | 1 <br/> [String](#String) | None |
| text_format | 0..1 <br/> [String](#String) | [en] Format of text (text, html, html_with_timestamps) [de] Format des Textes (text, html, html_with_timestamps)  |
| text_type | 0..1 <br/> [String](#String) | [en] Type of text (raw draft, edited version) [de] Typ des Textes (Rohfassung, bearbeitete Fassung)  |
| landing_page | 0..1 <br/> [String](#String) | [en] URL providing further information. [de] URL mit weiteren Informationen.  |
| media_url | 0..1 <br/> [String](#String) | URL to media file (audio/video) |
| media_type | 0..1 <br/> [String](#String) | Type of media (audio, video, document) |
| media_format | 0..1 <br/> [String](#String) | MIME type of the media file |
| documents | * <br/> [Work](#Work) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [speeches](#speeches) | range | [Speech](#Speech) |
| [Protocol](#Protocol) | [speeches](#speeches) | range | [Speech](#Speech) |














### Examples
#### Example: Speech-meeting_sr_winter25_Sitzung6_366631

```yaml
global_uri: ops:366631
language: fr
datetime_begin: '2025-12-19T09:20:00+01:00'
datetime_end: '2025-12-19T09:25:00+01:00'
actor_fullname: Pascal Broulis
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/18682
  wikidata_uri: https://www.wikidata.org/wiki/Q116407
  label: Pascal Broulis
role: speaker
text: Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec
  attention les différents commentaires qui ont été effectués sur mon postulat. Cela
  reste un postulat, ce n'est pas une motion. D'abord, je ne partage pas l'avis selon
  lequel ce postulat n'apporterait pas une valeur ajoutée. En effet, un "benchmark",
  à savoir un modèle chiffré de performance, permettrait de mieux comprendre les raisons
  des retards que notre pays rencontre en comparaison avec les principaux pays européens.
text_format: html
text_type: final
landing_page: https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631
media_url: https://par-pcache.simplex.tv/content?externalid=366631
media_type: video
media_format: video/mp4

```






</div>


# Texte und Medien

Parlamentarische Debatten werden nicht nur als strukturierte Daten erfasst, sondern auch als Texte und Multimedia-Aufzeichnungen. Diese Entitäten ermöglichen die Verwaltung von Transkripten, Audio-/Video-Aufzeichnungen und weiteren Medienformaten sowie die technische Infrastruktur für Datenaustausch und Mehrsprachigkeit.

## TextSegment

### Zweck
Erfasst Textabschnitte mit Versionierung und Sprachvarianten. Wird primär für Transkriptionen von Wortmeldungen verwendet, kann aber auch für andere Textdokumente eingesetzt werden.

### Struktur
- **text**: Der eigentliche Textinhalt
- **language**: Sprachcode (ISO 639-1)
- **format**: Format des Texts (plain, markdown, html)
- **version_type**: Art der Version
  - **raw**: Unbearbeitetes Rohtranskript
  - **edited**: Redaktionell bearbeitete Version
  - **translated**: Übersetzung in andere Sprache
  - **summary**: Zusammenfassung

### Designentscheid
**Warum separate Entität?**
- Ermöglicht mehrere Versionen desselben Texts (Rohfassung, bearbeitet, übersetzt)
- Versionskontrolle und Nachvollziehbarkeit von Änderungen
- Flexibilität bei Formaten (Plain, Markdown, HTML für unterschiedliche Ausgabekanäle)

### Anwendung
Hauptsächlich verknüpft mit Speech-Entitäten:
```
Speech
  ├─ TextSegment (Rohtranskript, de)
  ├─ TextSegment (Bearbeitetes Protokoll, de)
  ├─ TextSegment (Übersetzung, fr)
  └─ TextSegment (Zusammenfassung, de)
```

## Media

### Zweck
Referenziert Mediendateien (Audio, Video, Dokumente), die zu parlamentarischen Aktivitäten gehören.

### Struktur
- **media_type**: Art der Mediendatei
  - **audio**: Audio-Aufzeichnung
  - **video**: Video-Aufzeichnung
  - **document**: Dokumente (PDF, etc.)
  - **image**: Bilder
- **url**: URL zur Mediendatei
- **mime_type**: MIME-Type (audio/mp3, video/mp4, application/pdf, etc.)
- **title**: Titel der Mediendatei
- **description**: Beschreibung
- **language**: Sprache (bei sprachbasierten Medien)
- **duration**: Dauer (bei Audio/Video, in Sekunden)
- **file_size**: Dateigrösse in Bytes
- **quality**: Qualitätsangabe (z.B. "720p", "high", "low")

### Designentscheid
**Warum generische Media-Entität?**
- Einheitliche Struktur für alle Medientypen
- Erweiterbar für neue Formate
- Technische Metadaten zentral erfasst
- Mehrere Qualitätsstufen derselben Aufzeichnung möglich

### Anwendung
Kann an verschiedene Entitäten gehängt werden:
```
Speech
  ├─ Media (Audio-Aufzeichnung, MP3, 256kbps)
  ├─ Media (Audio-Aufzeichnung, MP3, 128kbps)
  ├─ Media (Video-Aufzeichnung, MP4, 1080p)
  └─ Media (Video-Aufzeichnung, MP4, 480p)

AgendaItem
  └─ Media (PDF der Vorlage)

Meeting
  └─ Media (Livestream-URL)



## Class: TextSegment 


_[en] A text segment such as cross-references or subtitles in meeting protocols._

_[de] Ein Textsegment wie Querverweise oder Zwischentitel in Sitzungsprotokollen._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| text | 1 <br/> [String](#String) | None |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](#Protocol) | [text_segments](#text_segments) | range | [TextSegment](#TextSegment) |



















</div>





## Class: Media 


_[en] Media files or documents (including protocols in PDF/HTML/WORD or links to audio/video)._

_[de] Mediendateien oder Dokumente (einschließlich Protokolle in PDF/HTML/WORD oder Links zu Audio/Video)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| title | 0..1 <br/> [String](#String) | None |
| media_type | 0..1 <br/> [String](#String) | Type of media (audio, video, document) |
| url | * <br/> [MultilingualString](#MultilingualString) | None |
| version | 0..1 <br/> [String](#String) | Version number or identifier |
| parent_type | 0..1 <br/> [String](#String) | Type of parent object (meeting, agenda, speech, affair) |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |






















</div>



## Class: MultilingualString 


_[en] A string that can contain text in multiple languages._

_[de] Ein String, der Text in mehreren Sprachen enthalten kann._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| text | 1 <br/> [String](#String) | None |
| language | 1 <br/> [String](#String) | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Legislature](#Legislature) | [name](#name) | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | [name](#name) | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | [url](#url) | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | [name](#name) | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | [url](#url) | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | [agenda_item_title](#agenda_item_title) | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | [agenda_item_description](#agenda_item_description) | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | [url](#url) | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | [agenda_item_title](#agenda_item_title) | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | [agenda_item_description](#agenda_item_description) | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | [url](#url) | range | [MultilingualString](#MultilingualString) |
| [Voting](#Voting) | [voting_title](#voting_title) | range | [MultilingualString](#MultilingualString) |
| [IndividualAttendance](#IndividualAttendance) | [reason](#reason) | range | [MultilingualString](#MultilingualString) |
| [Media](#Media) | [url](#url) | range | [MultilingualString](#MultilingualString) |



















</div>



## Class: Container 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| legislatures | * <br/> [Legislature](#Legislature) | None |
| sessions | * <br/> [Session](#Session) | None |
| meetings | * <br/> [Meeting](#Meeting) | None |
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | None |
| protocols | * <br/> [Protocol](#Protocol) | Collection of protocol records |
| votings | * <br/> [Voting](#Voting) | Collection of voting records |
| elections | * <br/> [Election](#Election) | Collection of election records |
| individual_votes | * <br/> [IndividualVote](#IndividualVote) | Collection of individual vote records |
| attendances | * <br/> [Attendance](#Attendance) | Collection of attendance records |
| individual_attendances | * <br/> [IndividualAttendance](#IndividualAttendance) | Collection of individual attendance records |
| speeches | * <br/> [Speech](#Speech) | Collection of speech records |
| resolutions | * <br/> [Resolution](#Resolution) | Collection of resolutionrecords |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |

















### Examples
#### Example: Container-meeting_sr_winter25_Sitzung6

```yaml
global_uri: ops:data_meeting_sr_winter25_Sitzung6

meetings:
  - global_uri: "parl:sr_winter25_sitzung_6"
    body_key: "CHE"
    meeting_type: "session"
    name:
      - text: "Sechste Sitzung"
        language: "de"
      - text: "Sixième séance"
        language: "fr"
    url:
      - text: "https://www.parlament.ch/de/ratsbetrieb/suche-Amtliches-bulletin"
        language: "de"
    actor_id:
      global_uri: "https://api.openparldata.ch/v1/bodies/42"
      label: "Ständerat"
      abbreviation:
        - value: "SR"
          language: de
    actor_name: "Ständerat"
    datetime_begin_planned: "2025-12-19T08:15:00+01:00"
    datetime_created: "2026-01-12T00:00:00+01:00"
    datetime_modified: "2026-01-12T00:00:00+01:00"

agenda_items:
  - global_uri: ops:69905
    parent_meeting: "parl:sr_winter25_sitzung_6"
    agenda_item_type: "item"
    datetime_begin_planned: "2025-12-19T09:15:00+01:00"
    datetime_begin_actual: "2025-12-19T09:20:00+01:00"
    agenda_item_number: "6"
    agenda_item_position: 4
    agenda_item_title:
      - text: "Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich durchführen, um die Verzögerungen zu verstehen"
        language: "de"
    affair_id: "affairs:24.4471"
    landing_page: "https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3"
    agenda_item_category: "agenda_item"
    datetime_created: "2026-01-12T00:00:00+01:00"
    datetime_modified: "2026-01-12T00:00:00+01:00"

speeches:
  - global_uri: ops:366631
    language: "fr"
    datetime_begin: "2025-12-19T09:20:00+01:00"
    datetime_end: "2025-12-19T09:25:00+01:00"
    actor_fullname: "Pascal Broulis"
    actor_id:
      global_uri: "https://api.openparldata.ch/v1/persons/18682"
      wikidata_uri: "https://www.wikidata.org/wiki/Q116407"
      label: "Pascal Broulis"
    role: "speaker"
    text: >-
      Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec attention
      les différents commentaires qui ont été effectués sur mon postulat. Cela reste un postulat,
      ce n'est pas une motion. D'abord, je ne partage pas l'avis selon lequel ce postulat
      n'apporterait pas une valeur ajoutée. En effet, un "benchmark", à savoir un modèle chiffré
      de performance, permettrait de mieux comprendre les raisons des retards que notre pays
      rencontre en comparaison avec les principaux pays européens.
    text_format: "html"
    text_type: "final"
    landing_page: "https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631"
    media_url: "https://par-pcache.simplex.tv/content?externalid=366631"
    media_type: "video"
    media_format: "video/mp4"

```
#### Example: Container-voting

```yaml
global_uri: ops:voting_examples_2025

votings:

- global_uri: ops:voting_sg_2025_001
  voting_title:
    - text: "Schlussabstimmung Energiegesetz"
      language: "de"
  voting_type: "final_vote"
  datetime_begin: "2025-03-15T14:30:00Z"
  datetime_end: "2025-03-15T14:35:00Z"
  total_count_yes: 78
  total_count_no: 42
  total_count_abstention: 5
  total_absent: 3
  total: 128
  majority_type: "absolute"
  majority_count: 65
  result_text: "Mit 78 zu 42 Stimmen bei 5 Enthaltungen angenommen"
  parent_agenda_item: ops:agenda_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/265"
    label: "Kantonsrat St. Gallen"
    abbreviation:
      - value: "KR"
        language: de
  datetime_created: "2025-03-15T14:30:00Z"
  datetime_modified: "2025-03-15T14:35:00Z"

- global_uri: ops:voting_be_2025_042
  voting_title:
    - text: "Änderungsantrag Art. 5 Abs. 2"
      language: "de"
    - text: "Proposition de modification art. 5 al. 2"
      language: "fr"
  voting_type: "preliminary_vote"
  datetime_begin: "2025-06-05T10:15:00Z"
  datetime_end: "2025-06-05T10:17:00Z"
  total_count_yes: 45
  total_count_no: 87
  total_count_abstention: 8
  total_absent: 10
  total: 150
  majority_type: "absolute"
  majority_count: 76
  result_text: "Mit 45 zu 87 Stimmen bei 8 Enthaltungen abgelehnt"
  parent_agenda_item: ops:agenda_item_be_2025_042
  parent_meeting: ops:meeting_be_2025_06_05
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/253"
    label: "Grosser Rat Bern"
    abbreviation:
      - value: "GR"
        language: de
  datetime_created: "2025-06-05T10:15:00Z"
  datetime_modified: "2025-06-05T10:15:00Z"

- global_uri: ops:voting_zh_budget_2026
  voting_title:
    - text: "Budgetbeschluss 2026"
      language: "de"
  voting_type: "final_vote"
  datetime_begin: "2025-11-20T16:45:00Z"
  datetime_end: "2025-11-20T16:50:00Z"
  total_count_yes: 105
  total_count_no: 70
  total_count_abstention: 5
  total_absent: 0
  total: 180
  majority_type: "absolute"
  majority_count: 91
  result_text: "Mit 105 zu 70 Stimmen bei 5 Enthaltungen angenommen"
  parent_agenda_item: ops:agenda_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/275"
    label: "Kantonsrat Zürich"
    abbreviation:
      - value: "KR"
        language: de
  datetime_created: "2025-11-20T16:45:00Z"
  datetime_modified: "2025-11-20T16:50:00Z"

# Realbeispiel Gemeinderat der Stadt Zürich (28.02.2024, 86. Sitzung):
# "Gleichgerichtete Anträge" mit mehreren Auswahloptionen (Zürich: mehrere Knöpfe).
# Die Optionen sind nicht Ja/Nein/Enthaltung, sondern Auswahl A–D und werden
# deshalb über total_other (Liste von TotalOther {count, label}) abgebildet.
# Quelle: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
- global_uri: ops:voting_zh_gr_2024_2023_361
  voting_title:
    - text: "Liegenschaften Stadt Zürich, Wohnhaus Magnusstrasse 27, Gesamtinstandsetzung, Grundrissanpassung, Netto-Zusatzkredit (Geschäft 2023/361)"
      language: "de"
  voting_type: "other"
  type_label: "Gleichgerichtete Anträge (Mehrfachauswahl)"
  datetime_begin: "2024-02-28T00:00:00Z"
  datetime_end: "2024-02-28T00:00:00Z"
  landing_page: "https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89"
  # Bei reinen Auswahlabstimmungen bleiben Ja/Nein/Enthaltung leer; jede Option
  # erhält einen eigenen TotalOther-Eintrag mit Stimmenzahl und Bezeichnung.
  total_other:
    - count: 75
      label: "Auswahl A (siegreich)"
    - count: 25
      label: "Auswahl B"
    - count: 12
      label: "Auswahl C"
    - count: 0
      label: "Auswahl D"
  total_absent: 13
  total: 112
  majority_type: "other"
  result_text: "Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25, Auswahl C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern)."
  parent_agenda_item: ops:agenda_item_zh_gr_2024_2023_361
  parent_meeting: ops:meeting_zh_gr_2024_02_28
  affair_id: "2023/361"
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/"
    label: "Gemeinderat der Stadt Zürich"
    abbreviation:
      - value: "GR"
        language: de
  datetime_created: "2024-02-28T00:00:00Z"
  datetime_modified: "2024-02-28T00:00:00Z"

individual_votes:

# Einzelstimmen zum Zürcher Mehrfachoptionen-Beispiel: Da die Auswahloptionen
# nicht Ja/Nein/Enthaltung sind, wird individual_vote_type "other" mit type_label
# je gewählter Option verwendet; abwesende Mitglieder erhalten "not_voted".
- global_uri: ops:vote_zh_gr_2024_2023_361_a1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/1"
    label: "Mitglied Auswahl A"
  seat_nr: "12"
  individual_vote_type: "other"
  type_label: "Auswahl A"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_b1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/2"
    label: "Mitglied Auswahl B"
  seat_nr: "47"
  individual_vote_type: "other"
  type_label: "Auswahl B"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_c1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/3"
    label: "Mitglied Auswahl C"
  seat_nr: "88"
  individual_vote_type: "other"
  type_label: "Auswahl C"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_zh_gr_2024_2023_361_abs1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: "https://www.gemeinderat-zuerich.ch/personen/4"
    label: "Abwesendes Mitglied"
  seat_nr: "103"
  individual_vote_type: "not_voted"
  datetime_created: "2024-02-28T00:00:00Z"

- global_uri: ops:vote_sg_2025_001_person_123
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27235"
    label: "Paul Schlegel"
  seat_nr: "1"
  individual_vote_type: "yes"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_456
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27234"
    label: "Andreas Eggenberger"
  seat_nr: "2"
  individual_vote_type: "no"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_789
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27233"
    label: "Thomas Ammann"
  seat_nr: "3"
  individual_vote_type: "abstention"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_sg_2025_001_person_321
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/25177"
    label: "Ruedi Thomann"
  seat_nr: "4"
  individual_vote_type: "not_voted"
  datetime_created: "2025-03-15T14:30:00Z"

- global_uri: ops:vote_zh_budget_2026_person_101
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/27237"
    label: "Thomas Wolf"
  seat_nr: "1"
  individual_vote_type: "yes"
  datetime_created: "2025-11-20T16:45:00Z"

- global_uri: ops:vote_zh_budget_2026_person_102
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/persons/25208"
    label: "Jean-Daniel Strub"
  seat_nr: "2"
  individual_vote_type: "no"
  datetime_created: "2025-11-20T16:45:00Z"

```
#### Example: Container-meeting_item

```yaml
global_uri: ops:agenda_items_1
agenda_items:
  - global_uri: ops:cea750a5bd7b420fa4da1c914f801384
    parent_meeting: ops:meeting_bern_2022_03_17
    agenda_item_type: item
    datetime_begin_planned: '2022-03-17T17:00:00Z'
    agenda_item_position: 29
    agenda_item_number: '8'
    agenda_item_title:
      - text: >-
          Interpellation Fraktion GB/JA! (Katharina Gallizzi, GB): Welche
          Konsequenzen haben die Klimaziele für das Gasnetz in Bern?
        language: de
    affair_id: affairs:2020.SR.000007
    url:
      - text: >-
          https://stadtrat.bern.ch/de/sitzungen/detail.php?gid=000d6cf5f0bc4d89a5171e0123cfbff5#cea750a5bd7b420fa4da1c914f801384
        language: de
    datetime_created: '2025-01-17T21:25:52Z'
    datetime_modified: '2025-01-17T21:25:52Z'
  - global_uri: ops:2023_10_03-52
    parent_meeting: ops:meeting_lausanne_2023_10_03
    agenda_item_type: item
    datetime_begin_planned: '2023-10-03T00:00:00Z'
    agenda_item_position: 52
    agenda_item_number: '52'
    agenda_item_title:
      - text: >-
          Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité
          commerciale » (FIM)
        language: fr
    state_id: postponed
    agenda_item_category: RAPPORTS
    affair_id: affairs:POS22/029
    url:
      - text: >-
          https://www.lausanne.ch/apps/agir/affaire/81/b7157ea2a4994086b65cf176768c6381.htm
        language: fr
    datetime_created: '2025-02-08T12:33:10Z'
    datetime_modified: '2025-02-08T12:33:10Z'
  - global_uri: ops:2025_05_20-23
    parent_meeting: ops:meeting_lausanne_2025_05_20
    agenda_item_type: item
    datetime_begin_planned: '2025-05-20T00:00:00Z'
    agenda_item_position: 23
    agenda_item_number: '23'
    agenda_item_title:
      - text: >-
          Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : «
          Interpellation urgente de Kulmiye Yusuf et crts – Solidarité sans
          frontières, Lausanne en faveur du respect du droit international et de
          la protection des populations civiles à Gaza »
        language: fr
    state_id: not_treated
    agenda_item_category: ANNONCES ET INTERPELLATIONS
    affair_id: affairs:INT25/027
    url:
      - text: >-
          https://www.lausanne.ch/apps/agir/affaire/6c/049b6c612fe2428f9be66ea39522ac6c.htm
        language: fr
    datetime_created: '2025-06-07T23:50:18Z'
    datetime_modified: '2025-06-07T23:50:18Z'
  - global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
    parent_meeting: ops:meeting_vaud_2008_04_30
    agenda_item_type: item
    datetime_begin_planned: '2008-04-30T00:00:00Z'
    agenda_item_position: 7
    agenda_item_number: '7'
    agenda_item_title:
      - text: >-
          Révision partielle de sept ordonnances fédérales relatives aux
          produits chimiques
        language: fr
    agenda_item_description:
      - text: >
          Le Conseil d'Etat approuve le projet de révision partielle de sept
          ordonnances fédérales relatives aux produits chimiques. Il salue la
          volonté des autorités fédérales d'introduire dans la législation
          fédérale les modifications nécessaires découlant des nouveaux
          règlements européens, afin d'éliminer des entraves au commerce et
          d'augmenter la sécurité d'évaluation des produits chimiques.
        language: fr
    url:
      - text: >-
          https://www.vd.ch/actualites/decisions-du-conseil-detat/seance-du-conseil-detat/seance/265632#7b3545e4-57dc-3901-aaa8-4020da6ab0c6
        language: fr
    datetime_created: '2024-12-06T10:50:04Z'
    datetime_modified: '2024-12-06T10:50:04Z'
  - global_uri: ops:06fb582b753c416d8fdb05fa13873545
    parent_meeting: ops:meeting_2011_11_23
    agenda_item_type: item
    datetime_begin_planned: '2011-11-23T00:00:00Z'
    agenda_item_position: 2
    agenda_item_title:
      - text: >-
          Interpellation Peter Mark betr. elektronische Datenerfassung durch
          Mitarbeiter im Werkhof – Versuchsphase
        language: de
    datetime_created: '2025-03-21T23:15:19Z'
    datetime_modified: '2025-03-21T23:15:19Z'
  - global_uri: ops:16155798_3
    parent_meeting: ops:meeting_schaffhausen_2025_03_31
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 2
    agenda_item_number: '2'
    agenda_item_title:
      - text: >-
          Motion Nr. 2023/9 von Rainer Schmidig vom 18. Dezember 2023 betreffend
          zeitgemässe Abzüge in den Art. 35 und 37 des Gesetzes über die
          direkten Steuern
        language: de
    agenda_item_category: Traktanden
    affair_id: affairs:MOT_2023_9
    datetime_created: '2025-05-02T11:23:49Z'
    datetime_modified: '2025-05-02T11:23:49Z'
  - global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
    parent_meeting: ops:meeting_bern_rr_2025_04_02
    agenda_item_type: item
    datetime_begin_planned: '2025-04-02T00:00:00Z'
    agenda_item_title:
      - text: >-
          Petition «Gleichberechtigung für Tagesfamilien: Gleich hohe
          Betreuungsgutscheine für alle Anbieter im Kanton Bern».
          Regierungsrätliches Antwortschreiben
        language: de
    affair_id: affairs:2025.STA.622
    url:
      - text: >-
          https://www.rr.be.ch/de/start/beschluesse/suche/geschaeftsdetail.html?guid=21c50b86d21b4b4baeb1a76738ff82a3
        language: de
    datetime_created: '2025-04-25T11:11:40Z'
    datetime_modified: '2025-04-25T11:11:40Z'
  - global_uri: ops:49_253
    parent_meeting: ops:meeting_2025_03_31
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 2
    agenda_item_number: '2'
    agenda_item_title:
      - text: Programmvereinbarungen 2024
        language: de
    datetime_created: '2025-03-29T01:07:14Z'
    datetime_modified: '2025-03-29T01:07:14Z'
  - global_uri: ops:16155798_4
    parent_meeting: ops:meeting_schaffhausen_2025_03_31_b
    agenda_item_type: item
    datetime_begin_planned: '2025-03-31T00:00:00Z'
    agenda_item_position: 3
    agenda_item_number: '3'
    agenda_item_title:
      - text: >-
          Volksmotion Nr. 2024/1 von Sandro Mamedow und Livia Schraff
          (Erstunterzeichnende) sowie weitere 150 Mitunterzeichnende vom 22.
          März 2024 mit dem Titel: «Für eine Stimme der Studierenden im
          Hochschulrat der Pädagogischen Hochschule Schaffhausen (PHSH)»
        language: de
    agenda_item_category: Traktanden
    affair_id: affairs:MOT_2024_1
    datetime_created: '2025-05-02T11:23:49Z'
    datetime_modified: '2025-05-02T11:23:49Z'
  - global_uri: ops:87b69a72919445a493a061d9b0daeba3
    parent_meeting: ops:meeting_be_2025_06_02
    agenda_item_type: item
    datetime_begin_planned: '2025-06-02T00:00:00Z'
    agenda_item_title:
      - text: Differenzierte Anpassung des Gehalts von Lehrpersonen ohne Lehrdiplom
        language: de
    affair_id: affairs:2025.GRPARL.81
    datetime_created: '2025-04-25T11:10:35Z'
    datetime_modified: '2025-04-25T11:10:35Z'
  - global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
    parent_meeting: ops:meeting_luzern_2025_01_28
    agenda_item_type: item
    datetime_begin_planned: '2025-01-28T00:00:00Z'
    agenda_item_position: 29
    agenda_item_number: '29'
    agenda_item_title:
      - text: >-
          Postulat Widmer Reichlin Gisela und Mit. über Massnahmen zur Erfüllung
          des Sonderschulkonkordats und zur gezielten Behebung des
          Fachkräftemangels im Bereich schulische Heilpädagogik / Bildungs- und
          Kulturdepartement
        language: de
    agenda_item_category: voting
    url:
      - text: >-
          https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
        language: de
    affair_id: affairs:2024P_125
    datetime_created: '2025-01-29T06:59:41Z'
    datetime_modified: '2025-01-29T06:59:41Z'
  - global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
    parent_meeting: ops:meeting_luzern_2025_01_28_b
    agenda_item_type: item
    datetime_begin_planned: '2025-01-28T00:00:00Z'
    agenda_item_position: 14
    agenda_item_number: '14'
    agenda_item_title:
      - text: >-
          Postulat Stadelmann Karin Andrea und Mit. über die Überprüfung und
          Anpassung der Kriterien zum früheren Eintritt von Kindern in die
          Basisstufe (den freiwilligen Kindergarten) / Bildungs- und
          Kulturdepartement
        language: de
    agenda_item_category: voting
    url:
      - text: >-
          https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=fa732e0e-7e5f-4d45-994a-fc74720c0781
        language: de
    affair_id: affairs:2023P_102
    datetime_created: '2025-01-29T06:59:41Z'
    datetime_modified: '2025-01-29T06:59:41Z'

```
#### Example: Container-session

```yaml
global_uri: ops:sessions_example_2025
sessions:

- global_uri: ops:session_5207
  body_key: "CHE"
  name:
    - text: "Frühjahrssession 2025"
      language: "de"
    - text: "Session de printemps 2025"
      language: "fr"
    - text: "Sessione primaverile 2025"
      language: "it"
  url:
    - text: "https://www.parlament.ch/de/ratsbetrieb/sessionen/fruehjahr-2025"
      language: "de"
    - text: "https://www.parlament.ch/fr/ratsbetrieb/sessionen/fruehjahr-2025"
      language: "fr"
    - text: "https://www.parlament.ch/it/ratsbetrieb/sessionen/fruehjahr-2025"
      language: "it"
  date_begin_planned: "2025-03-03"
  date_end_planned: "2025-03-21"
  parent_legislature: ops:legislature_51
  datetime_modified: "2025-04-24T00:19:37Z"
  datetime_created: "2025-03-20T14:27:09Z"

- global_uri: ops:session_be_summer_2025
  body_key: "BE"
  name:
    - text: "Sommersession 2025"
      language: "de"
    - text: "Session d'été 2025"
      language: "fr"
  url:
    - text: "https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
      language: "de"
    - text: "https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
      language: "fr"
  date_begin_planned: "2025-06-02"
  date_end_planned: "2025-06-12"
  datetime_modified: "2025-05-19T01:06:44Z"
  datetime_created: "2025-04-25T11:10:24Z"

- global_uri: ops:session_gl_landrat_2025_02_26
  body_key: "GL"
  name:
    - text: "Sitzung des Landrates vom 26.02.2025"
      language: "de"
  url:
    - text: "https://www.gl.ch/parlament/landrat/landratsprotokolle-ab-30-juni-2010.html/239"
      language: "de"
  date_begin_planned: "2025-02-26"
  date_end_planned: "2025-02-26"
  datetime_modified: "2025-04-25T13:40:34Z"
  datetime_created: "2025-04-23T22:58:39Z"

- global_uri: ops:session_gl_landsgemeinde_2025_05_04
  body_key: "GL"
  name:
    - text: "Landsgemeinde vom 04. Mai 2025"
      language: "de"
  url:
    - text: "https://www.landsgemeinde.gl.ch/landsgemeinde/2025-05-04"
      language: "de"
  date_begin_planned: "2025-05-04"
  date_end_planned: "2025-05-04"
  datetime_modified: "2025-04-25T13:40:34Z"
  datetime_created: "2025-04-23T22:58:39Z"

```
#### Example: Container-meeting

```yaml
global_uri: ops:meetings_1
meetings:
  - body_key: "BE"
    global_uri: ops:340dcf932fb044dd8f8c5c943267fbcc
    meeting_type: "session"
    name:
      - text: "Regierungssitzung vom 31. März 2021"
        language: "de"
      - text: "Séance du gouvernement du 31 mars 2021"
        language: "fr"
    url:
      - text: "https://www.rr.be.ch/de/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc"
        language: "de"
      - text: "https://www.rr.be.ch/fr/start/beschluesse/beschluesse-unterlagen-nach-sitzungen/sitzungs-detail?guid=340dcf932fb044dd8f8c5c943267fbcc"
        language: "fr"
    actor_id:
      global_uri: "actors:rr_be"
      label: "Regierungsrat Bern"
      abbreviation:
        - value: "RR"
          language: de
    actor_name: "Regierungsrat Bern"
    date_begin_planned: "2021-03-31"
    date_end_planned: "2021-03-31"
    datetime_created: "2024-10-28T01:22:26Z"
    datetime_modified: "2024-11-27T20:40:57Z"

  - body_key: "BE"
    global_uri: ops:e7c5d453-848a-430a-b024-1dd2f6873aa6
    meeting_type: "session"
    name:
      - text: "Donnerstag (Nachmittag)"
        language: "de"
    url:
      - text: "https://www.gr.be.ch/de/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
        language: "de"
      - text: "https://www.gr.be.ch/fr/start/sessionen/sessionen-auswahl/sessionsdetail.html?guid=66ccf0a9f4d24d318ff3b99e646644e8"
        language: "fr"
    actor_id:
      global_uri: "https://api.openparldata.ch/v1/bodies/253"
      label: "Grosser Rat Bern"
      abbreviation:
        - value: "GR"
          language: de
    actor_name: "Grosser Rat Bern"
    date_begin_planned: "2025-06-05"
    date_end_planned: "2025-06-05"
    datetime_created: "2025-04-25T11:10:25Z"
    datetime_modified: "2025-05-19T01:06:45Z"

```
#### Example: Container-meeting_complete

```yaml
global_uri: ops:meeting_examples_2025

meetings:

- global_uri: ops:meeting_sg_2025_03_15
  body_key: "SG"
  meeting_type: "session"
  name:
    - text: "Kantonsratssitzung vom 15. März 2025"
      language: "de"
  url:
    - text: "https://www.ratsinfo.sg.ch/sessions/2025-03-15"
      language: "de"
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/265"
    label: "Kantonsrat St. Gallen"
    abbreviation:
      - value: "KR"
        language: de
  actor_name: "Kantonsrat St. Gallen"
  datetime_begin_planned: "2025-03-15T08:00:00Z"
  datetime_end_planned: "2025-03-15T18:00:00Z"
  datetime_begin_actual: "2025-03-15T08:15:00Z"
  datetime_end_actual: "2025-03-15T17:30:00Z"
  state: "planned"
  location: "Kantonsratssaal, Regierungsgebäude St. Gallen"
  parent_legislature: ops:legislature_sg_2024_2028
  datetime_created: "2025-02-01T10:00:00Z"
  datetime_modified: "2025-03-15T17:30:00Z"

- global_uri: ops:meeting_be_committee_wak_2025_05_12
  body_key: "BE"
  meeting_type: "committee"
  name:
    - text: "Sitzung Kommission für Wirtschaft und Abgaben"
      language: "de"
    - text: "Séance Commission de l'économie et des redevances"
      language: "fr"
  url:
    - text: "https://www.gr.be.ch/kommissionen/wak/2025-05-12"
      language: "de"
  actor_id:
    global_uri: "actors:committee_wak_be"
    label: "Kommission für Wirtschaft und Abgaben (WAK)"
    abbreviation:
      - value: "WAK"
        language: de
  actor_name: "Kommission für Wirtschaft und Abgaben (WAK)"
  datetime_begin_planned: "2025-05-12T14:00:00Z"
  datetime_end_planned: "2025-05-12T17:00:00Z"
  datetime_begin_actual: "2025-05-12T14:10:00Z"
  datetime_end_actual: "2025-05-12T16:45:00Z"
  state: "planned"
  location: "Kommissionszimmer 301, Rathaus Bern"
  parent_legislature: ops:legislature_be_2022_2026
  datetime_created: "2025-04-15T09:00:00Z"
  datetime_modified: "2025-05-12T16:45:00Z"

- global_uri: ops:meeting_gl_landsgemeinde_2025
  body_key: "GL"
  meeting_type: "sitting"
  name:
    - text: "Landsgemeinde 2025"
      language: "de"
  url:
    - text: "https://www.landsgemeinde.gl.ch/2025"
      language: "de"
  actor_id:
    global_uri: "https://api.openparldata.ch/v1/bodies/258"
    label: "Landsgemeinde Glarus"
    abbreviation:
      - value: "LG"
        language: de
  actor_name: "Landsgemeinde Glarus"
  datetime_begin_planned: "2025-05-04T09:30:00Z"
  datetime_end_planned: "2025-05-04T14:00:00Z"
  datetime_begin_actual: "2025-05-04T09:30:00Z"
  datetime_end_actual: "2025-05-04T13:45:00Z"
  state: "planned"
  location: "Zaunplatz, Glarus"
  parent_legislature: ops:legislature_gl_2024_2028
  datetime_created: "2025-01-10T12:00:00Z"
  datetime_modified: "2025-05-04T13:45:00Z"

agenda_items:

- global_uri: ops:agenda_item_sg_2025_015
  parent_meeting: ops:meeting_sg_2025_03_15
  agenda_item_type: "item"
  agenda_item_number: "15"
  agenda_item_position: 15
  agenda_item_title:
    - text: "Energiegesetz - Schlussabstimmung"
      language: "de"
  agenda_item_description:
    - text: "Schlussabstimmung über das revidierte Energiegesetz des Kantons St. Gallen"
      language: "de"
  agenda_item_category: "Gesetzgebung"
  state_id: "completed"
  datetime_begin_planned: "2025-03-15T14:00:00Z"
  datetime_begin_actual: "2025-03-15T14:30:00Z"
  affair_id: "affairs:sg_2024_123_energiegesetz"
  datetime_created: "2025-02-01T10:00:00Z"
  datetime_modified: "2025-03-15T14:35:00Z"

- global_uri: ops:agenda_item_be_2025_042
  parent_meeting: ops:meeting_be_committee_wak_2025_05_12
  agenda_item_type: "item"
  agenda_item_number: "4.2"
  agenda_item_position: 42
  agenda_item_title:
    - text: "Steuergesetz - Detailberatung Art. 5"
      language: "de"
    - text: "Loi fiscale - Délibération détaillée art. 5"
      language: "fr"
  agenda_item_description:
    - text: "Beratung von Änderungsanträgen zu Artikel 5 des Steuergesetzes"
      language: "de"
    - text: "Délibération sur les propositions de modification de l'article 5 de la loi fiscale"
      language: "fr"
  agenda_item_category: "Gesetzgebung"
  state_id: "completed"
  datetime_begin_planned: "2025-05-12T15:00:00Z"
  datetime_begin_actual: "2025-05-12T15:15:00Z"
  affair_id: "affairs:be_2024_089_steuergesetz"
  datetime_created: "2025-04-15T09:00:00Z"
  datetime_modified: "2025-05-12T15:20:00Z"

- global_uri: ops:agenda_item_zh_budget_2026
  parent_meeting: ops:meeting_zh_2025_11_20
  agenda_item_type: "item"
  agenda_item_number: "8"
  agenda_item_position: 8
  agenda_item_title:
    - text: "Budget 2026"
      language: "de"
  agenda_item_description:
    - text: "Beratung und Beschlussfassung über das Kantonsbudget für das Jahr 2026"
      language: "de"
  agenda_item_category: "Budget und Finanzen"
  state_id: "completed"
  datetime_begin_planned: "2025-11-20T16:00:00Z"
  datetime_begin_actual: "2025-11-20T16:45:00Z"
  affair_id: "affairs:zh_2025_budget_2026"
  datetime_created: "2025-10-01T08:00:00Z"
  datetime_modified: "2025-11-20T16:50:00Z"

```






</div>


