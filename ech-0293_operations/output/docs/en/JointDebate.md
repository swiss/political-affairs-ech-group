

## Class: JointDebate 


_A joint debate: several agenda items are deliberated together, for instance substantively related affairs dealt with in a single debate. The joint debate hangs on an agenda item (AgendaItem), a protocol item (ProtocolItem), a meeting (Meeting) or a session (Session) and references the items debated jointly by their identifiers. Attached to a meeting or a session, it can also bring together agenda items that are distributed over several agenda positions or meetings._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| joint_agenda_item_ids | * <br/> [String](String.md) | Identifiers of the agenda items (AgendaItem or ProtocolItem) debated jointly.  |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Session](Session.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [Meeting](Meeting.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [IsAgendaItem](IsAgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [AgendaItem](AgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [ProtocolItem](ProtocolItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |



















</div>