

## Classe: Attendance 


_Liste de présence agrégée pour une séance (nombre de membres présents, absents, excusés) : elle retient quels membres d'un organe parlementaire étaient présents, absents ou excusés lors d'une séance. La présence est saisie à deux niveaux — par cet agrégat avec les totaux de la séance, et par une IndividualAttendance par personne, rattachée à celui-ci via parent_attendance. Les listes de présence servent à documenter la participation, à vérifier le quorum, à la transparence envers le public, à rendre compte de l'accomplissement des devoirs, à établir des statistiques sur les taux de présence ainsi qu'à administrer les indemnités et les frais._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | La séance à laquelle se rapporte la liste de présence.  |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Date et heure auxquelles la présence a été saisie.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| total_count | 0..1 <br/> [Integer](Integer.md) | Nombre total de membres de l'organe, valeur de référence pour le calcul du quorum (p. ex. 200 pour le Conseil national, 46 pour le Conseil des États). Le quorum lui-même n'est pas enregistré dans un champ propre : il résulte du rapport entre total_present et total_count et des règles de quorum de l'organe, et est calculé au besoin à partir des données.  |
| total_present | 0..1 <br/> [Integer](Integer.md) | Nombre de membres présents, p. ex. 185 sur 200.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Nombre de membres absents sans excuse, p. ex. 3 sur 200.  |
| total_excused | 0..1 <br/> [Integer](Integer.md) | Nombre de membres dont l'absence était excusée, p. ex. 12 sur 200.  |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](Container.md) | [attendances](attendances.md) | range | [Attendance](Attendance.md) |
| [IndividualAttendance](IndividualAttendance.md) | [parent_attendance](parent_attendance.md) | range | [Attendance](Attendance.md) |



















</div>