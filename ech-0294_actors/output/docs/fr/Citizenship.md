

## Classe: Citizenship 


_Nationalité (également utilisée pour la citoyenneté) d'une personne indiquant le pays et la validité temporelle. Si aucun `valid_from` n'est fourni, cette information n'est pas connue. S'il est établi que la nationalité est valable depuis la naissance, la date de naissance doit être répétée ici. En l'absence de `valid_through`, la nationalité est toujours en vigueur._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| country | 0..1 <br/> [String](String.md) | Code de pays ISO 3166-1 alpha-2.  |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [citizenships](citizenships.md) | range | [Citizenship](Citizenship.md) |



















</div>