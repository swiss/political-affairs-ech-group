

## Classe: Occupation 


_Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si l'activité est rémunérée, ainsi que la validité temporelle._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| is_paid | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'activité est rémunérée.  |
| occupation_code | 0..1 <br/> [String](String.md) | Code ISCO-19 du métier.  |
| label | 0..1 <br/> [String](String.md) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| organization_uid | 0..1 <br/> [String](String.md) | IDE de l'organisation issu du registre fédéral IDE (uid.admin.ch), dans le format d'échange d'eCH-0108 : CHE suivi de neuf chiffres, sans séparateurs (p. ex. CHE106063525). Le dernier chiffre est un chiffre de contrôle calculé modulo 11. La forme pointée CHE-106.063.525 est la présentation utilisée par uid.admin.ch et n'est pas saisie ici.  |
| organization_name | 0..1 <br/> [String](String.md) | Nom de l'organisation ou de l'entreprise.  |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [occupation_code](occupation_code.md)
- [label](label.md)










### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Person](Person.md) | [occupations](occupations.md) | range | [Occupation](Occupation.md) |














### Exemples
#### Exemple Occupation : swiss politicians Sofia Fisch Juristin

```yaml
occupations:
- label: Jurist*in
  is_active: true

```
#### Exemple Occupation : swiss politicians Beat Jans Politiker

```yaml
occupations:
- label: Politiker
  valid_from: 1964-01-01
  is_active: true

```






</div>