

## Class: Election 


_[en] An election procedure for selecting persons to positions._

_[de] Ein Wahlverfahren zur Wahl von Personen in Positionen._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | [en] The date and time when the meeting or voting begins. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | [en] The date and time when the meeting or voting ends. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](ElectionTypeEnum.md) | Type of election procedure |
| type_label | 0..1 <br/> [String](String.md) | [en] Custom type label when standard type values don't apply. [de] Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.  |
| title | 0..1 <br/> [String](String.md) | None |
| landing_page | 0..1 <br/> [String](String.md) | [en] URL providing further information. [de] URL mit weiteren Informationen.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | [en] Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list. [de] Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total | 0..1 <br/> [Integer](Integer.md) | [en] Total number of votes, excluding absent and president's vote. [de] Gesamtzahl der Stimmen, ohne abwesende und Präsidentenstimmen.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](MajorityTypeEnum.md) | [en] Type of majority required for the vote (absolute, two-thirds, etc.). [de] Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.).  |
| majority_count | 0..1 <br/> [Integer](Integer.md) | [en] Number of votes required for the relevant majority threshold. [de] Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind.  |
| result_text | 0..1 <br/> [String](String.md) | [en] Free text describing the outcome of the vote, e.g., "Accepted with 78 votes". [de] Freitext zur Beschreibung des Ergebnisses der Abstimmung, z.B. "Mit 78 Stimmen angenommen".  |
| parent_meeting | 0..1 <br/> [String](String.md) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | [en] If needed, this slot builds a hierarchy of agenda items. [de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten auf.  |
| affair_id | 0..1 <br/> [String](String.md) | [en] The connection to the affairs (business items) of the agenda item. [de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | [en] Reference to the acting body/organ (lightweight snapshot at time of linking). [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| documents | * <br/> [Work](Work.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [elections](elections.md) | range | [Election](Election.md) |



















</div>