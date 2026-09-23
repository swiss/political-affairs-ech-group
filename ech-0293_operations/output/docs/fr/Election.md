

## Classe: Election 


_Une élection par laquelle un organe parlementaire désigne une ou plusieurs personnes à une charge ou à une fonction. Contrairement au vote (Voting), qui tranche des questions matérielles, l'élection est une décision portant sur des personnes : elle a souvent lieu au scrutin secret et requiert en général la majorité absolue, alors que les votes sont le plus souvent ouverts. La présidente ou le président, qui ne participe pas aux votes, prend part aux élections. Chaque tour de scrutin est saisi comme une élection distincte ; les tours d'une même élection sont reliés par le point de l'ordre du jour commun — par exemple un premier tour à la majorité absolue resté sans résultat, suivi d'un second tour où la majorité relative suffit._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles la séance ou le vote commence.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles la séance ou le vote se termine.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](ElectionTypeEnum.md) | Type de procédure d'élection.  |
| type_label | 0..1 <br/> [String](String.md) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| title | 0..1 <br/> [String](String.md) | Titre de l'élection, p. ex. « Élection à la présidence de la CER ».  |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Nombre de membres absents qui n'ont pas pu participer. La liste de présence (Attendance) indique si une absence était excusée.  |
| total | 0..1 <br/> [Integer](Integer.md) | Nombre total de voix, sans les absents ni la voix de la présidence.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](MajorityTypeEnum.md) | Type de majorité requise pour le vote (absolue, deux tiers, etc.).  |
| majority_count | 0..1 <br/> [Integer](Integer.md) | Nombre de voix requis pour atteindre le seuil de majorité déterminant.  |
| result_text | 0..1 <br/> [String](String.md) | Texte libre décrivant le résultat, p. ex. « Adopté par 120 voix contre 75 et 5 abstentions ». Pour les votes, la décision catégorielle (adopté, rejeté, pris acte …) n'est pas retenue ici, mais dans la Resolution (resolution_type) du point de l'ordre du jour.  |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né.  |
| parent_protocol | 0..1 <br/> [Protocol](Protocol.md) | Le procès-verbal dans lequel le vote ou l'élection est consigné. Le vote a lieu au cours de la séance et se rattache donc au procès-verbal, et non à l'ordre du jour planifié à l'avance : ce qui a été mis à l'ordre du jour ne dit pas encore sur quoi il a effectivement été voté. Inversement, le procès-verbal reprend ses votes et élections sous forme de listes (votings, elections).  |
| parent_protocol_item | 0..1 <br/> [ProtocolItem](ProtocolItem.md) | Le point consigné au procès-verbal (ProtocolItem) sous lequel le vote ou l'élection a eu lieu. Absent lorsque le vote a eu lieu sans point de l'ordre du jour ; le rattachement à la séance découle alors uniquement de parent_protocol et parent_meeting.  |
| affair_id | 0..1 <br/> [String](String.md) | Identifiant de l'affaire (eCH-0295) à laquelle se rapporte l'enregistrement. Les points administratifs (p. ex. approbation du procès-verbal) n'ont pas d'affaire. Une affaire passe en règle générale par plusieurs points de l'ordre du jour — dans la législation, par exemple, le débat d'entrée en matière, la discussion par article, le vote final et, le cas échéant, la procédure d'élimination des divergences entre les conseils.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Référence à l'organe agissant (instantané au moment de la mise en relation).  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](Container.md) | [elections](elections.md) | range | [Election](Election.md) |
| [Protocol](Protocol.md) | [elections](elections.md) | range | [Election](Election.md) |



















</div>