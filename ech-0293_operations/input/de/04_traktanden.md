\newpage

<!-- ToDo: Michel -->

# Tagesordnung (Traktandenliste), Protokoll und Beschlüsse

Die Tagesordnung einer Sitzung wird durch Traktanden strukturiert; was tatsächlich behandelt und beschlossen wurde, hält das Protokoll fest.

## AgendaItem (Traktandum)

{{include:ech-0293_operations/output/docs/AgendaItem.md}}

{{include:ech-0293_operations/output/docs/AgendaItemTypeEnum.md}}

## Protokoll (Protocol)

Das Protokoll wird **referenziert, nicht eingebettet**. Damit gilt auch hier die Regel, die dieser Standard durchgehend anwendet — eingebettet wird, was keine eigene Identität besitzt (etwa `PersonReference` oder `GroupReference`), referenziert wird, was eine besitzt.

```
Container
  ├─ meetings       → Meeting
  │                     └─ has_protocol → Identifikator des Protokolls
  ├─ agenda_items   → AgendaItem  (vorher: geplante Traktanden, parent_meeting)
  └─ protocols      → Protocol    (nachher: Niederschrift, parent_meeting)
                        ├─ protocol_items  → ProtocolItem (gleiche Elemente wie AgendaItem)
                        ├─ votings
                        ├─ elections
                        ├─ speeches
                        ├─ text_segments
                        └─ documents
```

{{include:ech-0293_operations/output/docs/Protocol.md}}

### ProtocolItem (protokolliertes Traktandum)

{{include:ech-0293_operations/output/docs/ProtocolItem.md}}

## Gemeinsame Beratung (JointDebate)

{{include:ech-0293_operations/output/docs/JointDebate.md}}

## Resolution (Beschluss)

{{include:ech-0293_operations/output/docs/Resolution.md}}

{{include:ech-0293_operations/output/docs/ResolutionTypeEnum.md}}

## Motion (Anträge)

{{include:ech-0293_operations/output/docs/Motion.md}}
