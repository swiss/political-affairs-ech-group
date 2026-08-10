

## Classe: MultilingualString 


_Une chaîne de caractères pouvant contenir du texte en plusieurs langues._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| text | 1 <br/> [String](String.md) | Contenu textuel de l'élément.  |
| language | 1 <br/> [String](String.md) | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »).  |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
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