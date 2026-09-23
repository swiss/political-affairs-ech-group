

## Class: JointDebate 


_A joint debate: several agenda items are deliberated together. The joint debate hangs on an agenda item (AgendaItem) or a protocol item (ProtocolItem) and references the items debated jointly with it by their identifiers._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| joint_agenda_item_ids | * <br/> [String](String.md) | Identifiers of the agenda items (AgendaItem or ProtocolItem) debated jointly.  |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [AgendaItem](AgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [ProtocolItem](ProtocolItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |



















</div>