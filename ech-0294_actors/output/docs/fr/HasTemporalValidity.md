

## Classe: HasTemporalValidity 


_Une classe mixin qui fournit des slots pour modéliser la validité temporelle d'une information (et non d'un événement)._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable.  |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible.  |



### Utilisation de mixin

| mixed into | description |
| --- | --- |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |
| [Name](Name.md) | Un nom avec un type (p |
| [Citizenship](Citizenship.md) | Nationalité (également utilisée pour la citoyenneté) d'une personne indiquant... |
| [Gender](Gender.md) | Sexe d'une personne indiquant un code de sexe et la validité temporelle |
| [Occupation](Occupation.md) | Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si... |
| [Training](Training.md) | Formation ou éducation d'une personne indiquant un type (p |
| [ElectoralDistrict](ElectoralDistrict.md) | Circonscription ou région électorale dans laquelle une personne est politique... |





















</div>