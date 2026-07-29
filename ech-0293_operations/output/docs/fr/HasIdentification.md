

## Classe: HasIdentification 


_Une classe mixin qui fournit des slots pour l'identification d'une entité._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans.  |



### Utilisation de mixin

| mixed into | description |
| --- | --- |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |
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
| [TextSegment](TextSegment.md) | Un segment de texte tel qu'un renvoi ou un intertitre dans un procès-verbal d... |
| [Motion](Motion.md) | Une proposition formelle déposée au cours des délibérations |
| [Media](Media.md) | Fichiers médias ou documents (y compris les procès-verbaux en PDF/HTML/WORD o... |
| [PersonReference](PersonReference.md) | Référence légère à une personne avec les principales données d'identification... |
| [GroupReference](GroupReference.md) | Référence légère à un groupe avec les principales données d'identification au... |





















</div>