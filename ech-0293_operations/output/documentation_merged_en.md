---
title: "eCH-0293 Public Council Operations"
lang: en
toc: false
---

|**Name**|**Public Council Operations**|
|---|---|
|**eCH number**|eCH-0293|
|**Category**|Standard|
|**Maturity level**|Defined|
|**Version**|0.1.0|
|**Status**|In progress|
|**Adopted on**||
|**Issue date**||
|**Replaces version**||
|**Prerequisites**||
|**Annexes**|-|
|**Languages**|German (original) - English (data model)|
|**Authors**|Political Affairs specialist group: Nicole Aeby, David Imseng, Jonas Schärer, Lena Mina Friedrich, Manuel Weingartner, Orhan Saeedi, Michel Moret, Laurens Abu-Talib|
|**Publisher / Distribution**|eCH Association, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)|

\newpage

# Abstract

The standard eCH-0293 defines a common data model for recording and publishing information on public council operations in Switzerland. It covers the temporal organisation of parliamentary work (legislatures, sessions), the structuring of meetings and agenda items, votings and elections, individual votes, attendance lists as well as speeches and resolutions.

This standard is aimed at parliamentary services, software providers of parliamentary management systems, data users for analyses and visualisations, and open data platforms.

eCH-0293 is part of a family of standards for political data and works closely together with eCH-0294 (Political Actors), eCH-0295 (Parliamentary Affairs), eCH-0296 (Laws and Legal Texts) and eCH-0297 (Public Consultations).

\newpage

# Table of Contents

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \o "1-2" \h \z \u </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Right-click &gt; "Update field" to generate the table of contents.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```

\newpage

# Note

This document uses gender-inclusive language when referring to persons. It follows the [guidelines](https://www.bk.admin.ch/bk/de/home/dokumentation/sprachen/hilfsmittel-textredaktion/leitfaden-zum-geschlechtergerechten-formulieren.html) (German) of the Federal Chancellery. Depending on the situation, paired forms (citizens), gender-abstract forms (the insured person), gender-neutral forms or paraphrases without personal reference are used. The generic masculine is not permitted. Full forms are used in continuous text; short forms may be used in abbreviated passages, notably in tables. Gender asterisks and similar spellings are not used.

\newpage

# Introduction

## Context: public council operations

At federal, cantonal and communal level, councils and assemblies convene, deliberate on political affairs, take decisions and scrutinise the executive.

## The "Political Affairs" standard family

Political activity in Switzerland takes place at federal, cantonal and communal level – in parliaments and communal assemblies, in executives and administrations, in consultations and hearings, as well as through the direct-democratic participation of eligible voters. To this end, the "Political Affairs" specialist group of the eCH Association is developing a family of coordinated standards that structure this data across all federal levels. The standards use common data elements (eCH-0292) and reference one another via unique identifiers.

The family comprises:

- **eCH-0292 – Common Data Elements (Meta):** Defines the cross-cutting data elements and meta-processes on which the other standards build. eCH-0293 adopts from it, among other things, the identification and date elements as well as the FRBR structure for linked documents.
- **eCH-0293 – Public Council Operations (Operations) – this standard:** Describes public council operations – legislatures and sessions, meetings and agenda items, protocols and decisions, votings and elections, attendance as well as speeches.
- **eCH-0294 – Political Actors (Actors):** Defines persons, groups and bodies in the political context, as well as their memberships and interest links. eCH-0293 references these actors via `actor_id` – for instance which parliament convened and which person voted.
- **eCH-0295 – Parliamentary Affairs (Affairs):** Describes the life cycle of political affairs. Agenda items in eCH-0293 point to the corresponding affair via `affair_id`.
- **eCH-0296 – Enactments and Legal Texts (Laws):** Records the results of the parliamentary process – the adopted laws and enactments.
- **eCH-0297 – Public Consultations (Consultations):** Structures consultation procedures, which are often the starting point for parliamentary affairs.

The aim of this standard family is to create a commonly usable structure for political data and to provide organisations that publish information on political affairs with a robust data model.

## Distinction from the "Political Rights" specialist group

Alongside the "Political Affairs" specialist group, the eCH Association also maintains the "Political Rights" specialist group. Both concern the political domain, but cover different areas:

- **Political Affairs** (this standard family) describes the parliamentary and governmental process of forming opinions and reaching decisions: the actors (eCH-0294), council operations (eCH-0293), parliamentary affairs (eCH-0295), the enactments arising from them (eCH-0296), as well as the upstream consultations (eCH-0297).
- **Political Rights** deals with the exercise of political rights by eligible voters: voting and electoral registers, the conduct of popular votes and elections, electronic voting (eVoting), voting cards, as well as voting and election results (among others eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

This distinction matters particularly for eCH-0293, because the standard models votings and elections. What is decisive is not who is entitled to vote, but **where the decision is taken** – in the convened assembly or at the ballot box:

- **In the assembly** – this standard: votings and elections carried out by a convened body in the course of a sitting with an agenda. This includes roll-call votings and final votes in parliament as well as the election of authority members, judges or committee presidencies by the council. It is recorded via `Voting`, `IndividualVote` and `Election`.
- **At the ballot box** – "Political Rights" specialist group: popular votes and popular elections together with voting registers, conduct, voting cards and results. These are not modelled here.

Deliberately on the side of this standard are **Landsgemeinden and communal assemblies** (`meeting_type: sitting`). They are indeed assemblies of the eligible voters themselves, but they decide as a convened body with an agenda, speeches and resolutions – and are therefore represented like a council sitting.

A second point of contact concerns elected persons: candidates and elected persons appear in the election results of the "Political Rights" specialist group. As soon as persons hold a mandate, they are recorded in eCH-0294 as political actors with their roles and memberships – and eCH-0293 references them from there via `actor_id`.

\newpage

<!-- ToDo: Christian -->

# Temporal organisation of council operations

Parliamentary operations are organised in time on three levels: legislatures form the long-term frame, sessions structure the work within a legislature, and meetings are the concrete sittings in which affairs are deliberated. This hierarchy allows both long-term planning and flexible adaptation to current requirements.

## Legislature

### Term and meaning

A legislature denotes the period for which a parliament is elected and acts in its current composition. It is the highest temporal unit of parliamentary operations and marks the frame for a parliament's legislative work.

In Switzerland the duration of legislatures varies by federal level:

- **Federal level**: 4 years (National Council and Council of States)
- **Cantons**: mostly 4 years, in some cantons also 5 years
- **Communes**: varying, frequently 4 years

### Structure and hierarchy

The legislature stands hierarchically above the sessions and meetings:

```
Legislature
  └─ Sessions (e.g. spring session, autumn session)
      └─ Meetings (individual sittings)
          └─ Agenda Items
```

### Parliamentary context

Every legislature is assigned to a specific parliamentary body, identified by:

- **actor_id**: reference to the parliament as a political actor (e.g. National Council, cantonal parliament) according to eCH-0294 Actors
- **administrative_id**: administrative ID of the legislative body (e.g. commune, canton, country)

### Temporal placement

A legislature is characterised via the mixin `IsEventWithDuration`. The most important date fields are:

- **date_begin_planned** / **date_begin_actual**: planned respectively actual start of the legislature (usually after elections)
- **date_end_planned** / **date_end_actual**: planned respectively actual end of the legislature (before the next elections)

Where needed, analogous `datetime_*` variants with a time of day are available.

Example at federal level: the 51st legislature of the Swiss Parliament lasted from 5 December 2019 to 4 December 2023.

### Identification

The mixin `HasIdentification` provides `local_id`, `global_uri` and `wikidata_uri`. The `global_uri` is mandatory and serves as the unique identifier.

### Linked documents

The slot **documents** allows relevant documents (e.g. member directories of the legislature, affairs directories) to be linked as FRBR Works.



## Class: Legislature []{#Legislature}


_Term of office of a parliament as a legislative assembly. Usually lasts four years._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| administrative_id | 0..1 <br/> String | Administrative ID of the legislative body, such as a municipality, canton, or country.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Multilingual full designation.  |
| description | 0..1 <br/> String | Descriptive text of the element.  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | legislatures | range | [Legislature](#Legislature) |



















</div>

## Session

### Term and meaning

A session denotes a continuous sitting period of a parliament during which several meetings take place. It is the middle temporal unit between the legislature and the individual meetings.

### Distinction: session vs. meeting

This distinction is important for understanding the standard:

- **Session**: a sitting period that typically extends over several days or weeks
- **Meeting**: an individual sitting within a session

#### Example at federal level
```
Legislature (51st legislature)
  └─ Session (spring session 2024)
      ├─ Meeting (National Council sitting 4 March 2024)
      ├─ Meeting (Council of States sitting 4 March 2024)
      ├─ Meeting (National Council sitting 5 March 2024)
      └─ ...
```

### Assignment to bodies

A session relates to the political body that organises the sessions as a series of sittings. Examples:

- **Parliament**: sessions of a cantonal parliament or of the Federal Assembly
- **Committees**: sitting periods of parliamentary committees
- **Joint bodies**: e.g. sessions of the United Federal Assembly

Via **body_key** the body (e.g. "NR" for the National Council, "SR" for the Council of States) can be recorded as a key. Via **parent_legislature** the session is assigned to the corresponding legislature.

### Identification and numbering

Sessions are usually numbered. The following slots are available — they are compatible with the corresponding modelling of Meeting:

- **number**: sequential number (e.g. within the legislature or the year)
- **sequential_number**: sequential number as a string (roman numerals also possible)
- **position**: integer position
- **abbreviation**: short designation (e.g. "FS24" for the 2024 spring session)
- **name**: multilingual full designation

The mixin `HasIdentification` additionally provides `local_id`, `global_uri` and `wikidata_uri`.

### Temporal attributes

Sessions use the mixin `IsEventWithDuration` and therefore offer the same date fields as legislatures and meetings:

- **date_begin_planned** / **datetime_begin_planned**: planned start of the session
- **date_begin_actual** / **datetime_begin_actual**: actual start
- **date_end_planned** / **datetime_end_planned**: planned end of the session
- **date_end_actual** / **datetime_end_actual**: actual end

### Links

- **meetings**: list of the meetings within the session
- **documents**: linked FRBR Works (e.g. session programme, session preview)
- **url**: landing page of the session

### Flexibility in the standard

The standard is deliberately flexible in order to reflect different forms of organisation. Federal units without formal sessions can use this entity optionally or reference meetings directly.



## Class: Session []{#Session}


_A parliamentary session that groups multiple meetings and spans a specific time period._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| body_key | 0..1 <br/> String | Key identifying the political body or jurisdiction (e.g., BE for Bern, CHE for Switzerland).  |
| name | * <br/> [MultilingualString](#MultilingualString) | Multilingual full designation.  |
| number | 0..1 <br/> String | Sequential number, e.g. within the legislature, the session or the year.  |
| sequential_number | 0..1 <br/> Integer | Sequential number of the meeting, used for ordering.  |
| position | 0..1 <br/> String | Integer position within the superordinate sequence.  |
| meeting_abbreviation | 0..1 <br/> String | Short designation of the session or meeting (e.g. "FS24" for the 2024 spring session).  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing page or further web address, multilingual.  |
| parent_legislature | 0..1 <br/> String | The legislative body in which the meeting is based.  |
| meetings | * <br/> [Meeting](#Meeting) | Collection of meeting records.  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | sessions | range | [Session](#Session) |














### Examples
#### Example Session: Federal session with a trilingual designation

```yaml
sessions:
- global_uri: ops:session_5207
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
#### Example Session: Landsgemeinde as a sitting period

```yaml
sessions:
- global_uri: ops:session_gl_landsgemeinde_2025_05_04
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
#### Example Session: Cantonal session with a bilingual designation

```yaml
sessions:
- global_uri: ops:session_be_summer_2025
  body_key: BE
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
#### Example Session: One-day sitting period of a cantonal parliament

```yaml
sessions:
- global_uri: ops:session_gl_landrat_2025_02_26
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

## Meeting (individual sitting)

### Term and meaning

A meeting denotes an individual sitting of a parliamentary body. This is the concrete event at which the members of a parliament, a committee or another body assemble in order to deliberate affairs and take decisions.

### Types of meetings

The standard distinguishes different meeting types via the field **meeting_type** (enum `MeetingTypeEnum`):

#### session
Plenary sittings of the whole parliament or of one chamber

**Examples:**
- National Council sitting during the autumn session
- Sitting of a cantonal parliament
- Sitting of the United Federal Assembly

#### committee
Sittings of parliamentary committees

**Examples:**
- Sitting of the Committee for Economic Affairs and Taxation (WAK/CER)
- Control Committee (GPK/CdG)
- Foreign Affairs Committee (APK/CPE)

#### sitting
Special forms of assembly

**Examples:**
- Landsgemeinden (in the cantons of Glarus and Appenzell Innerrhoden)
- Citizens' commune assemblies
- Communal assemblies

#### various
Other forms of meeting that do not fall into the categories above

### Hierarchy and structure

A meeting is part of a session (where used) and contains several agenda items:

```
Session (spring session 2024)
  └─ Meeting (National Council sitting, 4 March 2024, 08:00)
      ├─ AgendaItem (item 1: welcome)
      ├─ AgendaItem (item 2: legislative deliberation)
      └─ AgendaItem (item 3: votings)
```

### Planned timing vs. reality

Via the mixin `IsEventWithDuration` the meeting distinguishes between planned and actual points in time:

#### Planned dates
- **date_begin_planned** / **datetime_begin_planned**: planned start
- **date_end_planned** / **datetime_end_planned**: planned end

#### Actual dates
- **date_begin_actual** / **datetime_begin_actual**: actual start
- **date_end_actual** / **datetime_end_actual**: actual end

This distinction is important because:
- sittings can be delayed
- agenda items can be brought forward or postponed
- sittings can end earlier than planned

**Use case:** a sitting planned for 14:00 only starts at 14:25 due to delays and ends at 17:30 instead of 18:00.

### Meeting state

The field **state** (enum `StateEnum`) records the current state of a meeting:

- **planned**: the sitting is planned and will take place as scheduled
- **canceled**: the sitting has been cancelled
- **postponed**: the sitting has been postponed

Via **state_name** a divergent, free-text state description can be added.

This state is important for:
- up-to-date information for members of parliament and the public
- historical traceability of planning changes
- automatic notifications in case of changes

### Identification and numbering

Meetings are identified by:

- **local_id** / **global_uri** / **wikidata_uri** (via the mixin `HasIdentification`)
- **number**: sequential number (e.g. "5" for the 5th sitting of a session)
- **sequential_number**: sequential number as a string (roman numerals also possible)
- **position**: integer position within the session
- **abbreviation**: short designation (e.g. "NR-24-05")
- **name**: multilingual full designation

### Place of the sitting

The field **location** records the place of the sitting:

- Physical place: "Federal Palace, National Council chamber"
- Virtual sittings: "Video conference via [platform]"
- Hybrid formats: "Federal Palace and video conference"

### Assignment to bodies

The responsible body is referenced via **actor_id** (according to eCH-0294 Actors). Via **actor_name** the name of the body can additionally be recorded for quick access, via **body_key** a short key (e.g. "NR", "SR"). Via **administrative_id** the administrative level can be indicated; **group_name** and **group_id** complement groupings where needed.

- Plenary sittings: reference to the whole parliament
- Committee sittings: reference to the specific committee
- Joint sittings: reference to the joint body

### Hierarchical links

- **parent_meeting**: if a meeting is part of a superordinate meeting
- **parent_legislature**: the legislature within which the meeting takes place

### Relations to other entities

A meeting connects various elements of parliamentary operations:

- **Agenda Items**: the items dealt with
- **Votings**: votings during the sitting
- **Elections**: elections during the sitting
- **Speeches**: speeches and statements
- **Attendance**: attendance lists (via `Attendance.parent_meeting`)
- **documents**: linked FRBR Works (minutes, meeting documents, daily journal, etc.)



## Class: Meeting []{#Meeting}


_A general meeting class used for Sessions, Comittee Meetings, individual session Sittings and other various Meetings._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| body_key | 0..1 <br/> String | Key identifying the political body or jurisdiction (e.g., BE for Bern, CHE for Switzerland).  |
| meeting_type | 0..1 <br/> [MeetingTypeEnum](#MeetingTypeEnum) | Type of the meeting, e.g. session, committee, sitting, various.  |
| administrative_id | 0..1 <br/> String | Administrative ID of the legislative body, such as a municipality, canton, or country.  |
| name | * <br/> [MultilingualString](#MultilingualString) | Multilingual full designation.  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing page or further web address, multilingual.  |
| group_name | 0..1 <br/> String | Name of the group or body.  |
| group_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the group or body (lightweight snapshot at time of linking).  |
| number | 0..1 <br/> String | Sequential number, e.g. within the legislature, the session or the year.  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| sequential_number | 0..1 <br/> Integer | Sequential number of the meeting, used for ordering.  |
| position | 0..1 <br/> String | Integer position within the superordinate sequence.  |
| meeting_abbreviation | 0..1 <br/> String | Short designation of the session or meeting (e.g. "FS24" for the 2024 spring session).  |
| actor_name | 0..1 <br/> String | Name of the political body (e.g., Nationalrat).  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| state | 0..1 <br/> [StateEnum](#StateEnum) | Current state of the meeting (planned, canceled, postponed).  |
| state_name | 0..1 <br/> String | Custom state description for the meeting.  |
| description | 0..1 <br/> String | Descriptive text of the element.  |
| location | 0..1 <br/> String | Place where the meeting is held (physical room, video conference or hybrid format).  |
| parent_meeting | 0..1 <br/> String | The linked meeting ID that groups the current meeting.  |
| parent_legislature | 0..1 <br/> String | The legislative body in which the meeting is based.  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| protocol_ref | 0..1 <br/> [Protocol](#Protocol) | The protocol (minutes) of this meeting, recorded after the meeting.  |
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | meetings | range | [Meeting](#Meeting) |
| [Session](#Session) | meetings | range | [Meeting](#Meeting) |














### Examples
#### Example Meeting: Council of States sitting with protocol and speeches

```yaml
meetings:
- global_uri: parl:sr_winter25_sitzung_6
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
#### Example Meeting: Cantonal parliament sitting with agenda items and votings

```yaml
meetings:
- global_uri: ops:meeting_sg_2025_03_15
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
#### Example Meeting: Half-day sitting within a session

```yaml
meetings:
- body_key: BE
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
#### Example Meeting: Committee sitting with an attendance list

```yaml
meetings:
- global_uri: ops:meeting_be_committee_wak_2025_05_12
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
#### Example Meeting: Government sitting with a bilingual designation

```yaml
meetings:
- body_key: BE
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
#### Example Meeting: Landsgemeinde as meeting type sitting

```yaml
meetings:
- global_uri: ops:meeting_gl_landsgemeinde_2025
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

## Enum: MeetingTypeEnum []{#MeetingTypeEnum}




_Type of the meeting._




<div data-search-exclude markdown="1">

URI: [ops:MeetingTypeEnum](https://ch.paf.link/schema/operations/MeetingTypeEnum)

### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| session |  Plenary sitting of the whole parliament or of one chamber.  |
| | [ops:enum/meeting_type/session](ops:enum/meeting_type/session) |
| committee |  Meeting of a parliamentary committee.  |
| | [ops:enum/meeting_type/committee](ops:enum/meeting_type/committee) |
| sitting |  Special forms of assembly (e.g. Landsgemeinde, communal assembly).  |
| | [ops:enum/meeting_type/sitting](ops:enum/meeting_type/sitting) |
| various |  Other forms of meeting not covered by the categories above.  |
| | [ops:enum/meeting_type/various](ops:enum/meeting_type/various) |







</div>

## Enum: StateEnum []{#StateEnum}




_State of the meeting._




<div data-search-exclude markdown="1">

URI: [ops:StateEnum](https://ch.paf.link/schema/operations/StateEnum)

### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| planned |  The meeting is planned and will take place as scheduled.  |
| | [ops:enum/state/planned](ops:enum/state/planned) |
| canceled |  The meeting has been cancelled.  |
| | [ops:enum/state/canceled](ops:enum/state/canceled) |
| postponed |  The meeting has been postponed.  |
| | [ops:enum/state/postponed](ops:enum/state/postponed) |







</div>

# Attendance and speeches

Besides the formal decisions, the standard also documents participation in sittings and the debates held. Attendance lists record who took part in a sitting, while speeches capture the parliamentary debate with text and media recordings.

## Attendance

## Term and meaning

Attendance records which members of a parliamentary body were present, absent or excused at a sitting. It serves to document participation and is a prerequisite for the quorum.

## Two-level structure

The standard distinguishes two levels of attendance recording:

### 1. Attendance (aggregated level)
Summary of attendance for a meeting:
- Total number of persons present
- Total number of persons absent (excused / unexcused)
- Quorum

### 2. IndividualAttendance (individual level)
Detailed recording for each individual person:
- Who was present?
- Who was absent?
- Was the absence excused?

```
Meeting (National Council sitting 4 March 2024)
  └─ Attendance (aggregated attendance)
      ├─ IndividualAttendance (person A: present)
      ├─ IndividualAttendance (person B: excused)
      ├─ IndividualAttendance (person C: absent)
      └─ ...
```

## Attendance (aggregated level)

### Assignment to meeting and body

- **parent_meeting**: reference to the specific sitting to which the attendance list belongs
- **actor_id**: reference to the body (parliament, committee) according to eCH-0294 Actors
- **datetime_begin**: point in time of the attendance recording

### Aggregated figures

- **total_count**: total number of all members of the body (reference value for quorum calculations, e.g. 200 for the National Council, 46 for the Council of States)
- **total_present**: number of members present
- **total_excused**: number of excused members
- **total_absent**: number of unexcused absent members

**Example:**
- Total: 200
- Present: 185
- Excused: 12
- Absent: 3

### Quorum

The quorum results from the ratio of `total_present` to `total_count` and the respective quorum rules of the body. It is therefore not stored as a separate field but calculated from the data where needed.

## IndividualAttendance (individual level)

### Link

- **parent_attendance**: reference to the superordinate `Attendance` aggregate (which in turn hangs on the meeting). The individual record is thereby cleanly assigned to the meeting.
- **actor_id**: reference to the person according to eCH-0294 Actors

### Attendance type

The field **attendance_type** (enum `AttendanceTypeEnum`) records the type of attendance:

- **present**: present in person
- **remote**: present via remote access (e.g. video conference)
- **substitute**: substitution — another person participated as a stand-in

> The modelling of substitution (e.g. who substituted for whom, with which voting right) is being elaborated further in [issue #24](https://github.com/swiss/political-affairs-ech-group/issues/24).
>
> A second status axis `present` / `excused` / `absent` ("whether present") in parallel to the existing axis "how present" is under discussion as an extension.

### Reason

The field **reason** (multilingual) can record the reason for absence or lateness as free text.

## Difference: Attendance vs. IndividualVote

Important delimitation:

| Aspect | Attendance | IndividualVote |
|--------|------------|----------------|
| Records | Presence at the sitting | Vote cast in a voting |
| Point in time | Start of / during the sitting | Point in time of the voting |
| Granularity | Per meeting | Per voting |

**Example:** a person can be present at the sitting (Attendance: present) but be recorded as absent for a specific voting (IndividualVote: absent) because they briefly left the room at that moment.

## Purposes of use

The attendance entities enable:

1. **Documentation**: traceable recording of participation
2. **Quorum check**: ensuring the capacity to take decisions
3. **Transparency**: public information about attendance
4. **Accountability**: monitoring the fulfilment of duties
5. **Statistics**: evaluation of attendance rates
6. **Administration**: calculation of compensation and expenses



## Class: Attendance []{#Attendance}


_Aggregated attendance record for a meeting (number of members present, absent, excused)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | The linked meeting ID that groups the current meeting.  |
| datetime_begin | 0..1 <br/> Datetime | The date and time when the meeting or voting begins.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| total_count | 0..1 <br/> Integer | Total number of members of the body (reference value for quorum calculations).  |
| total_present | 0..1 <br/> Integer | Total number of members present.  |
| total_absent | 0..1 <br/> Integer | Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list.  |
| total_excused | 0..1 <br/> Integer | Total number of excused absences.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | attendances | range | [Attendance](#Attendance) |
| [IndividualAttendance](#IndividualAttendance) | parent_attendance | range | [Attendance](#Attendance) |



















</div>



## Class: IndividualAttendance []{#IndividualAttendance}


_Individual attendance record for a specific person at a meeting (linked via the parent Attendance aggregate)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_attendance | 0..1 <br/> [Attendance](#Attendance) | The Attendance aggregate this individual attendance record belongs to.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Reference to the acting person (lightweight snapshot at time of linking).  |
| attendance_type | 0..1 <br/> [AttendanceTypeEnum](#AttendanceTypeEnum) | Type of individual attendance.  |
| reason | * <br/> [MultilingualString](#MultilingualString) | Reason for absence or lateness (free-text, multilingual).  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | individual_attendances | range | [IndividualAttendance](#IndividualAttendance) |



















</div>

## Enum: AttendanceTypeEnum []{#AttendanceTypeEnum}




_Type of individual attendance._




<div data-search-exclude markdown="1">

URI: [ops:AttendanceTypeEnum](https://ch.paf.link/schema/operations/AttendanceTypeEnum)

### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| remote |  Remote participation  |
| | [ops:enum/attendance_type/remote](ops:enum/attendance_type/remote) |
| substitute |  Substitute (Stellvertretung)  |
| | [ops:enum/attendance_type/substitute](ops:enum/attendance_type/substitute) |
| present |  Present in person  |
| | [ops:enum/attendance_type/present](ops:enum/attendance_type/present) |







</div>

\newpage

<!-- ToDo: Michel -->

# Agenda, protocol and decisions

The agenda of a sitting is structured by agenda items. The agenda items count as the planning of a sitting and are no longer changed in the data once the sitting has started. The same data elements are then used to record the protocol and the decisions it contains.

If the agenda changes during a sitting, these changes are recorded in the protocol, and the agenda of the next sitting is adjusted accordingly.

## AgendaItem

### Purpose of the entity

AgendaItem structures the agenda of a sitting and connects the temporal organisation (Meeting) with the substantive affairs (Affairs from eCH-0295). It is the central entity for representing the course of a sitting.

### Hierarchy and structure

Agenda items can be organised hierarchically in order to represent the structure of complex agendas:

```
Meeting (sitting of 4 March 2024)
  ├─ AgendaItem 1: announcements and welcome
  ├─ AgendaItem 2: legislative deliberations
  │   ├─ AgendaItem 2.1: energy act (detailed deliberation)
  │   ├─ AgendaItem 2.2: energy act (final vote)
  │   └─ AgendaItem 2.3: health act (entry debate)
  └─ AgendaItem 3: miscellaneous
```

The hierarchy is represented via the field **parent_agenda_item**, which references the superordinate agenda item.

### Identification and numbering

- **id**: unique identifier
- **number**: agenda item number on the agenda (e.g. "2.1", "3")
- **position**: sort order (for the presentation)
- **title**: title of the agenda item

### Types of agenda items

The field **agenda_item_type** distinguishes different kinds:

- **item**: a regular agenda item with deliberation and, where applicable, a voting
- **item_group**: a group of agenda items (e.g. "legislative deliberations")
- **note**: informative entries without a voting (e.g. "announcements")

### Relation to parliamentary affairs

The field **affairs** references the corresponding parliamentary affairs according to eCH-0295. An agenda item can relate to several affairs:

- **Single affair**: an agenda item deals with a specific bill
- **Several affairs**: an agenda item combines related affairs
- **No affair**: administrative agenda items (e.g. "approval of the protocol")

**Example:** the agenda item "Energy act — final vote" references the affair "23.XXX Energy Act" in eCH-0295.

### Temporal planning

- **date_time**: planned point in time of the treatment
- **date_time_actual**: actual point in time of the treatment

This distinction is important because:
- the agenda is fixed in advance
- the actual course can deviate from it
- agenda items can be brought forward, postponed or adjourned

### Status and result

#### Status
The field **status** shows the processing state:
- "pending": not yet dealt with
- "in_progress": currently under deliberation
- "completed": treatment finished
- "postponed": adjourned to a later sitting
- "withdrawn": withdrawn

#### Result
The field **result** records the result of the treatment:
- "accepted": accepted
- "rejected": rejected
- "referred": referred back (e.g. to a committee)
- "noted": noted
- "no_decision": no decision taken

### Categorisation

The field **category** allows grouping according to substantive criteria:
- "Legislation"
- "Budget and finance"
- "Interpellations and questions"
- "Elections"
- "Miscellaneous"

This categorisation is not standardised and can vary from one federal unit to another.

### Resolutions on agenda items

The field **resolution** references the resolution(s) taken on this agenda item. A resolution documents the formal decision:

```
AgendaItem: "Energy act — final vote"
  └─ Resolution: "Acceptance of the energy act with 120 to 75 votes and 5 abstentions"
      └─ Voting: details of the voting
```

### Description and URL

- **description**: detailed description of the agenda item
- **url**: array of multilingual URLs to meeting documents:
  - dispatches and reports
  - motions
  - amendments
  - voting results

### Particularities of the various procedures

#### Legislative procedure
An affair passes through several agenda items:
1. Entry debate
2. Detailed deliberation
3. Final vote
4. Where applicable, elimination of differences between the chambers

#### Interpellations and questions
- Submission as an agenda item
- Answer of the government
- Where applicable, discussion

#### Elections
- Nomination as an agenda item
- Conduct of the election
- Announcement of the result

### Link to other entities

An AgendaItem is the central link between:

- **Meeting**: the sitting in which it is dealt with
- **Affairs** (eCH-0295): the substantive affairs
- **Resolution**: the formal decision
- **Voting**: the voting(s) on the agenda item
- **Speech**: statements and speeches on the agenda item

### Application examples

...

### Purposes of use

1. Structuring the course of the sitting and the agenda
2. Link between meetings and affairs (eCH-0295)
3. Documentation of status and result per agenda item
4. Basis for sitting protocols and publications



## Class: AgendaItem []{#AgendaItem}


_An agenda item of a meeting._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | The linked meeting ID that groups the current meeting.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | Type of agenda item, distinguishing individual items from groups.  |
| agenda_item_number | 0..1 <br/> String | Sequential number of the agenda item (string type to support roman numerals).  |
| agenda_item_position | 0..1 <br/> Integer | Integer position of the agenda item in the meeting sequence.  |
| leading_actor_id | 0..1 <br/> String | The leading department for the agenda item.  |
| speaking_actor_id | 0..1 <br/> String | The speaker or head of the department for the agenda item.  |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | Title of the agenda item.  |
| affair_id | 0..1 <br/> String | The connection to the affairs (business items) of the agenda item.  |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | Subtitle or detailed description of the agenda item.  |
| state_id | 0..1 <br/> String | State identifier (reference to state enum or custom state).  |
| state_name | 0..1 <br/> String | Custom state description for the meeting.  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing page or further web address, multilingual.  |
| agenda_item_category | 0..1 <br/> String | Category for grouped agenda items (e.g., introduction, by department, technical agenda items).  |
| parent_agenda_item | 0..1 <br/> String | If needed, this slot builds a hierarchy of agenda items.  |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | The resolution or decision taken on this agenda item.  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | agenda_items | range | [AgendaItem](#AgendaItem) |
| [JointDebate](#JointDebate) | agenda_items | range | [AgendaItem](#AgendaItem) |














### Examples
#### Example AgendaItem: Budget agenda item

```yaml
agenda_items:
- global_uri: ops:agenda_item_zh_budget_2026
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
#### Example AgendaItem: Motion within a group of agenda items

```yaml
agenda_items:
- global_uri: ops:16155798_3
  parent_meeting: ops:meeting_schaffhausen_2025_03_31
  agenda_item_type: item
  datetime_begin_planned: '2025-03-31T00:00:00Z'
  agenda_item_position: 2
  agenda_item_number: '2'
  agenda_item_title:
  - text: >-
      Motion Nr. 2023/9 von Rainer Schmidig vom 18. Dezember 2023 betreffend zeitgemässe
      Abzüge in den Art. 35 und 37 des Gesetzes über die direkten Steuern
    language: de
  agenda_item_category: Traktanden
  affair_id: affairs:MOT_2023_9
  datetime_created: '2025-05-02T11:23:49Z'
  datetime_modified: '2025-05-02T11:23:49Z'

```
#### Example AgendaItem: Agenda item of a Council of States sitting

```yaml
agenda_items:
- global_uri: ops:69905
  parent_meeting: parl:sr_winter25_sitzung_6
  agenda_item_type: item
  datetime_begin_planned: '2025-12-19T09:15:00+01:00'
  datetime_begin_actual: '2025-12-19T09:20:00+01:00'
  agenda_item_number: '6'
  agenda_item_position: 4
  agenda_item_title:
  - text: >-
      Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich durchführen,
      um die Verzögerungen zu verstehen
    language: de
  affair_id: affairs:24.4471
  landing_page: >-
    https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
  agenda_item_category: agenda_item
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'

```
#### Example AgendaItem: Postulate category voting

```yaml
agenda_items:
- global_uri: ops:0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
  parent_meeting: ops:meeting_luzern_2025_01_28
  agenda_item_type: item
  datetime_begin_planned: '2025-01-28T00:00:00Z'
  agenda_item_position: 29
  agenda_item_number: '29'
  agenda_item_title:
  - text: >-
      Postulat Widmer Reichlin Gisela und Mit. über Massnahmen zur Erfüllung des Sonderschulkonkordats
      und zur gezielten Behebung des Fachkräftemangels im Bereich schulische Heilpädagogik
      / Bildungs- und Kulturdepartement
    language: de
  agenda_item_category: voting
  url:
  - text: >-
      https://www.lu.ch/kr/Sessionen/sessionsdaten_2020/Abstimmungsresultate/Detail?TraktandumGuid=0de4ecdb-23f1-49ab-95b8-1afc2e4feb1a
    language: de
  affair_id: affairs:2024P_125
  datetime_created: '2025-01-29T06:59:41Z'
  datetime_modified: '2025-01-29T06:59:41Z'

```
#### Example AgendaItem: Interpellation of a parliamentary group

```yaml
agenda_items:
- global_uri: ops:cea750a5bd7b420fa4da1c914f801384
  parent_meeting: ops:meeting_bern_2022_03_17
  agenda_item_type: item
  datetime_begin_planned: '2022-03-17T17:00:00Z'
  agenda_item_position: 29
  agenda_item_number: '8'
  agenda_item_title:
  - text: >-
      Interpellation Fraktion GB/JA! (Katharina Gallizzi, GB): Welche Konsequenzen
      haben die Klimaziele für das Gasnetz in Bern?
    language: de
  affair_id: affairs:2020.SR.000007
  url:
  - text: >-
      https://stadtrat.bern.ch/de/sitzungen/detail.php?gid=000d6cf5f0bc4d89a5171e0123cfbff5#cea750a5bd7b420fa4da1c914f801384
    language: de
  datetime_created: '2025-01-17T21:25:52Z'
  datetime_modified: '2025-01-17T21:25:52Z'

```
#### Example AgendaItem: Petition as an agenda item

```yaml
agenda_items:
- global_uri: ops:21c50b86d21b4b4baeb1a76738ff82a3_2025-04-02_1_de
  parent_meeting: ops:meeting_bern_rr_2025_04_02
  agenda_item_type: item
  datetime_begin_planned: '2025-04-02T00:00:00Z'
  agenda_item_title:
  - text: >-
      Petition «Gleichberechtigung für Tagesfamilien: Gleich hohe Betreuungsgutscheine
      für alle Anbieter im Kanton Bern». Regierungsrätliches Antwortschreiben
    language: de
  affair_id: affairs:2025.STA.622
  url:
  - text: >-
      https://www.rr.be.ch/de/start/beschluesse/suche/geschaeftsdetail.html?guid=21c50b86d21b4b4baeb1a76738ff82a3
    language: de
  datetime_created: '2025-04-25T11:11:40Z'
  datetime_modified: '2025-04-25T11:11:40Z'

```
#### Example AgendaItem: Partial revision of several ordinances in French

```yaml
agenda_items:
- global_uri: ops:7b3545e4-57dc-3901-aaa8-4020da6ab0c6
  parent_meeting: ops:meeting_vaud_2008_04_30
  agenda_item_type: item
  datetime_begin_planned: '2008-04-30T00:00:00Z'
  agenda_item_position: 7
  agenda_item_number: '7'
  agenda_item_title:
  - text: >-
      Révision partielle de sept ordonnances fédérales relatives aux produits chimiques
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
  - text: >-
      https://www.vd.ch/actualites/decisions-du-conseil-detat/seance-du-conseil-detat/seance/265632#7b3545e4-57dc-3901-aaa8-4020da6ab0c6
    language: fr
  datetime_created: '2024-12-06T10:50:04Z'
  datetime_modified: '2024-12-06T10:50:04Z'

```
#### Example AgendaItem: Substantive affair without an agenda category

```yaml
agenda_items:
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

```
#### Example AgendaItem: Detailed deliberation of an article of an act

```yaml
agenda_items:
- global_uri: ops:agenda_item_be_2025_042
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
  - text: >-
      Délibération sur les propositions de modification de l'article 5 de la loi fiscale
    language: fr
  agenda_item_category: Gesetzgebung
  state_id: completed
  datetime_begin_planned: '2025-05-12T15:00:00Z'
  datetime_begin_actual: '2025-05-12T15:15:00Z'
  affair_id: affairs:be_2024_089_steuergesetz
  datetime_created: '2025-04-15T09:00:00Z'
  datetime_modified: '2025-05-12T15:20:00Z'

```
#### Example AgendaItem: Interpellation as an agenda item

```yaml
agenda_items:
- global_uri: ops:06fb582b753c416d8fdb05fa13873545
  parent_meeting: ops:meeting_2011_11_23
  agenda_item_type: item
  datetime_begin_planned: '2011-11-23T00:00:00Z'
  agenda_item_position: 2
  agenda_item_title:
  - text: >-
      Interpellation Peter Mark betr. elektronische Datenerfassung durch Mitarbeiter
      im Werkhof – Versuchsphase
    language: de
  datetime_created: '2025-03-21T23:15:19Z'
  datetime_modified: '2025-03-21T23:15:19Z'

```
#### Example AgendaItem: Substantive affair from a cantonal parliamentary information system

```yaml
agenda_items:
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

```
#### Example AgendaItem: Agenda item with a final vote

```yaml
agenda_items:
- global_uri: ops:agenda_item_sg_2025_015
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
#### Example AgendaItem: Popular motion within a group of agenda items

```yaml
agenda_items:
- global_uri: ops:16155798_4
  parent_meeting: ops:meeting_schaffhausen_2025_03_31_b
  agenda_item_type: item
  datetime_begin_planned: '2025-03-31T00:00:00Z'
  agenda_item_position: 3
  agenda_item_number: '3'
  agenda_item_title:
  - text: >-
      Volksmotion Nr. 2024/1 von Sandro Mamedow und Livia Schraff (Erstunterzeichnende)
      sowie weitere 150 Mitunterzeichnende vom 22. März 2024 mit dem Titel: «Für eine
      Stimme der Studierenden im Hochschulrat der Pädagogischen Hochschule Schaffhausen
      (PHSH)»
    language: de
  agenda_item_category: Traktanden
  affair_id: affairs:MOT_2024_1
  datetime_created: '2025-05-02T11:23:49Z'
  datetime_modified: '2025-05-02T11:23:49Z'

```
#### Example AgendaItem: French-language agenda item postulate

```yaml
agenda_items:
- global_uri: ops:2023_10_03-52
  parent_meeting: ops:meeting_lausanne_2023_10_03
  agenda_item_type: item
  datetime_begin_planned: '2023-10-03T00:00:00Z'
  agenda_item_position: 52
  agenda_item_number: '52'
  agenda_item_title:
  - text: >-
      Postulat de Mme Franziska MEINHERZ : « Lausanne sans publicité commerciale »
      (FIM)
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

```
#### Example AgendaItem: Postulate with a voting

```yaml
agenda_items:
- global_uri: ops:fa732e0e-7e5f-4d45-994a-fc74720c0781
  parent_meeting: ops:meeting_luzern_2025_01_28_b
  agenda_item_type: item
  datetime_begin_planned: '2025-01-28T00:00:00Z'
  agenda_item_position: 14
  agenda_item_number: '14'
  agenda_item_title:
  - text: >-
      Postulat Stadelmann Karin Andrea und Mit. über die Überprüfung und Anpassung
      der Kriterien zum früheren Eintritt von Kindern in die Basisstufe (den freiwilligen
      Kindergarten) / Bildungs- und Kulturdepartement
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
#### Example AgendaItem: Urgent interpellation in French

```yaml
agenda_items:
- global_uri: ops:2025_05_20-23
  parent_meeting: ops:meeting_lausanne_2025_05_20
  agenda_item_type: item
  datetime_begin_planned: '2025-05-20T00:00:00Z'
  agenda_item_position: 23
  agenda_item_number: '23'
  agenda_item_title:
  - text: >-
      Interpellation urgente du 20 mai 2025 de M. Yusuf KULMIYE : « Interpellation
      urgente de Kulmiye Yusuf et crts – Solidarité sans frontières, Lausanne en faveur
      du respect du droit international et de la protection des populations civiles
      à Gaza »
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

```






</div>

## Enum: AgendaItemTypeEnum []{#AgendaItemTypeEnum}




_Type of agenda item, distinguishing individual items from grouped items._




<div data-search-exclude markdown="1">

URI: [ops:AgendaItemTypeEnum](https://ch.paf.link/schema/operations/AgendaItemTypeEnum)

### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| item |  Individual agenda item (Traktandum)  |
| | [ops:enum/agenda_item_type/item](ops:enum/agenda_item_type/item) |
| group |  Group of agenda items (Traktandengruppe)  |
| | [ops:enum/agenda_item_type/group](ops:enum/agenda_item_type/group) |







</div>

## Protocol

### Purpose of the entity

While the agenda items represent the **planning** of a sitting, the protocol records the **actual course** after the sitting. `Protocol` is a wrapper container kept exactly once per sitting (`Meeting`) that bundles the agenda items actually dealt with (`protocol_items`), votings, speeches as well as verbatim text segments and documents.

```
Meeting
  ├─ agenda_items   (before: planned agenda items)
  └─ protocol_ref   (after: the record)
        ├─ protocol_items  → ProtocolItem (like AgendaItem)
        ├─ votings
        ├─ speeches
        ├─ text_segments
        └─ documents
```



## Class: Protocol []{#Protocol}


_The minutes of a meeting, recorded after the meeting. A wrapper container bundling the actually handled agenda items (protocol_items), votings, speeches, verbatim text segments and linked documents._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | The linked meeting ID that groups the current meeting.  |
| protocol_items | * <br/> [ProtocolItem](#ProtocolItem) | Agenda items as actually recorded in the protocol.  |
| votings | * <br/> [Voting](#Voting) | Collection of voting records.  |
| speeches | * <br/> [Speech](#Speech) | Collection of speech records.  |
| text_segments | * <br/> [TextSegment](#TextSegment) | Collection of text segments (e.g. verbatim protocol).  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | protocols | range | [Protocol](#Protocol) |
| [Meeting](#Meeting) | protocol_ref | range | [Protocol](#Protocol) |



















</div>

### ProtocolItem (agenda item as recorded)

`ProtocolItem` inherits all fields of `AgendaItem` (`is_a: AgendaItem`) and represents an agenda item as it was actually recorded in the protocol.



## Class: ProtocolItem []{#ProtocolItem}


_An agenda item as actually recorded in the protocol._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_meeting | 0..1 <br/> String | The linked meeting ID that groups the current meeting. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](#AgendaItemTypeEnum) | Type of agenda item, distinguishing individual items from groups. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| agenda_item_number | 0..1 <br/> String | Sequential number of the agenda item (string type to support roman numerals). <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| agenda_item_position | 0..1 <br/> Integer | Integer position of the agenda item in the meeting sequence. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| leading_actor_id | 0..1 <br/> String | The leading department for the agenda item. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| speaking_actor_id | 0..1 <br/> String | The speaker or head of the department for the agenda item. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| agenda_item_title | * <br/> [MultilingualString](#MultilingualString) | Title of the agenda item. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| affair_id | 0..1 <br/> String | The connection to the affairs (business items) of the agenda item. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| agenda_item_description | * <br/> [MultilingualString](#MultilingualString) | Subtitle or detailed description of the agenda item. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| state_id | 0..1 <br/> String | State identifier (reference to state enum or custom state). <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| state_name | 0..1 <br/> String | Custom state description for the meeting. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| landing_page | 0..1 <br/> String | URL providing further information. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing page or further web address, multilingual. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| agenda_item_category | 0..1 <br/> String | Category for grouped agenda items (e.g., introduction, by department, technical agenda items). <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| parent_agenda_item | 0..1 <br/> String | If needed, this slot builds a hierarchy of agenda items. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| has_resolution | 0..1 <br/> [Resolution](#Resolution) | The resolution or decision taken on this agenda item. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity. <br/><br/>Inheritance: [AgendaItem](#AgendaItem) |
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](#IsEventWithDuration) |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Protocol](#Protocol) | protocol_items | range | [ProtocolItem](#ProtocolItem) |



















</div>

## Joint debate (JointDebate)

### Purpose of the entity

`JointDebate` combines several agenda items that are deliberated together — for instance substantively related affairs dealt with in a single debate.



## Class: JointDebate []{#JointDebate}


_Agenda Items which are debated together._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | Collection of agenda item records.  |






















</div>

## Resolution

### Purpose of the entity

The Resolution entity records the formal decision on an agenda item. It documents **what** was decided, while Voting documents **how** (with which procedure and which ratio of votes) the decision was taken.

### Relation to AgendaItem and Voting

```
AgendaItem (Energy act — final vote)
  ├─ Resolution (acceptance of the energy act)
  └─ Voting (120 yes, 75 no, 5 abstentions)
```

An AgendaItem can have several Resolutions (e.g. in case of several votings on the same agenda item). Each Resolution typically references a Voting containing the voting details.

### Types of resolutions

The **resolution_type** field uses a controlled vocabulary:

#### accepted
The agenda item was accepted

**Application:**
- Bills were accepted
- Motions were approved
- Decisions were taken

#### rejected
The agenda item was rejected

**Application:**
- Bills were rejected
- Motions were dismissed
- Rejection decisions

#### referred_back
Referral back to another body

**Application:**
- Referral back to a committee for revision
- Referral back to the government
- Back to the other chamber (in bicameral systems)

#### noted
Noted

**Application:**
- Reports without a voting
- Announcements
- Informative agenda items

#### postponed
Adjourned

**Application:**
- Deferral of the treatment
- Not yet ready for a decision
- Further clarifications needed

#### withdrawn
Withdrawn

**Application:**
- The proposer withdraws the bill
- The affair is not pursued further

#### amended
Accepted with amendments

**Application:**
- Act accepted with amendments
- Modified version adopted
- Compromise solution

#### no_decision
No decision taken

**Application:**
- No majority for any motion
- Tie without a casting vote
- Not able to take decisions

### Design decision: why a separate Resolution entity?

**The alternative would have been:** storing the resolution type directly in AgendaItem.

**Reasons for a separate entity:**

1. **Several decisions per agenda item**: an agenda item can have several decisions (e.g. first an amendment, then the overall vote)

2. **Structured link to votings**: clear 1:1 relation between Resolution and Voting

3. **Multilingual decision texts**: a Resolution can contain detailed decision texts in several languages

4. **Temporal flexibility**: a Resolution can be recorded separately in time from the AgendaItem

### Decision text

- **title**: short summary of the decision
- **description**: detailed decision text

**Example:**
- title: "Acceptance of the energy act"
- description: "The National Council accepts the Federal Act on the Energy Transition in the version of the committee with 120 to 75 votes and 5 abstentions."

### Link to the voting

The field **voting_id** references the corresponding Voting containing the voting details:

- Ratio of votes
- Voting procedure
- Individual votes (in roll-call votings)

**Not all resolutions have a voting:**
- "Noted" often occurs without a formal voting
- Tacit acceptances
- Administrative decisions

### Timestamps

- **datetime_created**: point in time of the decision
- **datetime_modified**: last change (e.g. in case of corrections)

### URLs and documentation

The field **url** can reference further documents:
- Detailed decision texts
- Reasons
- Legal bases

### Use cases in different contexts

#### Legislative procedure
Several resolutions for different phases:
1. Resolution "entry" (accepted/rejected)
2. Resolution on article 1 (accepted/amended)
3. Resolution on article 2 (accepted)
4. Resolution overall vote (accepted/rejected)

#### Elimination of differences (bicameral system)
- Resolution "adherence to the version of the first chamber"
- Resolution "maintaining its own version"
- Resolution "acceptance of the compromise proposal"

#### Committee work
- Resolution "referral back to the committee with an additional mandate"
- Resolution "adoption of the committee report"

### Technical considerations

#### Granularity
The granularity of resolution recording varies:
- **Detailed**: every individual voting gets its own resolution
- **Aggregated**: only the final decision is recorded

The standard permits both approaches.

#### Multilingualism
In multilingual parliaments (CH, BE, etc.) decision texts have to be recorded in all official languages. This is done via MultilingualString arrays in title and description.

### Purposes of use

1. **Official documentation**: what was decided?
2. **Legal force**: formal proof of the decision
3. **Public information**: comprehensible summary of complex votings
4. **Affairs management**: tracking of decisions and their implementation
5. **Statistical evaluation**: acceptance and rejection rates



## Class: Resolution []{#Resolution}


_A resolution or decision taken on an agenda item, including voting procedures._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](#ResolutionTypeEnum) | Type of resolution taken on the agenda item.  |
| type_label | 0..1 <br/> String | Custom type label when standard type values don't apply.  |
| vote_procedures | * <br/> String | Procedures for voting, such as secret ballot or open vote.  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | resolutions | range | [Resolution](#Resolution) |
| [AgendaItem](#AgendaItem) | has_resolution | range | [Resolution](#Resolution) |
| [ProtocolItem](#ProtocolItem) | has_resolution | range | [Resolution](#Resolution) |



















</div>

## Enum: ResolutionTypeEnum []{#ResolutionTypeEnum}




_Type of resolution taken on an agenda item._




<div data-search-exclude markdown="1">

URI: [ops:ResolutionTypeEnum](https://ch.paf.link/schema/operations/ResolutionTypeEnum)

### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| accepted |  Accepted (Annahme)  |
| | [ops:enum/resolution_type/accepted](ops:enum/resolution_type/accepted) |
| rejected |  Rejected (Ablehnung)  |
| | [ops:enum/resolution_type/rejected](ops:enum/resolution_type/rejected) |
| noted |  Noted (Kenntnisnahme)  |
| | [ops:enum/resolution_type/noted](ops:enum/resolution_type/noted) |
| accepted_point_by_point |  Accepted point by point (Punktweise Annahme)  |
| | [ops:enum/resolution_type/accepted_point_by_point](ops:enum/resolution_type/accepted_point_by_point) |
| accepted_with_postulate |  Accepted with postulate (Annahme mit Postulat)  |
| | [ops:enum/resolution_type/accepted_with_postulate](ops:enum/resolution_type/accepted_with_postulate) |
| orally_settled |  Orally settled (Mündlich erledigt)  |
| | [ops:enum/resolution_type/orally_settled](ops:enum/resolution_type/orally_settled) |
| nearly_unanimous |  Nearly unanimous (Beinahe einstimmig)  |
| | [ops:enum/resolution_type/nearly_unanimous](ops:enum/resolution_type/nearly_unanimous) |
| other |  Other resolution type not covered by standard categories  |
| | [ops:enum/resolution_type/other](ops:enum/resolution_type/other) |







</div>

## Motion

### Purpose

Records motions submitted during the sitting (amendments, procedural motions, etc.).

### Structure

- **motion_type**: type of the motion
  - **amendment**: amendment to a legal text
  - **procedural**: procedural motion (e.g. closing the debate)
  - **referral**: referral motion
  - **other**: other motions
- **title**: short title of the motion
- **description**: full text of the motion
- **proposer_person_id**: the person submitting the motion
- **seconder_person_id**: seconders (where required)
- **result**: result (accepted, rejected, withdrawn)

### Design decision

**Why a separate entity instead of just in AgendaItem?**
- An agenda item can contain several motions
- Motions have their own life cycle (submitted, seconded, voted on)
- Structured recording of proposer and supporters
- Separate votings per motion are possible

### Application

Linked with AgendaItem and optionally with Voting:

```
AgendaItem (Energy act — art. 15)
  ├─ Motion (amendment person A)
  │   └─ Voting (voting on the amendment)
  ├─ Motion (amendment person B)
  │   └─ Voting (voting on the amendment)
  └─ Voting (voting on the article as a whole)
```



## Class: Motion []{#Motion}


_A formal proposal or motion submitted during proceedings._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| title | 0..1 <br/> String | Title of the element.  |
| description | 0..1 <br/> String | Descriptive text of the element.  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |






















</div>

\newpage

<!-- ToDo: Nicole -->

# Votings and elections

Parliamentary decisions are taken either by votings on substantive questions or by elections of persons. The standard clearly distinguishes these two mechanisms and additionally records, in open procedures, the individual voting behaviour of every member of parliament. Presidents of parliament generally do not take part in votings; they only vote in elections. In votings with a tie they cast the deciding vote.

## Voting

## Purpose of the entity

"Voting" records the voting process and the result of a formal decision in parliament. The entity documents the subject of the voting (the question), the procedure (how the vote was taken) and the result (with which ratio of votes).

## Types of votings

The standard distinguishes different voting types via the field **voting_type**:

### intermediate
Intermediate votings during the deliberation.

**Examples:**
- Voting on entering into an affair
- Voting on a motion
- Opposing two motions that exclude each other or that refer to the same passage of text
- Contingent voting when more than two motions relate to the same subject
- Voting on a single article of an act
- Overall vote after the first reading of an enactment deliberated in two readings

### final
The concluding voting on the entire bill

**Examples:**
- Final vote after the last reading of an enactment
- Overall vote on a decree
- Acceptance or rejection of a bill as a whole
- Point-by-point voting on a parliamentary initiative

### casting
Deciding vote of the chair in case of a tie. The chair does not take part in votings but has the deciding vote in case of a tie. In a secret voting, in case of a tie the motion of the preliminarily deliberating council body counts as accepted.

### secret
Secret casting of votes in votings and elections

**Application:**
- Election of persons
- Voting on a particularly sensitive substantive affair such as a pardon request or the lifting of immunity
- Voting after a confidential deliberation
- Secret voting upon request

## Structure of a voting

A voting is always assigned to a sitting phase and/or a sitting, an agenda item and an affair with an affair title and an affair number. It comprises the voting type, the subject of the voting (the question), the result and — in a non-secret voting — the individual votes of the members.
It can either:

```
AgendaItem (15) affair (Energy act — art. 15)
  └─ Voting (intermediate voting on art. 15)
      ├─ IndividualVote (person A: yes)
      ├─ IndividualVote (person B: no)
      └─ IndividualVote (person C: yes)
```


Example selection:
3 options: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
5 options: https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=23f01ba9b3f3410cb9cfb85f32f3dfe0

## Voting procedures

The field **procedure** describes how the vote is conducted:

### Open procedures
- **show_of_hands**: show of hands (traditional)
- **standing**: standing up (rarer)
- **electronic**: electronic voting (frequent at federal and cantonal level)
- **roll_call**: roll-call voting with calling of names
- **remote_voting**: external casting of votes during crises (individual council members communicate their vote to the parliamentary presidency ahead of the sitting day. The externally cast votes are recorded simultaneously with the voting running in the council.)
- **circulation_voting**: circulation procedure during crises (the parliamentary presidency conducts the voting by circulation and informs about the result)
- **virtual_voting**: casting of votes at virtual sittings during crises.

### Secret procedures
- **secret_ballot**: secret ballot with voting slips
- **electronic_secret**: electronic secret voting

The choice of procedure determines whether individual votes can be recorded:
- Open procedures: individual votes can be documented
- Secret procedures: only the overall result is available


## Voting result

The result is recorded in two ways:

### Detailed figures
- **total_count_yes**: number of yes votes
- **total_count_no**: number of no votes
- **total_count_abstention**: number of abstentions
- **total_other**: numbers of votes for additional options where not only yes/no/abstention are available (see the section "Multiple options")
- **total_absent**: number of absent members (who could not vote)
- **total**: total number of voting members (without absentees and the presidency's vote)
- **majority_count**: number of votes required for the necessary majority

### Overall result
The result is described as free text in the field **result_text** (e.g. "Accepted with 120 to 75 votes and 5 abstentions"). The categorical decision (accepted / rejected / noted etc.) is not recorded on the voting itself but via the class **Resolution** (slot **resolution_type**) on the agenda item. In case of a tie, a possible deciding vote of the presidency is modelled via a separate voting (`voting_type: tie_breaker_president`) respectively a new voting.

**Example** (final vote, simple yes/no voting):
- total_count_yes: 120
- total_count_no: 75
- total_count_abstention: 5
- total_absent: 0
- total: 200
- result_text: "Accepted with 120 to 75 votes and 5 abstentions"
- Resolution.resolution_type: accepted

<!-- TODO: weitere komplexere Beispiele ergänzen — Ordnungsantrag, Wiederholung einer Abstimmung. (Cup-/Mehrfachabstimmung und Stichentscheid sind abgedeckt.) -->

### Multiple options (selection votings / "motions in the same direction")

Not every voting knows only yes, no and abstention. If several motions in the same direction relate to the same substantive question, the members vote on more than two variants simultaneously (in Zurich colloquially "cup voting", technically via several voting buttons). The prevailing variant is the one with the most votes.

Such procedures are represented as follows:

- **voting_type** = `other`, complemented by a meaningful **type_label** (e.g. "Motions in the same direction (multiple choice)").
- The standard fields **total_count_yes / total_count_no / total_count_abstention** remain empty, because the options do not correspond to yes/no/abstention.
- Instead, every selection option gets an entry in **total_other** (list of `TotalOther` with **count** and **label**). This allows any number of options with their respective vote counts to be recorded.
- At the level of the individual vote, **individual_vote_type** is set to `other` and the chosen option is recorded via **type_label** (e.g. "Selection A"); absent members get `not_voted`.
- As **majority_type**, `other` is used, because it is not a fixed threshold but the relative majority among the options that decides.

**Example** (City of Zurich communal council, 86th sitting of 28.02.2024, affair 2023/361 "Residential building Magnusstrasse 27, net additional credit") — motions in the same direction with four selection options:

| Option | Votes |
|--------|-------|
| Selection A (prevailing) | 75 |
| Selection B | 25 |
| Selection C | 12 |
| Selection D | 0 |
| Absent | 13 |

- Total cast: 112 (of 125 members)
- Result: selection A accepted (relative majority)

The complete modelling of this case can be found in `data_voting.yaml` (`ops:voting_zh_gr_2024_2023_361`).

## Majority types

The field **majority_type** defines the required majority:

### simple
Simple majority (more yes than no)

**Application:**
- Standard case for most decisions
- Abstentions do not count

**Example:** 100 yes, 80 no, 20 abstentions → accepted

### absolute
Absolute majority (more than half of all members)

**Application:**
- Elections
- Constitutional amendments in some cantons
- Particularly important decisions

**Example:** with 200 members at least 101 yes votes are required

### two_thirds
Two-thirds majority

**Application:**
- Urgency clauses at federal level
- Constitutional amendments in some cantons
- Lifting of immunity

**Example:** with 200 members at least 134 yes votes are required

### qualified
Qualified majority (other thresholds)

**Application:**
- Special requirements in individual cantons or communes
- The concrete quorum is indicated in **majority_threshold**

## Threshold

For qualified majorities, the field **majority_threshold** indicates the exact threshold (e.g. 0.6 for 60%).

## Quorum

The field **quorum** defines the minimum number of members present for the capacity to take decisions:

**Example:** a parliament with 200 members can take decisions if at least 100 members are present (quorum: 100).

## Roll-call votings
The field **named_vote** indicates whether the voting is a roll-call voting:

- **true**: the individual votes are recorded and published
- **false**: only the overall result is recorded

Roll-call votings are important for:
- transparency of voting behaviour
- analysis of voting patterns
- accountability towards the electorate

## Relation to individual votes

In roll-call votings the Voting entity references the individual IndividualVote entities:

```
Voting
  ├─ IndividualVote (person A)
  ├─ IndividualVote (person B)
  └─ ...
```

**Example:** name list in an accordion https://www.tagblatt.gr.be.ch/shareparl?agendaItemUid=e65d81c90d1d43deb19ef078f7e363f3&segmentType=vote&unitName=default&scroll=true&autoplay=false


## Description and documentation

- **description**: description of what was voted on (subject of the voting, voting question)
- **url**: multilingual URLs to voting details

## Timestamps

- **datetime_created**: point in time of conducting the voting
- **datetime_modified**: last update (e.g. in case of corrections to the voting protocol)




## Class: Voting []{#Voting}


_A voting procedure with individual votes and results._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| datetime_begin | 0..1 <br/> Datetime | The date and time when the meeting or voting begins.  |
| datetime_end | 0..1 <br/> Datetime | The date and time when the meeting or voting ends.  |
| voting_type | 0..1 <br/> [VotingTypeEnum](#VotingTypeEnum) | Type of voting procedure (preliminary, final, secret, etc.).  |
| type_label | 0..1 <br/> String | Custom type label when standard type values don't apply.  |
| voting_title | * <br/> [MultilingualString](#MultilingualString) | Title or question being voted on. If no specific subject exists, do not use the business item title.  |
| optional | 0..1 <br/> Boolean | Indicates if the meeting or voting is optional.  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| label_yes | 0..1 <br/> String | Meaning of a 'yes' vote.  |
| label_no | 0..1 <br/> String | Meaning of a 'no' vote.  |
| label_abstention | 0..1 <br/> String | Meaning of an 'abstention' vote.  |
| tie_breaker | 0..1 <br/> Boolean | Indicates if a tie-breaker was used in the voting.  |
| total_count_yes | 0..1 <br/> Integer | Total number of 'yes' votes.  |
| total_count_no | 0..1 <br/> Integer | Total number of 'no' votes.  |
| total_count_abstention | 0..1 <br/> Integer | Total number of abstentions.  |
| total_other | * <br/> TotalOther | Used when multiple options are presented for voting (e.g., 5 buttons in Zurich).  |
| total_absent | 0..1 <br/> Integer | Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list.  |
| total | 0..1 <br/> Integer | Total number of votes, excluding absent and president's vote.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | Type of majority required for the vote (absolute, two-thirds, etc.).  |
| majority_count | 0..1 <br/> Integer | Number of votes required for the relevant majority threshold.  |
| result_text | 0..1 <br/> String | Free text describing the outcome of the vote, e.g., "Accepted with 78 votes".  |
| parent_meeting | 0..1 <br/> String | The linked meeting ID that groups the current meeting.  |
| parent_agenda_item | 0..1 <br/> String | If needed, this slot builds a hierarchy of agenda items.  |
| affair_id | 0..1 <br/> String | The connection to the affairs (business items) of the agenda item.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | votings | range | [Voting](#Voting) |
| [Protocol](#Protocol) | votings | range | [Voting](#Voting) |
| [IndividualVote](#IndividualVote) | parent_voting | range | [Voting](#Voting) |














### Examples
#### Example Voting: Intermediate voting on an amendment

```yaml
votings:
- global_uri: ops:voting_be_2025_042
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
#### Example Voting: Final vote with individual votes

```yaml
votings:
- global_uri: ops:voting_sg_2025_001
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
#### Example Voting: Final vote on the budget

```yaml
votings:
- global_uri: ops:voting_zh_budget_2026
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
#### Example Voting: Motions in the same direction with multiple choice

```yaml
votings:
- global_uri: ops:voting_zh_gr_2024_2023_361
  voting_title:
  - text: >-
      Liegenschaften Stadt Zürich, Wohnhaus Magnusstrasse 27, Gesamtinstandsetzung,
      Grundrissanpassung, Netto-Zusatzkredit (Geschäft 2023/361)
    language: de
  voting_type: other
  type_label: Gleichgerichtete Anträge (Mehrfachauswahl)
  datetime_begin: '2024-02-28T00:00:00Z'
  datetime_end: '2024-02-28T00:00:00Z'
  landing_page: >-
    https://www.gemeinderat-zuerich.ch/abstimmungen/detail.php?aid=aa10c137274f424fa4eda877e7644a89
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
  result_text: >-
    Auswahl A mit 75 von 112 abgegebenen Stimmen angenommen (Auswahl B: 25, Auswahl
    C: 12, Auswahl D: 0; 13 abwesend von 125 Mitgliedern).
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






</div>

## Enum: VotingTypeEnum []{#VotingTypeEnum}




_Type of voting procedure._




<div data-search-exclude markdown="1">

URI: [ops:VotingTypeEnum](https://ch.paf.link/schema/operations/VotingTypeEnum)

### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| preliminary_vote |  Preliminary vote (Zwischenabstimmung)  |
| | [ops:enum/voting_type/preliminary_vote](ops:enum/voting_type/preliminary_vote) |
| final_vote |  Final vote (Schlussabstimmung)  |
| | [ops:enum/voting_type/final_vote](ops:enum/voting_type/final_vote) |
| tie_breaker_president |  President's tie-breaking vote (Stichentscheid Präsidium)  |
| | [ops:enum/voting_type/tie_breaker_president](ops:enum/voting_type/tie_breaker_president) |
| secret_vote |  Secret ballot (Geheime Wahl/Abstimmung)  |
| | [ops:enum/voting_type/secret_vote](ops:enum/voting_type/secret_vote) |
| other |  Other voting type  |
| | [ops:enum/voting_type/other](ops:enum/voting_type/other) |







</div>

## Enum: MajorityTypeEnum []{#MajorityTypeEnum}




_Type of majority required for the vote._




<div data-search-exclude markdown="1">

URI: [ops:MajorityTypeEnum](https://ch.paf.link/schema/operations/MajorityTypeEnum)

### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| absolute |  Absolute majority.  |
| | [ops:enum/majority_type/absolute](ops:enum/majority_type/absolute) |
| two_thirds |  Two-thirds majority.  |
| | [ops:enum/majority_type/two_thirds](ops:enum/majority_type/two_thirds) |
| other |  Other majority threshold not covered by the standard categories.  |
| | [ops:enum/majority_type/other](ops:enum/majority_type/other) |







</div>

## Individual Vote

## Purpose of the entity

IndividualVote records the voting behaviour of individual members of parliament in roll-call votings. The entity is only created if a voting is not conducted secretly (Voting.is_nominal = true).

## Relation to the voting

Every individual vote is part of a superordinate voting:

```
Voting (final vote energy act)
  ├─ IndividualVote (National Councillor Anna Müller: yes)
  ├─ IndividualVote (National Councillor Beat Schweizer: no)
  ├─ IndividualVote (National Councillor Carla Rossi: abstention)
  └─ ...
```

## Identification of the person

The voting person is referenced via the field **person_id**. This ID corresponds to a person according to the eCH-0294 Actors standard.

Additional identification data can be recorded as well:
- **person_name**: name of the person (for quick access)
- **person_number**: internal number (e.g. mandate number)
- **person_political_group**: parliamentary group affiliation
- **person_party**: party affiliation

## Types of votes

TODO: describe the handling of "other" votes, i.e. votes for options that are not yes, no or abstention.

The field **vote** records the type of the vote cast:

### yes
Yes vote (approval)

**Meaning:** the person approves the bill / the motion.

### no
No vote (rejection)

**Meaning:** the person rejects the bill / the motion.

### abstention
Abstention

**Meaning:** the person takes part in the voting but abstains. When voting electronically, they press the "abstention" button.

## Vote weight

The field **weight** records the weight of the vote:

- **Standard case**: 1.0 (one vote)
- **Special cases**: other values possible

### Use cases for a divergent vote weight

1. **Substitution**: in some systems a person can vote on behalf of an absent person (weight: 2.0)
3. **Communal assemblies**: in special cases legal entities can hold several votes
4. **Historical systems**: in some cantons different groups of persons formerly had different vote weights

## Group affiliation

The field **group_id** records the parliamentary group affiliation at the time of the voting:

**Benefit:**
- Analysis of voting behaviour by group
- Determination of party discipline
- Identification of coalitions

**Example:** in a voting on the energy act 90% of the SP group vote yes, 80% of the SVP group vote no.

## Position and order

The field **position** defines the grouping and sort order in the presentation:

**Application:**
- Alphabetical sorting by surname
- Sorting by parliamentary group
- Sorting by vote cast (first yes, then no, then abstentions)
- Grouping by parliamentary group, within the group by yes, no, abstentions and within the subgroup alphabetically

## Description and context

The field **description** can record additional information:

**Examples:**
- "Abstention due to a conflict of interest (board member of an energy company)"
- "Absent due to illness"

## Timestamps

- **datetime_created**: first publication
- **datetime_modified**: last update (e.g. in case of corrections to the publication)

## Attendance vs. casting a vote

Important difference:

- **Attendance** (another entity): records the general presence at a sitting
- **IndividualVote**: records the specific vote cast in a voting

A person can be present at a sitting (Attendance) but be recorded as "absent" or "did_not_vote" in individual votings (e.g. when briefly leaving the room).

## Roll-call vs. secret votings

IndividualVote entities are only recorded in roll-call (open) votings:

- **Roll-call voting**: every vote is recorded and is public
- **Secret voting**: only the overall result is recorded, no IndividualVotes



## Class: IndividualVote []{#IndividualVote}


_An individual vote cast by a member during a voting procedure._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| parent_voting | 0..1 <br/> [Voting](#Voting) | The ID of the voting associated with the individual vote.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Reference to the acting person (lightweight snapshot at time of linking).  |
| seat_nr | 0..1 <br/> String | The seat number of the individual vote, if applicable.  |
| weight | 0..1 <br/> Integer | The number of votes held by the individual, if applicable (e.g., in cases where a person has multiple votes).  |
| individual_vote_type | 0..1 <br/> [IndividualVoteTypeEnum](#IndividualVoteTypeEnum) | Type of vote cast (yes, no, abstention, no vote, etc.).  |
| type_label | 0..1 <br/> String | Custom type label when standard type values don't apply.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | individual_votes | range | [IndividualVote](#IndividualVote) |














### Examples
#### Example IndividualVote: Yes vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_123
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27235
    label: Paul Schlegel
  seat_nr: '1'
  individual_vote_type: 'yes'
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Example IndividualVote: No vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_456
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27234
    label: Andreas Eggenberger
  seat_nr: '2'
  individual_vote_type: 'no'
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Example IndividualVote: Abstention

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_789
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27233
    label: Thomas Ammann
  seat_nr: '3'
  individual_vote_type: abstention
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Example IndividualVote: Absent in a multiple-choice voting

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_abs1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/4
    label: Abwesendes Mitglied
  seat_nr: '103'
  individual_vote_type: not_voted
  datetime_created: '2024-02-28T00:00:00Z'

```
#### Example IndividualVote: Yes vote on the budget

```yaml
individual_votes:
- global_uri: ops:vote_zh_budget_2026_person_101
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/27237
    label: Thomas Wolf
  seat_nr: '1'
  individual_vote_type: 'yes'
  datetime_created: '2025-11-20T16:45:00Z'

```
#### Example IndividualVote: No vote on the budget

```yaml
individual_votes:
- global_uri: ops:vote_zh_budget_2026_person_102
  parent_voting: ops:voting_zh_budget_2026
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/25208
    label: Jean-Daniel Strub
  seat_nr: '2'
  individual_vote_type: 'no'
  datetime_created: '2025-11-20T16:45:00Z'

```
#### Example IndividualVote: Did not vote

```yaml
individual_votes:
- global_uri: ops:vote_sg_2025_001_person_321
  parent_voting: ops:voting_sg_2025_001
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/25177
    label: Ruedi Thomann
  seat_nr: '4'
  individual_vote_type: not_voted
  datetime_created: '2025-03-15T14:30:00Z'

```
#### Example IndividualVote: Individual vote for selection option C

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_c1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/3
    label: Mitglied Auswahl C
  seat_nr: '88'
  individual_vote_type: other
  type_label: Auswahl C
  datetime_created: '2024-02-28T00:00:00Z'

```
#### Example IndividualVote: Individual vote for selection option A

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_a1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/1
    label: Mitglied Auswahl A
  seat_nr: '12'
  individual_vote_type: other
  type_label: Auswahl A
  datetime_created: '2024-02-28T00:00:00Z'

```
#### Example IndividualVote: Individual vote for selection option B

```yaml
individual_votes:
- global_uri: ops:vote_zh_gr_2024_2023_361_b1
  parent_voting: ops:voting_zh_gr_2024_2023_361
  actor_id:
    global_uri: https://www.gemeinderat-zuerich.ch/personen/2
    label: Mitglied Auswahl B
  seat_nr: '47'
  individual_vote_type: other
  type_label: Auswahl B
  datetime_created: '2024-02-28T00:00:00Z'

```






</div>

## Enum: IndividualVoteTypeEnum []{#IndividualVoteTypeEnum}




_Type of individual vote cast by a member._




<div data-search-exclude markdown="1">

URI: [ops:IndividualVoteTypeEnum](https://ch.paf.link/schema/operations/IndividualVoteTypeEnum)

### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| yes |  Vote in favor (yes)  |
| | [ops:enum/individual_vote_type/yes](ops:enum/individual_vote_type/yes) |
| no |  Vote against (no)  |
| | [ops:enum/individual_vote_type/no](ops:enum/individual_vote_type/no) |
| abstention |  Abstention  |
| | [ops:enum/individual_vote_type/abstention](ops:enum/individual_vote_type/abstention) |
| not_voted |  Not Voted  |
| | [ops:enum/individual_vote_type/not_voted](ops:enum/individual_vote_type/not_voted) |
| tie_breaker |  Tie-breaking vote, usually cast by the presiding officer  |
| | [ops:enum/individual_vote_type/tie_breaker](ops:enum/individual_vote_type/tie_breaker) |
| other |  Other vote type  |
| | [ops:enum/individual_vote_type/other](ops:enum/individual_vote_type/other) |







</div>

## Election

## Term and meaning

An election denotes the designation of one or more persons to an office or a function by a parliamentary body. In contrast to votings, in which substantive questions are decided, elections concern decisions about persons.

## Difference: election vs. voting

| Criterion | Election | Voting |
|-----------|----------|--------|
| Subject | Persons | Substantive questions, bills |
| Result | Elected person(s) | Accepted / rejected |
| Procedure | Often secret | Often open |
| Majority | Mostly absolute | Mostly simple |

## Types of elections

The standard distinguishes different election types via the field **election_type**:

### open
Open election

**Characteristic:**
- The casting of votes is publicly visible
- Every member casts their vote openly
- It is traceable who elected whom

**Application:**
- Where transparency is desired
- In uncontested elections
- In smaller bodies

### secret
Secret election

**Characteristic:**
- The casting of votes is anonymous
- Voting slips or an electronic secret voting system
- It is not traceable who elected whom

**Application:**
- Elections of persons (standard)
- Where a free, uninfluenced decision is to be guaranteed
- Often prescribed by law

**Examples at federal level:**
- Election of the Federal Council
- Election of the federal judges
- Election of the committee presidencies

**Examples at cantonal level:**
- Election of the president of the parliament
- Election of the president of the government
- Election of the presidents of the highest cantonal courts
- Election of the judges
- Election of the state chancellor
- Election of the committee presidencies

### tacit
Tacit election

**Characteristic:**
- No formal voting required
- The election takes place by acclamation or consensus
- Only if no opposing votes are raised

**Application:**
- In case of unanimity
- Uncontested elections
- Re-elections without an opposing candidate

**Example:** re-election of a committee president without an opposing candidacy

## Assignment to agenda items

Every election is assigned to an agenda item:

```
AgendaItem (election of the Federal Council)
  └─ Election (election for department XY)
      ├─ Candidate A: 120 votes
      ├─ Candidate B: 75 votes
      └─ Blank ballots: 5
```

## Description and title

- **title**: title of the election (e.g. "Election of the WAK committee presidency")
- **description**: detailed description, context, special circumstances

## Election result

The field **result** records the result:

- **elected**: person(s) elected
- **not_elected**: no person elected (e.g. absolute majority not reached)
- **deferred**: election postponed
- **withdrawn**: election withdrawn

## Elected person(s)

The field **elected_person_id** contains the ID(s) of the elected person(s) according to eCH-0294 Actors.

In case of multiple elections (e.g. election of several committee members at once) several IDs can be recorded.

## Distribution of votes

In open elections or after publication of the results:

- **total_votes**: total number of votes cast
- **valid_votes**: valid votes
- **invalid_votes**: invalid votes
- **blank_votes**: blank ballots

Additionally details per candidate (via separate entities or as structured data).

## Election procedure

The field **procedure** describes the concrete procedure:

- **written_ballot**: written election with voting slips
- **electronic**: electronic election
- **show_of_hands**: show of hands (in open elections)
- **acclamation**: acclamation (in tacit elections)

## Majority requirements

The field **majority_type** defines the required majority:

### absolute
Absolute majority (more than half of those voting)

**Application:**
- Federal Council election
- Election of committee presidencies
- Standard case for elections of persons

**Example:** with 200 votes cast at least 101 votes are required

**Particularity:** if nobody reaches the absolute majority in the first round, a second round usually follows in which a simple majority suffices.

### simple
Simple majority (more votes than the other candidates)

**Application:**
- Second round after an unsuccessful first round
- Some committee elections

### qualified
Qualified majority

**Application:**
- Rarer in elections
- Special functions with increased requirements

## Rounds of voting

In elections requiring an absolute majority in the first round:

```
1st round (absolute majority required)
   └─ No candidate reaches the absolute majority

2nd round (simple majority suffices)
   └─ Candidate A elected
```

Every round is recorded as a separate Election entity, connected via the common agenda item.

## Timestamps

- **datetime_created**: point in time of conducting the election
- **datetime_modified**: last update

## URL and documentation

- **url**: multilingual URLs to election documents:
  - candidate profiles
  - election results
  - protocols

## Particularities of the various elections

### Federal Council election
- Secret election
- Absolute majority required (in the 1st round)
- By the United Federal Assembly

### Federal judge election
- Secret election
- Proportional principle (consideration of parties, regions, genders)

### Committee presidencies
- Election by the respective parliament
- Often less public

### Cantonal and communal level
- Great variety of election procedures
- Partly popular election instead of parliamentary election
- Differing majority requirements

## Transparency and confidentiality

Field of tension:
- **Secrecy of the ballot**: protection of the individual electoral decision
- **Transparency**: public interest in the election result

In secret elections:
- Only the overall result is published
- No IndividualVote entities
- Protection of the freedom of choice

In open elections:
- Individual votes cast can be recorded
- Higher transparency
- Potential social pressure effects



## Class: Election []{#Election}


_An election procedure for selecting persons to positions._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| datetime_begin | 0..1 <br/> Datetime | The date and time when the meeting or voting begins.  |
| datetime_end | 0..1 <br/> Datetime | The date and time when the meeting or voting ends.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](#ElectionTypeEnum) | Type of election procedure.  |
| type_label | 0..1 <br/> String | Custom type label when standard type values don't apply.  |
| title | 0..1 <br/> String | Title of the element.  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| total_absent | 0..1 <br/> Integer | Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list.  |
| total | 0..1 <br/> Integer | Total number of votes, excluding absent and president's vote.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](#MajorityTypeEnum) | Type of majority required for the vote (absolute, two-thirds, etc.).  |
| majority_count | 0..1 <br/> Integer | Number of votes required for the relevant majority threshold.  |
| result_text | 0..1 <br/> String | Free text describing the outcome of the vote, e.g., "Accepted with 78 votes".  |
| parent_meeting | 0..1 <br/> String | The linked meeting ID that groups the current meeting.  |
| parent_agenda_item | 0..1 <br/> String | If needed, this slot builds a hierarchy of agenda items.  |
| affair_id | 0..1 <br/> String | The connection to the affairs (business items) of the agenda item.  |
| actor_id | 0..1 <br/> [GroupReference](#GroupReference) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | elections | range | [Election](#Election) |



















</div>

## Enum: ElectionTypeEnum []{#ElectionTypeEnum}




_Type of election procedure._




<div data-search-exclude markdown="1">

URI: [ops:ElectionTypeEnum](https://ch.paf.link/schema/operations/ElectionTypeEnum)

### Permissible Values
| Value | Description |
|------------------------|----------------------------------------------------------------------------|
| secret |  Secret election (Geheime Wahl)  |
| | [ops:enum/election_type/secret](ops:enum/election_type/secret) |
| open |  Open election (Offene Wahl)  |
| | [ops:enum/election_type/open](ops:enum/election_type/open) |
| silent |  Silent election without opponent (Stille Wahl ohne Gegenkandidat)  |
| | [ops:enum/election_type/silent](ops:enum/election_type/silent) |







</div>

\newpage

<!-- ToDo: David -->


Debate

* -> video recording -> speech transcript
*   -> verbatim protocol -> text to timestamp -> text contains the timestamps -> text document (with or without a definition of the format (span types))
*   -> edited protocol -> agenda item to timestamp

## Speech

## Term and meaning

A speech denotes an oral contribution by a person during a parliamentary sitting. It is the central instrument of political debate and of expressing opinions in parliament.

## Types of speeches

Parliamentary speeches take various forms:

### Main statements
- Detailed positions on an affair
- Justification of motions
- Presentation of the group's opinion

### Short interventions
- Brief statements
- Interposed questions
- Corrections

### Group declarations
- Official position of a parliamentary group
- Delivered by the group's spokesperson

### Government statements
- Positions of government members
- Answering of questions
- Defence of bills

## Structure and assignment

A speech is always assigned to a specific context:

```
Meeting (sitting)
  └─ AgendaItem
      └─ Speech (statement of person A)
          ├─ TextSegment (transcription)
          ├─ Media (audio recording)
          └─ Media (video recording)
```

### Assignment fields

- **meeting_id**: the sitting in which the speech was made
- **agenda_item_id**: the agenda item that was spoken to
- **person_id**: the speaking person (according to eCH-0294 Actors)

## Identification of the speakers

- **person_id**: unique identification of the person
- **person_name**: name for quick access
- **role**: role of the person (e.g. "group president", "rapporteur", "Federal Councillor")

## Temporal recording

- **start_time**: start of the speech
- **end_time**: end of the speech
- **duration**: duration in seconds (calculated or recorded)

These time indications enable:
- precise referencing in audio and video recordings
- analysis of speaking time per person / group
- monitoring of compliance with time limits

## Language of the speech

The field **language** records the language in which the speech was made:

- **de**: German
- **fr**: French
- **it**: Italian
- **rm**: Romansh
- **en**: English

## Text documents

The field **text_segments** references TextSegment entities containing the spoken text.

### Different text versions

#### Raw transcript
- Verbatim transcription
- Unedited, with filler words
- Available directly after the sitting

#### Edited transcript
- Editorially revised
- Grammatically corrected
- Official protocol version

#### Translations
- Into other national languages
- For international publications

### TextSegment structure

Every TextSegment can contain:
- **text**: the actual text
- **language**: language of the text
- **version**: kind of version (raw, edited, translated)
- **format**: format (plain, markdown, HTML)

## Multimedia recordings

The field **media** references Media entities with audio and video recordings.

### Audio recordings
- Original sound of the speech
- Format: MP3, WAV, etc.
- Technical metadata (quality, bitrate)

### Video recordings
- Visual recording (in plenary sittings)
- Format: MP4, WebM, etc.
- Various resolutions

### Livestreaming
- Real-time transmission
- URL of the stream
- Archiving after the sitting

## Title and description

- **title**: short title (e.g. "Statement on energy policy")
- **description**: summary or context of the speech

## Type of speech

The field **speech_type** can distinguish various kinds:

- **statement**: position statement
- **question**: question
- **response**: answer (e.g. government to a question)
- **procedural**: procedural motion
- **declaration**: declaration



## Class: Speech []{#Speech}


_A speech or statement made during a meeting (also called Votum or speaker segment)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| language | 0..1 <br/> String | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |
| start | 0..1 <br/> String | Start indicator or position.  |
| datetime_begin | 0..1 <br/> Datetime | The date and time when the meeting or voting begins.  |
| datetime_end | 0..1 <br/> Datetime | The date and time when the meeting or voting ends.  |
| actor_fullname | 0..1 <br/> String | Full name of the actor/person.  |
| actor_id | 0..1 <br/> [PersonReference](#PersonReference) | Reference to the acting person (lightweight snapshot at time of linking).  |
| role | 0..1 <br/> String | Role of the person (e.g., commission speaker).  |
| text | 1 <br/> String | Text content of the element.  |
| text_format | 0..1 <br/> String | Format of text (text, html, html_with_timestamps).  |
| text_type | 0..1 <br/> String | Type of text (raw draft, edited version).  |
| landing_page | 0..1 <br/> String | URL providing further information.  |
| media_url | 0..1 <br/> String | URL to media file (audio/video).  |
| media_type | 0..1 <br/> String | Type of media (audio, video, document).  |
| media_format | 0..1 <br/> String | MIME type of the media file.  |
| documents | * <br/> Work | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> Date | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](#Container) | speeches | range | [Speech](#Speech) |
| [Protocol](#Protocol) | speeches | range | [Speech](#Speech) |














### Examples
#### Example Speech: Speech with verbatim text and video recording

```yaml
speeches:
- global_uri: ops:366631
  language: fr
  datetime_begin: '2025-12-19T09:20:00+01:00'
  datetime_end: '2025-12-19T09:25:00+01:00'
  actor_fullname: Pascal Broulis
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/18682
    wikidata_uri: http://www.wikidata.org/entity/Q116407
    label: Pascal Broulis
  role: speaker
  text: >-
    Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec
    attention les différents commentaires qui ont été effectués sur mon postulat.
    Cela reste un postulat, ce n'est pas une motion. D'abord, je ne partage pas l'avis
    selon lequel ce postulat n'apporterait pas une valeur ajoutée. En effet, un "benchmark",
    à savoir un modèle chiffré de performance, permettrait de mieux comprendre les
    raisons des retards que notre pays rencontre en comparaison avec les principaux
    pays européens.
  text_format: html
  text_type: final
  landing_page: >-
    https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631
  media_url: https://par-pcache.simplex.tv/content?externalid=366631
  media_type: video
  media_format: video/mp4

```






</div>


# Texts and media

Parliamentary debates are recorded not only as structured data but also as texts and multimedia recordings. These entities enable the management of transcripts, audio and video recordings and further media formats, as well as the technical infrastructure for data exchange and multilingualism.

## TextSegment

### Purpose
Records text passages with versioning and language variants. Used primarily for transcriptions of speeches, but can also be applied to other text documents.

### Structure
- **text**: the actual text content
- **language**: language code (ISO 639-1)
- **format**: format of the text (plain, markdown, html)
- **version_type**: kind of version
  - **raw**: unedited raw transcript
  - **edited**: editorially revised version
  - **translated**: translation into another language
  - **summary**: summary

### Design decision
**Why a separate entity?**
- Allows several versions of the same text (raw, edited, translated)
- Version control and traceability of changes
- Flexibility regarding formats (plain, markdown, HTML for different output channels)

### Application
Mainly linked with Speech entities:
```
Speech
  ├─ TextSegment (raw transcript, de)
  ├─ TextSegment (edited protocol, de)
  ├─ TextSegment (translation, fr)
  └─ TextSegment (summary, de)
```

## Media

### Purpose
References media files (audio, video, documents) belonging to parliamentary activities.

### Structure
- **media_type**: kind of media file
  - **audio**: audio recording
  - **video**: video recording
  - **document**: documents (PDF, etc.)
  - **image**: images
- **url**: URL of the media file
- **mime_type**: MIME type (audio/mp3, video/mp4, application/pdf, etc.)
- **title**: title of the media file
- **description**: description
- **language**: language (for language-based media)
- **duration**: duration (for audio/video, in seconds)
- **file_size**: file size in bytes
- **quality**: quality indication (e.g. "720p", "high", "low")

### Design decision
**Why a generic Media entity?**
- Uniform structure for all media types
- Extensible for new formats
- Technical metadata recorded centrally
- Several quality levels of the same recording possible

### Application
Can be attached to various entities:
```
Speech
  ├─ Media (audio recording, MP3, 256 kbps)
  ├─ Media (audio recording, MP3, 128 kbps)
  ├─ Media (video recording, MP4, 1080p)
  └─ Media (video recording, MP4, 480p)

AgendaItem
  └─ Media (PDF of the bill)

Meeting
  └─ Media (livestream URL)
```



## Class: TextSegment []{#TextSegment}


_A text segment such as cross-references or subtitles in meeting protocols._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| text | 1 <br/> String | Text content of the element.  |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Protocol](#Protocol) | text_segments | range | [TextSegment](#TextSegment) |



















</div>



## Class: Media []{#Media}


_Media files or documents (including protocols in PDF/HTML/WORD or links to audio/video)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| title | 0..1 <br/> String | Title of the element.  |
| media_type | 0..1 <br/> String | Type of media (audio, video, document).  |
| url | * <br/> [MultilingualString](#MultilingualString) | Landing page or further web address, multilingual.  |
| version | 0..1 <br/> String | Version number or identifier.  |
| parent_type | 0..1 <br/> String | Type of parent object (meeting, agenda, speech, affair).  |






















</div>



## Class: MultilingualString []{#MultilingualString}


_A string that can contain text in multiple languages._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| text | 1 <br/> String | Text content of the element.  |
| language | 1 <br/> String | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Legislature](#Legislature) | name | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | name | range | [MultilingualString](#MultilingualString) |
| [Session](#Session) | url | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | name | range | [MultilingualString](#MultilingualString) |
| [Meeting](#Meeting) | url | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | agenda_item_title | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | agenda_item_description | range | [MultilingualString](#MultilingualString) |
| [AgendaItem](#AgendaItem) | url | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | agenda_item_title | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | agenda_item_description | range | [MultilingualString](#MultilingualString) |
| [ProtocolItem](#ProtocolItem) | url | range | [MultilingualString](#MultilingualString) |
| [Voting](#Voting) | voting_title | range | [MultilingualString](#MultilingualString) |
| [IndividualAttendance](#IndividualAttendance) | reason | range | [MultilingualString](#MultilingualString) |
| [Media](#Media) | url | range | [MultilingualString](#MultilingualString) |



















</div>



## Class: Container []{#Container}


_Container for the records of public council operations: legislatures, sessions, meetings, agenda items, protocols, votings, elections, attendances, speeches and resolutions._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| legislatures | * <br/> [Legislature](#Legislature) | Collection of legislature records.  |
| sessions | * <br/> [Session](#Session) | Collection of session records.  |
| meetings | * <br/> [Meeting](#Meeting) | Collection of meeting records.  |
| agenda_items | * <br/> [AgendaItem](#AgendaItem) | Collection of agenda item records.  |
| protocols | * <br/> [Protocol](#Protocol) | Collection of protocol records.  |
| votings | * <br/> [Voting](#Voting) | Collection of voting records.  |
| elections | * <br/> [Election](#Election) | Collection of election records.  |
| individual_votes | * <br/> [IndividualVote](#IndividualVote) | Collection of individual vote records.  |
| attendances | * <br/> [Attendance](#Attendance) | Collection of attendance records.  |
| individual_attendances | * <br/> [IndividualAttendance](#IndividualAttendance) | Collection of individual attendance records.  |
| speeches | * <br/> [Speech](#Speech) | Collection of speech records.  |
| resolutions | * <br/> [Resolution](#Resolution) | Collection of resolution records.  |

















### Examples
#### Example Container: meeting

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
#### Example Container: meeting sr winter25 Sitzung6

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
      wikidata_uri: "http://www.wikidata.org/entity/Q116407"
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
#### Example Container: meeting complete

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
#### Example Container: meeting item

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
#### Example Container: voting

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
#### Example Container: session

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






</div>

\newpage

# Shared elements

## Reference classes

`PersonReference` and `GroupReference` name a person or a group without describing them here: what a person or a body is, is defined by eCH-0294; council operations merely point to it. Besides the pointer, the reference retains the key characteristics **at the time of linking** — for a speech, for instance, the parliamentary group the speaker belonged to back then.

This serves three purposes:

- **Useful local data** without costly queries of the complete entity
- **No redundancy**, since not all information has to be repeated at every mention
- **Implicit versioning**, as the reference stays unchanged even if the linked person or group changes later

Unlike an entity, a reference is not identified in its own right — it merely names an identified entity. That is why `global_uri` is not mandatory here: all that is required is that at least one of `local_id` or `global_uri` is set. A system that only knows the local id of the referenced entity states that; it is resolved within the same delivery. Beyond the delivery, the `global_uri` does the pointing.



## Class: PersonReference []{#PersonReference}


_Lightweight reference to a person with key identification data at time of linking. Preserves historical accuracy even if the person changes later. The referenced person is identified by `local_id` or `global_uri`; at least one of the two is required._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier of the referenced entity. It is resolved within the same delivery. <br/><br/>Inheritance: HasReferenceIdentification |
| global_uri | 0..1 <br/> Uriorcurie | The unique, globally valid URI of the referenced entity. Unlike a local_id it also resolves beyond the delivery. <br/><br/>Inheritance: HasReferenceIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: HasReferenceIdentification |
| label | 1 <br/> String | Mandatory short display name to identify the person within the organisation (e.g. with added birth year to distinguish persons with the same name).  |
| label_long | 0..1 <br/> String | Optional long display name including academic titles and full official name (e.g. "Dr. Maria Muster-Beispiel").  |
| group_label | 0..1 <br/> String | Name of the body/group at time of linking.  |

##### Constraints


At least one of the following must be set:

- local_id
- global_uri










### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [IndividualVote](#IndividualVote) | actor_id | range | [PersonReference](#PersonReference) |
| [IndividualAttendance](#IndividualAttendance) | actor_id | range | [PersonReference](#PersonReference) |
| [Speech](#Speech) | actor_id | range | [PersonReference](#PersonReference) |



















</div>



## Class: GroupReference []{#GroupReference}


_Lightweight reference to a group with key identification data at time of linking. The referenced group is identified by `local_id` or `global_uri`; at least one of the two is required. A `local_id` is resolved within the same delivery, a `global_uri` also beyond it._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier of the referenced entity. It is resolved within the same delivery. <br/><br/>Inheritance: HasReferenceIdentification |
| global_uri | 0..1 <br/> Uriorcurie | The unique, globally valid URI of the referenced entity. Unlike a local_id it also resolves beyond the delivery. <br/><br/>Inheritance: HasReferenceIdentification |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: HasReferenceIdentification |
| label | 0..1 <br/> String | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| abbreviation | * <br/> MultilingualValue | Abbreviation (can be multilingual).  |

##### Constraints


At least one of the following must be set:

- local_id
- global_uri










### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Legislature](#Legislature) | actor_id | range | [GroupReference](#GroupReference) |
| [Meeting](#Meeting) | group_id | range | [GroupReference](#GroupReference) |
| [Meeting](#Meeting) | actor_id | range | [GroupReference](#GroupReference) |
| [Voting](#Voting) | actor_id | range | [GroupReference](#GroupReference) |
| [Election](#Election) | actor_id | range | [GroupReference](#GroupReference) |
| [Attendance](#Attendance) | actor_id | range | [GroupReference](#GroupReference) |



















</div>

## Mixin classes

Three classes carry no data of their own; they bundle slots that look the same across many classes — the identification of an entity, its creation and modification dates, and the temporal course of an event with planned and actual start and end. They come from the specialist group's common schema (eCH-0292) and are imported by its standards so that the same information is named alike and behaves alike everywhere.

A mixin is not a superclass: no instance of a mixin class is ever created, and nothing of it shows in the data. The attribute tables of the classes therefore list the inherited slots individually and note their origin under "Inheritance" — the three sections below explain what stands behind that note.



## Class: HasIdentification []{#HasIdentification}


_A mixin class that provides slots for the identification of an entity. It is used for entities that are identified in their own right; their `global_uri` is the identifier and therefore mandatory._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> String | Local identifier. For example, a UUID from the council information system.  |
| global_uri | 1 <br/> Uriorcurie | A unique, globally valid URI for the entity.  |
| wikidata_uri | 0..1 <br/> Uriorcurie | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans.  |



### Mixin Usage

[Container](#Container), [Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem), [Protocol](#Protocol), [Voting](#Voting), [IndividualVote](#IndividualVote), [Election](#Election), [Attendance](#Attendance), [IndividualAttendance](#IndividualAttendance), [Speech](#Speech), [TextSegment](#TextSegment), [Motion](#Motion), [Media](#Media)





















</div>



## Class: HasCreationModificationDates []{#HasCreationModificationDates}


_A mixin class that provides slots for modeling creation and modification dates of an entity._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| date_created | 0..1 <br/> Date | The date when an entity was created.  |
| datetime_created | 0..1 <br/> Datetime | The date and time when an entity was created.  |
| date_modified | 0..1 <br/> Date | The date when an entity was last modified.  |
| datetime_modified | 0..1 <br/> Datetime | The date and time when an entity was last modified.  |



### Mixin Usage

[Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem), [Protocol](#Protocol), [Voting](#Voting), [IndividualVote](#IndividualVote), [Election](#Election), [Attendance](#Attendance), [IndividualAttendance](#IndividualAttendance), [Speech](#Speech)





















</div>



## Class: IsEventWithDuration []{#IsEventWithDuration}


_A mixin class that provides slots for modeling events or occurrences with time duration._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| date_begin_actual | 0..1 <br/> Date | The actual start date of an event or occurrence with time duration.  |
| datetime_begin_actual | 0..1 <br/> Datetime | The actual start date and time of an event or occurrence with time duration.  |
| date_begin_planned | 0..1 <br/> Date | The planned start date of an event or occurrence with time duration.  |
| datetime_begin_planned | 0..1 <br/> Datetime | The planned start date and time of an event or occurrence with time duration.  |
| date_end_actual | 0..1 <br/> Date | The actual end date of an event or occurrence with time duration.  |
| datetime_end_actual | 0..1 <br/> Datetime | The actual end date and time of an event or occurrence with time duration.  |
| date_end_planned | 0..1 <br/> Date | The planned end date of an event or occurrence with time duration.  |
| datetime_end_planned | 0..1 <br/> Datetime | The planned end date and time of an event or occurrence with time duration.  |



### Mixin Usage

[Legislature](#Legislature), [Session](#Session), [Meeting](#Meeting), [AgendaItem](#AgendaItem)





















</div>

\newpage

# Appendix A – References & bibliography

Where a version is stated, it is the one this standard was developed against.

## Standards of the "Political Affairs" specialist group

The standards of the specialist group are developed jointly and reference one another. All of them currently carry the status "In Arbeit" (in progress; as of 10 August 2026); no version is therefore stated.

| | |
|------------------|----------------------------------------------------------------------------------|
|eCH-0292|eCH-0292: Meta-processes for political affairs – shared data elements, from which this standard takes the reference classes and the mixins: [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|eCH-0294|eCH-0294: Political actors – defines the persons and groups that `PersonReference` and `GroupReference` point to: [https://www.ech.ch/de/ech/ech-0294](https://www.ech.ch/de/ech/ech-0294)|
|eCH-0295|eCH-0295: Parliamentary affairs – the affairs dealt with in agenda items, votings and speeches: [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|eCH-0296|eCH-0296: Legal acts and legislative texts: [https://www.ech.ch/de/ech/ech-0296](https://www.ech.ch/de/ech/ech-0296)|
|eCH-0297|eCH-0297: Public consultations: [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Code lists and further sources

| | |
|------------------|----------------------------------------------------------------------------------|
|ISO 639-1|ISO (International Organization for Standardization). Language codes, used in the `language` slot of `MultilingualString`.|
|Dublin Core|DCMI Metadata Terms. Source of several `slot_uri` assignments (prefix `dcterms`): [https://www.dublincore.org/specifications/dublin-core/dcmi-terms/](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)|
|LinkML|Modelling language in which this standard is defined: [https://linkml.io](https://linkml.io)|

