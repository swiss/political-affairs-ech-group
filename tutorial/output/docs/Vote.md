

## Class: Vote 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](String.md) | None |
| is_part_of | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | None |
| question | 1 <br/> [String](String.md) | None |
| datetime_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual date and time of an instantaneous event or occurrence (without time duration).  |
| result | 0..1 <br/> [ResultEnum](ResultEnum.md) | None |
| is_part_of_agenda_item | 0..1 <br/> [AgendaItem](AgendaItem.md) | None |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AgendaItem](AgendaItem.md) | [votes](votes.md) | range | [Vote](Vote.md) |
| [Container](Container.md) | [votes](votes.md) | range | [Vote](Vote.md) |



















</div>