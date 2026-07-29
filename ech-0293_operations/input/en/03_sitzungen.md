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

{{include:ech-0293_operations/output/docs/Legislature.md}}

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

{{include:ech-0293_operations/output/docs/Session.md}}

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

{{include:ech-0293_operations/output/docs/Meeting.md}}

{{include:ech-0293_operations/output/docs/MeetingTypeEnum.md}}

{{include:ech-0293_operations/output/docs/StateEnum.md}}

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

{{include:ech-0293_operations/output/docs/Attendance.md}}

{{include:ech-0293_operations/output/docs/IndividualAttendance.md}}

{{include:ech-0293_operations/output/docs/AttendanceTypeEnum.md}}
