

## Class: Resolution 


_A resolution or decision taken on an agenda item, including voting procedures._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](ResolutionTypeEnum.md) | Type of resolution taken on the agenda item.  |
| type_label | 0..1 <br/> [String](String.md) | Custom type label when standard type values don't apply.  |
| vote_procedures | * <br/> [String](String.md) | Procedures for voting, such as secret ballot or open vote.  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [resolutions](resolutions.md) | range | [Resolution](Resolution.md) |
| [AgendaItem](AgendaItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |
| [ProtocolItem](ProtocolItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |



















</div>