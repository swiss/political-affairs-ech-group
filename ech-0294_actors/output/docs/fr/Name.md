

## Classe: Name 


_Un nom avec un type (p. ex. nom d'usage, nom officiel), une valeur et une validité temporelle._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| name_type | 0..1 <br/> [NameTypeEnum](NameTypeEnum.md) | Type de nom selon eCH-0011 (personNameData).  |
| value | 0..1 <br/> [String](String.md) | La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc.  |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [names](names.md) | range | [Name](Name.md) |



















</div>