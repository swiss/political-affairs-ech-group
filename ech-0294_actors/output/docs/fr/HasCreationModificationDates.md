

## Classe: HasCreationModificationDates 


_A mixin class that provides slots for modeling creation and modification dates of an entity._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created.  |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created.  |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified.  |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified.  |



### Utilisation de mixin

| mixed into | description |
| --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |
| [Group](Group.md) | A political group, organization, or body (e |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |





















</div>