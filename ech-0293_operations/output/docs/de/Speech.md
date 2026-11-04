

## Klasse: Speech 


_Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt): der mündliche Beitrag einer Person in einer parlamentarischen Sitzung und damit das zentrale Instrument der politischen Debatte und Meinungsäusserung im Parlament. Wortmeldungen haben verschiedene Formen — Hauptvoten (ausführliche Stellungnahmen zu einem Geschäft, Begründung von Anträgen, Darlegung der Fraktionsmeinung), Kurzinterventionen (Zwischenfragen, Richtigstellungen), Fraktionserklärungen, vorgetragen durch die Fraktionssprecherin oder den Fraktionssprecher, sowie Regierungsvoten (Beantwortung von Fragen, Verteidigung von Vorlagen). Eine Wortmeldung hält fest, wer wann unter welchem Traktandum gesprochen hat, mit dem Wortlaut als Text und, wo vorhanden, als Audio- oder Videoaufzeichnung. Sie kann auf zwei Wegen geliefert werden: eingebettet im Protokoll (Protocol.speeches), wo sich die Sitzung aus dem umgebenden Protokoll ergibt, das Traktandum aber nicht, oder flach in Container.speeches, wo ohne Referenzen jeder Bezug fehlte. parent_meeting und parent_agenda_item werden deshalb in beiden Fällen geführt; sie tragen dieselben Werte wie bei Voting und Election und machen die Wortmeldung unabhängig davon auswertbar, aus welcher Lieferform sie stammt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung bezeichnet er die übergeordnete Sitzung, bei Abstimmung, Wahl, Wortmeldung, Anwesenheitsliste oder Protokoll die Sitzung, in der der Eintrag entstanden ist. Traktanden führen ihn nicht: Sie sind in ihre Sitzung eingebettet.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem Traktandum bildet er eine Hierarchie von Traktanden — z.B. eine Traktandengruppe „Gesetzesberatungen“ mit den Untertraktanden „Energiegesetz (Detailberatung)“ und „Energiegesetz (Schlussabstimmung)“; bei einer Wortmeldung bezeichnet er das Traktandum, unter dem sie erfolgte.  |
| language | 0..1 <br/> [String](String.md) | Sprache, in der gesprochen wurde, z.B. de (Deutsch), fr (Französisch), it (Italienisch), rm (Rätoromanisch) oder en (Englisch).  |
| start | 0..1 <br/> [String](String.md) | Startangabe oder Position.  |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Datum und Uhrzeit, zu der die Wortmeldung begann. Zusammen mit datetime_end ermöglicht sie die genaue Referenzierung in Audio- und Videoaufzeichnungen, die Analyse der Redezeit pro Person oder Fraktion und die Kontrolle der Einhaltung von Zeitlimiten.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | Datum und Uhrzeit, zu der die Wortmeldung endete; die Redezeit ergibt sich aus der Differenz zu datetime_begin.  |
| actor_fullname | 0..1 <br/> [String](String.md) | Name der sprechenden Person, für den schnellen Zugriff ohne Auflösung von actor_id.  |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | Die sprechende Person, als Referenz auf eine Person gemäss eCH-0294.  |
| role | 0..1 <br/> [String](String.md) | Rolle, in der die Person spricht, z.B. Fraktionspräsidentin oder Fraktionspräsident, Berichterstatterin oder Berichterstatter, Bundesrätin oder Bundesrat.  |
| text | 1 <br/> [String](String.md) | Wortlaut der Wortmeldung.  |
| text_format | 0..1 <br/> [String](String.md) | Format des Textes (text, html, html_with_timestamps).  |
| text_type | 0..1 <br/> [String](String.md) | Fassung des Wortlauts: das Rohtranskript (wörtliche, unbearbeitete Niederschrift mit Füllwörtern, direkt nach der Sitzung verfügbar) oder das bearbeitete Transkript (redaktionell überarbeitet und grammatikalisch korrigiert, die offizielle Protokollversion).  |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen.  |
| media_url | 0..1 <br/> [String](String.md) | URL der Audio- oder Videoaufzeichnung der Wortmeldung oder des Livestreams während der Sitzung, der danach archiviert wird.  |
| media_type | 0..1 <br/> [String](String.md) | Art der Aufzeichnung: Audio (Originalton der Wortmeldung) oder Video (visuelle Aufzeichnung, in der Regel bei Plenarsitzungen).  |
| media_format | 0..1 <br/> [String](String.md) | MIME-Typ der Aufzeichnung, z.B. audio/mpeg (MP3), audio/wav, video/mp4 oder video/webm.  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |
| [Protocol](Protocol.md) | [speeches](speeches.md) | range | [Speech](Speech.md) |














### Beispiele
#### Beispiel Speech: Speech with verbatim text and video recording

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