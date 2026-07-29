

## Classe: Manifestation 


_FRBR Manifestation : une forme de fichier concrète d'une Expression, adressable au moyen d'une URL._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](String.md) | Identifiant univoque de l'élément.  |
| dates | * <br/> [Date](Date.md) | Dates relatives à l'élément, chacune assortie d'une indication de type.  |
| format | 0..1 <br/> [String](String.md) | Le format de fichier de la manifestation (p. ex. pdf, html).  |
| manifestation_url | 0..1 <br/> [Uri](Uri.md) | URL sous laquelle la forme de fichier peut être consultée.  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Expression](Expression.md) | [manifestations](manifestations.md) | range | [Manifestation](Manifestation.md) |



















</div>