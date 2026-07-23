

## Class: Person 


_A person with identifiers, names, addresses, citizenships, and occupations._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 1 <br/> [String](String.md) | Mandatory short display name to identify the person within the organisation (e.g. with added birth year to distinguish persons with the same name). Preferred: PersonOfficialName combined with PersonCallFirstName.  |
| label_long | 0..1 <br/> [String](String.md) | Optional long display name including academic titles and full official name (e.g. "Dr. Maria Muster-Beispiel").  |
| birth_year | 0..1 <br/> [Integer](Integer.md) | Year of birth. Only to be used, if there is no full `birthDate` available.  |
| birth_date | 0..1 <br/> [Date](Date.md) | Exact date of birth if available and public. This field has precedence over the field `birthYear`.  |
| death_date | 0..1 <br/> [Date](Date.md) | Exact date of death.  |
| picture | 0..1 <br/> [Uri](Uri.md) | Link to an image (preferred: PNG, then JPG, then GIF).  |
| names | * <br/> [Name](Name.md) | Names of the person with type and value.  |
| addresses | * <br/> [Address](Address.md) | Addresses with type (private, business, local).  |
| language_proficiencies | * <br/> [LanguageProficiency](LanguageProficiency.md) | Language proficiencies of the person.  |
| citizenships | * <br/> [Citizenship](Citizenship.md) | Citizenships of the person.  |
| genders | * <br/> [Gender](Gender.md) | Gender of the person.  |
| occupations | * <br/> [Occupation](Occupation.md) | Occupations or professions of the person.  |
| trainings | * <br/> [Training](Training.md) | Trainings or educations of the person. Guideline: generally only provide the highest qualification obtained.  |
| contacts | * <br/> [Contact](Contact.md) | Contact information (email, website, social media). Guideline: email is quasi-mandatory and should always be provided where available.  |
| interest_links | * <br/> [InterestLink](InterestLink.md) | Collection of interest links.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





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
- training_type: '3223'
  value: dipl. nat. ETH
contacts:
- contact_type: email
  value: beat.jans@admin.ch
- contact_type: contact_website
  value: http://www.beat-jans.ch

```
#### Example: Person-swiss_politicians_Gerri_Beretta-Piccoli

```yaml
local_id: 1269
global_uri: https://www4.ti.ch/poteri/gc/parlamento/composizione-del-parlamento/composizione-nelle-ultime-legislature/dettaglio-deputati/?user_gcparlamento_pi3%5BcanID%5D=1269
label: Gerri Beretta-Piccoli
names:
- name_type: PersonFirstName
  value: Fausto
- name_type: PersonCallFirstName
  value: Gerri
- name_type: PersonOfficialName
  value: Beretta-Piccoli

```
#### Example: Person-swiss_politicians_Cristina_Bozzi-Brunel

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
#### Example: Person-swiss_politicians_Alois_Arnold_1965

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
#### Example: Person-swiss_politicians_Alois_Arnold_1981

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






</div>