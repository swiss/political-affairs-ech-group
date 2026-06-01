---
title: "eCH-0294 Politische Akteure: Personen, Gruppen und Organe"
lang: de
toc: false
---

| **Name**              | **Politische Akteure: Personen, Gruppen und Organe**                                                                       |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------|
| **eCH-Nummer**        | eCH-0294                                                                                                                   |
| **Kategorie**         | Entwurf                                                                                                                    |
| **Reifegrad**         | Fachgruppen Internes Review                                                                                                |
| **Version**           | 0.1                                                                                                                        |
| **Status**            |                                                                                                                            |
| **Beschluss am**      |                                                                                                                            |
| **Ausgabedatum**      |                                                                                                                            |
| **Ersetzt Version**   | 0.0                                                                                                                        |
| **Voraussetzungen**   | eCH-0292 (Gemeinsame Datenelemente)                                                                                        |
| **Beilagen**          | -                                                                                                                          |
| **Sprachen**          | English (Original)                                                                                                         |
| **Autoren**           | Fachgruppe politische Geschäfte: Julie Silberstein, Laurence Brandenberger, Daniela Koller, Thomas Roth, Stefan Oderbolz, Fabian Davolio, Orhan Saeedi   |
| **Herausgeber / Vertrieb** | Verein eCH, Räffelstr. 20, 8045                                                                                       |

# Summary

Management summary of the document.

# Table of Contents

< manually insert TOC here >



# Einführung

Der Inhalt dieses Substandards sind die politischen Akteure, seien es Personen (Rats- oder Verwaltungsmitglieder) oder Gruppen (Parteien, Fraktionen, Gremien, Kommissionen und Verbände).

Zum einen wird eine Struktur definiert, die es erlaubt, Informationen in Ratsinformationssystemen oder ähnlichen Systemen der Öffentlichkeit strukturiert zur Verfügung zu stellen. Zum anderen werden den politischen Akteuren eindeutige Identifikatoren zugeteilt, mit dem Ziel, aus anderen Standards dieser Fachgruppe darauf referenzieren zu können.

Es wurde bei der Definition darauf geachtet, dass es den publizierenden Organisationen ermöglicht wird, alle Informationen möglichst strukturiert zu veröffentlichen. Dies erlaubt es, für die Konsumenten einen maximalen Nutzen zu erzielen. Es ist aber jeweils auch möglich auszudrücken, wenn Informationen nicht in der maximalen Detailstufe vorhanden sind. (Es kann zum Beispiel bei einem Vornamen angegeben werden, ob es sich um den Rufnamen oder den amtlichen Namen handelt. Falls diese Information aber nicht vorhanden ist, kann der Name auch ohne diese Zusatzinformation publiziert werden.)

## Ziele des Standards und erhoffte Wirkung

Das Ziel des Standards ist es, Organisationen, welche Informationen zu politischen Geschäften veröffentlichen, ein Datenmodell zur Verfügung zu stellen. Die Wirkung, die dabei erhofft wird, ist eine einheitliche Informationsgrundlage zu den politischen Geschäften in der Schweiz über alle föderalen Ebenen hinweg. Damit können die Informationen im politischen Diskurs besser gelesen, verarbeitet und verstanden werden. Die Transparenz und Nachvollziehbarkeit der Entscheidungen im politischen System der Schweiz soll weiter erhöht werden.

Besondere Ziele des Substandards sind, die Akteure im politischen Prozess identifizierbar zu machen und mit den rechtlich nötigen Informationen auszugestalten. Als weiteres Ziel wird ein langfristiger Abgleich der Akteure über die föderalen Stufen angestrebt. Der Substandard bietet eine Struktur an, welche von den jeweiligen Organisationen (Städte, Kantone und Bund) nach deren Anforderungen und rechtlichem Kontext umgesetzt werden kann.

## Identifizierte Zielgruppen

Die Arbeitsgruppe hat folgende Zielgruppen für den Standard identifiziert, welche direkt oder indirekt angesprochen werden. Diese Zielgruppen wurden als Leitfaden bei Entscheidungen zum Standard als Bedarfsträger identifiziert.

* Städte/Gemeinden, Kantone und Eidgenossenschaft (Publikation im Auftrag)
* Politikerinnen und Politiker (Entstehung und Konsum)
* Journalismus, Forschung: Politikwissenschaft, Historiker, Open-Data-Portale, Politmonitor/OParlData (Konsum, Monitoring und Veredelung von Informationen)
* Öffentliche Verwaltung: Statistikämter und Archive (Auswertung, Monitoring, Archivierung)
* Öffentlichkeit (Konsum)

## Arbeitsvorgang

Folgende Themen wurden in der aufgeführten Reihenfolge seit 2025 in der Subgruppe angegangen:

1. Personen: Ratsmitglieder, Verwaltungsmitglieder
2. Gruppen / Organe / Interessengruppen: Parteien, Fraktionen, Gremien, Kommissionen, Verbände
3. Interessenbindungen, Konflikte, Politikfinanzierung
4. Verknüpfungen gleicher Personen über föderale Stufen hinweg

## Allgemeine übergreifende Technische Informationen

### Identifikatoren

Das vorliegende Daten-Modell erlaubt es folgende Typen von Identifikatoren zu verwenden:

1. **Lokaler Identifikator (`local_id`)**: Ein systeminterner Identifikator welcher vom publizierenden System genutzt wird, wenn nicht schon ausschliesslich eine `global_uri` benutzt wird. (Optional)

2. **Globaler Identifikator (`global_uri`)**: Ein globaler Identifikator welcher über verschiedene Systeme hinweg gültig ist. Dieser besteht meist aus einem Namespace (Domainnamen) der publizierenden Organisation zusammen mit einem lokalen Identifikator. (z.B. https://ld.bs.ch/personen_id/3456) (Zwingend)

3. **Wikidata Identifikator (`wikidata_uri`)**: Eine Wikidata Identifikator, um Personen und Gruppen Systemübergreifend zu identifizieren (z.B. http://www.wikidata.org/entity/Q115531 für Adolf Ogi) (Optional)


### Temporale Validität

Viele Attribute unterstützen zeitliche Gültigkeit durch `valid_from` und `valid_until`, wie z.B. Name, Adresse, Geschlecht, Staatsbürgerschaft, Beruf und Wahlkreis.

**Beispiel:**
```yaml
names:
  - name_type: officialLastName
    value: Müller
    valid_from: 1980-01-01
    valid_until: 2010-06-15
  - name_type: officialLastName
    value: Meier-Müller
    valid_from: 2010-06-16
```

# Person

## Einführung und Zielsetzung

Das Personenschema beschreibt natürliche Personen im politischen Kontext und zielt darauf ab, eine präzise und gleichzeitig flexible Datenstruktur bereitzustellen. Die Umsetzung soll es ermöglichen, vorhandene Informationen hochgradig strukturiert abzubilden (z.B. der Name nach Typisierung vom BFS), aber auch Informationen, die weniger klar und vollständing sind, darzustellen. Das Ziel ist es zu ermöglichen die Qualität kontinuierlich zu verbessern.

**Kernziele:**

- **Präzision**: Unterstützung von zeitlich gültigen Attributen (z.B. Namen, Adressen, Geschlecht).
- **Flexibilität**: Optionale Felder erlauben schrittweise Datenanreicherung.
- **Interoperabilität**: URIs als globale Identifikatoren wo vorhanden, inklusive der Möglichkeit auf Wikidata Einträge zu verweisen.
- **Mehrsprachigkeit**: Unterstützung mehrsprachiger Inhalte gemäss Schweizer Anforderungen.

Notiz: *Die Verknüpfung von Personen im öffentlichen Interesse (Politikerinnen und Politiker) über die federalen Ebenen hinweg wird als ein wichtiges Langzeitziel gesehen. Eine zentrale Datenbank oder Identifizierungstelle der Personen kann nicht durch die Fachgruppe realisiert werden. Es gibt Ansätze im Datenmodell, damit man kontinuierlich die Identifikatoren über die Stufen hinweg harmonisieren kann. Zum einen durch die Benutzung von Global eindeutigen Identifikatoren (URIs), sowie von Vorschlägen welche bestehenden offenen Datenbanken zu verwenden (Wikidata). *




## Class: Person 


_[de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Berufen._

_[en] A person with identifiers, names, addresses, citizenships, and occupations._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.). [en] Option to assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| label_long | 0..1 <br/> [String](#String) | [de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.). [en] Option to assign an extended label to a structured piece of information (e.g., display name with title, position, etc.).  |
| birth_year | 0..1 <br/> [Integer](#Integer) | [de] Geburtsjahr. [en] Year of birth. Only to be used, if there is no full `birthDate` available.  |
| birth_date | 0..1 <br/> [Date](#Date) | [de] Genaues Geburtsdatum. [en] Exact date of birth if available and public. This field has precedence over the field `birthYear`.  |
| death_date | 0..1 <br/> [Date](#Date) | [de] Genaues Todesdatum. [en] Exact date of death.  |
| picture | 0..1 <br/> [Uri](#Uri) | [de] Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF). [en] Link to an image (preferred: PNG, then JPG, then GIF).  |
| names | * <br/> [Name](#Name) | [en] Names of the person with type and value. [de] Namen der Person mit Typ und Wert.  |
| addresses | * <br/> [Address](#Address) | [de] Adressen mit Typ (privat, geschäftlich, lokal). [en] Addresses with type (private, business, local).  |
| language_proficiencies | * <br/> [LanguageProficiency](#LanguageProficiency) | [de] Sprachkompetenzen der Person. [en] Language proficiencies of the person.  |
| citizenships | * <br/> [Citizenship](#Citizenship) | [de] Staatsbürgerschaften der Person. [en] Citizenships of the person.  |
| genders | * <br/> [Gender](#Gender) | [de] Geschlecht der Person. [en] Gender of the person.  |
| occupations | * <br/> [Occupation](#Occupation) | [de] Berufe oder Tätigkeiten der Person. [en] Occupations or professions of the person.  |
| trainings | * <br/> [Training](#Training) | [de] Ausbildungen oder Bildungen der Person. [en] Trainings or educations of the person.  |
| contacts | * <br/> [Contact](#Contact) | [en] Contact information (email, website, social media). [de] Kontaktinformationen (E-Mail, Website, Social Media).  |
| electoral_district | 0..1 <br/> [ElectoralDistrict](#ElectoralDistrict) | [de] Link zum Wahlbezirk. [en] Link to the electoral district.  |
| interest_links | * <br/> [InterestLink](#InterestLink) | [de] Sammlung von Interessenbindungen. [en] Collection of interest links.range: InterestLink  |
| local_id | 0..1 <br/> [String](#String) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [persons](#persons) | range | [Person](#Person) |














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



## Class: Name 


_[de] Ein Name mit einem Typ (z.B. Rufname, amtlicher Name) und einem Wert und einer zeitlichen Gültigkeit._

_[en] A name with a type (e.g., call name, official name) and a value._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| name_type | 0..1 <br/> [NameTypeEnum](#NameTypeEnum) | [de] Typ des Namens. [en] Type of name.  |
| value | 0..1 <br/> [String](#String) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc. [en] The value of an information besides other attributes such as type, language, etc.  |
| valid_from | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [names](#names) | range | [Name](#Name) |



















</div> 



## Class: Address 


_[de] Eine Adresse mit einem Typ (z.B. Privatadresse, Geschäftsadresse) und einem Wert._

_[en] An address with a type (e.g., private address, business address) and a value._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| address_type | 0..1 <br/> [AddressTypeEnum](#AddressTypeEnum) | [de] Typ der Adresse. [en] Type of address.  |
| address_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [de] URI der Adresse. [en] URI of the address.  |
| street_address | 0..1 <br/> [String](#String) | [de] Strassenadresse. [en] Street address.  |
| postal_code | 0..1 <br/> [Integer](#Integer) | [de] Postleitzahl. [en] Postal code.  |
| postal_locality | 0..1 <br/> [String](#String) | [de] Ort. [en] Locality.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [addresses](#addresses) | range | [Address](#Address) |
| [Group](#Group) | [addresses](#addresses) | range | [Address](#Address) |














### Examples
#### Example: Address-douglas_adams_Douglas_Adams_1

```yaml
address_type: privateAddress
address_uri: https://www.wikidata.org/wiki/Q42#P969
street_address: 1234 Fictional St, London, UK
postal_code: 12345
postal_locality: London

```
#### Example: Address-swiss_politicians_Beat_Jans_1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```






</div> 

## Enum: AddressTypeEnum 




_[en] Types of addresses._

_[de] Adresstypen._

__



<div data-search-exclude markdown="1">

URI: [act:AddressTypeEnum](https://ld.ech.ch/schema/0294/actors/AddressTypeEnum)

### Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| privateAddress | None | [en] Private address |
| businessAddress | None | [en] Business address |
| localAddress | None | [en] Local address |







</div> 



## Class: LanguageProficiency 


_[de] Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um die bevorzugte Sprache oder die Muttersprache handelt._

_[en] Language proficiency of a person indicating the language and whether it is the preferred language or native language._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| language | 0..1 <br/> [String](#String) | [de] Sprachcode im ISO 639-1 Format. [en] Language code in ISO 639-1 format.  |
| is_correspondence | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob es sich um die bevorzugte Sprache handelt. [en] Indicates if this is the preferred language.  |
| is_native | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob es sich um die Muttersprache handelt. [en] Indicates if this is the native language.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [language_proficiencies](#language_proficiencies) | range | [LanguageProficiency](#LanguageProficiency) |



















</div> 



## Class: Citizenship 


_[de] Staatsangehörigkeit einer Person unter Angabe des Landes und der zeitlichen Gültigkeit. Wenn kein `valid_from` angegeben ist, ist diese Information nicht bekannt. Ist bekannt, dass die Staatsangehörigkeit seit der Geburt gültig ist, ist das Geburtsdatum hier anzugeben. Wenn kein `valid_through` angegeben ist, ist die Staatsangehörigkeit weiterhin gültig._

_[en] Citizenship (also used for Nationality) of a person indicating the country and temporal validity. If there is no `valid_from` provided, the information is not known. If it is known that the citizenship is valid from birth, the birthdate is to be repeated here. If there is no `valid_through`, the citizenship is still active._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| country | 0..1 <br/> [String](#String) | [de] ISO 3166 Ländercode. [en] ISO 3166 country code.  |
| valid_from | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [citizenships](#citizenships) | range | [Citizenship](#Citizenship) |



















</div> 



## Class: Gender 


_[de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen Gültigkeit._

_[en] Gender of a person indicating a gender code and temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| gender_code | 0..1 <br/> [String](#String) | [de] Geschlechtscode (z.B. gemäß ISO 5218). [en] Gender code (e.g., according to ISO 5218).  |
| pronouns | * <br/> [String](#String) | [de] Von der Person verwendete Pronomen. [en] Pronouns used by the person.  |
| valid_from | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [genders](#genders) | range | [Gender](#Gender) |



















</div> 



## Class: Occupation 


_[de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Codes, ob die Position bezahlt ist, und der zeitlichen Gültigkeit._

_[en] Occupation or profession of a person indicating a label, an ISCO-19 code, whether the position is paid, and temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Position bezahlt ist. [en] Indicates if the position is paid.  |
| occupation_code | 0..1 <br/> [String](#String) | [de] ISCO-19 Code der Tätigkeit. [en] ISCO-19 code of the occupation.  |
| label | 0..1 <br/> [String](#String) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.). [en] Option to assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| enterprise_uid | 0..1 <br/> [String](#String) | [de] UID des Unternehmens. [en] UID of the enterprise.  |
| enterprise | 0..1 <br/> [String](#String) | [de] Name des Unternehmens. [en] Name of the enterprise.  |
| valid_from | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [occupations](#occupations) | range | [Occupation](#Occupation) |














### Examples
#### Example: Occupation-douglas_adams_Douglas_Adams_writer

```yaml
label: writer
valid_from: 1979-01-01
valid_through: 2001-05-11
is_active: false
is_paid: true

```
#### Example: Occupation-swiss_politicians_Beat_Jans_Politiker

```yaml
label: Politiker
valid_from: 1964-01-01
is_active: true

```






</div> 



## Class: Training 


_[de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z.B. Schulabschluss, Universitätsabschluss, Militärdienst), eines Labels, eines ISCO-19 Codes und der zeitlichen Gültigkeit._

_[en] Training or education of a person indicating a type (e.g., school diploma, university degree, military service), a label, an ISCO-19 code, and temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| training_type | 0..1 <br/> [TrainingTypeEnum](#TrainingTypeEnum) | [de] Typ der Ausbildung oder Bildung. [en] Type of training or education.  |
| training_code | 0..1 <br/> [String](#String) | [de] ISCO-19 Code der Ausbildung oder Bildung. [en] ISCO-19 code of the training or education.  |
| value | 0..1 <br/> [String](#String) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc. [en] The value of an information besides other attributes such as type, language, etc.  |
| valid_from | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [trainings](#trainings) | range | [Training](#Training) |



















</div> 



## Class: Contact 


_[de] Kontaktinformation einer Person mit Angabe eines Typs (z.B. E-Mail, LinkedIn) und eines Werts._

_[en] Contact information of a person indicating a type (e.g., email, LinkedIn) and a value._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| contact_type | 0..1 <br/> [ContactTypeEnum](#ContactTypeEnum) | [de] Typ der Kontaktinformation. [en] Type of contact information.  |
| value | 0..1 <br/> [String](#String) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc. [en] The value of an information besides other attributes such as type, language, etc.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [contacts](#contacts) | range | [Contact](#Contact) |
| [Group](#Group) | [contacts](#contacts) | range | [Contact](#Contact) |



















</div> 



## Class: ElectoralDistrict 


_[de] Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit zeitlicher Gültigkeit._

_[en] Electoral district or region where a person is politically active; with temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| district | 0..1 <br/> [String](#String) | [de] Wahlkreis oder Wahlregion. [en] Electoral district or region.  |
| valid_from | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [electoral_district](#electoral_district) | range | [ElectoralDistrict](#ElectoralDistrict) |














### Examples
#### Example: ElectoralDistrict-douglas_adams_Douglas_Adams_1

```yaml
district: London Central
valid_from: 2020-01-01
valid_through: 2025-01-01

```
#### Example: ElectoralDistrict-swiss_politicians_Beat_Jans_1

```yaml
district: Basel-Stadt
valid_from: 2010-01-01

```






</div>



## Class: InterestLink 


_[de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation._

_[en] An interest link (conflict of interest, political financing) of a person to an organization._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| person_reference | 0..1 <br/> [PersonReference](#PersonReference) | [de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung. [en] Reference to a person with snapshot data at time of linking.  |
| interest_type | 1 <br/> [InterestTypeEnum](#InterestTypeEnum) | [de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein). [en] Type of interest link (professional activity, political office, association).  |
| organization_label | 0..1 <br/> [String](#String) | [en] Label of the organization. [de] Bezeichnung der Organisation.  |
| organization_uid | 0..1 <br/> [String](#String) | [en] UID of the organization (for analysis with NOGA codes, etc.). [de] UID der Organisation (für Auswertungen mit NOGA-Codes, etc.).  |
| organization_address | 0..1 <br/> [String](#String) | [en] Address of the organization. [de] Adresse der Organisation.  |
| legal_form | 0..1 <br/> [String](#String) | [en] Legal form of the organization. [de] Rechtsform der Organisation.  |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Position bezahlt ist. [en] Indicates if the position is paid.  |
| committee | 0..1 <br/> [String](#String) | [en] Committee or board (e.g., foundation board, board of directors). [de] Gremium (z.B. Stiftungsrat, Verwaltungsrat).  |
| function_role | 0..1 <br/> [String](#String) | [en] Function or role in the organization. [de] Funktion oder Rolle in der Organisation.  |
| local_id | 0..1 <br/> [String](#String) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |
| [Person](#Person) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |














### Examples
#### Example: InterestLink-interest_links_il_burkart_001

```yaml
global_uri: act:il_burkart_001
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Burkart Advisory GmbH, Baden
legal_form: Gesellschaft mit beschränkter Haftung
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_007

```yaml
global_uri: act:il_burkart_007
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: FONDATION SUISSE DE DEMINAGE (FSD), Genf
legal_form: Stiftung
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_011

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: Verein Landesausstellung Svizra27, Aarau
legal_form: Verein
committee: Vorstand
function_role: Mitglied
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_010

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: Allianz Sicherheit Schweiz, Baden
legal_form: Verein
committee: Vorstand
function_role: Präsident
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_002

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Birchmeier Holding AG, Döttingen
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_004

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: ELCA Group SA, Lausanne
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_003

```yaml
global_uri: act:il_burkart_003
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Bovida Real Estate AG, Baar
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_006

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: FDP.Die Liberalen
legal_form: Verein
committee: Vorstand
function_role: Präsident
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_008

```yaml
global_uri: act:il_burkart_008
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Stiebel Eltron AG, Lupfig
legal_form: Aktiengesellschaft
committee: Beirat
function_role: Beirat
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_009

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: Verein
committee: Vorstand
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_005

```yaml
global_uri: act:il_burkart_005
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: Verein
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```






</div>

# Gruppen und Organe (Groups)

## Einführung und Zielsetzung

Das Group-Schema beschreibt politische Gruppen, Organisationen und Körperschaften im schweizerischen politischen System. Ein Organ ist in dieser Definition eine Ansammlung von Personen, die durch einen Typ und weitere Attribute charakterisiert wird.

**Kernziele:**
- **Strukturierung**: Einheitliche Erfassung aller politischen Akteure (Legislative, Exekutive, Judikative, Zivilgesellschaft)
- **Hierarchien**: Abbildung von Organisationsstrukturen (Parteien, Kommissionen, Departemente)
- **Föderalismus**: Unterstützung aller föderalen Ebenen (Bund, Kantone, Gemeinden)
- **Mehrsprachigkeit**: Multilinguale Namen und Abkürzungen

## Anwendungszwecke

Das Schema unterstützt verschiedene Einsatzszenarien:

1. **Organisation innerhalb eines Parlamentssystems**: Parlamente, Kommissionen, Fraktionen
2. **Publikation an die Öffentlichkeit**: Transparente Darstellung politischer Strukturen
3. **Systeme mit politischen Personen**: Zuordnung von Personen zu Gruppen (Memberships)
4. **Analysen**: Untersuchungen von Gruppenzusammensetzungen und Netzwerken
5. **Parteilisten**: Verwaltung von Wahllisten (z.B. UNIBE Parteilisten-Datenbank)



## Class: Group 


_[de] Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission, Parlament, Departement)._

_[en] A political group, organization, or body (e.g., party, committee, parliament, department)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| group_type | 0..1 <br/> [GroupType](#GroupType) | [de] Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament oder ähnliches. Die genaue Bennenung und Beschreibung der Gruppierung wird über `name` gemacht. [en] Link to the group type.  |
| label | 0..1 <br/> [String](#String) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.). [en] Option to assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | [de] Abkürzung (kann mehrsprachig sein). [en] Abbreviation (can be multilingual).  |
| description | * <br/> [MultilingualValue](#MultilingualValue) | [de] Kurze Beschreibung der Gruppierung. [en] Description of the entity.  |
| landing_page | 0..1 <br/> [Uri](#Uri) | [de] Website mit weiteren Informationen. [en] Website providing further information.  |
| parent_groups | * <br/> [Uriorcurie](#Uriorcurie) | [de] Übergeordneten Gruppe. Zum Beispiel die Mutterpartei, zu Kantonalenparteien. Oder zur Beschreibung der Hierarchie in Exekutive. Verknüpfung von Subkommissionen mit Kommissionen. (parentGroup wird immer im selben group_type verwendet.) [en] Link to parent groups.  |
| spatial | 0..1 <br/> [String](#String) | [de] Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer, z.B. ld.admin.ch/municipality/1234, ld.admin.ch/canton/23). [en] Spatial reference (fos-municipality number, fos-canton number, e.g., ld.admin.ch/municipality/1234, ld.admin.ch/canton/23).  |
| contacts | * <br/> [Contact](#Contact) | [en] Contact information (email, website, social media). [de] Kontaktinformationen (E-Mail, Website, Social Media).  |
| addresses | * <br/> [Address](#Address) | [de] Adressen mit Typ (privat, geschäftlich, lokal). [en] Addresses with type (private, business, local).  |
| statutes_url | 0..1 <br/> [String](#String) | [de] URL zu Parteistatuten (optional für Parteien). [en] URL to party statutes (optional for parties).  |
| party_color | 0..1 <br/> [String](#String) | [de] Parteifarbe (optional für Parteien). [en] Party color (optional for parties).  |
| local_id | 0..1 <br/> [String](#String) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [groups](#groups) | range | [Group](#Group) |



















</div>

# Mitgliedschaften (Memberships)

## Einführung und Zielsetzung

Das Membership-Schema bildet die Beziehung zwischen Personen und Gruppen ab. Es ist das zentrale Bindeglied im Actor-Schema und ermöglicht die Zuordnung von Personen zu Parteien, Fraktionen, Kommissionen, Parlamenten und anderen politischen Organen.

**Kernziele:**
- **Verknüpfung**: Strukturierte Verbindung zwischen Person und Group
- **Rollen**: Erfassung der Funktion innerhalb der Gruppe
- **Zeitliche Dimension**: Dokumentation von Beginn und Ende der Mitgliedschaft
- **Status**: Unterscheidung zwischen aktiven und inaktiven Mitgliedschaften
- **Stimmberechtigung**: Erfassung der Stimmberechtigung (relevant für Parlamente)

## Anwendungsszenarien

Memberships werden für verschiedene Zuordnungen verwendet:

1. **Parteimitgliedschaften**: Zugehörigkeit zu politischen Parteien
2. **Fraktionsmitgliedschaften**: Zuordnung zu parlamentarischen Fraktionen
3. **Kommissionsmitgliedschaften**: Mitarbeit in parlamentarischen Kommissionen
4. **Parlamentsmitgliedschaften**: Mandate in Parlamenten (Bund, Kantone, Gemeinden)
5. **Regierungsmitgliedschaften**: Mitgliedschaft in Exekutivorganen
6. **Delegationen**: Teilnahme an Delegationen
7. **Gremien**: Mitwirkung in Gremien und Arbeitsgruppen

## Technische Struktur

### Identifikatoren und Referenzen

Eine Membership verknüpft Person und Gruppe über eingebettete **`PersonReference`** / **`GroupReference`** (Snapshot zum Zeitpunkt der Verknüpfung, jeweils mit `global_uri`):

| Attribut | Typ | Pflicht | Beschreibung |
|----------|-----|---------|--------------|
| `global_uri` | URI | Ja | Identifikator der Mitgliedschaft |
| `person_reference` | PersonReference | Nein | Referenz auf die Person (mind. `global_uri`, optional `label`) |
| `group_reference` | GroupReference | Nein | Referenz auf die Gruppe (mind. `global_uri`, optional `label`) |

**Beispiel:**
```yaml
global_uri: act:membership_jans_sp
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q813067
group_reference:
  global_uri: act:sp_basel_stadt
```

### Datenmodell (LinkML-Auszug)

```yaml
global_uri: act:membership_jans_sp
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q813067
group_reference:
  global_uri: act:sp_basel_stadt
role_type:
  role_type_enum: member
valid_from: 1990-01-01
is_active: true
```

## Datenstruktur

### Pflichtfelder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `global_uri` | URI | Eindeutiger Identifikator der Mitgliedschaft |

### Optionale Felder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `person_reference` | PersonReference | Referenz zur Person |
| `group_reference` | GroupReference | Referenz zur Gruppe |
| `role_type` | RoleType | Rolle (`role_type_enum`, optional `label`) |
| `valid_from` | date | Beginn der Mitgliedschaft |
| `valid_through` | date | Ende der Mitgliedschaft |
| `is_active` | boolean | Gibt an, ob die Mitgliedschaft derzeit aktiv ist |
| `authorized_to_vote` | boolean | Stimmberechtigung (relevant für Parlamente) |
| `datetime_modified` | datetime | Letzte Aktualisierung des Datensatzes |
| `datetime_created` | datetime | Erstellung des Datensatzes |

## Rollen (`role_type`)

Das Attribut `role_type` beschreibt die Funktion der Person in der Gruppe. Standardisierte Werte über `RoleEnum` (`member`, `president`, `stellvertreter`, `other`); bei `other` zusätzlich `label` (z.B. «Sekretär», «Ersatzmitglied»).

Unterstützende Personen einer Gruppierung (Regierung/Rat) sind Mitglieder des Gremiums; die konkrete Funktion wird über `role_type` ausgedrückt (z.B. Sekretär/Sekretärin).

### RoleEnum im Schema

| `role_type_enum` | Verwendung |
|------------------|------------|
| `member` | Reguläres Mitglied (Standard) |
| `president` | Präsident/in, Vorsitz |
| `stellvertreter` | Stellvertretung |
| `other` | Weitere Rollen; `label` setzen (siehe Listen unten) |

### Typische Rollen in Parlamenten

- **Mitglied**: Reguläres Parlamentsmitglied
- **Präsident/Präsidentin**: Parlamentspräsident/in
- **Vizepräsident/Vizepräsidentin**: Stellvertretung
- **Ersatzmitglied**: Stellvertretende Person
- **Beobachter/Beobachterin**: Beobachterstatus ohne Stimmrecht

### Typische Rollen in Kommissionen

- **Mitglied**: Reguläres Kommissionsmitglied
- **Präsident/Präsidentin**: Kommissionspräsident/in
- **Vizepräsident/Vizepräsidentin**: Stellvertretung
- **Ersatzmitglied**: Stellvertretende Person
- **Sekretär/Sekretärin**: Kommissionssekretär/in (oft nicht stimmberechtigtes Mitglied)

### Typische Rollen in Parteien

- **Mitglied**: Parteimitglied
- **Präsident/Präsidentin**: Parteipräsident/in
- **Vorstandsmitglied**: Mitglied des Parteivorstands
- **Geschäftsführer/Geschäftsführerin**: Geschäftsführung
- **Ehrenmitglied**: Ehrenmitgliedschaft

### Typische Rollen in Regierungen

- **Regierungsrat/Regierungsrätin**: Mitglied der Kantonsregierung
- **Bundesrat/Bundesrätin**: Mitglied des Bundesrats
- **Bundespräsident/Bundespräsidentin**: Rotierendes Amt
- **Vizepräsident/Vizepräsidentin**: Stellvertretung

## Zeitliche Validität

### valid_from und valid_through

Mitgliedschaften haben einen klar definierten Beginn und oft auch ein Ende:

```yaml
# Parlamentsmandat mit fester Amtszeit
global_uri: act:membership_caroni_sr
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q493598
group_reference:
  global_uri: act:staenderat
role_type:
  role_type_enum: member
valid_from: 2015-12-07  # Amtsantritt nach Wahl
valid_through: 2023-11-30  # Ende der Amtsperiode
authorized_to_vote: true
```

```yaml
# Parteimitgliedschaft ohne Enddatum
global_uri: act:membership_riniker_fdp
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q77074968
group_reference:
  global_uri: act:fdp_aargau
role_type:
  role_type_enum: member
valid_from: 2000-01-01
# valid_through nicht gesetzt = noch aktiv
is_active: true
```

### is_active

Alternative oder Ergänzung zu `valid_from`/`valid_through`:

- `true`: Mitgliedschaft ist derzeit aktiv
- `false`: Mitgliedschaft ist inaktiv/beendet
- Nicht gesetzt: Aktivität wird aus `valid_from`/`valid_through` abgeleitet

**Verwendung:**
```yaml
# Explizite Markierung als aktiv
is_active: true
valid_from: 2019-01-01

# Explizite Markierung als beendet
is_active: false
valid_from: 2015-01-01
valid_through: 2019-12-31
```

## Stimmberechtigung (authorized_to_vote)

Das Attribut `authorized_to_vote` gibt an, ob die Person in der Gruppe stimmberechtigt ist.

**Relevant für:**
- Parlamentsmitgliedschaften
- Kommissionsmitgliedschaften
- Gremien mit Beschlussfassungen

**Nicht stimmberechtigt können sein:**
- Ersatzmitglieder (wenn nicht im Einsatz)
- Beobachter/Beobachterinnen
- Sekretärinnen/Sekretäre
- Gäste

**Beispiele:**
```yaml
# Stimmberechtigtes Mitglied
role_type:
  role_type_enum: member
authorized_to_vote: true

# Nicht stimmberechtigtes Ersatzmitglied
role_type:
  role_type_enum: other
  label: Ersatzmitglied
authorized_to_vote: false

# Kommissionssekretär ohne Stimmrecht
role_type:
  role_type_enum: other
  label: Sekretär
authorized_to_vote: false
```

## Mehrfachmitgliedschaften

Eine Person kann gleichzeitig mehrere Mitgliedschaften haben:

```yaml
# Container-Struktur
persons:
  - global_uri: https://www.wikidata.org/wiki/Q493598
    label: Andrea Caroni

memberships:
  # Parteimitgliedschaft
  - global_uri: act:membership_caroni_fdp
    person_reference:
      global_uri: https://www.wikidata.org/wiki/Q493598
    group_reference:
      global_uri: act:fdp_appenzell
    role_type:
      role_type_enum: member
    valid_from: 1998-01-01
    is_active: true

  # Parlamentsmandat
  - global_uri: act:membership_caroni_sr
    person_reference:
      global_uri: https://www.wikidata.org/wiki/Q493598
    group_reference:
      global_uri: act:staenderat
    role_type:
      role_type_enum: member
    valid_from: 2015-12-07
    authorized_to_vote: true
    is_active: true

  # Fraktionsmitgliedschaft
  - global_uri: act:membership_caroni_fdp_fraktion
    person_reference:
      global_uri: https://www.wikidata.org/wiki/Q493598
    group_reference:
      global_uri: act:fdp_fraktion_sr
    role_type:
      role_type_enum: member
    valid_from: 2015-12-07
    is_active: true

  # Kommissionsmitgliedschaft
  - global_uri: act:membership_caroni_rk_sr
    person_reference:
      global_uri: https://www.wikidata.org/wiki/Q493598
    group_reference:
      global_uri: act:rechtskommission_sr
    role_type:
      role_type_enum: member
    valid_from: 2016-01-01
    valid_through: 2019-12-31
    authorized_to_vote: true
    is_active: false
```

## Hierarchische Darstellung

Memberships können auch hierarchisch organisiert werden:

### Partei → Fraktion
```yaml
# Person ist Mitglied einer Partei
- global_uri: act:membership_jans_sp
  person_reference:
    global_uri: https://www.wikidata.org/wiki/Q813067
  group_reference:
    global_uri: act:sp_schweiz
  role_type:
    role_type_enum: member
  valid_from: 1980-01-01

# Person ist Mitglied der SP-Fraktion im Nationalrat
- global_uri: act:membership_jans_sp_fraktion
  person_reference:
    global_uri: https://www.wikidata.org/wiki/Q813067
  group_reference:
    global_uri: act:sp_fraktion_nr
  role_type:
    role_type_enum: member
  valid_from: 2010-12-06
```

Die Fraktion selbst hat eine `parent_groups`-Beziehung zur Partei (siehe Group-Schema).

## Wechsel und Nachfolge

### Parteiwechsel

```yaml
# SP-Mitgliedschaft (beendet)
- global_uri: act:membership_mueller_sp
  person_reference:
    global_uri: act:person_mueller
  group_reference:
    global_uri: act:sp_zuerich
  role_type:
    role_type_enum: member
  valid_from: 2010-01-01
  valid_through: 2018-06-30
  is_active: false

# Grüne-Mitgliedschaft (neu)
- global_uri: act:membership_mueller_gruene
  person_reference:
    global_uri: act:person_mueller
  group_reference:
    global_uri: act:gruene_zuerich
  role_type:
    role_type_enum: member
  valid_from: 2018-07-01
  is_active: true
```

### Rollenwechsel innerhalb einer Gruppe

```yaml
# Reguläres Mitglied
- global_uri: act:membership_schmidt_kommission_1
  person_reference:
    global_uri: act:person_schmidt
  group_reference:
    global_uri: act:sik_nr
  role_type:
    role_type_enum: member
  valid_from: 2016-01-01
  valid_through: 2019-12-31

# Präsidentin (Nachfolge-Membership)
- global_uri: act:membership_schmidt_kommission_2
  person_reference:
    global_uri: act:person_schmidt
  group_reference:
    global_uri: act:sik_nr
  role_type:
    role_type_enum: president
  valid_from: 2020-01-01
  is_active: true
```

## Interoperabilität

### Verknüpfung im Container

```yaml
global_uri: act:political_actors_dataset
persons:
  - global_uri: https://www.wikidata.org/wiki/Q813067
    label: Beat Jans
    # ... weitere Person-Attribute

groups:
  - global_uri: act:sp_basel_stadt
    group_type:
      group_type_enum: party
    label: SP Basel-Stadt
    # ... weitere Group-Attribute

memberships:
  - global_uri: act:membership_jans_sp
    person_reference:
      global_uri: https://www.wikidata.org/wiki/Q813067
    group_reference:
      global_uri: act:sp_basel_stadt
    role_type:
      role_type_enum: member
    valid_from: 1990-01-01
    is_active: true
```

### Auswertungen

**Nach Gruppe:**
```sparql
# Alle Mitglieder der SP Basel-Stadt
SELECT ?person ?role WHERE {
  ?membership a act:Membership ;
    act:groupReference act:sp_basel_stadt ;
    act:personReference ?person ;
    act:roleType ?role ;
    act:isActive true .
}
```

**Nach Person:**
```sparql
# Alle Gruppen von Beat Jans
SELECT ?group ?role WHERE {
  ?membership a act:Membership ;
    act:personReference <https://www.wikidata.org/wiki/Q813067> ;
    act:groupReference ?group ;
    act:roleType ?role ;
    act:isActive true .
}
```

## Anwendungsbeispiele

### Beispiel 1: Nationalratsmandat

```yaml
global_uri: act:membership_riniker_nr
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q77074968
group_reference:
  global_uri: act:nationalrat
role_type:
  role_type_enum: member
valid_from: 2019-12-02  # Amtsantritt nach Wahl 2019
valid_through: 2023-11-30  # Ende der Legislaturperiode
authorized_to_vote: true
is_active: false  # Legislatur ist beendet
datetime_created: 2019-12-02T00:00:00Z
datetime_modified: 2023-11-30T00:00:00Z
```

### Beispiel 2: Kommissionsmitgliedschaft mit Präsidium

```yaml
# Reguläres Mitglied
global_uri: act:membership_caroni_rk_1
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q493598
group_reference:
  global_uri: act:rechtskommission_sr
role_type:
  role_type_enum: member
valid_from: 2016-01-01
valid_through: 2019-12-31
authorized_to_vote: true
is_active: false

# Präsident
global_uri: act:membership_caroni_rk_2
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q493598
group_reference:
  global_uri: act:rechtskommission_sr
role_type:
  role_type_enum: president
valid_from: 2020-01-01
valid_through: 2023-12-31
authorized_to_vote: true
is_active: false
```

### Beispiel 3: Parteimitgliedschaft über alle Ebenen

```yaml
# Bundesebene
- global_uri: act:membership_jans_sp_ch
  person_reference:
    global_uri: https://www.wikidata.org/wiki/Q813067
  group_reference:
    global_uri: act:sp_schweiz
  role_type:
    role_type_enum: member
  valid_from: 1980-01-01
  is_active: true

# Kantonsebene
- global_uri: act:membership_jans_sp_bs
  person_reference:
    global_uri: https://www.wikidata.org/wiki/Q813067
  group_reference:
    global_uri: act:sp_basel_stadt
  role_type:
    role_type_enum: member
  valid_from: 1980-01-01
  is_active: true

# Gemeinde (optional)
- global_uri: act:membership_jans_sp_basel
  person_reference:
    global_uri: https://www.wikidata.org/wiki/Q813067
  group_reference:
    global_uri: act:sp_stadt_basel
  role_type:
    role_type_enum: other
    label: Vorstandsmitglied
  valid_from: 2000-01-01
  valid_through: 2010-12-31
  is_active: false
```

### Beispiel 4: Bundesrat

```yaml
global_uri: act:membership_luisier_vd_regierung
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q24699807
group_reference:
  global_uri: act:regierungsrat_vaud
role_type:
  role_type_enum: other
  label: Conseillère d'État
valid_from: 2022-07-01
is_active: true
authorized_to_vote: true
datetime_created: 2022-07-01T00:00:00Z
```

### Beispiel 5: Fraktionsmitgliedschaft

```yaml
global_uri: act:membership_riniker_fdp_fraktion
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q77074968
group_reference:
  global_uri: act:fdp_fraktion_nr
role_type:
  role_type_enum: member
valid_from: 2019-12-02
valid_through: 2023-11-30
is_active: false
datetime_created: 2019-12-02T00:00:00Z
```

### Beispiel 6: Ersatzmitglied

```yaml
global_uri: act:membership_mueller_gpk_ersatz
person_reference:
  global_uri: act:person_mueller
group_reference:
  global_uri: act:gpk_nr
role_type:
  role_type_enum: other
  label: Ersatzmitglied
valid_from: 2020-01-01
valid_through: 2023-12-31
authorized_to_vote: false  # Ersatzmitglieder sind normalerweise nicht stimmberechtigt
is_active: false
```

### Beispiel 7: Delegation

```yaml
global_uri: act:membership_caroni_delegation
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q493598
group_reference:
  global_uri: act:delegation_europarat
role_type:
  role_type_enum: other
  label: Delegierter
valid_from: 2016-01-01
is_active: true
authorized_to_vote: true
```

## Auswertungsmöglichkeiten

### Aktive Mitgliedschaften

Filtern nach `is_active: true` oder `valid_through` nicht gesetzt:
```yaml
SELECT * FROM memberships
WHERE is_active = true
OR (valid_from <= CURRENT_DATE AND (valid_through IS NULL OR valid_through >= CURRENT_DATE))
```

### Historische Analysen

- Parteiwechsel über Zeit
- Durchschnittliche Dauer von Mandaten
- Fluktuation in Kommissionen
- Karrierewege (Gemeinde → Kanton → Bund)

### Netzwerkanalysen

- Welche Personen sind in denselben Gruppen?
- Ko-Mitgliedschaften in Kommissionen
- Parteizugehörigkeit vs. Fraktionszugehörigkeit

### Stimmberechtigungen

- Anzahl stimmberechtigter Mitglieder pro Gruppe
- Anteil von Ersatzmitgliedern
- Quorum-Berechnungen

## Unterschied zu InterestLink

**Membership** vs. **InterestLink**:

| Aspekt | Membership | InterestLink |
|--------|-----------|--------------|
| **Zweck** | Formale Zugehörigkeit zu politischen Gruppen | Interessenbindungen und Konflikte |
| **Zielgruppe** | Gruppen im Actor-Schema | Externe Organisationen |
| **Beispiele** | Parteimitglied, Kommissionsmitglied | Verwaltungsratsmandat, Vereinsvorstand |
| **Transparenzpflicht** | Standard-Zuordnung | Offenlegungspflicht wegen Interessenkonflikten |
| **Stimmberechtigung** | Ja (authorized_to_vote) | Nein |

**Überschneidung:**
Eine Person kann sowohl Membership (z.B. Nationalrat) als auch InterestLink (z.B. Verwaltungsrat bei Swisscom) haben.

## Referenzen

Siehe vollständige LinkML-Schema-Dokumentation:



## Class: Membership 


_[de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe._

_[en] A membership relationship between a person and a group._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| person_reference | 0..1 <br/> [PersonReference](#PersonReference) | [de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung. [en] Reference to a person with snapshot data at time of linking.  |
| group_reference | 0..1 <br/> [GroupReference](#GroupReference) | [de] Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfung. [en] Reference to a group with snapshot data at time of linking.  |
| role_type | 0..1 <br/> [RoleType](#RoleType) | [en] Role of the person in the membership or function. [de] Rolle der Person in der Mitgliedschaft oder Funktion.  |
| authorized_to_vote | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Person stimmberechtigt ist. [en] Indicates if the person is authorized to vote.  |
| local_id | 0..1 <br/> [String](#String) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [memberships](#memberships) | range | [Membership](#Membership) |



















</div> 

# Interessenbindungen (Interest Links)

## Einführung und Zielsetzung

Das InterestLink-Schema erfasst Interessenbindungen, Interessenkonflikte und Verflechtungen von Personen im politischen Kontext mit Organisationen. Der Standard orientiert sich an den Transparenzanforderungen für Parlamentsmitglieder gemäss [Bundesversammlung - Interessenbindungen](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

**Kernziele:**
- **Transparenz**: Offenlegung von potenziellen Interessenkonflikten
- **Strukturierte Erfassung**: Einheitliche Klassifikation nach Art der Interessenbindung
- **Auswertbarkeit**: Verknüpfung mit UID-Register für statistische Analysen (NOGA-Codes)
- **Zeitliche Nachvollziehbarkeit**: Dokumentation von Start und Ende der Bindung

## Technische Struktur

### Identifikatoren und Referenzen

Das InterestLink-Schema verknüpft Personen mit Organisationen:

| Attribut | Typ | Pflicht | Beschreibung |
|----------|-----|---------|--------------|
| `id` | URI | Ja | Eindeutiger Identifikator der Interessenbindung |
| `person_id` | string | Ja | Referenz zur Person (act:person_123 oder Wikidata-ID) |

**Beispiel:**
```yaml
id: act:interest_link_12345
person_id: https://www.wikidata.org/wiki/Q493598
```

## Datenstruktur

### Pflichtfelder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `id` | URI | Eindeutiger Identifikator |
| `person_id` | string | Referenz zur Person |
| `interest_type` | InterestTypeEnum | Art der Interessenbindung (siehe unten) |

### Optionale Felder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `organization_label` | string | Name/Bezeichnung der Organisation |
| `organization_uid` | string | UID-Nummer der Organisation (eCH-0097) |
| `organization_address` | string | Adresse der Organisation |
| `legal_form` | string | Rechtsform (AG, GmbH, Verein, Stiftung, etc.) |
| `valid_from` | date | Beginn der Interessenbindung |
| `valid_until` | date | Ende der Interessenbindung |
| `paid` | boolean | Gibt an, ob die Position bezahlt ist |
| `committee` | string | Gremium (Stiftungsrat, Verwaltungsrat, etc.) |
| `function_role` | string | Funktion/Rolle in der Organisation |
| `datetime_updated` | datetime | Letzte Aktualisierung des Datensatzes |
| `datetime_created` | datetime | Erstellung des Datensatzes |

## Klassifikation: InterestTypeEnum

Interessenbindungen werden in drei Hauptkategorien klassifiziert:

### 1. professional_activity (Berufliche Tätigkeit)

Berufliche Tätigkeiten ausserhalb des politischen Mandats.

**Beispiele:**
- Anstellung in einem Unternehmen
- Selbstständige Tätigkeit
- Beratungsmandate
- Verwaltungsratsmandate in Privatunternehmen

```yaml
interest_type: professional_activity
organization_label: Swisscom AG
organization_uid: CHE-116.281.426
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
paid: true
```

### 2. political_office (Politische Ämter)

Politische Ämter und Mandate auf anderen föderalen Ebenen oder in anderen Körperschaften.

**Beispiele:**
- Mitgliedschaft in kantonalen oder kommunalen Parlamenten
- Regierungsräte
- Kommissionsmitgliedschaften
- Ämter in ausserparlamentarischen Kommissionen

```yaml
interest_type: political_office
organization_label: Gemeinderat Herisau
organization_address: Rathaus, 9100 Herisau
function_role: Gemeinderat
valid_from: 2018-01-01
paid: true
```

### 3. association (Vereinsmitgliedschaft)

Mitgliedschaften in Vereinen, Verbänden und Interessenorganisationen.

**Beispiele:**
- Branchenverbände
- Berufsverbände
- Lobbyorganisationen
- Gemeinnützige Vereine
- Stiftungen

```yaml
interest_type: association
organization_label: Schweizerischer Gewerbeverband
organization_uid: CHE-105.967.319
legal_form: Verein
function_role: Vorstandsmitglied
paid: false
```

## Organisation-UID und NOGA-Codes

Die `organization_uid` ermöglicht die Verknüpfung mit dem eidgenössischen Unternehmensregister:

**Vorteile:**
- Automatische Zuordnung von NOGA-Codes (Branchenklassifikation)
- Statistische Auswertungen nach Wirtschaftszweigen
- Eindeutige Identifikation der Organisation
- Verknüpfung mit Unternehmensdaten (Rechtsform, Adresse, etc.)

**Format:** eCH-0097 konform (CHE-XXX.XXX.XXX)

```yaml
organization_uid: CHE-116.281.426  # Swisscom AG
```

**Nachschlagen:** https://www.uid.admin.ch/

## Temporale Validität

Interessenbindungen ändern sich im Laufe der Zeit:

```yaml
# Wechsel von Positionen
- id: act:interest_link_001
  person_id: https://www.wikidata.org/wiki/Q493598
  interest_type: professional_activity
  organization_label: Credit Suisse
  committee: Verwaltungsrat
  valid_from: 2015-01-01
  valid_until: 2020-12-31
  paid: true

- id: act:interest_link_002
  person_id: https://www.wikidata.org/wiki/Q493598
  interest_type: professional_activity
  organization_label: UBS AG
  organization_uid: CHE-357.686.674
  committee: Verwaltungsrat
  valid_from: 2021-01-01
  paid: true
```

## Gremien und Funktionen

### Typische Gremien (`committee`)

Nach Schweizer Recht und Praxis:

- **Verwaltungsrat** (VR): Oberstes Führungsorgan einer AG
- **Stiftungsrat**: Oberstes Organ einer Stiftung
- **Vorstand**: Geschäftsführendes Organ eines Vereins
- **Aufsichtsrat**: Kontrollgremium
- **Beirat**: Beratendes Gremium
- **Geschäftsleitung**: Operative Führung

### Typische Funktionen (`function_role`)

- Präsident/Präsidentin
- Vizepräsident/Vizepräsidentin
- Mitglied
- Delegierter
- Geschäftsführer/Geschäftsführerin
- Berater/Beraterin

## Bezahlung (paid)

Das Attribut `paid` gibt an, ob die Position vergütet ist:

- `true`: Bezahlte Position (Entschädigung, Honorar, Lohn)
- `false`: Ehrenamtliche/unbezahlte Position

Bereits kleine Entschädigungen (z.B. Sitzungsgelder) gelten als bezahlt.

## Interoperabilität

### Verknüpfung mit Person-Schema

Interessenbindungen werden in zwei Formen referenziert:

1. **In der Container-Struktur:**
```yaml
# Container-Ebene
id: act:example_container
persons:
  - id: https://www.wikidata.org/wiki/Q493598
    label: Andrea Caroni
    # ... weitere Person-Attribute

interest_links:
  - id: act:interest_link_001
    person_id: https://www.wikidata.org/wiki/Q493598
    interest_type: professional_activity
    organization_label: Universität St. Gallen
```

2. **Direkt bei der Person:**
```yaml
persons:
  - id: https://www.wikidata.org/wiki/Q493598
    label: Andrea Caroni
    interest_links_person:
      - id: act:interest_link_001
        interest_type: professional_activity
        organization_label: Universität St. Gallen
```

### Verknüpfung mit UID-Register

Die UID ermöglicht Abfragen im Unternehmensregister:

```yaml
organization_uid: CHE-116.281.426
```

Liefert automatisch:
- Firmenname
- Rechtsform
- Adresse
- NOGA-Code (Branche)
- Handelsregistereintrag

## Unterschied zu Membership

| Aspekt | Membership | InterestLink |
|--------|-----------|--------------|
| **Zweck** | Formale Zugehörigkeit zu politischen Gruppen | Interessenbindungen und Konflikte |
| **Zielgruppe** | Gruppen im Actor-Schema | Externe Organisationen |
| **Beispiele** | Parteimitglied, Kommissionsmitglied | Verwaltungsratsmandat, Vereinsvorstand |
| **Transparenzpflicht** | Standard-Zuordnung | Offenlegungspflicht wegen Interessenkonflikten |
| **Stimmberechtigung** | Ja (authorized_to_vote) | Nein |

Eine Person kann sowohl Membership (z.B. Nationalrat) als auch InterestLink (z.B. Verwaltungsrat bei Swisscom) haben.

## Anwendungsbeispiele

### Beispiel 1: Verwaltungsratsmandat in AG

```yaml
id: act:interest_link_caroni_001
person_id: https://www.wikidata.org/wiki/Q493598
interest_type: professional_activity
organization_label: Swiss Re AG
organization_uid: CHE-101.458.980
organization_address: Mythenquai 50/60, 8022 Zürich
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
valid_from: 2018-04-01
paid: true
datetime_created: 2024-01-15T10:30:00Z
datetime_updated: 2024-01-15T10:30:00Z
```

### Beispiel 2: Politisches Amt auf kantonaler Ebene

```yaml
id: act:interest_link_riniker_001
person_id: https://www.wikidata.org/wiki/Q77074968
interest_type: political_office
organization_label: Grosser Rat des Kantons Aargau
organization_address: Regierungsgebäude, 5001 Aarau
function_role: Grossrätin
valid_from: 2009-01-01
valid_until: 2019-12-31
paid: true
```

### Beispiel 3: Vereinsmitgliedschaft (ehrenamtlich)

```yaml
id: act:interest_link_jans_001
person_id: https://www.wikidata.org/wiki/Q813067
interest_type: association
organization_label: Pro Natura Basel
legal_form: Verein
function_role: Vorstandsmitglied
valid_from: 2010-01-01
paid: false
```

### Beispiel 4: Stiftungsrat

```yaml
id: act:interest_link_luisier_001
person_id: https://www.wikidata.org/wiki/Q24699807
interest_type: professional_activity
organization_label: Fondation pour le développement durable
legal_form: Stiftung
committee: Stiftungsrat
function_role: Präsidentin
valid_from: 2020-06-01
paid: false
```

### Beispiel 5: Mehrere Interessenbindungen einer Person

```yaml
id: act:container_example
persons:
  - id: https://www.wikidata.org/wiki/Q493598
    label: Andrea Caroni
    interest_links_person:
      - id: act:interest_001
        interest_type: professional_activity
        organization_label: Universität St. Gallen
        organization_uid: CHE-105.817.549
        function_role: Honorarprofessor
        paid: true
        valid_from: 2015-01-01

      - id: act:interest_002
        interest_type: association
        organization_label: FDP Schweiz
        legal_form: Verein
        function_role: Mitglied
        paid: false
        valid_from: 2000-01-01

      - id: act:interest_003
        interest_type: professional_activity
        organization_label: Rechtsanwaltskanzlei Caroni
        legal_form: Einzelunternehmen
        function_role: Inhaber
        paid: true
        valid_from: 2008-01-01
```

## Auswertungsmöglichkeiten

### Nach Interessentyp

Statistische Auswertung nach Art der Interessenbindung:
- Anzahl beruflicher Tätigkeiten pro Person
- Anteil politischer Ämter auf verschiedenen Ebenen
- Vereinsmitgliedschaften nach Partei

### Nach Branche (NOGA-Code)

Über die UID-Verknüpfung:
- Welche Wirtschaftszweige sind im Parlament vertreten?
- Häufung von Mandaten in bestimmten Branchen
- Verflechtungen zwischen Politik und Wirtschaft

### Nach Bezahlung

- Anteil bezahlter vs. ehrenamtlicher Tätigkeiten
- Durchschnittliche Anzahl bezahlter Mandate
- Kumulation von Einkommen

### Zeitliche Entwicklung

- Beginn/Ende von Interessenbindungen
- Wechsel zwischen Organisationen
- Dauer von Mandaten

## Referenzen

**Weiterführende Dokumentation:**
- [Bundesversammlung - Interessenbindungen Nationalrat](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf)
- [UID-Register](https://www.uid.admin.ch/)
- [eCH-0097: Unternehmens-Identifikationsnummer](https://www.ech.ch/de/ech/ech-0097)
- [NOGA-Codes (Branchenklassifikation)](https://www.bfs.admin.ch/bfs/de/home/statistiken/industrie-dienstleistungen/nomenklatur/noga.html)

Siehe vollständige LinkML-Schema-Dokumentation:



## Class: InterestLink 


_[de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation._

_[en] An interest link (conflict of interest, political financing) of a person to an organization._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| person_reference | 0..1 <br/> [PersonReference](#PersonReference) | [de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung. [en] Reference to a person with snapshot data at time of linking.  |
| interest_type | 1 <br/> [InterestTypeEnum](#InterestTypeEnum) | [de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein). [en] Type of interest link (professional activity, political office, association).  |
| organization_label | 0..1 <br/> [String](#String) | [en] Label of the organization. [de] Bezeichnung der Organisation.  |
| organization_uid | 0..1 <br/> [String](#String) | [en] UID of the organization (for analysis with NOGA codes, etc.). [de] UID der Organisation (für Auswertungen mit NOGA-Codes, etc.).  |
| organization_address | 0..1 <br/> [String](#String) | [en] Address of the organization. [de] Adresse der Organisation.  |
| legal_form | 0..1 <br/> [String](#String) | [en] Legal form of the organization. [de] Rechtsform der Organisation.  |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Position bezahlt ist. [en] Indicates if the position is paid.  |
| committee | 0..1 <br/> [String](#String) | [en] Committee or board (e.g., foundation board, board of directors). [de] Gremium (z.B. Stiftungsrat, Verwaltungsrat).  |
| function_role | 0..1 <br/> [String](#String) | [en] Function or role in the organization. [de] Funktion oder Rolle in der Organisation.  |
| local_id | 0..1 <br/> [String](#String) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. [en] Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#de] Eine eindeutige, global gültige URI für die Entität. [en] A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz. [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum, an dem eine Entität erstellt wurde. [en] The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. [en] The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum, an dem eine Entität zuletzt geändert wurde. [en] The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. [en] The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |
| [Person](#Person) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |














### Examples
#### Example: InterestLink-interest_links_il_burkart_001

```yaml
global_uri: act:il_burkart_001
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Burkart Advisory GmbH, Baden
legal_form: Gesellschaft mit beschränkter Haftung
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_007

```yaml
global_uri: act:il_burkart_007
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: FONDATION SUISSE DE DEMINAGE (FSD), Genf
legal_form: Stiftung
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_011

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: Verein Landesausstellung Svizra27, Aarau
legal_form: Verein
committee: Vorstand
function_role: Mitglied
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_010

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: Allianz Sicherheit Schweiz, Baden
legal_form: Verein
committee: Vorstand
function_role: Präsident
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_002

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Birchmeier Holding AG, Döttingen
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_004

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: ELCA Group SA, Lausanne
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_003

```yaml
global_uri: act:il_burkart_003
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Bovida Real Estate AG, Baar
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_006

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: FDP.Die Liberalen
legal_form: Verein
committee: Vorstand
function_role: Präsident
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_008

```yaml
global_uri: act:il_burkart_008
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Stiebel Eltron AG, Lupfig
legal_form: Aktiengesellschaft
committee: Beirat
function_role: Beirat
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_009

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: Verein
committee: Vorstand
function_role: Mitglied
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_005

```yaml
global_uri: act:il_burkart_005
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: Verein
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```






</div>

