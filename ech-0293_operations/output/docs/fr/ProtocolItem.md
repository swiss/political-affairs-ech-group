

## Classe: ProtocolItem 


_Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-verbal._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance liée qui regroupe la séance courante. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Type de point de l'ordre du jour, distinguant les points isolés des groupes de points. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| agenda_item_number | 0..1 <br/> [String](String.md) | Numéro d'ordre du point de l'ordre du jour (type chaîne, afin de permettre les chiffres romains). <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Position (nombre entier) du point de l'ordre du jour dans le déroulement de la séance. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| leading_actor_id | 0..1 <br/> [String](String.md) | Le département responsable du point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| speaking_actor_id | 0..1 <br/> [String](String.md) | La ou le porte-parole ou la cheffe ou le chef du département pour le point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Titre du point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| affair_id | 0..1 <br/> [String](String.md) | Le lien vers les affaires rattachées au point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Sous-titre ou description détaillée du point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| state_id | 0..1 <br/> [String](String.md) | Identifiant d'état (renvoi à l'énumération des états ou à un état propre). <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| state_name | 0..1 <br/> [String](String.md) | Description personnalisée de l'état de la séance. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| url | * <br/> [MultilingualString](MultilingualString.md) | Page d'accueil ou adresse web complémentaire, multilingue. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| agenda_item_category | 0..1 <br/> [String](String.md) | Catégorie pour les points de l'ordre du jour regroupés (p. ex. introduction, par département, points techniques). <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | La décision prise sur ce point de l'ordre du jour. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité. <br/><br/>Héritage : [AgendaItem](AgendaItem.md) |
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
| [Protocol](Protocol.md) | [protocol_items](protocol_items.md) | range | [ProtocolItem](ProtocolItem.md) |



















</div>