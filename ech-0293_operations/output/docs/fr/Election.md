

## Classe: Election 


_Une procédure d'élection visant à pourvoir des fonctions par des personnes._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles la séance ou le vote commence.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles la séance ou le vote se termine.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](ElectionTypeEnum.md) | Type de procédure d'élection.  |
| type_label | 0..1 <br/> [String](String.md) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| title | 0..1 <br/> [String](String.md) | Titre de l'élément.  |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Nombre total de membres absents. La distinction entre absent et absent excusé se fait dans la liste de présence.  |
| total | 0..1 <br/> [Integer](Integer.md) | Nombre total de voix, sans les absents ni la voix de la présidence.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](MajorityTypeEnum.md) | Type de majorité requise pour le vote (absolue, deux tiers, etc.).  |
| majority_count | 0..1 <br/> [Integer](Integer.md) | Nombre de voix requis pour atteindre le seuil de majorité déterminant.  |
| result_text | 0..1 <br/> [String](String.md) | Texte libre décrivant le résultat du vote, p. ex. « Accepté par 78 voix ».  |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance liée qui regroupe la séance courante.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre du jour.  |
| affair_id | 0..1 <br/> [String](String.md) | Le lien vers les affaires rattachées au point de l'ordre du jour.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Référence à l'organe agissant (instantané allégé au moment de la mise en relation).  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [elections](elections.md) | range | [Election](Election.md) |



















</div>