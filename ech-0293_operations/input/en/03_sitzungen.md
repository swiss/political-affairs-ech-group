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
