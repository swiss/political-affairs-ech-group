

## Klasse: GroupReference 


_Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 0..1 <br/> [String](String.md) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abkürzung (kann mehrsprachig sein).  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [group_reference](group_reference.md) | range | [GroupReference](GroupReference.md) |



















</div>