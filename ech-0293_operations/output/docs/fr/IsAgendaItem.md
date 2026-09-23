

## Classe: IsAgendaItem 


_Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : désignation, type, acteurs, lien avec l'affaire, état, décision ainsi que les textes et documents rattachés. Elle est utilisée par le point planifié (AgendaItem) et par le point consigné (ProtocolItem), de sorte que les deux portent les mêmes éléments sans que l'un dépende de l'autre._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance liée qui regroupe la séance courante.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Type de point de l'ordre du jour, distinguant les points isolés des groupes de points.  |
| agenda_item_number | 0..1 <br/> [String](String.md) | Numéro d'ordre du point de l'ordre du jour (type chaîne, afin de permettre les chiffres romains).  |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Position (nombre entier) du point de l'ordre du jour dans le déroulement de la séance.  |
| leading_actor_id | 0..1 <br/> [String](String.md) | Le département responsable du point de l'ordre du jour.  |
| speaking_actor_id | 0..1 <br/> [String](String.md) | La ou le porte-parole ou la cheffe ou le chef du département pour le point de l'ordre du jour.  |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Titre du point de l'ordre du jour.  |
| affair_id | 0..1 <br/> [String](String.md) | Le lien vers les affaires rattachées au point de l'ordre du jour.  |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Sous-titre ou description détaillée du point de l'ordre du jour.  |
| state_id | 0..1 <br/> [String](String.md) | Identifiant d'état (renvoi à l'énumération des états ou à un état propre).  |
| state_name | 0..1 <br/> [String](String.md) | Description personnalisée de l'état de la séance.  |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| agenda_item_category | 0..1 <br/> [String](String.md) | Catégorie pour les points de l'ordre du jour regroupés (p. ex. introduction, par département, points techniques).  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre du jour.  |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | La décision prise sur ce point de l'ordre du jour.  |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Ensemble de segments de texte (p. ex. procès-verbal in extenso).  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |



### Utilisation de mixin

[AgendaItem](AgendaItem.md), [ProtocolItem](ProtocolItem.md)





















</div>