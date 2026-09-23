

## Classe: ProtocolItem 


_Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-verbal. Il porte les mêmes éléments qu'AgendaItem par le mixin IsAgendaItem, mais constitue une classe à part entière : le point consigné n'est pas un cas particulier du point planifié. Il naît indépendamment et peut comprendre des points jamais mis à l'ordre du jour, de même que l'ordre du jour peut comprendre des points jamais traités._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
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
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Type de point de l'ordre du jour, distinguant les points isolés des groupes de points. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_number | 0..1 <br/> [String](String.md) | Numéro du point sur l'ordre du jour, p. ex. « 2.1 » ou « 3 » (chaîne de caractères, afin de permettre aussi les chiffres romains). <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Position entière du point dans le déroulement de la séance, déterminante pour le tri et l'affichage. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| leading_actor_id | 0..1 <br/> [String](String.md) | Le département responsable du point de l'ordre du jour. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| speaking_actor_id | 0..1 <br/> [String](String.md) | La ou le porte-parole ou la cheffe ou le chef du département pour le point de l'ordre du jour. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Titre du point de l'ordre du jour. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| affair_id | 0..1 <br/> [String](String.md) | Identifiant de l'affaire (eCH-0295) à laquelle se rapporte l'enregistrement. Les points administratifs (p. ex. approbation du procès-verbal) n'ont pas d'affaire. Une affaire passe en règle générale par plusieurs points de l'ordre du jour — dans la législation, par exemple, le débat d'entrée en matière, la discussion par article, le vote final et, le cas échéant, la procédure d'élimination des divergences entre les conseils. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Sous-titre ou description détaillée du point de l'ordre du jour. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| state_id | 0..1 <br/> [String](String.md) | Identifiant d'état du point (renvoi à une énumération des états ou à un état propre), p. ex. pending (pas encore traité), in_progress (en délibération), completed (traité), postponed (renvoyé à une séance ultérieure) ou withdrawn (retiré). <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| state_name | 0..1 <br/> [String](String.md) | Désignation de statut divergente, en texte libre, là où l'énumération des statuts ne suffit pas. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| url | * <br/> [MultilingualString](MultilingualString.md) | Page d'accueil ou adresse web complémentaire, multilingue. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_category | 0..1 <br/> [String](String.md) | Catégorisation libre du point selon son contenu ou son regroupement, p. ex. « Législation », « Budget et finances », « Interpellations et questions », « Élections », par département, ou points introductifs et techniques. La catégorisation n'est pas standardisée et peut varier selon l'unité fédérale. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifiant du point de l'ordre du jour auquel cet enregistrement se rattache. Pour un point de l'ordre du jour, il forme une hiérarchie de points — p. ex. un groupe « Délibérations législatives » avec les sous-points « Loi sur l'énergie (discussion par article) » et « Loi sur l'énergie (vote final) » ; pour une intervention, il désigne le point sous lequel elle a été faite. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | La décision formelle prise sur ce point de l'ordre du jour, p. ex. l'adoption de la loi sur l'énergie. Le vote sous-jacent avec son rapport de voix est saisi séparément comme Voting. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| joint_debates | * <br/> [JointDebate](JointDebate.md) | Délibérations communes rattachées à cet enregistrement : pour un point de l'ordre du jour, les délibérations dans lesquelles il est traité conjointement avec d'autres points ; pour une séance ou une session, les délibérations communes qui s'y tiennent. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Ensemble de segments de texte (p. ex. procès-verbal in extenso). <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |
| documents | * <br/> [Work](Work.md) | Documents relatifs au point de l'ordre du jour, sous forme de FRBR Works, p. ex. messages et rapports, propositions et propositions d'amendement. <br/><br/>Héritage : [IsAgendaItem](IsAgendaItem.md) |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [protocol_items](protocol_items.md) | range | [ProtocolItem](ProtocolItem.md) |
| [Voting](Voting.md) | [parent_protocol_item](parent_protocol_item.md) | range | [ProtocolItem](ProtocolItem.md) |
| [Election](Election.md) | [parent_protocol_item](parent_protocol_item.md) | range | [ProtocolItem](ProtocolItem.md) |



















</div>