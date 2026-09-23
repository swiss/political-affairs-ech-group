\newpage

<!-- ToDo: Michel -->

# Ordre du jour, procès-verbal et décisions

L'ordre du jour d'une séance est structuré par des points de l'ordre du jour ; ce qui a effectivement été traité et décidé est consigné au procès-verbal.

## AgendaItem (point de l'ordre du jour)

{{include:ech-0293_operations/output/docs/AgendaItem.md}}

{{include:ech-0293_operations/output/docs/AgendaItemTypeEnum.md}}

## Procès-verbal (Protocol)

Le procès-verbal est **référencé et non imbriqué**. La règle appliquée de bout en bout par la présente norme vaut donc ici aussi : est imbriqué ce qui ne possède pas d'identité propre (par exemple `PersonReference` ou `GroupReference`), est référencé ce qui en possède une.

```
Container
  ├─ meetings       → Meeting
  │                     ├─ agenda_items → AgendaItem  (avant : points planifiés)
  │                     └─ has_protocol → identifiant du procès-verbal
  └─ protocols      → Protocol    (après : consignation, parent_meeting)
                        ├─ protocol_items  → ProtocolItem (mêmes éléments qu'AgendaItem)
                        ├─ votings
                        ├─ elections
                        ├─ speeches
                        ├─ text_segments
                        └─ documents
```

{{include:ech-0293_operations/output/docs/Protocol.md}}

### ProtocolItem (point consigné au procès-verbal)

{{include:ech-0293_operations/output/docs/ProtocolItem.md}}

## Délibération commune (JointDebate)

{{include:ech-0293_operations/output/docs/JointDebate.md}}

## Resolution (décision)

{{include:ech-0293_operations/output/docs/Resolution.md}}

{{include:ech-0293_operations/output/docs/ResolutionTypeEnum.md}}

## Motion (propositions)

{{include:ech-0293_operations/output/docs/Motion.md}}
