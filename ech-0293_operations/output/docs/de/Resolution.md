

## Klasse: Resolution 


_Eine Resolution oder Entscheidung zu einem Traktandum, einschliesslich Abstimmungsverfahren._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](ResolutionTypeEnum.md) | Art der Resolution zum Traktandum.  |
| type_label | 0..1 <br/> [String](String.md) | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| vote_procedures | * <br/> [String](String.md) | Verfahren für die Abstimmung, wie geheime Abstimmung oder offene Abstimmung.  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [resolutions](resolutions.md) | range | [Resolution](Resolution.md) |
| [AgendaItem](AgendaItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |
| [ProtocolItem](ProtocolItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |



















</div>