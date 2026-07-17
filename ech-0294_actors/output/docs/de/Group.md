

## Klasse: Group 


_Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission, Parlament, Departement)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| group_type | 1 <br/> [GroupType](GroupType.md) | Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament oder ähnliches. Die genaue Benennung und Beschreibung der Gruppierung wird über `label` gemacht.  |
| label | 1 <br/> [String](String.md) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abkürzung (kann mehrsprachig sein).  |
| description | * <br/> [MultilingualValue](MultilingualValue.md) | Kurze Beschreibung der Gruppierung.  |
| landing_page | 0..1 <br/> [Uri](Uri.md) | Website mit weiteren Informationen.  |
| parent_groups | * <br/> [Uriorcurie](Uriorcurie.md) | Übergeordnete Gruppe. Zum Beispiel die Mutterpartei zu Kantonalparteien, oder zur Beschreibung der Hierarchie in der Exekutive. Auch zur Verknüpfung von Subkommissionen mit Kommissionen oder Fraktionen mit Parlament und Partei. (parentGroup wird typischerweise im selben group_type verwendet, typenübergreifende Verknüpfungen sind aber erlaubt, z.B. Fraktion → Parlament und Fraktion → Partei.)  |
| spatial | 0..1 <br/> [String](String.md) | Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer oder Land). Formate: Gemeinde: ld.admin.ch/municipality/1234, Kanton: ld.admin.ch/canton/23, Bund: ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](Contact.md) | Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.  |
| addresses | * <br/> [Address](Address.md) | Adressen mit Typ (privat, geschäftlich, lokal).  |
| statutes_url | 0..1 <br/> [String](String.md) | URL zu Parteistatuten (PDF oder Webseite; optional für Parteien).  |
| party_color | 0..1 <br/> [String](String.md) | Parteifarbe als Hexadezimalwert (optional für Parteien, z.B. "#FF0000").  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [groups](groups.md) | range | [Group](Group.md) |



















</div>