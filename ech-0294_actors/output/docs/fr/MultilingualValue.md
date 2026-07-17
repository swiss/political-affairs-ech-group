

## Classe: MultilingualValue 


_Une chaîne de caractères multilingue avec indication de la langue._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| value | 0..1 <br/> [String](String.md) | La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc.  |
| language | 0..1 <br/> [String](String.md) | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »).  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [abbreviation](abbreviation.md) | range | [MultilingualValue](MultilingualValue.md) |
| [Group](Group.md) | [description](description.md) | range | [MultilingualValue](MultilingualValue.md) |
| [GroupReference](GroupReference.md) | [abbreviation](abbreviation.md) | range | [MultilingualValue](MultilingualValue.md) |



















</div>