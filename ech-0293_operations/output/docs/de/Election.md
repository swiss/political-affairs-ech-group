

## Klasse: Election 


_Eine Wahl, mit der ein parlamentarisches Organ eine oder mehrere Personen für ein Amt oder eine Funktion bestimmt. Im Unterschied zur Abstimmung (Voting), die über Sachfragen entscheidet, ist die Wahl ein Personenentscheid: Sie erfolgt oft geheim und erfordert meist das absolute Mehr, während Abstimmungen meist offen sind. Die Präsidentin oder der Präsident, die an Abstimmungen nicht teilnehmen, stimmen bei Wahlen mit. Jeder Wahlgang wird als eigene Wahl erfasst; die Wahlgänge einer Wahl sind über das gemeinsame Traktandum verbunden — etwa ein erster Wahlgang mit absolutem Mehr, der ohne Ergebnis bleibt, und ein zweiter Wahlgang, in dem das relative Mehr genügt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](ElectionTypeEnum.md) | Art des Wahlverfahrens.  |
| type_label | 0..1 <br/> [String](String.md) | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| title | 0..1 <br/> [String](String.md) | Titel der Wahl, z.B. „Wahl Kommissionspräsidium WAK“.  |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Anzahl abwesender Mitglieder, die nicht teilnehmen konnten. Ob eine Abwesenheit entschuldigt war, hält die Anwesenheitsliste (Attendance) fest.  |
| total | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](MajorityTypeEnum.md) | Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.).  |
| majority_count | 0..1 <br/> [Integer](Integer.md) | Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind.  |
| result_text | 0..1 <br/> [String](String.md) | Freitext, der das Ergebnis beschreibt, z.B. „Mit 120 zu 75 Stimmen bei 5 Enthaltungen angenommen“. Bei Abstimmungen wird der kategorische Entscheid (angenommen, abgelehnt, Kenntnisnahme …) nicht hier, sondern in der Resolution (resolution_type) des Traktandums festgehalten.  |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung bezeichnet er die übergeordnete Sitzung, bei Traktandum, Abstimmung, Wahl, Wortmeldung oder Protokoll die Sitzung, in der der Eintrag entstanden ist.  |
| parent_protocol | 0..1 <br/> [Protocol](Protocol.md) | Das Protokoll, in dem die Abstimmung oder Wahl festgehalten ist. Abgestimmt wird im Verlauf der Sitzung, weshalb die Abstimmung im Protokoll und nicht in der vorgängig geplanten Traktandenliste verankert ist: Was traktandiert wurde, sagt noch nicht, worüber tatsächlich abgestimmt wurde. Umgekehrt führt das Protokoll seine Abstimmungen und Wahlen als Listen (votings, elections).  |
| parent_protocol_item | 0..1 <br/> [ProtocolItem](ProtocolItem.md) | Das protokollierte Traktandum (ProtocolItem), unter dem abgestimmt oder gewählt wurde. Entfällt, wenn ohne Traktandierung abgestimmt wurde; die Zuordnung zur Sitzung ergibt sich dann allein aus parent_protocol und parent_meeting.  |
| affair_id | 0..1 <br/> [String](String.md) | Identifikator des Geschäfts (eCH-0295), auf das sich der Eintrag bezieht. Administrative Traktanden (z.B. Genehmigung des Protokolls) haben kein Geschäft. Ein Geschäft durchläuft in der Regel mehrere Traktanden — in der Gesetzgebung etwa Eintretensdebatte, Detailberatung, Schlussabstimmung und gegebenenfalls die Differenzbereinigung zwischen den Räten.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf das handelnde Organ/Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [elections](elections.md) | range | [Election](Election.md) |
| [Protocol](Protocol.md) | [elections](elections.md) | range | [Election](Election.md) |



















</div>