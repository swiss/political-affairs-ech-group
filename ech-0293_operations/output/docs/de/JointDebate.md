

## Klasse: JointDebate 


_Eine gemeinsame Beratung: Mehrere Traktanden werden zusammen behandelt, etwa inhaltlich zusammenhängende Geschäfte, die in einer einzigen Debatte beraten werden. Die gemeinsame Beratung hängt an einem Traktandum (AgendaItem), einem Protokoll-Traktandum (ProtocolItem), einer Sitzung (Meeting) oder einer Session (Session) und verweist über deren Identifikatoren auf die gemeinsam behandelten Traktanden. An einer Sitzung oder Session angehängt, kann sie auch Traktanden zusammenfassen, die auf mehrere Traktandenpositionen oder Sitzungen verteilt sind._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| joint_agenda_item_ids | * <br/> [String](String.md) | Identifikatoren der gemeinsam behandelten Traktanden (AgendaItem oder ProtocolItem).  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Session](Session.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [Meeting](Meeting.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [IsAgendaItem](IsAgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [AgendaItem](AgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [ProtocolItem](ProtocolItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |



















</div>