

## Classe: IndividualAttendance 


_Constatation individuelle de la présence d'une personne à une séance (rattachée à l'agrégat Attendance parent). Elle porte sur la séance dans son ensemble et se distingue de la voix individuelle (IndividualVote), qui retient la voix exprimée lors d'un vote déterminé : une personne présente à la séance (attendance_type present) peut être saisie avec not_voted lors d'un vote particulier parce qu'elle a brièvement quitté la salle à ce moment-là._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| parent_attendance | 0..1 <br/> [Attendance](Attendance.md) | L'agrégat Attendance auquel appartient cet enregistrement ; comme l'agrégat est lui-même rattaché à la séance, la saisie individuelle est ainsi attribuée à la séance.  |
| person_reference | 0..1 <br/> [PersonReference](PersonReference.md) | La personne dont la présence est saisie, sous forme de référence à une personne selon eCH-0294.  |
| attendance_type | 0..1 <br/> [AttendanceTypeEnum](AttendanceTypeEnum.md) | Type de présence individuelle.  |
| reason | * <br/> [MultilingualString](MultilingualString.md) | Motif de l'absence, du retard ou de la suppléance (texte libre, multilingue).  |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](Container.md) | [individual_attendances](individual_attendances.md) | range | [IndividualAttendance](IndividualAttendance.md) |



















</div>