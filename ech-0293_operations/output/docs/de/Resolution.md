

## Klasse: Resolution 


_Der formale Beschluss zu einem Traktandum, einschliesslich der angewandten Abstimmungsverfahren. Er hält fest, was entschieden wurde, während Voting festhält, wie entschieden wurde (Verfahren und Stimmenverhältnis). Nicht jeder Beschluss beruht auf einer formalen Abstimmung: Kenntnisnahmen, stille Annahmen oder Administrativbeschlüsse kommen ohne eine solche zustande._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](ResolutionTypeEnum.md) | Art der Resolution zum Traktandum.  |
| type_label | 0..1 <br/> [String](String.md) | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| vote_procedures | * <br/> [String](String.md) | Verfahren, in denen abgestimmt wurde. Offene Verfahren: Handzeichen, Aufstehen, elektronische Abstimmung, Namensaufruf, in Krisenlagen zudem externe Stimmabgabe (vorgängig dem Präsidium mitgeteilte Stimmen, die zusammen mit der Abstimmung im Rat erfasst werden), Zirkulationsverfahren oder Stimmabgabe an virtuellen Sitzungen. Geheime Verfahren: Stimmzettel, elektronische geheime Abstimmung. Das Verfahren bestimmt, ob Einzelstimmen erfasst werden können.  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [resolutions](resolutions.md) | range | [Resolution](Resolution.md) |
| [IsAgendaItem](IsAgendaItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |
| [AgendaItem](AgendaItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |
| [ProtocolItem](ProtocolItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |



















</div>