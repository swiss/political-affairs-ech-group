

## Classe: Legislature 


_Durée du mandat d'un parlement en tant qu'assemblée législative. Elle est en règle générale de quatre ans._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| administrative_id | 0..1 <br/> [String](String.md) | Identifiant administratif du corps législatif, p. ex. commune, canton ou pays.  |
| name | * <br/> [MultilingualString](MultilingualString.md) | Désignation complète multilingue.  |
| description | 0..1 <br/> [String](String.md) | Texte descriptif de l'élément.  |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Référence à l'organe agissant (instantané allégé au moment de la mise en relation).  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | La date de début effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | La date de début planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | La date de fin effective d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | La date de fin planifiée d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée. <br/><br/>Héritage : [IsEventWithDuration](IsEventWithDuration.md) |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [legislatures](legislatures.md) | range | [Legislature](Legislature.md) |



















</div>