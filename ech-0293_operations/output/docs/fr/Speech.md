

## Classe: Speech 


_Une intervention prononcée au cours d'une séance (également appelée prise de parole)._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| language | 0..1 <br/> [String](String.md) | Code de langue au format ISO 639-1 (deux lettres minuscules, par ex. « de », « fr », « it », « en »).  |
| start | 0..1 <br/> [String](String.md) | Indication de début ou position.  |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles la séance ou le vote commence.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles la séance ou le vote se termine.  |
| actor_fullname | 0..1 <br/> [String](String.md) | Nom complet de l'actrice ou de l'acteur, respectivement de la personne.  |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | Référence à la personne agissante (instantané au moment de la mise en relation).  |
| role | 0..1 <br/> [String](String.md) | Rôle de la personne (p. ex. rapporteuse ou rapporteur de commission).  |
| text | 1 <br/> [String](String.md) | Contenu textuel de l'élément.  |
| text_format | 0..1 <br/> [String](String.md) | Format du texte (text, html, html_with_timestamps).  |
| text_type | 0..1 <br/> [String](String.md) | Type de texte (version brute, version éditée).  |
| landing_page | 0..1 <br/> [String](String.md) | URL fournissant des informations complémentaires.  |
| media_url | 0..1 <br/> [String](String.md) | URL du fichier média (audio/vidéo).  |
| media_type | 0..1 <br/> [String](String.md) | Type de média (audio, vidéo, document).  |
| media_format | 0..1 <br/> [String](String.md) | Type MIME du fichier média.  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |
| [Protocol](Protocol.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |














### Exemples
#### Exemple Speech : Speech with verbatim text and video recording

```yaml
speeches:
- global_uri: ops:366631
  language: fr
  datetime_begin: '2025-12-19T09:20:00+01:00'
  datetime_end: '2025-12-19T09:25:00+01:00'
  actor_fullname: Pascal Broulis
  actor_id:
    global_uri: https://api.openparldata.ch/v1/persons/18682
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