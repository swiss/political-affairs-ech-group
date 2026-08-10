

## Classe: IsEventWithDuration 


_Une classe mixin qui fournit des slots pour modéliser des événements ou occurrences avec une durée._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| date_begin_actual | 0..1 <br/> [Date](Date.md) | La date de début effective d'un événement ou d'une occurrence avec durée.  |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée.  |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | La date de début planifiée d'un événement ou d'une occurrence avec durée.  |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée.  |
| date_end_actual | 0..1 <br/> [Date](Date.md) | La date de fin effective d'un événement ou d'une occurrence avec durée.  |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée.  |
| date_end_planned | 0..1 <br/> [Date](Date.md) | La date de fin planifiée d'un événement ou d'une occurrence avec durée.  |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée.  |



### Utilisation de mixin

| mixed into | description |
| --- | --- |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |





















</div>