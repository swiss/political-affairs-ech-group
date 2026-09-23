\newpage

<!-- ToDo: Michel -->

# Agenda, protocol and decisions

The agenda of a sitting is structured by agenda items; what was actually dealt with and decided is recorded in the protocol.

## AgendaItem

{{include:ech-0293_operations/output/docs/AgendaItem.md}}

{{include:ech-0293_operations/output/docs/AgendaItemTypeEnum.md}}

## Protocol

The protocol is **referenced, not embedded**. The rule this standard applies throughout therefore holds here as well — what has no identity of its own is embedded (`PersonReference` or `GroupReference`, say), what has one is referenced.

```
Container
  ├─ meetings       → Meeting
  │                     └─ has_protocol → identifier of the protocol
  ├─ agenda_items   → AgendaItem  (before: planned agenda items, parent_meeting)
  └─ protocols      → Protocol    (after: the record, parent_meeting)
                        ├─ protocol_items  → ProtocolItem (same elements as AgendaItem)
                        ├─ votings
                        ├─ elections
                        ├─ speeches
                        ├─ text_segments
                        └─ documents
```

{{include:ech-0293_operations/output/docs/Protocol.md}}

### ProtocolItem (agenda item as recorded)

{{include:ech-0293_operations/output/docs/ProtocolItem.md}}

## Joint debate (JointDebate)

{{include:ech-0293_operations/output/docs/JointDebate.md}}

## Resolution

{{include:ech-0293_operations/output/docs/Resolution.md}}

{{include:ech-0293_operations/output/docs/ResolutionTypeEnum.md}}

## Motion

{{include:ech-0293_operations/output/docs/Motion.md}}
