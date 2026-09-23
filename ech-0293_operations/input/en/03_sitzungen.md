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

The legislature forms the long-term frame, the session structures the work within a legislature, the meeting is the concrete sitting in which affairs are deliberated, and the agenda item structures the individual sitting. The levels interlock in two ways: the session takes its sittings as a list (`meetings`), while sitting and agenda item point upwards by reference (`parent_legislature`, `parent_session`, `parent_meeting`, `parent_agenda_item`): the session refers to its legislature, the sitting to its session.

The first three classes are described below, the agenda item in the next chapter.

## Common elements

The three classes are deliberately built alike. The following fields have the same meaning on all levels.

**Identification.** `global_uri` is the identifier and is mandatory. `local_id` takes the id of the delivering system, `wikidata_uri` points to the Wikidata entry where one exists.

**Begin and end.** The temporal data is recorded twice: `date_begin_planned` and `date_end_planned` hold what was scheduled, `date_begin_actual` and `date_end_actual` what actually happened. Where the time of day matters, the `datetime_*` variants are available.

**Space and body.** `spatial` points to the spatial unit according to LINDAS — country, canton, district or commune, thus `https://ld.admin.ch/canton/2` rather than "BE". It is the same field with which eCH-0294 locates its groups, so that council operations and the actors who carry them point to the same resource. Who convenes within that spatial unit is stated by `actor_id`, a lightweight reference to the body according to eCH-0294.

**Linked documents.** `documents` links documents as FRBR works according to eCH-0292 — for the legislature, for instance, membership and affair registers, for the session the session programme, for the meeting the bulletin and annexes (the protocol, by contrast, via `has_protocol`).

## Legislature

A legislature denotes the period for which a parliament is elected and acts in its current composition.

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

{{include:ech-0293_operations/output/docs/Meeting.md}}

{{include:ech-0293_operations/output/docs/StateEnum.md}}
