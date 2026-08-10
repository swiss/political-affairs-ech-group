

## Klasse: HasIdentification 


_Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügung stellt. Sie wird für Entitäten verwendet, die aus sich heraus identifiziert sind; deren `global_uri` ist der Identifikator und daher obligatorisch._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans.  |



### Mixin-Verwendung

[Container](Container.md), [Person](Person.md), [Group](Group.md), [Membership](Membership.md), [InterestLink](InterestLink.md), [ElectoralDistrict](ElectoralDistrict.md)





















</div>