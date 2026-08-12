\newpage

# Attendance

Attendance lists record who took part in a sitting. They document participation and are the basis on which a body's capacity to take decisions can be assessed.

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
