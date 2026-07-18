

## Klasse: ElectoralDistrict 


_Wahlkreis oder Wahlregion, die einer Mitgliedschaft zugeordnet ist. Die zeitliche Gültigkeit wird von der umschliessenden Mitgliedschaft übernommen._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 0..1 <br/> [String](String.md) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Für IRI-Referenzen sollen die LINDAS-Ressourcen verwendet werden. Die IRI für die verschiedenen Verwaltungsebenen der Schweizer Raumeinheiten sind bei LINDAS zu finden: https://ld.admin.ch/country/CHE. Unter den Links im Abschnitt schema:containsPlace kann die gewünschte Ebene gefunden werden. Beispiele für die einzelnen Verwaltungsebenen: - Land - Schweiz: https://ld.admin.ch/country/CHE - Kanton - Aargau: https://ld.admin.ch/canton/19 - Bezirk - Brig: https://ld.admin.ch/district/2301 - Gemeinde - Versoix: https://ld.admin.ch/municipality/6644 <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [electoral_district](electoral_district.md) | range | [ElectoralDistrict](ElectoralDistrict.md) |



















</div>