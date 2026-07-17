

## Classe: Gender 


_Sexe d'une personne indiquant un code de sexe et la validité temporelle._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| gender_code | 0..1 <br/> [GenderCodeEnum](GenderCodeEnum.md) | Code de sexe. Valeurs recommandées : male, female, diverse.  |
| label | 0..1 <br/> [String](String.md) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| pronouns | * <br/> [String](String.md) | Pronoms utilisés par la personne.  |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [genders](genders.md) | range | [Gender](Gender.md) |



















</div>