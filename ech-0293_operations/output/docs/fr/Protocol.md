

## Classe: Protocol 


_Le procès-verbal établi après la séance. Un conteneur qui regroupe les points effectivement traités (protocol_items), les votes, les interventions, les segments de texte in extenso et les documents liés._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance liée qui regroupe la séance courante.  |
| protocol_items | * <br/> [ProtocolItem](ProtocolItem.md) | Points de l'ordre du jour tels qu'ils ont effectivement été consignés au procès-verbal.  |
| votings | * <br/> [Voting](Voting.md) | Ensemble des votes.  |
| speeches | * <br/> [Speech](Speech.md) | Ensemble des interventions.  |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Ensemble de segments de texte (p. ex. procès-verbal in extenso).  |
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
| [Container](Container.md) | [protocols](protocols.md) | range | [Protocol](Protocol.md) |
| [Meeting](Meeting.md) | [protocol_ref](protocol_ref.md) | range | [Protocol](Protocol.md) |



















</div>