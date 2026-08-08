

## Klasse: Speech 


_Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| language | 0..1 <br/> [String](String.md) | Sprachcode im ISO 639-1 Format (zwei Kleinbuchstaben, z.B. "de", "fr", "it", "en").  |
| start | 0..1 <br/> [String](String.md) | Startangabe oder Position.  |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| actor_fullname | 0..1 <br/> [String](String.md) | Vollständiger Name der Akteurin oder des Akteurs bzw. der Person.  |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | Referenz auf die handelnde Person (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| role | 0..1 <br/> [String](String.md) | Rolle der Person (z.B. Kommissionssprecherin oder Kommissionssprecher).  |
| text | 1 <br/> [String](String.md) | Textinhalt des Elements.  |
| text_format | 0..1 <br/> [String](String.md) | Format des Textes (text, html, html_with_timestamps).  |
| text_type | 0..1 <br/> [String](String.md) | Typ des Textes (Rohfassung, bearbeitete Fassung).  |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen.  |
| media_url | 0..1 <br/> [String](String.md) | URL zur Mediendatei (Audio/Video).  |
| media_type | 0..1 <br/> [String](String.md) | Art des Mediums (Audio, Video, Dokument).  |
| media_format | 0..1 <br/> [String](String.md) | MIME-Typ der Mediendatei.  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |
| [Protocol](Protocol.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |














### Beispiele
#### Beispiel: Speech with verbatim text and video recording

```yaml
global_uri: ops:366631
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
  Je remercie la rapporteuse pour son rapport exhaustif. J'ai également lu avec attention
  les différents commentaires qui ont été effectués sur mon postulat. Cela reste un
  postulat, ce n'est pas une motion. D'abord, je ne partage pas l'avis selon lequel
  ce postulat n'apporterait pas une valeur ajoutée. En effet, un "benchmark", à savoir
  un modèle chiffré de performance, permettrait de mieux comprendre les raisons des
  retards que notre pays rencontre en comparaison avec les principaux pays européens.
text_format: html
text_type: final
landing_page: >-
  https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-videos?TranscriptId=366631
media_url: https://par-pcache.simplex.tv/content?externalid=366631
media_type: video
media_format: video/mp4

```






</div>