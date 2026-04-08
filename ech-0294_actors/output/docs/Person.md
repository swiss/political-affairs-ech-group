---
search:
  boost: 10.0
---

# Class: Person 


_[de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Berufen._

_[en] A person with identifiers, names, addresses, citizenships, and occupations._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.md) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... | direct |
| [label_long](label_long.md) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel z... | direct |
| [birth_year](birth_year.md) | 0..1 <br/> [Integer](Integer.md) | [de] Geburtsjahr | direct |
| [birth_date](birth_date.md) | 0..1 <br/> [Date](Date.md) | [de] Genaues Geburtsdatum | direct |
| [death_year](death_year.md) | 0..1 <br/> [Integer](Integer.md) | [de] Todesjahr | direct |
| [death_date](death_date.md) | 0..1 <br/> [Date](Date.md) | [de] Genaues Todesdatum | direct |
| [picture](picture.md) | 0..1 <br/> [String](String.md) | [de] Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF) | direct |
| [names](names.md) | * <br/> [Name](Name.md) | [en] Names of the person with type and value | direct |
| [addresses](addresses.md) | * <br/> [Address](Address.md) | [de] Adressen mit Typ (privat, geschäftlich, lokal) | direct |
| [language_proficiencies](language_proficiencies.md) | * <br/> [LanguageProficiency](LanguageProficiency.md) | [de] Sprachkompetenzen der Person | direct |
| [citizenships](citizenships.md) | * <br/> [Citizenship](Citizenship.md) | [de] Staatsbürgerschaften der Person | direct |
| [genders](genders.md) | * <br/> [Gender](Gender.md) | [de] Geschlecht der Person | direct |
| [occupations](occupations.md) | * <br/> [Occupation](Occupation.md) | [de] Berufe oder Tätigkeiten der Person | direct |
| [trainings](trainings.md) | * <br/> [Training](Training.md) | [de] Ausbildungen oder Bildungen der Person | direct |
| [contacts](contacts.md) | * <br/> [Contact](Contact.md) | [en] Contact information (email, website, social media) | direct |
| [electoral_district](electoral_district.md) | 0..1 <br/> [ElectoralDistrict](ElectoralDistrict.md) | [de] Link zum Wahlbezirk | direct |
| [interest_links](interest_links.md) | * <br/> [InterestLink](InterestLink.md) | [de] Sammlung von Interessenbindungen | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](HasIdentification.md) |
| [date_created](date_created.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_created](datetime_created.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [date_modified](date_modified.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_modified](datetime_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [persons](persons.md) | range | [Person](Person.md) |
| [Membership](Membership.md) | [concerned_person](concerned_person.md) | range | [Person](Person.md) |
| [InterestLink](InterestLink.md) | [concerned_person](concerned_person.md) | range | [Person](Person.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Person |
| native | act:Person |







