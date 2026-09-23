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

The legislature forms the long-term frame, the session structures the work within a legislature, the meeting is the concrete sitting in which affairs are deliberated, and the agenda item structures the individual sitting. The levels interlock in two ways: downwards they are embedded — the session takes up its sittings (`meetings`), sitting and session their agenda items (`agenda_items`); upwards, references point — the session to its legislature (`parent_legislature`), the sitting to its session (`parent_session`) or, where there is no session, directly to the legislature (`parent_legislature`). Within the agenda, `parent_agenda_item` represents the division into sub-items.

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

{{include:ech-0293_operations/output/docs/Session.md}}

## Meeting (individual sitting)

A meeting is the individual sitting of a body — the level at which agenda items are deliberated, decisions taken and speeches recorded.

{{include:ech-0293_operations/output/docs/Meeting.md}}

{{include:ech-0293_operations/output/docs/StateEnum.md}}
