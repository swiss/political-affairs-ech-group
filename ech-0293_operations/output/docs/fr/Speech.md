

## Classe: Speech 


_Une intervention prononcée au cours d'une séance (également appelée prise de parole) : la contribution orale d'une personne lors d'une séance parlementaire et, partant, l'instrument central du débat politique et de l'expression des opinions au parlement. Les interventions revêtent différentes formes — interventions principales (prises de position détaillées sur une affaire, développement de propositions, exposé de l'avis du groupe parlementaire), interventions brèves (questions intermédiaires, rectifications), déclarations de groupe présentées par la porte-parole ou le porte-parole du groupe, ainsi qu'interventions du gouvernement (réponses à des questions, défense de projets). Une intervention retient qui a parlé, quand et sous quel point de l'ordre du jour, avec le texte prononcé et, le cas échéant, un enregistrement audio ou vidéo. Elle peut être livrée de deux manières : imbriquée dans le procès-verbal (Protocol.speeches), où la séance ressort du procès-verbal environnant mais non le point de l'ordre du jour, ou à plat dans Container.speeches, où tout rattachement ferait défaut sans références. parent_meeting et parent_agenda_item sont donc renseignés dans les deux cas ; ils portent les mêmes valeurs que pour Voting et Election et rendent l'intervention exploitable indépendamment de sa forme de livraison._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un vote, une élection, une intervention, une liste de présence ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né. Les points de l'ordre du jour ne le portent pas : ils sont imbriqués dans leur séance.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifiant du point de l'ordre du jour auquel cet enregistrement se rattache. Pour un point de l'ordre du jour, il forme une hiérarchie de points — p. ex. un groupe « Délibérations législatives » avec les sous-points « Loi sur l'énergie (discussion par article) » et « Loi sur l'énergie (vote final) » ; pour une intervention, il désigne le point sous lequel elle a été faite.  |
| language | 0..1 <br/> [String](String.md) | Langue dans laquelle l'intervention a été prononcée, p. ex. de (allemand), fr (français), it (italien), rm (romanche) ou en (anglais).  |
| start | 0..1 <br/> [String](String.md) | Indication de début ou position.  |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Date et heure auxquelles l'intervention a commencé. Avec datetime_end, elle permet de situer précisément l'intervention dans les enregistrements audio et vidéo, d'analyser le temps de parole par personne ou par groupe parlementaire et de contrôler le respect des limites de temps.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | Date et heure auxquelles l'intervention s'est terminée ; le temps de parole résulte de la différence avec datetime_begin.  |
| actor_fullname | 0..1 <br/> [String](String.md) | Nom de la personne qui s'exprime, pour un accès rapide sans résolution de actor_id.  |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | La personne qui s'exprime, sous forme de référence à une personne selon eCH-0294.  |
| role | 0..1 <br/> [String](String.md) | Rôle dans lequel la personne s'exprime, p. ex. présidente ou président de groupe parlementaire, rapporteuse ou rapporteur, conseillère fédérale ou conseiller fédéral.  |
| text | 1 <br/> [String](String.md) | Texte prononcé de l'intervention.  |
| text_format | 0..1 <br/> [String](String.md) | Format du texte (text, html, html_with_timestamps).  |
| text_type | 0..1 <br/> [String](String.md) | Version du texte : la transcription brute (transcription littérale, non retravaillée et avec les mots de remplissage, disponible directement après la séance) ou la transcription éditée (revue par la rédaction et corrigée sur le plan grammatical, la version officielle du procès-verbal).  |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires.  |
| media_url | 0..1 <br/> [String](String.md) | URL de l'enregistrement audio ou vidéo de l'intervention, ou de la diffusion en direct pendant la séance, archivée par la suite.  |
| media_type | 0..1 <br/> [String](String.md) | Type d'enregistrement : audio (son original de l'intervention) ou vidéo (enregistrement visuel, en général lors des séances plénières).  |
| media_format | 0..1 <br/> [String](String.md) | Type MIME de l'enregistrement, p. ex. audio/mpeg (MP3), audio/wav, video/mp4 ou video/webm.  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](Container.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |
| [Protocol](Protocol.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |














### Exemples
#### Exemple Speech : Speech with verbatim text and video recording

```yaml
speeches:
- global_uri: ops:366631
  parent_meeting: parl:sr_winter25_sitzung_6
  parent_agenda_item: ops:69905
  language: fr
  datetime_begin: '2025-12-19T09:20:00+01:00'
  datetime_end: '2025-12-19T09:25:00+01:00'
  actor_fullname: Pascal Broulis
  actor_id:
    global_uri: actors:person_pascal_broulis
    wikidata_uri: http://www.wikidata.org/entity/Q116407
    label: Pascal Broulis
  role: speaker
  text: >-
    Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec
    attention les différents commentaires qui ont été effectués sur mon postulat.
    Cela reste un postulat, ce n'est pas une motion. D'abord, je ne partage pas l'avis
    selon lequel ce postulat n'apporterait pas une valeur ajoutée. En effet, un "benchmark",
    à savoir un modèle chiffré de performance, permettrait de mieux comprendre les
    raisons des retards que notre pays rencontre en comparaison avec les principaux
    pays européens.
  text_format: html
  text_type: final
  landing_page: >-
    https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631
  media_url: https://par-pcache.simplex.tv/content?externalid=366631
  media_type: video
  media_format: video/mp4

```






</div>