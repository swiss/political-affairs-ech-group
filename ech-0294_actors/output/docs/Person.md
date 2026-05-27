

# Class: Person 


_[de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Berufen._

_[en] A person with identifiers, names, addresses, citizenships, and occupations._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.). [en] Option to assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| label_long | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.). [en] Option to assign an extended label to a structured piece of information (e.g., display name with title, position, etc.).  |
| birth_year | 0..1 <br/> [Integer](Integer.md) | [de] Geburtsjahr. [en] Year of birth. Only to be used, if there is no full `birthDate` available.  |
| birth_date | 0..1 <br/> [Date](Date.md) | [de] Genaues Geburtsdatum. [en] Exact date of birth if available and public. This field has precedence over the field `birthYear`.  |
| death_date | 0..1 <br/> [Date](Date.md) | [de] Genaues Todesdatum. [en] Exact date of death.  |
| picture | 0..1 <br/> [Uri](Uri.md) | [de] Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF). [en] Link to an image (preferred: PNG, then JPG, then GIF).  |
| names | * <br/> [Name](Name.md) | [en] Names of the person with type and value. [de] Namen der Person mit Typ und Wert.  |
| addresses | * <br/> [Address](Address.md) | [de] Adressen mit Typ (privat, geschäftlich, lokal). [en] Addresses with type (private, business, local).  |
| language_proficiencies | * <br/> [LanguageProficiency](LanguageProficiency.md) | [de] Sprachkompetenzen der Person. [en] Language proficiencies of the person.  |
| citizenships | * <br/> [Citizenship](Citizenship.md) | [de] Staatsbürgerschaften der Person. [en] Citizenships of the person.  |
| genders | * <br/> [Gender](Gender.md) | [de] Geschlecht der Person. [en] Gender of the person.  |
| occupations | * <br/> [Occupation](Occupation.md) | [de] Berufe oder Tätigkeiten der Person. [en] Occupations or professions of the person.  |
| trainings | * <br/> [Training](Training.md) | [de] Ausbildungen oder Bildungen der Person. [en] Trainings or educations of the person.  |
| contacts | * <br/> [Contact](Contact.md) | [en] Contact information (email, website, social media). [de] Kontaktinformationen (E-Mail, Website, Social Media).  |
| electoral_district | 0..1 <br/> [ElectoralDistrict](ElectoralDistrict.md) | [de] Link zum Wahlbezirk. [en] Link to the electoral district.  |
| interest_links | * <br/> [InterestLink](InterestLink.md) | [de] Sammlung von Interessenbindungen. [en] Collection of interest links.range: InterestLink  |
| local_id | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [persons](persons.md) | range | [Person](Person.md) |














### Examples
#### Example: Person-swiss_politicians_Beat_Jans

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
- training_type: uni
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
#### Example: Person-douglas_adams_Douglas_Adams

```yaml
global_uri: https://www.wikidata.org/wiki/Q42
label: Douglas Adams
label_long: Douglas Noël Adams
birth_year: 1952
birth_date: 1952-03-11
picture: https://commons.wikimedia.org/wiki/File:Douglas_adams_portrait.jpg
names:
- name_type: PersonFirstName
  value: Douglas
- name_type: PersonOfficialName
  value: Adams
  valid_from: 1952-03-11
addresses:
- address_type: privateAddress
  address_uri: https://www.wikidata.org/wiki/Q42#P969
  street_address: 1234 Fictional St, London, UK
  postal_code: 12345
  postal_locality: London
language_proficiencies:
- language: en
  is_correspondence: true
  is_native: true
citizenships:
- country: GB
  valid_from: 1952-03-11
genders:
- gender_code: male
  valid_from: 1952-03-11
  pronouns:
  - he
  - him
occupations:
- label: writer
  valid_from: 1979-01-01
  valid_through: 2001-05-11
  is_active: false
  is_paid: true
trainings:
- training_type: schulabschluss
  value: High School Diploma
contacts:
- contact_type: email
  value: douglas.adams@adams-familiy.org
electoral_district:
  district: London Central
  valid_from: 2020-01-01
  valid_through: 2025-01-01

```






</div>