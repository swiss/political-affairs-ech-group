

## Klasse: HasReferenceIdentification 


_Eine Mixin-Klasse, welche die Slots bereitstellt, mit denen eine Referenz die Entität benennt, auf die sie zeigt. Im Unterschied zu `HasIdentification` identifiziert sie nicht das referenzierende Objekt selbst; deshalb ist `global_uri` hier weder Identifikator noch obligatorisch: Ein System, das nur die lokale Id der referenzierten Entität führt, gibt diese an. Eine Referenzklasse, die diesen Mixin verwendet, soll mindestens eines von beiden verlangen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator der referenzierten Entität. Er wird innerhalb derselben Lieferung aufgelöst.  |
| global_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Die eindeutige, global gültige URI der referenzierten Entität. Im Unterschied zu einer local_id ist sie auch über die Lieferung hinaus auflösbar.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans.  |



### Mixin-Verwendung

| mixed into | description |
| --- | --- |
| [PersonReference](PersonReference.md) | Kurzreferenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum... |
| [GroupReference](GroupReference.md) | Kurzreferenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum... |





















</div>