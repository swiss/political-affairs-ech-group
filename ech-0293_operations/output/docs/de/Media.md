

## Klasse: Media 


_Mediendateien oder Dokumente (einschliesslich Protokolle in PDF/HTML/WORD oder Links zu Audio/Video)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| title | 0..1 <br/> [String](String.md) | Titel des Elements.  |
| media_type | 0..1 <br/> [String](String.md) | Art des Mediums (Audio, Video, Dokument).  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing Page oder weiterführende Webadresse, mehrsprachig.  |
| version | 0..1 <br/> [String](String.md) | Versionsnummer oder Versionskennung.  |
| parent_type | 0..1 <br/> [String](String.md) | Typ des übergeordneten Objekts (Sitzung, Traktandum, Wortmeldung, Geschäft).  |






















</div>