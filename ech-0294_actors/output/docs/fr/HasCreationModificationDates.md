

## Classe: HasCreationModificationDates 


_Une classe mixin qui fournit des slots pour modéliser les dates de création et de modification d'une entité._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée.  |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée.  |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois.  |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois.  |



### Utilisation de mixin

[Person](Person.md), [Group](Group.md), [Membership](Membership.md), [InterestLink](InterestLink.md)





















</div>