

## Classe: IsAgendaItem 


_Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : désignation, type, acteurs, lien avec l'affaire, état, décision ainsi que les textes et documents rattachés. Elle est utilisée par le point planifié (AgendaItem) et par le point consigné (ProtocolItem), de sorte que les deux portent les mêmes éléments sans que l'un dépende de l'autre._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Type de point de l'ordre du jour, distinguant les points isolés des groupes de points.  |
| agenda_item_number | 0..1 <br/> [String](String.md) | Numéro du point sur l'ordre du jour, p. ex. « 2.1 » ou « 3 » (chaîne de caractères, afin de permettre aussi les chiffres romains).  |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Position entière du point dans le déroulement de la séance, déterminante pour le tri et l'affichage.  |
| leading_actor_id | 0..1 <br/> [String](String.md) | Le département responsable du point de l'ordre du jour.  |
| speaking_actor_id | 0..1 <br/> [String](String.md) | La ou le porte-parole ou la cheffe ou le chef du département pour le point de l'ordre du jour.  |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Titre du point de l'ordre du jour.  |
| affair_id | 0..1 <br/> [String](String.md) | Identifiant de l'affaire (eCH-0295) à laquelle se rapporte l'enregistrement. Les points administratifs (p. ex. approbation du procès-verbal) n'ont pas d'affaire. Une affaire passe en règle générale par plusieurs points de l'ordre du jour — dans la législation, par exemple, le débat d'entrée en matière, la discussion par article, le vote final et, le cas échéant, la procédure d'élimination des divergences entre les conseils.  |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Sous-titre ou description détaillée du point de l'ordre du jour.  |
| state_id | 0..1 <br/> [String](String.md) | Identifiant d'état du point (renvoi à une énumération des états ou à un état propre), p. ex. pending (pas encore traité), in_progress (en délibération), completed (traité), postponed (renvoyé à une séance ultérieure) ou withdrawn (retiré).  |
| state_name | 0..1 <br/> [String](String.md) | Désignation de statut divergente, en texte libre, là où l'énumération des statuts ne suffit pas.  |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| agenda_item_category | 0..1 <br/> [String](String.md) | Catégorisation libre du point selon son contenu ou son regroupement, p. ex. « Législation », « Budget et finances », « Interpellations et questions », « Élections », par département, ou points introductifs et techniques. La catégorisation n'est pas standardisée et peut varier selon l'unité fédérale.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifiant du point de l'ordre du jour auquel cet enregistrement se rattache. Pour un point de l'ordre du jour, il forme une hiérarchie de points — p. ex. un groupe « Délibérations législatives » avec les sous-points « Loi sur l'énergie (discussion par article) » et « Loi sur l'énergie (vote final) » ; pour une intervention, il désigne le point sous lequel elle a été faite.  |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | La décision formelle prise sur ce point de l'ordre du jour, p. ex. l'adoption de la loi sur l'énergie. Le vote sous-jacent avec son rapport de voix est saisi séparément comme Voting.  |
| joint_debates | * <br/> [JointDebate](JointDebate.md) | Délibérations communes rattachées à cet enregistrement : pour un point de l'ordre du jour, les délibérations dans lesquelles il est traité conjointement avec d'autres points ; pour une séance ou une session, les délibérations communes qui s'y tiennent.  |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Ensemble de segments de texte (p. ex. procès-verbal in extenso).  |
| documents | * <br/> [Work](Work.md) | Documents relatifs au point de l'ordre du jour, sous forme de FRBR Works, p. ex. messages et rapports, propositions et propositions d'amendement.  |



### Utilisation de mixin

[AgendaItem](AgendaItem.md), [ProtocolItem](ProtocolItem.md)





















</div>