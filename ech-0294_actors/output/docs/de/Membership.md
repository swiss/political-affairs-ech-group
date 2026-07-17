

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
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [memberships](memberships.md) | range | [Membership](Membership.md) |



















</div>