

## Class: Speech 


_A speech or statement made during a meeting (also called Votum or speaker segment): the oral contribution of a person in a parliamentary sitting and thus the central instrument of political debate and of expressing opinions in parliament. Speeches take various forms — main statements (detailed positions on an affair, justification of motions, presentation of the parliamentary group's opinion), short interventions (interjected questions, corrections), declarations by a parliamentary group delivered by its spokesperson, and statements by members of the government (answering questions, defending bills). A speech records who spoke when and under which agenda item, with the wording as text and, where available, as an audio or video recording. It can be delivered in two ways: embedded in the protocol (Protocol.speeches), where the meeting follows from the surrounding protocol but the agenda item does not, or flat in Container.speeches, where without references any link would be missing. parent_meeting and parent_agenda_item are therefore set in both cases; they carry the same values as on Voting and Election and make the speech evaluable regardless of the delivery form it came in._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on a voting, election, speech, attendance list or protocol it names the meeting in which the record arose. Agenda items do not carry it: they are embedded in their meeting.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifier of the agenda item this record belongs to. On an agenda item it builds a hierarchy of agenda items — e.g. an item group "Gesetzesberatungen" with the sub-items "Energiegesetz (Detailberatung)" and "Energiegesetz (Schlussabstimmung)"; on a speech it names the agenda item under which the speech was given.  |
| language | 0..1 <br/> [String](String.md) | Language in which the speech was given, e.g. de (German), fr (French), it (Italian), rm (Romansh) or en (English).  |
| start | 0..1 <br/> [String](String.md) | Start indicator or position.  |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Date and time at which the speech began. Together with datetime_end it allows the speech to be located precisely in audio and video recordings, speaking time to be analysed per person or parliamentary group, and compliance with time limits to be checked.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | Date and time at which the speech ended; the speaking time results from the difference to datetime_begin.  |
| actor_fullname | 0..1 <br/> [String](String.md) | Name of the speaking person, for quick access without resolving person_reference.  |
| person_reference | 0..1 <br/> [PersonReference](PersonReference.md) | The speaking person, as a reference to a person according to eCH-0294.  |
| role | 0..1 <br/> [String](String.md) | Role in which the person speaks, e.g. president of a parliamentary group, rapporteur or member of the Federal Council.  |
| text | 1 <br/> [String](String.md) | Wording of the speech.  |
| text_format | 0..1 <br/> [String](String.md) | Format of text (text, html, html_with_timestamps).  |
| text_type | 0..1 <br/> [String](String.md) | Version of the wording: the raw transcript (verbatim, unedited and including filler words, available directly after the sitting) or the edited transcript (editorially revised and grammatically corrected, the official protocol version).  |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information.  |
| media_url | 0..1 <br/> [String](String.md) | URL of the audio or video recording of the speech, or of the live stream during the sitting, which is archived afterwards.  |
| media_type | 0..1 <br/> [String](String.md) | Type of the recording: audio (original sound of the speech) or video (visual recording, usually of plenary sittings).  |
| media_format | 0..1 <br/> [String](String.md) | MIME type of the recording, e.g. audio/mpeg (MP3), audio/wav, video/mp4 or video/webm.  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |
| [Protocol](Protocol.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |














### Examples
#### Example Speech: Speech with verbatim text and video recording

```yaml
speeches:
- global_uri: ops:366631
  parent_meeting: parl:sr_winter25_sitzung_6
  parent_agenda_item: ops:69905
  language: fr
  datetime_begin: '2025-12-19T09:20:00+01:00'
  datetime_end: '2025-12-19T09:25:00+01:00'
  actor_fullname: Pascal Broulis
  person_reference:
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