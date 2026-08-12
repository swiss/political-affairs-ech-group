\newpage

<!-- ToDo: Christian -->

# Temporal organisation of council operations

Council operations are structured in time by four classes:

```
Legislature (legislature)
  └─ Session (e.g. spring session)
      └─ Meeting (individual sitting)
          └─ AgendaItem (agenda item)
```

The legislature forms the long-term frame, the session structures the work within a legislature, the meeting is the concrete sitting in which affairs are deliberated, and the agenda item structures the individual sitting. The levels interlock in two ways: the session takes its sittings as a list (`meetings`), while sitting and agenda item point upwards by reference (`parent_legislature`, `parent_meeting`, `parent_agenda_item`). Those who keep no sessions deliver their sittings individually and attach them to the legislature via `parent_legislature`.

The first three classes are described below, the agenda item in the next chapter.

## Common elements

The three classes are deliberately built alike. The following fields have the same meaning on all levels.

**Identification.** `global_uri` is the identifier and is mandatory. `local_id` takes the id of the delivering system, `wikidata_uri` points to the Wikidata entry where one exists.

**Begin and end.** The temporal data is recorded twice: `date_begin_planned` and `date_end_planned` hold what was scheduled, `date_begin_actual` and `date_end_actual` what actually happened. Where the time of day matters, the `datetime_*` variants are available.

**Space and body.** `spatial` points to the spatial unit according to LINDAS — country, canton, district or commune, thus `https://ld.admin.ch/canton/2` rather than "BE". It is the same field with which eCH-0294 locates its groups, so that council operations and the actors who carry them point to the same resource. Who convenes within that spatial unit is stated by `actor_id`, a lightweight reference to the body according to eCH-0294.

**Linked documents.** `documents` links documents as FRBR works according to eCH-0292 — for the legislature, for instance, membership and affair registers, for the session the session programme, for the meeting the protocol.

## Legislature

A legislature denotes the period for which a parliament is elected and acts in its current composition.

### Duration and course

The duration is not prescribed — the examples show a four-year and a five-year term. Unlike at the sitting level, planning and actual course hardly diverge here; where a legislature is fixed to the day by law, `*_planned` and `*_actual` carry the same dates.

{{include:ech-0293_operations/output/docs/Legislature.md}}

## Session (sitting period)

A session is a continuous sitting period in which several meetings take place.

### Optional level

The session is the only one of the three levels that may be dispensed with: federal entities without formal sessions leave it out and record their sittings directly. Session and meeting may also coincide — a one-day sitting of a cantonal parliament or a Landsgemeinde is recorded as a sitting period with a single meeting.

### Numbering

Numbering practice differs widely, which is why four fields are available: `number` holds the running number as a figure, `sequential_number` the same information as a string (and therefore also Roman numerals), `position` the position within the legislature and `meeting_abbreviation` a short designation such as "FS24". The meeting has the same four fields.

{{include:ech-0293_operations/output/docs/Session.md}}

## Meeting (individual sitting)

A meeting is the individual sitting of a body — the level at which agenda items are deliberated, decisions taken and speeches recorded.

### Meeting types

`meeting_type` distinguishes four types: `session` for plenary sittings of a parliament or a chamber, `committee` for committee sittings, `sitting` for assemblies such as Landsgemeinden, communal assemblies and citizens' communal assemblies, and `various` as a catch-all. The value `sitting` is a deliberate choice: Landsgemeinden and communal assemblies are assemblies of the eligible voters themselves, but they decide as a convened body with an agenda and are therefore represented like a council sitting.

### Planning and course

At this level, scheduled and actual times regularly diverge: a sitting scheduled for 14:00 only begins at 14:25 because of delays and ends at 17:30 instead of 18:00. Whether a sitting takes place as planned at all is held by `state` (`planned`, `canceled`, `postponed`); `state_name` takes a diverging, free-text status designation. `location` records the place of the sitting — the physical room ("Federal Palace, National Council chamber"), a video conference or a hybrid format.

### Anchor points

The meeting is the node to which the remaining classes of this standard attach: agenda items (`AgendaItem`), votings and elections (`Voting`, `Election`), speeches (`Speech`) as well as the attendance list (`Attendance.parent_meeting`). `documents` links sitting documents such as the bulletin or annexes, `protocol_ref` the protocol. `parent_meeting` represents sittings that are part of a superordinate sitting; `actor_name`, `group_name` and `group_id` additionally hold body and grouping in plain text.

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
