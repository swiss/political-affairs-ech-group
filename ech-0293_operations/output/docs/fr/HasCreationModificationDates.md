

## Classe: HasCreationModificationDates 


_Une classe mixin qui fournit des slots pour modéliser les dates de création et de modification d'une entité._




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
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |
| [Protocol](Protocol.md) | Le procès-verbal établi après la séance |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |
| [IndividualVote](IndividualVote.md) | Une voix individuelle exprimée par un membre lors d'une procédure de vote |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |
| [IndividualAttendance](IndividualAttendance.md) | Constatation individuelle de la présence d'une personne à une séance (rattach... |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |





















</div>