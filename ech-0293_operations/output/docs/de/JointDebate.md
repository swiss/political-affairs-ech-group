

## Klasse: JointDebate 


_Eine gemeinsame Beratung: Mehrere Traktanden werden zusammen behandelt. Die gemeinsame Beratung hängt an einem Traktandum (AgendaItem) oder einem Protokoll-Traktandum (ProtocolItem) und verweist über deren Identifikatoren auf die gemeinsam behandelten Traktanden._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| joint_agenda_item_ids | * <br/> [String](String.md) | Identifikatoren der gemeinsam behandelten Traktanden (AgendaItem oder ProtocolItem).  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [AgendaItem](AgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [ProtocolItem](ProtocolItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |



















</div>