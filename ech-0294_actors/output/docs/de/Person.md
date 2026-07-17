

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
| electoral_district | 0..1 <br/> [ElectoralDistrict](ElectoralDistrict.md) | Link zum Wahlbezirk.  |
| interest_links | * <br/> [InterestLink](InterestLink.md) | Sammlung von Interessenbindungen.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [persons](persons.md) | range | [Person](Person.md) |














### Beispiele
#### Beispiel: Person-swiss_politicians_Beat_Jans

```yaml
local_id: 4032
global_uri: https://data-example.parlament.ch/person/4032
wikidata_uri: https://www.wikidata.org/wiki/Q813067
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
electoral_district:
  district: Basel-Stadt
  valid_from: 2010-01-01

```






</div>