

## Klasse: Person 


_Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Berufen._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 1 <br/> [String](String.md) | Obligatorischer Kurzname zur Identifikation der Person innerhalb der Organisation (z.B. mit Geburtsjahr zur Unterscheidung von Personen mit gleichem Namen). Bevorzugt: PersonOfficialName (amtlicher Name) kombiniert mit PersonCallFirstName (Rufname).  |
| label_long | 0..1 <br/> [String](String.md) | Optionaler langer Anzeigename mit akademischen Titeln und vollständigem amtlichem Namen (z.B. "Dr. Maria Muster-Beispiel").  |
| birth_year | 0..1 <br/> [Integer](Integer.md) | Geburtsjahr. Nur zu verwenden, wenn kein vollständiges `birthDate` vorhanden ist.  |
| birth_date | 0..1 <br/> [Date](Date.md) | Genaues Geburtsdatum, sofern verfügbar und öffentlich. Dieses Feld hat Vorrang vor dem Feld `birthYear`.  |
| death_date | 0..1 <br/> [Date](Date.md) | Genaues Todesdatum.  |
| picture | 0..1 <br/> [Uri](Uri.md) | Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF).  |
| names | * <br/> [Name](Name.md) | Namen der Person mit Typ und Wert.  |
| addresses | * <br/> [Address](Address.md) | Adressen mit Typ (privat, geschäftlich, lokal).  |
| language_proficiencies | * <br/> [LanguageProficiency](LanguageProficiency.md) | Sprachkompetenzen der Person.  |
| citizenships | * <br/> [Citizenship](Citizenship.md) | Staatsbürgerschaften der Person.  |
| genders | * <br/> [Gender](Gender.md) | Geschlecht der Person.  |
| occupations | * <br/> [Occupation](Occupation.md) | Berufe oder Tätigkeiten der Person.  |
| trainings | * <br/> [Training](Training.md) | Ausbildungen oder Bildungen der Person. Richtlinie: Im Grundsatz nur die höchste Ausbildung angeben.  |
| contacts | * <br/> [Contact](Contact.md) | Kontaktinformationen (E-Mail, Website, Social Media). Richtlinie: E-Mail ist quasi-obligatorisch und sollte wenn vorhanden immer angegeben werden.  |
| interest_links | * <br/> [InterestLink](InterestLink.md) | Sammlung von Interessenbindungen.  |
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
| [Container](Container.md) | [persons](persons.md) | range | [Person](Person.md) |














### Beispiele
#### Beispiel: Name variant alongside the official double name

```yaml
local_id: 280958
global_uri: https://parlament.winterthur.ch/behoerdenmitglieder/280958
label: Cristina Bozzi-Brunel
names:
- name_type: PersonFirstName
  value: Cristina
- name_type: PersonOfficialName
  value: Bozzi-Brunel
- name_type: PersonOriginalName
  value: Brunel

```
#### Beispiel: Call name differing from the official first name

```yaml
local_id: 1269
global_uri: >-
  https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269
label: Gerri Beretta-Piccoli
names:
- name_type: PersonFirstName
  value: Fausto
- name_type: PersonCallFirstName
  value: Gerri
- name_type: PersonOfficialName
  value: Beretta-Piccoli

```
#### Beispiel: Non-binary gender entry with occupation and training

```yaml
local_id: 72c7232be92944e3876f3b6723824ff9
global_uri: >-
  https://stadtrat.bern.ch/de/mitglieder/detail.php?gid=72c7232be92944e3876f3b6723824ff9
label: Sofia Fisch
birth_year: 1996
names:
- name_type: PersonFirstName
  value: Sofia
- name_type: PersonOfficialName
  value: Fisch
genders:
- gender_code: non_binary
  label: divers
occupations:
- label: Jurist*in
  is_active: true
trainings:
- training_type: '3223'
  value: MLaw

```
#### Beispiel: Telling apart persons with identical names via the label

```yaml
local_id: 6447
global_uri: https://www.ur.ch/behoerdenmitglieder/6447
label: Alois Arnold (1981)
birth_year: 1981
names:
- name_type: PersonFirstName
  value: Alois
- name_type: PersonOfficialName
  value: Arnold

```
#### Beispiel: Fully recorded person

```yaml
local_id: 4032
global_uri: https://www.admin.ch/de/beat-jans
wikidata_uri: http://www.wikidata.org/entity/Q813067
label: Beat Jans
label_long: Beat Jans, dipl. nat. ETH
birth_year: 1964
birth_date: 1964-07-12
picture: https://commons.wikimedia.org/wiki/File:Beat_Jans_(2026)_(cropped).jpg
names:
- name_type: PersonFirstName
  value: Beat
- name_type: PersonOfficialName
  value: Jans
  valid_from: 1964-07-12
addresses:
- address_type: businessAddress
  postal_locality: Basel-Stadt
language_proficiencies:
- language: de
  is_correspondence: true
  is_native: true
citizenships:
- country: CH
  valid_from: 1964-07-12
genders:
- gender_code: male
  valid_from: 1964-07-12
occupations:
- label: Politiker
  valid_from: 1964-01-01
  is_active: true
trainings:
- training_type: '3223'
  value: dipl. nat. ETH
contacts:
- contact_type: email
  value: beat.jans@admin.ch
- contact_type: contact_website
  value: http://www.beat-jans.ch

```
#### Beispiel: Telling apart persons with identical names via the label second person

```yaml
local_id: 6370
global_uri: https://www.ur.ch/behoerdenmitglieder/6370
label: Alois Arnold (1965)
birth_year: 1965
names:
- name_type: PersonFirstName
  value: Alois
- name_type: PersonOfficialName
  value: Arnold

```






</div>