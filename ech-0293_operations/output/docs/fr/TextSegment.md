

## Classe: TextSegment 


_Un segment de texte tel qu'un renvoi ou un intertitre dans un procès-verbal de séance._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| text | 1 <br/> [String](String.md) | Contenu textuel de l'élément.  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [text_segments](text_segments.md) | range | [TextSegment](TextSegment.md) |



















</div>