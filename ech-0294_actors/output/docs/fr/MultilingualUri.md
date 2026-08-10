

## Classe: MultilingualUri 


_Une URI accompagnée de la langue de la ressource vers laquelle elle renvoie. Structure identique à MultilingualValue, mais la valeur est une URI : elle est utilisée là où le même contenu est publié à une adresse propre par langue._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| value | 1 <br/> [Uri](Uri.md) | La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc.  |
| language | 1 <br/> [String](String.md) | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »).  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [landing_page](landing_page.md) | range | [MultilingualUri](MultilingualUri.md) |



















</div>