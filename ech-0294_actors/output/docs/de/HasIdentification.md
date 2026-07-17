

## Klasse: HasIdentification 


_Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügung stellt._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz.  |



### Mixin-Verwendung

| mixed into | description |
| --- | --- |
| [Container](Container.md) | Container für politische Akteure, Gruppen und Beziehungen |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |
| [PersonReference](PersonReference.md) | Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikations... |
| [GroupReference](GroupReference.md) | Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifikations... |





















</div>