

## Classe: HasCreationModificationDates 


_Une classe mixin qui fournit des slots pour modéliser les dates de création et de modification d'une entité._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée.  |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée.  |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois.  |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois.  |



### Utilisation de mixin

| mixed into | description |
| --- | --- |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |





















</div>