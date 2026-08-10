

## Klasse: Membership 


_Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die eine formale Zugehörigkeit darstellt (z.B. Parteimitglied, Kommissionsmitglied, Parlamentarier/in). Im Unterschied zu InterestLink, der externe Interessenbindungen und Interessenkonflikte zu Organisationen ausserhalb des Akteur-Schemas abbildet._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| person_reference | 1 <br/> [PersonReference](PersonReference.md) | Kurzreferenz auf eine Person, welche deren Merkmale zum Zeitpunkt der Verknüpfung festhält.  |
| group_reference | 1 <br/> [GroupReference](GroupReference.md) | Kurzreferenz auf eine Gruppe, welche deren Merkmale zum Zeitpunkt der Verknüpfung festhält.  |
| electoral_district | 0..1 <br/> [ElectoralDistrict](ElectoralDistrict.md) | Wahlkreis der Mitgliedschaft. Wird angegeben, wo das Mandat in einem Wahlkreis errungen wurde; er wird deshalb an der Mitgliedschaft geführt und nicht an der Person.  |
| role_type | 0..1 <br/> [RoleType](RoleType.md) | Rolle der Person in der Mitgliedschaft oder Funktion.  |
| authorized_to_vote | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Person in der Gruppe stimmberechtigt ist. Typischerweise false für Ersatzmitglieder (wenn nicht im Einsatz), Beobachter/innen, Sekretär/innen und Gäste.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Mitgliedschaft derzeit aktiv ist. Kann `valid_from`/`valid_through` ergänzen oder ersetzen. Wenn nicht gesetzt, wird die Aktivität aus den zeitlichen Gültigkeitsfeldern abgeleitet.  |
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














### Beispiele
#### Beispiel Membership: The same person at another level with another electoral district

```yaml
global_uri: act:ms_jans_nationalrat
person_reference:
  local_id: 4032
  global_uri: https://www.admin.ch/de/beat-jans
  label: Beat Jans
group_reference:
  global_uri: https://www.parlament.ch/de/organe/nationalrat
  label: Nationalrat
electoral_district:
  global_uri: https://ld.admin.ch/canton/12
  label: Basel-Stadt
role_type:
  role_type_enum: member
authorized_to_vote: true
valid_from: 2010-05-31
valid_through: 2011-12-04
is_active: false

```
#### Beispiel Membership: Executive mandate with a presiding role

```yaml
global_uri: act:ms_jans_regierungsrat_bs
person_reference:
  local_id: 4032
  global_uri: https://www.admin.ch/de/beat-jans
  label: Beat Jans
group_reference:
  local_id: 1300
  global_uri: https://www.regierungsrat.bs.ch/
  label: Regierungsrat Basel-Stadt
role_type:
  role_type_enum: president
  role_label:
  - value: Regierungspräsident
    language: de
authorized_to_vote: true
valid_from: 2021-02-03
valid_through: 2023-12-31
is_active: false

```
#### Beispiel Membership: Person and group from the same delivery with electoral district

```yaml
global_uri: act:ms_jans_grossrat_bs
person_reference:
  local_id: 4032
  global_uri: https://www.admin.ch/de/beat-jans
  label: Beat Jans
group_reference:
  local_id: 33
  global_uri: https://www.grosserrat.bs.ch/
  label: Grosser Rat Basel-Stadt
electoral_district:
  global_uri: https://grosserrat.bs.ch/wahlkreise/kleinbasel
  label: Kleinbasel
role_type:
  role_type_enum: member
authorized_to_vote: true
valid_from: 2001-02-07
valid_through: 2011-04-30
is_active: false

```
#### Beispiel Membership: Ongoing mandate without an end date

```yaml
global_uri: act:ms_jans_bundesrat
person_reference:
  local_id: 4032
  global_uri: https://www.admin.ch/de/beat-jans
  label: Beat Jans
group_reference:
  global_uri: https://www.admin.ch/de/der-bundesrat
  label: Bundesrat
role_type:
  role_type_enum: member
authorized_to_vote: true
valid_from: 2024-01-01
is_active: true

```
#### Beispiel Membership: Parliamentary group membership alongside the council mandate

```yaml
global_uri: act:ms_jans_fraktion_sp_bs
person_reference:
  local_id: 4032
  global_uri: https://www.admin.ch/de/beat-jans
  label: Beat Jans
group_reference:
  global_uri: https://grosserrat.bs.ch/gremien/parteien-und-fraktionen/sp
  label: Sozialdemokratische Partei (SP)
role_type:
  role_type_enum: member
authorized_to_vote: true
valid_from: 2001-02-07
valid_through: 2011-04-30
is_active: false

```
#### Beispiel Membership: Committee membership with a duration of its own

```yaml
global_uri: act:ms_jans_wak_bs
person_reference:
  local_id: 4032
  global_uri: https://www.admin.ch/de/beat-jans
  label: Beat Jans
group_reference:
  global_uri: https://grosserrat.bs.ch/gremien/sachkommissionen/wirtschaft-abgaben
  label: Wirtschafts- und Abgabekommission (WAK)
role_type:
  role_type_enum: member
authorized_to_vote: true
valid_from: 2003-02-12
valid_through: 2011-04-30
is_active: false

```
#### Beispiel Membership: Party membership without temporal information

```yaml
global_uri: act:ms_jans_partei_sp
person_reference:
  local_id: 4032
  global_uri: https://www.admin.ch/de/beat-jans
  label: Beat Jans
group_reference:
  global_uri: https://www.sp-ps.ch/
  label: Sozialdemokratische Partei der Schweiz
role_type:
  role_type_enum: member
is_active: true

```






</div>