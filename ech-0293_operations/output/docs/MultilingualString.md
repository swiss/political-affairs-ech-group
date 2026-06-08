

## Class: MultilingualString 


_[en] A string that can contain text in multiple languages._

_[de] Ein String, der Text in mehreren Sprachen enthalten kann._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| text | 1 <br/> [String](String.md) | None |
| language | 1 <br/> [String](String.md) | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Legislature](Legislature.md) | [name](name.md) | range | [MultilingualString](MultilingualString.md) |
| [Session](Session.md) | [name](name.md) | range | [MultilingualString](MultilingualString.md) |
| [Session](Session.md) | [url](url.md) | range | [MultilingualString](MultilingualString.md) |
| [Meeting](Meeting.md) | [name](name.md) | range | [MultilingualString](MultilingualString.md) |
| [Meeting](Meeting.md) | [url](url.md) | range | [MultilingualString](MultilingualString.md) |
| [AgendaItem](AgendaItem.md) | [agenda_item_title](agenda_item_title.md) | range | [MultilingualString](MultilingualString.md) |
| [AgendaItem](AgendaItem.md) | [agenda_item_description](agenda_item_description.md) | range | [MultilingualString](MultilingualString.md) |
| [AgendaItem](AgendaItem.md) | [url](url.md) | range | [MultilingualString](MultilingualString.md) |
| [ProtocolItem](ProtocolItem.md) | [agenda_item_title](agenda_item_title.md) | range | [MultilingualString](MultilingualString.md) |
| [ProtocolItem](ProtocolItem.md) | [agenda_item_description](agenda_item_description.md) | range | [MultilingualString](MultilingualString.md) |
| [ProtocolItem](ProtocolItem.md) | [url](url.md) | range | [MultilingualString](MultilingualString.md) |
| [Voting](Voting.md) | [voting_title](voting_title.md) | range | [MultilingualString](MultilingualString.md) |
| [IndividualAttendance](IndividualAttendance.md) | [reason](reason.md) | range | [MultilingualString](MultilingualString.md) |
| [Media](Media.md) | [url](url.md) | range | [MultilingualString](MultilingualString.md) |



















</div>