

## Class: Resolution 


_[en] A resolutionor decision taken on an agenda item, including voting procedures._

_[de] Eine Resolution oder Entscheidung zu einem Traktandum, einschließlich Abstimmungsverfahren._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](ResolutionTypeEnum.md) | [en] Type of resolutiontaken on the agenda item. [de] Art der Resolution zum Traktandum.  |
| type_label | 0..1 <br/> [String](String.md) | [en] Custom type label when standard type values don't apply. [de] Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| vote_procedures | * <br/> [String](String.md) | [en] Procedures for voting, such as secret ballot or open vote. [de] Verfahren für die Abstimmung, wie geheime Abstimmung oder offene Abstimmung.  |
| documents | * <br/> [Work](Work.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [resolutions](resolutions.md) | range | [Resolution](Resolution.md) |
| [AgendaItem](AgendaItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |
| [ProtocolItem](ProtocolItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |



















</div>