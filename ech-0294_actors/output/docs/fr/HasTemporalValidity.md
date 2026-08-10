

## Classe: HasTemporalValidity 


_Une classe mixin qui fournit des slots pour modéliser la validité temporelle d'une information (et non d'un événement)._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable.  |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'information est actuellement valable. Peut être utile lorsque cette information est explicitement disponible.  |



### Utilisation de mixin

[Group](Group.md), [Membership](Membership.md), [InterestLink](InterestLink.md), [Name](Name.md), [Citizenship](Citizenship.md), [Gender](Gender.md), [Occupation](Occupation.md), [Training](Training.md)





















</div>