

## Klasse: Membership 


_Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die eine formale Zugehörigkeit darstellt (z.B. Parteimitglied, Kommissionsmitglied, Parlamentarier/in). Im Unterschied zu InterestLink, der externe Interessenbindungen und Interessenkonflikte zu Organisationen ausserhalb des Akteur-Schemas abbildet._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| person_reference | 0..1 <br/> [PersonReference](PersonReference.md) | Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.  |
| group_reference | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.  |
| role_type | 0..1 <br/> [RoleType](RoleType.md) | Rolle der Person in der Mitgliedschaft oder Funktion.  |
| authorized_to_vote | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Person in der Gruppe stimmberechtigt ist. Typischerweise false für Ersatzmitglieder (wenn nicht im Einsatz), Beobachter/innen, Sekretär/innen und Gäste.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Mitgliedschaft derzeit aktiv ist. Kann `valid_from`/`valid_through` ergänzen oder ersetzen. Wenn nicht gesetzt, wird die Aktivität aus den zeitlichen Gültigkeitsfeldern abgeleitet.  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39 für die Schweiz. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [memberships](memberships.md) | range | [Membership](Membership.md) |



















</div>