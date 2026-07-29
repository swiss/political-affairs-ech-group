

## Klasse: Election 


_Ein Wahlverfahren zur Wahl von Personen in Positionen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](ElectionTypeEnum.md) | Art des Wahlverfahrens.  |
| type_label | 0..1 <br/> [String](String.md) | Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| title | 0..1 <br/> [String](String.md) | Titel des Elements.  |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](MajorityTypeEnum.md) | Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.).  |
| majority_count | 0..1 <br/> [Integer](Integer.md) | Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind.  |
| result_text | 0..1 <br/> [String](String.md) | Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. „Mit 78 Stimmen angenommen“.  |
| parent_meeting | 0..1 <br/> [String](String.md) | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf.  |
| affair_id | 0..1 <br/> [String](String.md) | Die Verbindung zu den Geschäften des Traktandums.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [elections](elections.md) | range | [Election](Election.md) |



















</div>