

## Classe: Training 


_Formation ou éducation d'une personne indiquant un type (p. ex. diplôme scolaire, diplôme universitaire, service militaire), un libellé, un code ISCO-19 et la validité temporelle._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| training_type | 0..1 <br/> [TrainingTypeEnum](TrainingTypeEnum.md) | Type de formation ou d'éducation.  |
| training_code | 0..1 <br/> [String](String.md) | Code ISCO-19 de la formation ou de l'éducation.  |
| value | 0..1 <br/> [String](String.md) | La valeur proprement dite d'une information, en plus d'autres attributs tels que le type, la langue, etc.  |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [trainings](trainings.md) | range | [Training](Training.md) |



















</div>