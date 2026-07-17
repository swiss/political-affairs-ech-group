

## Class: Speech 


_[en] A speech or statement made during a meeting (also called Votum or speaker segment)._

_[de] Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| language | 0..1 <br/> [String](String.md) | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |
| start | 0..1 <br/> [String](String.md) | Start indicator or position |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | [en] The date and time when the meeting or voting begins. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | [en] The date and time when the meeting or voting ends. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| actor_fullname | 0..1 <br/> [String](String.md) | Full name of the actor/person |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | [en] Reference to the acting person (lightweight snapshot at time of linking). [de] Referenz auf die handelnde Person (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| role | 0..1 <br/> [String](String.md) | Role of the person (e.g., commission speaker) |
| text | 1 <br/> [String](String.md) | None |
| text_format | 0..1 <br/> [String](String.md) | [en] Format of text (text, html, html_with_timestamps) [de] Format des Textes (text, html, html_with_timestamps)  |
| text_type | 0..1 <br/> [String](String.md) | [en] Type of text (raw draft, edited version) [de] Typ des Textes (Rohfassung, bearbeitete Fassung)  |
| landing_page | 0..1 <br/> [String](String.md) | [en] URL providing further information. [de] URL mit weiteren Informationen.  |
| media_url | 0..1 <br/> [String](String.md) | URL to media file (audio/video) |
| media_type | 0..1 <br/> [String](String.md) | Type of media (audio, video, document) |
| media_format | 0..1 <br/> [String](String.md) | MIME type of the media file |
| documents | * <br/> [Work](Work.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |
| [Protocol](Protocol.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |














### Examples
#### Example: Speech-meeting_sr_winter25_Sitzung6_366631

```yaml
global_uri: ops:366631
language: fr
datetime_begin: '2025-12-19T09:20:00+01:00'
datetime_end: '2025-12-19T09:25:00+01:00'
actor_fullname: Pascal Broulis
actor_id:
  global_uri: https://api.openparldata.ch/v1/persons/18682
  wikidata_uri: https://www.wikidata.org/wiki/Q116407
  label: Pascal Broulis
role: speaker
text: Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec
  attention les différents commentaires qui ont été effectués sur mon postulat. Cela
  reste un postulat, ce n'est pas une motion. D'abord, je ne partage pas l'avis selon
  lequel ce postulat n'apporterait pas une valeur ajoutée. En effet, un "benchmark",
  à savoir un modèle chiffré de performance, permettrait de mieux comprendre les raisons
  des retards que notre pays rencontre en comparaison avec les principaux pays européens.
text_format: html
text_type: final
landing_page: https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631
media_url: https://par-pcache.simplex.tv/content?externalid=366631
media_type: video
media_format: video/mp4

```






</div>