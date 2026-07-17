

## Classe: Occupation 


_Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si le poste est rémunéré, ainsi que la validité temporelle._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | Indique si le poste est rémunéré.  |
| occupation_code | 0..1 <br/> [String](String.md) | Code ISCO-19 du métier.  |
| label | 0..1 <br/> [String](String.md) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| organization_uid | 0..1 <br/> [String](String.md) | IDE de l'organisation (format eCH-0097 : CHE-XXX.XXX.XXX) issu du registre fédéral IDE (uid.admin.ch).  |
| organization_name | 0..1 <br/> [String](String.md) | Nom de l'organisation ou de l'entreprise.  |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [occupations](occupations.md) | range | [Occupation](Occupation.md) |














### Exemples
#### Exemple : Occupation-swiss_politicians_Beat_Jans_Politiker

```yaml
label: Politiker
valid_from: 1964-01-01
is_active: true

```






</div>