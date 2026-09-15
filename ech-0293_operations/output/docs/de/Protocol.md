

## Klasse: Protocol 


_Das nach der Sitzung erstellte Protokoll. Ein Wrapper-Container, der die tatsächlich behandelten Traktanden (protocol_items), Abstimmungen, Wortmeldungen, Wortlaut-Textsegmente und verknüpfte Dokumente bündelt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung bezeichnet er die übergeordnete Sitzung, bei Traktandum, Abstimmung, Wahl, Wortmeldung oder Protokoll die Sitzung, in der der Eintrag entstanden ist.  |
| protocol_items | * <br/> [ProtocolItem](ProtocolItem.md) | Traktanden, wie sie im Protokoll tatsächlich festgehalten wurden.  |
| votings | * <br/> [Voting](Voting.md) | Sammlung der Abstimmungen.  |
| speeches | * <br/> [Speech](Speech.md) | Sammlung der Wortmeldungen.  |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Sammlung von Textsegmenten (z.B. Wortprotokoll).  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [protocols](protocols.md) | range | [Protocol](Protocol.md) |
| [Meeting](Meeting.md) | [protocol_ref](protocol_ref.md) | range | [Protocol](Protocol.md) |














### Beispiele
#### Beispiel Protocol: Protocol as an entity in its own right referenced by the meeting

```yaml
protocols:
- global_uri: ops:protokoll_sr_winter25_sitzung_6
  parent_meeting: parl:sr_winter25_sitzung_6
  protocol_items:
  - global_uri: ops:protokollpunkt_69905
    parent_meeting: parl:sr_winter25_sitzung_6
    agenda_item_type: item
    agenda_item_number: '6'
    agenda_item_position: 4
    agenda_item_title:
    - text: >-
        Postulat Broulis Pascal. Bauprojekte im Mobilitätsbereich. Einen Vergleich
        durchführen, um die Verzögerungen zu verstehen
      language: de
    affair_id: affairs:24.4471
    datetime_begin_actual: '2025-12-19T09:20:00+01:00'
    landing_page: >-
      https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-die-verhandlungen?SubjectId=69905#votum3
    agenda_item_category: agenda_item
    datetime_created: '2026-01-12T00:00:00+01:00'
    datetime_modified: '2026-01-12T00:00:00+01:00'
  datetime_created: '2026-01-12T00:00:00+01:00'
  datetime_modified: '2026-01-12T00:00:00+01:00'

```






</div>