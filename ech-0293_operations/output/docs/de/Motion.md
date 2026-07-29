

## Klasse: Motion 


_Ein formeller Antrag, der während der Verhandlungen eingereicht wird._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| title | 0..1 <br/> [String](String.md) | Titel des Elements.  |
| description | 0..1 <br/> [String](String.md) | Beschreibender Text zum Element.  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |






















</div>