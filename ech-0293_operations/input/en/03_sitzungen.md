\newpage

<!-- ToDo: Christian -->

# Temporal organisation of council operations

Council operations are organised in time on three levels: legislatures form the long-term frame, sessions structure the work within a legislature, and meetings are the concrete sittings in which affairs are deliberated.

```
Legislature (legislature)
  └─ Session (e.g. spring session)
      └─ Meeting (individual sitting)
          └─ AgendaItem (agenda item)
```

The three classes are deliberately built alike: identification, temporal data, the link to the body and linked documents work identically on all three levels. These common conventions are described once, at the legislature; for session and meeting only the particularities of the respective level follow.

## Legislature

A legislature denotes the period for which a parliament is elected and acts in its current composition. Its duration is not prescribed — the examples at the end of this section show a four-year and a five-year term.

### Planned and actual

Begin and end are recorded twice: `date_begin_planned` and `date_end_planned` hold the planning, `date_begin_actual` and `date_end_actual` the actual course. Where the time of day matters, the `datetime_*` variants are available. For a legislature, planning and actual course usually coincide; the same fields apply unchanged to session and meeting, where they regularly diverge.

### Identification

`global_uri` is the identifier and is mandatory. `local_id` takes the id of the delivering system, `wikidata_uri` points to the Wikidata entry where one exists. This applies equally to session and meeting.

### Link to the body

`actor_id` points, as a lightweight reference, to the body according to eCH-0294 (e.g. National Council, cantonal parliament), `administrative_id` to the administrative unit for which that body acts (country, canton, commune). This pair recurs on the meeting.

### Linked documents

`documents` links documents as FRBR works according to eCH-0292 — for the legislature, for instance, membership and affair registers, for the session the session programme, for the meeting the protocol.

{{include:ech-0293_operations/output/docs/Legislature.md}}

## Session (sitting period)

A session is a continuous sitting period in which several meetings take place. It is the middle level — and it is optional: federal entities without formal sessions leave it out and record their meetings directly.

### Session or meeting?

The session is the period, the meeting the individual sitting within it:

```
Legislature (51st legislature)
  └─ Session (2024 spring session)
      ├─ Meeting (National Council sitting of 4 March 2024)
      ├─ Meeting (Council of States sitting of 4 March 2024)
      └─ ...
```

Both levels may coincide: a one-day sitting of a cantonal parliament or a Landsgemeinde is recorded as a sitting period with a single meeting — the examples show both cases.

### Numbering

Sessions are numbered, with widely differing practice: `number` holds the running number as a figure, `sequential_number` the same information as a string (and therefore also Roman numerals), `position` the position within the legislature and `meeting_abbreviation` a short designation such as "FS24". The meeting has the same four fields.

### Classification and links

`body_key` holds the body as a short key (e.g. "NR", "SR"), `parent_legislature` assigns the session to its legislature, `meetings` lists the sittings belonging to it, `url` points to the landing page.

{{include:ech-0293_operations/output/docs/Session.md}}

## Meeting (individual sitting)

A meeting is the individual sitting of a body — the level at which agenda items are deliberated, decisions taken and speeches recorded.

### Meeting types

`meeting_type` distinguishes four types: `session` for plenary sittings of a parliament or a chamber, `committee` for committee sittings, `sitting` for assemblies such as Landsgemeinden, communal assemblies and citizens' communal assemblies, and `various` as a catch-all. The value `sitting` is a deliberate choice: Landsgemeinden and communal assemblies are assemblies of the eligible voters themselves, but they decide as a convened body with an agenda and are therefore represented like a council sitting.

### Planning and reality

At the sitting level, planning and actual course regularly diverge: a sitting scheduled for 14:00 only begins at 14:25 because of delays and ends at 17:30 instead of 18:00. This is precisely what the `*_planned` and `*_actual` fields are for; for times of day, the `datetime_*` variants are to be used. Whether a sitting takes place as planned at all is held by `state` (`planned`, `canceled`, `postponed`); `state_name` takes a diverging, free-text status designation.

### Location

`location` records the place of the sitting — the physical room ("Federal Palace, National Council chamber"), a video conference or a hybrid format.

### Link to the body and classification

In addition to `actor_id` and `administrative_id`, `actor_name` holds the name of the body for quick access and `body_key` a short key; `group_name` and `group_id` supplement groupings where needed. `parent_meeting` represents sittings that are part of a superordinate sitting, `parent_legislature` assigns the sitting to the legislature. Numbering works as for the session.

### Anchor points

The meeting is the node to which the remaining classes of this standard attach: agenda items (`AgendaItem`), votings and elections (`Voting`, `Election`), speeches (`Speech`) as well as the attendance list (`Attendance.parent_meeting`). `documents` links sitting documents such as the bulletin or annexes, `protocol_ref` the protocol.

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
