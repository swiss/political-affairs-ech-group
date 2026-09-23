

## Class: Resolution 


_The formal decision taken on an agenda item, including the voting procedures applied. It records what was decided, whereas Voting records how it was decided (procedure and vote ratio). Not every decision rests on a formal vote: noting a report, tacit acceptance or administrative decisions come about without one._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](ResolutionTypeEnum.md) | Type of resolution taken on the agenda item.  |
| type_label | 0..1 <br/> [String](String.md) | Custom type label when standard type values don't apply.  |
| vote_procedures | * <br/> [String](String.md) | Procedures by which the vote was taken. Open procedures: show of hands, standing, electronic voting, roll call, and in crisis situations remote voting (votes communicated to the presidency beforehand and recorded together with the vote in the chamber), circulation procedure or voting in virtual sittings. Secret procedures: secret ballot with ballot papers, electronic secret voting. The procedure determines whether individual votes can be recorded.  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [resolutions](resolutions.md) | range | [Resolution](Resolution.md) |
| [IsAgendaItem](IsAgendaItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |
| [AgendaItem](AgendaItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |
| [ProtocolItem](ProtocolItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |



















</div>