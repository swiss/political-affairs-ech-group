---
title: "eCH-0294 Politische Akteure: Personen, Gruppen und Organe"
lang: de
toc: false
---

| **Name**              | **Politische Akteure: Personen, Gruppen und Organe**                                                                       |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------|
| **eCH-Nummer**        | eCH-0294                                                                                                                   |
| **Kategorie**         | Entwurf                                                                                                                    |
| **Reifegrad**         | Fachgruppen interner Review                                                                                                |
| **Version**           | 0.2                                                                                                                        |
| **Status**            |                                                                                                 |
| **Beschluss am**      |                                                                                                                            |
| **Ausgabedatum**      |                                                                                                                            |
| **Ersetzt Version**   | 0.0                                                                                                                        |
| **Voraussetzungen**   | eCH-0292 (Gemeinsame Datenelemente)                                                                                        |
| **Beilagen**          | -                                                                                                                          |
| **Sprachen**          | Deutsch (Original) - English (Datamodel)                                                                                    |
| **Autoren**           | Fachgruppe politische Geschäfte: Julie Silberstein, Laurence Brandenberger, Daniela Koller, Thomas Roth, Stefan Oderbolz, Fabian Davolio, Orhan Saeedi, Christian Gutknecht, Michael Luggen |
| **Herausgeber / Vertrieb** | Verein eCH, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)                             |

\newpage

# Abstrakt

Der Entwurf eCH-0294 „Politische Akteure: Personen, Gruppen und Organe“ definiert ein einheitliches Datenmodell zur strukturierten Publikation politischer Akteure in der Schweiz. Er umfasst natürliche Personen, politische Gruppen und Organe, Mitgliedschaften zwischen Personen und Gruppen sowie Interessenbindungen. Ziel ist es, föderal übergreifend vergleichbare, maschinenlesbare und nachnutzbare Informationen bereitzustellen, um Transparenz, Nachvollziehbarkeit und Analysefähigkeit politischer Prozesse zu verbessern.

Der Standard richtet sich an öffentliche Stellen aller Staatsebenen, politische Akteure, Medien, Forschung und Öffentlichkeit und schafft eine Grundlage für interoperable politische Informationssysteme in der Schweiz.

\newpage

# Inhaltsverzeichnis

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Rechtsklick &gt; „Felder aktualisieren“, um das Inhaltsverzeichnis zu erzeugen.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```


\newpage

# Einführung

## Die Standardfamilie „Politische Geschäfte"

Das politische Geschehen der Schweiz findet auf Bundes-, Kantons- und Gemeindeebene statt – in Parlamenten und Gemeindeversammlungen, in Exekutiven und Verwaltungen, in Vernehmlassungen und Konsultationen sowie über die direktdemokratische Mitwirkung der Stimmberechtigten. Die Fachgruppe „Politische Geschäfte" des Vereins eCH entwickelt dafür eine Familie aufeinander abgestimmter Standards, welche diese Daten föderal übergreifend strukturieren. Die Standards nutzen gemeinsame Datenelemente (eCH-0292) und referenzieren sich gegenseitig über eindeutige Identifikatoren.

Die Familie umfasst:

- **eCH-0292 – Gemeinsame Datenelemente (Meta):** Definiert die übergreifend genutzten Datenelemente und Metaprozesse, auf denen die übrigen Standards aufbauen.
- **eCH-0293 – Öffentlicher Ratsbetrieb (Operations):** Beschreibt den öffentlichen Ratsbetrieb – Sitzungen, Traktanden, Wortmeldungen sowie Abstimmungen und Wahlen.
- **eCH-0294 – Politische Akteure (Actors) – dieser Standard:** Definiert Personen, Gruppen und Organe im politischen Kontext sowie deren Mitgliedschaften und Interessenbindungen. Die übrigen Standards referenzieren diese Akteure über ihre Identifikatoren.
- **eCH-0295 – Parlamentarische Geschäfte (Affairs):** Beschreibt den Lebenszyklus politischer Geschäfte.
- **eCH-0296 – Erlasse und Gesetzestexte (Laws):** Erfasst die Resultate des parlamentarischen Prozesses – die verabschiedeten Gesetze und Erlasse.
- **eCH-0297 – Öffentliche Konsultationen (Consultations):** Strukturiert Vernehmlassungsverfahren, die oft Ausgangspunkt für parlamentarische Geschäfte sind.

Ziel dieser Standardfamilie ist es, eine gemeinsam nutzbare Struktur für politische Daten zu schaffen und Organisationen, die Informationen zu politischen Geschäften veröffentlichen, ein tragfähiges Datenmodell an die Hand zu geben.

## Abgrenzung zur Fachgruppe „Politische Rechte"

Neben der Fachgruppe „Politische Geschäfte" besteht beim Verein eCH die Fachgruppe „Politische Rechte". Beide betreffen den politischen Bereich, decken aber unterschiedliche Domänen ab:

- **Politische Geschäfte** (diese Standardfamilie) beschreibt den parlamentarischen und behördlichen Willensbildungs- und Entscheidungsprozess: die Akteure (eCH-0294), den Ratsbetrieb (eCH-0293), die parlamentarischen Geschäfte (eCH-0295), die daraus hervorgehenden Erlasse (eCH-0296) sowie die vorgelagerten Vernehmlassungen (eCH-0297).
- **Politische Rechte** befasst sich mit der Ausübung der politischen Rechte durch die Stimmberechtigten: Stimm- und Wahlregister, die Durchführung von Volksabstimmungen und Wahlen, die elektronische Stimmabgabe (eVoting), Stimmrechtsausweise sowie Abstimmungs- und Wahlergebnisse (u.a. eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

Berührungspunkte bestehen an zwei Stellen:

- **Abstimmungen und Wahlen:** eCH-0293 erfasst Abstimmungen und Wahlen **innerhalb des Ratsbetriebs** (z.B. namentliche Abstimmungen im Parlament oder die Wahl von Behördenmitgliedern durch den Rat), während Volksabstimmungen und Volkswahlen samt der zugehörigen Register, Durchführung und Ergebnisse von der Fachgruppe „Politische Rechte" abgedeckt werden.
- **Gewählte Personen:** In den Wahlergebnissen der Fachgruppe „Politische Rechte" erscheinen Kandidierende und Gewählte. Sobald Personen ein Mandat innehaben, werden sie in eCH-0294 als politische Akteurinnen und Akteure mit ihren Rollen und Mitgliedschaften geführt.

## Der Standard eCH-0294 – Politische Akteure

Dieser Standard definiert vier Hauptklassen:

- **Person** – Natürliche Personen im politischen Kontext
- **Group** – Gremien, Parteien, Fraktionen, Räte, Kommissionen, Organisationen etc.
- **Membership** – Verbindung zwischen Personen und Gruppen
- **InterestLink** – Interessenbindungen von Personen

`Membership` ist das zentrale Bindeglied zwischen `Person` und `Group` und hält fest, in welchem Parlament, in welcher Kommission etc. eine Person aktiv ist oder war. `InterestLink` ermöglicht die Beschreibung von Interessenbindungen.
\newpage

# Person

Das Personenschema beschreibt natürliche Personen im politischen Kontext.

- **Stabile Person, zeitlich gültige Merkmale:** Die `Person` selbst trägt keine zeitliche Gültigkeit, ihre Merkmale hingegen schon – Name, Staatsangehörigkeit, Geschlecht, Beruf, Ausbildung und Wahlkreis tragen je eigene `valid_from`/`valid_through`. So bleibt die Identität der Person stabil, während sich einzelne Angaben über die Zeit ändern und die Historie erhalten bleibt (z. B. Namensänderung bei Heirat oder Wechsel des Wahlkreises).
- **Obligatorischer Anzeigename (`label`) neben strukturierten Namen (`names`):** Jede Person hat einen zwingenden Kurznamen, damit auch bei unvollständigen Angaben immer ein Anzeigename vorhanden ist. Empfohlen wird die Kombination aus amtlichem Namen (`PersonOfficialName`) und Rufname (`PersonCallFirstName`), bei Namensgleichheit ergänzt um das Geburtsjahr. `label_long` nimmt zusätzlich akademische Titel auf; die feingliedrige, typisierte Namensstruktur (`names`) ist optional.
- **Namenstypen nach amtlicher Systematik:** Die Namenstypen (`NameTypeEnum`) folgen der Registerharmonisierung des BFS bzw. eCH-0011 (u. a. amtlicher Name, angestammter Name, Allianzname, Rufname sowie Varianten für ausländische Ausweise). Damit sind die Namen mit den amtlichen Personenregistern kompatibel, statt eine eigene Systematik einzuführen.
- **`birth_year` als datensparsame Alternative zu `birth_date`:** Ist das genaue Geburtsdatum nicht verfügbar oder nicht zur Veröffentlichung bestimmt, kann nur das Geburtsjahr angegeben werden. Liegt ein `birth_date` vor, hat es Vorrang.
- **Mehrfachwerte statt Einzelwerte:** Namen, Staatsangehörigkeiten und Geschlechtsangaben sind als Listen mit zeitlicher Gültigkeit modelliert – etwa für Doppelbürgerschaften, Namensänderungen oder eine sich ändernde Geschlechtsangabe.
- **Harmonisierung über föderale Ebenen (Langzeitziel):** Die Verknüpfung derselben Person über die föderalen Ebenen hinweg ist ein wichtiges Langzeitziel. Der Aufbau einer zentralen Personendatenbank läge ausserhalb des Auftrags der eCH-Fachgruppe. Da für diesen Zweck bereits eine offene, etablierte Infrastruktur besteht, wird **Wikidata als übergreifender Identifikator empfohlen** (`wikidata_uri`); zusammen mit global eindeutigen Identifikatoren (URIs) lässt sich die Zuordnung so schrittweise über die Systeme hinweg harmonisieren.




## Class: Person 


_A person with identifiers, names, addresses, citizenships, and occupations._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 1 <br/> [String](#String) | Mandatory short display name to identify the person within the organisation (e.g. with added birth year to distinguish persons with the same name). Preferred: PersonOfficialName combined with PersonCallFirstName.  |
| label_long | 0..1 <br/> [String](#String) | Optional long display name including academic titles and full official name (e.g. "Dr. Maria Muster-Beispiel").  |
| birth_year | 0..1 <br/> [Integer](#Integer) | Year of birth. Only to be used, if there is no full `birthDate` available.  |
| birth_date | 0..1 <br/> [Date](#Date) | Exact date of birth if available and public. This field has precedence over the field `birthYear`.  |
| death_date | 0..1 <br/> [Date](#Date) | Exact date of death.  |
| picture | 0..1 <br/> [Uri](#Uri) | Link to an image (preferred: PNG, then JPG, then GIF).  |
| names | * <br/> [Name](#Name) | Names of the person with type and value.  |
| addresses | * <br/> [Address](#Address) | Addresses with type (private, business, local).  |
| language_proficiencies | * <br/> [LanguageProficiency](#LanguageProficiency) | Language proficiencies of the person.  |
| citizenships | * <br/> [Citizenship](#Citizenship) | Citizenships of the person.  |
| genders | * <br/> [Gender](#Gender) | Gender of the person.  |
| occupations | * <br/> [Occupation](#Occupation) | Occupations or professions of the person.  |
| trainings | * <br/> [Training](#Training) | Trainings or educations of the person. Guideline: generally only provide the highest qualification obtained.  |
| contacts | * <br/> [Contact](#Contact) | Contact information (email, website, social media). Guideline: email is quasi-mandatory and should always be provided where available.  |
| electoral_district | 0..1 <br/> [ElectoralDistrict](#ElectoralDistrict) | Link to the electoral district.  |
| interest_links | * <br/> [InterestLink](#InterestLink) | Collection of interest links.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [persons](#persons) | range | [Person](#Person) |














### Examples
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
- training_type: '2421'
  value: High School Diploma
contacts:
- contact_type: email
  value: douglas.adams@adams-familiy.org
electoral_district:
  district: London Central
  valid_from: 2020-01-01
  valid_through: 2025-01-01

```
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
electoral_district:
  district: Basel-Stadt
  valid_from: 2010-01-01

```






</div>



## Class: Name 


_A name with a type (e.g., call name, official name), a value, and a temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| name_type | 0..1 <br/> [NameTypeEnum](#NameTypeEnum) | Type of name according to eCH-0011 (personNameData).  |
| value | 0..1 <br/> [String](#String) | The value of an information besides other attributes such as type, language, etc.  |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [names](#names) | range | [Name](#Name) |



















</div>

## Enum: NameTypeEnum 




_Categories of name types according to eCH-0011 (personNameData) and https://dam-api.bfs.admin.ch/hub/api/dam/assets/24565576/master, URI according to I14Y identifier but as class and not as attribute. Descriptions and translations according to I14Y._

__



<div data-search-exclude markdown="1">

URI: [act:NameTypeEnum](https://ld.ech.ch/schema/0294/actors/NameTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| PersonOfficialName |  According to the official catalogue of characters (No. 211) for the harmonisation of registers: Name according to official documents. The official name corresponds to the name appearing in the Swiss civil register. For foreign nationals with no civil status events in Switzerland, the official name corresponds to the name appearing on the foreign passport or identity card (see ‘Name according to foreign passport’ or SEM guidelines on the determination and spelling of names of foreign nationals dated 1 January 2012. If no official documents exist, see also ‘Name according to declaration’ (e.g. in the case of asylum seekers). The official name may consist of one or more parts.  |
| | [https://register.ld.admin.ch/i14y/concept/personOfficialName](https://register.ld.admin.ch/i14y/concept/personOfficialName) |
| PersonOriginalName |  According to the official catalogue of characters (No. 212) for the harmonisation of registers: Name of filiation according to official documents, which corresponds to the person's name before their first marriage or registered partnership. It may also be a maiden name acquired by decision to change one's name (see Art. 24, para. 2 OEC, RS 211.112.2).  |
| | [https://register.ld.admin.ch/i14y/concept/personOriginalName](https://register.ld.admin.ch/i14y/concept/personOriginalName) |
| PersonAllianceName |  According to the official catalogue of characters (No. 213) for the harmonisation of registers: The alliance name shows the connection between two people who are married or living in a registered partnership. An alliance name that has already been used may be retained after the dissolution of the marriage or partnership if the official name has not been changed upon dissolution. It is attached to the official name with a hyphen and is formed with the partner's maiden name or the person's own maiden name. Upon request, the alliance name may be entered in the passport or on the identity card.  |
| | [https://register.ld.admin.ch/i14y/concept/personAllianceName](https://register.ld.admin.ch/i14y/concept/personAllianceName) |
| PersonNameOnForeignPassport |  According to the official catalogue of characters (No. 214) for the harmonisation of registers: For persons of foreign nationality. This name corresponds to the entry marked in the machine-readable zone of the passport. If this zone includes abbreviated surnames or first names, these must, as far as possible, be recorded in full, according to the entry in the passport.  |
| | [https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport) |
| PersonAliasName |  According to the official character catalogue (No. 215) for the harmonisation of registers: Name (e.g. stage name, religious name) which, on the basis of an accepted application, may be used by the person. The alias name may consist of one or more parts (e.g. also the alias first name and alias surname).  |
| | [https://register.ld.admin.ch/i14y/concept/personAliasName](https://register.ld.admin.ch/i14y/concept/personAliasName) |
| PersonOtherName |  According to the official catalogue of characters (No. 216) for the harmonisation of registers: Other official names according to Swiss civil status documents (Art. 24, para. 3 OEC) or according to foreign documents, which are neither surnames nor first names.  |
| | [https://register.ld.admin.ch/i14y/concept/personOtherName](https://register.ld.admin.ch/i14y/concept/personOtherName) |
| PersonDeclaredForeignerName |  According to the official catalogue of characters (No. 217) for the harmonisation of registers: For foreign nationals who do not have official documents (mainly in the field of asylum).  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName) |
| PersonFirstName |  First names taken from the birth certificate, the civil registry (Infostar) in the order in which they appear, or taken from foreign identity documents.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstName](https://register.ld.admin.ch/i14y/concept/personFirstName) |
| PersonCallFirstName |  A person has the right to choose a common first name from the list of their official first names. The common first name may consist of one or more first names (from those listed under ‘official first names’).  |
| | [https://register.ld.admin.ch/i14y/concept/personCallFirstName](https://register.ld.admin.ch/i14y/concept/personCallFirstName) |
| PersonFirstNameOnForeignPassport |  For persons of foreign nationality. To be used in combination with the name as it appears on the foreign passport.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport) |
| PersonDeclaredForeignerFirstName |  For persons of foreign nationality who do not have official documents (mainly in the field of asylum). To be used in combination with the defined Name according to declaration.  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName) |







</div>



## Class: LanguageProficiency 


_Language proficiency of a person indicating the language and whether it is the preferred language or native language._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| language | 0..1 <br/> [String](#String) | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |
| is_correspondence | 0..1 <br/> [Boolean](#Boolean) | Indicates if this is the preferred language.  |
| is_native | 0..1 <br/> [Boolean](#Boolean) | Indicates if this is the native language.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [language_proficiencies](#language_proficiencies) | range | [LanguageProficiency](#LanguageProficiency) |



















</div>



## Class: Citizenship 


_Citizenship (also used for Nationality) of a person indicating the country and temporal validity. If there is no `valid_from` provided, the information is not known. If it is known that the citizenship is valid from birth, the birthdate is to be repeated here. If there is no `valid_through`, the citizenship is still active._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| country | 0..1 <br/> [String](#String) | ISO 3166-1 alpha-2 country code.  |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [citizenships](#citizenships) | range | [Citizenship](#Citizenship) |



















</div>



## Class: Gender 


_Gender of a person indicating a gender code and temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| gender_code | 0..1 <br/> [GenderCodeEnum](#GenderCodeEnum) | Gender code. Recommended values: male, female, diverse.  |
| label | 0..1 <br/> [String](#String) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| pronouns | * <br/> [String](#String) | Pronouns used by the person.  |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [genders](#genders) | range | [Gender](#Gender) |



















</div>

## Enum: GenderCodeEnum 




_Gender codes for persons. If the gender is not known, no gender entry shall be added. The `diverse` code shall be used together with a label to provide further details about the self-identified gender._

__



<div data-search-exclude markdown="1">

URI: [act:GenderCodeEnum](https://ld.ech.ch/schema/0294/actors/GenderCodeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| male |  Male. |
| |  |
| female |  Female. |
| |  |
| diverse |  Diverse / non-binary. |
| |  |







</div>



## Class: Occupation 


_Occupation or profession of a person indicating a label, an ISCO-19 code, whether the position is paid, and temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Indicates if the position is paid.  |
| occupation_code | 0..1 <br/> [String](#String) | ISCO-19 code of the occupation.  |
| label | 0..1 <br/> [String](#String) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| organization_uid | 0..1 <br/> [String](#String) | UID of the organization (eCH-0098 format: CHE-XXX.XXX.XXX of the federal UID register (uid.admin.ch).  |
| organization_name | 0..1 <br/> [String](#String) | Name of the organization or enterprise.  |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |





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


_Training or education of a person indicating a type (e.g., school diploma, university degree, military service), a label, an ISCO-19 code, and temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| training_type | 0..1 <br/> [TrainingTypeEnum](#TrainingTypeEnum) | Type of training or education.  |
| training_code | 0..1 <br/> [String](#String) | ISCO-19 code of the training or education.  |
| value | 0..1 <br/> [String](#String) | The value of an information besides other attributes such as type, language, etc.  |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [trainings](#trainings) | range | [Training](#Training) |



















</div>

## Enum: TrainingTypeEnum 




_Types of training or education based on the Swiss BFS LEVEL_EDUC codelist._

__



<div data-search-exclude markdown="1">

URI: [act:TrainingTypeEnum](https://ld.ech.ch/schema/0294/actors/TrainingTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| 10 |  Maximum compulsory school. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/10](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/10) |
| 110 |  No education. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/110](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/110) |
| 120 |  Compulsory school attended but not completed. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/120](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/120) |
| 130 |  Compulsory school. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/130](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/130) |
| 140 |  1 year of education / transitional education. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/140](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/140) |
| 20 |  Upper secondary level. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/20](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/20) |
| 22 |  Upper secondary level - Vocational education and training (VET). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/22](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/22) |
| 220 |  Apprenticeship in a company (EFZ/EBA) / basic vocational training / vocational school / trade school. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/220](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/220) |
| 2210 |  Apprenticeship 2 years (EBA) / basic vocational training / vocational school / trade school. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2210](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2210) |
| 2211 |  Apprenticeship in a company 2 years (EBA) / basic vocational training. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2211](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2211) |
| 2212 |  Vocational school / trade school 2 years. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2212](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2212) |
| 2220 |  Apprenticeship 3-4 years (EFZ) / vocational school / trade school. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2220](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2220) |
| 2221 |  Apprenticeship in a company 3-4 years (EFZ). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2221](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2221) |
| 2222 |  Vocational school / trade school 3-4 years. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2222](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2222) |
| 24 |  Upper secondary level - general education. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/24](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/24) |
| 241 |  Upper secondary specialised schools / diploma middle school. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/241](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/241) |
| 2411 |  Upper secondary specialised schools / diploma middle school 2 years. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2411](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2411) |
| 2412 |  Upper secondary specialised schools / diploma middle school 3 years. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2412](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2412) |
| 242 |  Baccalaureate / teaching diploma. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/242](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/242) |
| 2421 |  Baccalaureate. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2421](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2421) |
| 2422 |  Teaching diploma. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2422](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2422) |
| 243 |  Vocational / specialised baccalaureate. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/243](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/243) |
| 2431 |  Vocational baccalaureate. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2431](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2431) |
| 2432 |  Specialised baccalaureate. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2432](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/2432) |
| 30 |  Tertiary level. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/30](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/30) |
| 31 |  Professional education. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/31](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/31) |
| 310 |  Professional examination with federal diploma / advanced federal diploma / PET diploma. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/310](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/310) |
| 311 |  Professional examination with federal diploma of higher education. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/311](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/311) |
| 312 |  Professional examination with advanced federal diploma of higher education / PET diploma. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/312](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/312) |
| 313 |  College of Higher Education. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/313](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/313) |
| 3131 |  College of Higher Education 2 years full time or 3 years part-time. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3131](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3131) |
| 3132 |  College of Higher Education 3 years full time or 4 years part-time. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3132](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3132) |
| 32 |  Higher education institutions. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/32](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/32) |
| 321 |  Bachelor universities, institutes of technology, universities of applied sciences, universities of teacher education. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/321](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/321) |
| 3211 |  Bachelor universities of applied sciences (including UAS diploma). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3211](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3211) |
| 3212 |  Bachelor universities of teacher education (including UTE first degree). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3212](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3212) |
| 3213 |  Bachelor universities, institutes of technology (UIT). |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3213](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3213) |
| 322 |  Master universities, institutes of technology, universities of applied sciences, universities of teacher education. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/322](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/322) |
| 3221 |  Master universities of applied sciences. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3221](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3221) |
| 3222 |  Master universities of teacher education. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3222](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3222) |
| 3223 |  Master universities, institutes of technology (UIT) including UNI / UIT diploma. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3223](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/3223) |
| 323 |  Doctorate or habilitation. |
| | [https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/323](https://register.ld.admin.ch/i14y/concept/LEVEL_EDUC/323) |
| military |  Military service (Swiss army). Use `value` to specify the rank reached. |
| |  |







</div>



## Class: ElectoralDistrict 


_Electoral district or region where a person is politically active; with temporal validity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| district | 0..1 <br/> [String](#String) | Electoral district or region.  |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |





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

\newpage

# Gruppen und Organe (Groups)

Das Group-Schema bildet politische Gruppen, Organisationen und Körperschaften ab.

- **Ein generisches Modell statt vieler Spezialklassen:** Parlamente, Parteien, Fraktionen, Kommissionen, Departemente, Gerichte und zivilgesellschaftliche Organisationen werden alle als *eine* Klasse `Group` abgebildet und über `group_type` unterschieden. Das hält das Modell einfach und ohne Schemaänderung erweiterbar – Legislative, Exekutive, Judikative und Zivilgesellschaft sind damit gleichermassen abbildbar.
- **Gruppen und Sub-Gruppen über `parent_groups`:** Untergeordnete Gruppen verweisen auf ihre übergeordnete Gruppe – z. B. eine Kommission des Ständerats, eine Subkommission innerhalb einer Kommission, eine Kantonalpartei unter ihrer Mutterpartei oder eine Behörde innerhalb einer Direktion. Die Hierarchie entsteht so aus diesen Verweisen statt aus einer festen Ebenenstruktur. Sie bleibt meist innerhalb desselben `group_type`; typenübergreifende und mehrfache Verweise sind aber möglich (z. B. eine Fraktion, die zugleich auf ihr Parlament und ihre Partei verweist).
- **Zeitliche Gültigkeit auch für Gruppen:** Über `valid_from`/`valid_through` lassen sich z. B. nur während einer Legislatur bestehende Kommissionen oder Umbenennungen und Fusionen von Parteien abbilden.



## Class: Group 


_A political group, organization, or body (e.g., party, committee, parliament, department)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| group_type | 0..1 <br/> [GroupType](#GroupType) | Type of group (e.g., party, commission, parliament, or similar). The exact naming and description of the group is provided via `label`.  |
| label | 0..1 <br/> [String](#String) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abbreviation (can be multilingual).  |
| description | * <br/> [MultilingualValue](#MultilingualValue) | Description of the entity.  |
| landing_page | 0..1 <br/> [Uri](#Uri) | Website providing further information.  |
| parent_groups | * <br/> [Uriorcurie](#Uriorcurie) | Link to parent groups. For example, the parent party for cantonal parties, or to describe the hierarchy in the executive. Also used to link sub-commissions to commissions, or factions to both their parliament and their party. (parentGroup is typically used within the same group_type, but cross-type links are permitted, e.g., faction → parliament and faction → party.)  |
| spatial | 0..1 <br/> [String](#String) | Spatial reference (fos-municipality number, fos-canton number, or country). Formats: municipality: ld.admin.ch/municipality/1234, canton: ld.admin.ch/canton/23, country: ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](#Contact) | Contact information (email, website, social media). Guideline: email is quasi-mandatory and should always be provided where available.  |
| addresses | * <br/> [Address](#Address) | Addresses with type (private, business, local).  |
| statutes_url | 0..1 <br/> [String](#String) | URL to party statutes (PDF or webpage; optional for parties).  |
| party_color | 0..1 <br/> [String](#String) | Party color as hexadecimal value (optional for parties, e.g., "#FF0000").  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [groups](#groups) | range | [Group](#Group) |



















</div>



## Class: GroupType 


_Type of group (e.g., party, committee, parliament, department)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| group_type_enum | 0..1 <br/> [GroupTypeEnum](#GroupTypeEnum) | Link to the controlled vocabulary for group types.  |
| label | 0..1 <br/> [String](#String) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](#Group) | [group_type](#group_type) | range | [GroupType](#GroupType) |



















</div>

## Enum: GroupTypeEnum 




_Types of political groups and organizations._

__



<div data-search-exclude markdown="1">

URI: [act:GroupTypeEnum](https://ld.ech.ch/schema/0294/actors/GroupTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| party |  Political party at federal, cantonal, or municipal level. Each federal level is managed as its own group (e.g., national party, cantonal party, municipal party).  |
| | [act:enum/group_type/party](act:enum/group_type/party) |
| list |  Electoral list (can be part of a party or independent).  |
| | [act:enum/group_type/list](act:enum/group_type/list) |
| workgroup |  Ad-hoc working group, typically with a limited duration.  |
| | [act:enum/group_type/workgroup](act:enum/group_type/workgroup) |
| parliament |  Parliament at federal, cantonal, or municipal level (e.g., Federal Assembly, National Council, Council of States, Grand Council, cantonal parliament, municipal parliament).  |
| | [act:enum/group_type/parliament](act:enum/group_type/parliament) |
| delegation |  Delegation.  |
| | [act:enum/group_type/delegation](act:enum/group_type/delegation) |
| commission |  Commission (permanent or ad-hoc), including supervisory commissions (e.g., CPC), subject commissions, parliamentary investigation commissions (PIC), and audit commissions.  |
| | [act:enum/group_type/commission](act:enum/group_type/commission) |
| faction |  Parliamentary faction.  |
| | [act:enum/group_type/faction](act:enum/group_type/faction) |
| parliamentary_bureau |  Parliamentary bureau.  |
| | [act:enum/group_type/parliamentary_bureau](act:enum/group_type/parliamentary_bureau) |
| presidency |  Presidency of parliament.  |
| | [act:enum/group_type/presidency](act:enum/group_type/presidency) |
| government |  Government / Executive as a collective body (e.g., Federal Council, Cantonal Government, City or Municipal Council).  |
| | [act:enum/group_type/government](act:enum/group_type/government) |
| department |  Government department.  |
| | [act:enum/group_type/department](act:enum/group_type/department) |
| office |  Government office.  |
| | [act:enum/group_type/office](act:enum/group_type/office) |
| extraparliamentary_commission |  Extra-parliamentary commission with a government mandate (e.g., Bank Council of the Swiss National Bank, FINMA).  |
| | [act:enum/group_type/extraparliamentary_commission](act:enum/group_type/extraparliamentary_commission) |
| interest_group |  Interest group from civil society.  |
| | [act:enum/group_type/interest_group](act:enum/group_type/interest_group) |
| control_body |  Control or supervisory body (e.g., Federal Finance Control EFC, supervisory authority AB-BA).  |
| | [act:enum/group_type/control_body](act:enum/group_type/control_body) |
| parliamentary_services |  Parliamentary services.  |
| | [act:enum/group_type/parliamentary_services](act:enum/group_type/parliamentary_services) |
| court |  Court / Judiciary at any level (e.g., Federal Court, Cantonal Court, District Court).  |
| | [act:enum/group_type/court](act:enum/group_type/court) |
| association |  Association.  |
| | [act:enum/group_type/association](act:enum/group_type/association) |
| petition_carrier |  Petition carrier.  |
| | [act:enum/group_type/petition_carrier](act:enum/group_type/petition_carrier) |
| university |  University or educational institution as an outsourced provider of public tasks.  |
| | [act:enum/group_type/university](act:enum/group_type/university) |
| other |  Other group type not covered by standard categories.  |
| | [act:enum/group_type/other](act:enum/group_type/other) |







</div>
\newpage

# Mitgliedschaften (Memberships)

Das Membership-Schema bildet die Beziehung zwischen Personen und Gruppen ab und ist das zentrale Bindeglied im Akteur-Schema.

- **Abgrenzung zu Interessenbindungen (`InterestLink`):** `Membership` erfasst die *formale Zugehörigkeit* einer Person zu einer Gruppe innerhalb des Akteur-Schemas (z. B. Partei-, Kommissions- oder Parlamentsmitgliedschaft). Interessenbindungen und Interessenkonflikte zu Organisationen *ausserhalb* des Schemas sind bewusst davon getrennt und werden über `InterestLink` abgebildet (siehe folgendes Kapitel).
- **Referenzen mit Snapshot statt Einbettung (`person_reference`/`group_reference`):** Eine Mitgliedschaft verweist über leichtgewichtige Referenzen auf Person und Gruppe und hält dabei deren wichtigste Identifikationsmerkmale zum Zeitpunkt der Verknüpfung fest. So bleibt der Eintrag historisch korrekt, auch wenn sich Person oder Gruppe später ändern.
- **Aktivität explizit oder abgeleitet (`is_active`):** Ob eine Mitgliedschaft aktiv ist, kann explizit über `is_active` gesetzt oder aus der zeitlichen Gültigkeit abgeleitet werden. Ist `is_active` nicht gesetzt, ergibt sich die Aktivität aus `valid_from`/`valid_through`.
- **Mitgliedschaft ≠ Stimmrecht (`authorized_to_vote`):** Das Stimmrecht wird getrennt von der Mitgliedschaft geführt – typischerweise `false` bei Ersatzmitgliedern (ausser im Einsatz), Beobachtenden, dem Sekretariat und Gästen.
- **Rolle als kontrolliertes Vokabular mit Freitext-Option (`role_type`):** Die Rolle in der Gruppe (z. B. Mitglied, Präsidium, Stellvertretung) wird über ein kontrolliertes Vokabular (`RoleEnum`) angegeben; für nicht abgedeckte Rollen dient der Wert `other` mit einer freien Bezeichnung.



## Class: Membership 


_A membership relationship between a person and a group, representing formal affiliation (e.g., party member, commission member, parliamentarian). Distinct from InterestLink, which covers external interest bindings and conflicts of interest to organizations outside the actor schema._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| person_reference | 0..1 <br/> [PersonReference](#PersonReference) | Reference to a person with snapshot data at time of linking.  |
| group_reference | 0..1 <br/> [GroupReference](#GroupReference) | Reference to a group with snapshot data at time of linking.  |
| role_type | 0..1 <br/> [RoleType](#RoleType) | Role of the person in the membership or function.  |
| authorized_to_vote | 0..1 <br/> [Boolean](#Boolean) | Indicates if the person is authorized to vote in the group. Typically false for substitute members (when not deputizing), observers, secretaries, and guests.  |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates if the membership is currently active. Can complement or replace `valid_from`/`valid_through`. If not set, activity is derived from the temporal validity fields.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [memberships](#memberships) | range | [Membership](#Membership) |



















</div>

\newpage

# Interessenbindungen (Interest Links)

Das InterestLink-Schema erfasst Interessenbindungen, Interessenkonflikte und Verflechtungen von Personen mit Organisationen. Es orientiert sich an den Transparenzanforderungen für Parlamentsmitglieder gemäss [Bundesversammlung – Interessenbindungen](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

- **Abgrenzung zu Mitgliedschaften (`Membership`):** `InterestLink` bildet Bindungen zu Organisationen *ausserhalb* des Akteur-Schemas ab (Interessenkonflikte, Politikfinanzierung) – im Unterschied zur formalen Zugehörigkeit *innerhalb* des Schemas, die über `Membership` erfasst wird.
- **Obligatorische Klassifikation (`interest_type`):** Jede Bindung wird zwingend nach Art eingeordnet (berufliche Tätigkeit, politische Ämter, Verein), angelehnt an die Offenlegungskategorien der Bundesversammlung.
- **Organisation über UID referenzierbar (`organization_uid`):** Ist die Organisation im UID-Register erfasst, wird sie über ihre UID (eCH-0098, `CHE-XXX.XXX.XXX`) referenziert – das ermöglicht Auswertungen, z. B. mit NOGA-Codes. Für Organisationen ohne UID stehen `organization_name`/`organization_address` bereit; die Rechtsform folgt einem kontrollierten Vokabular (`LegalFormEnum`).
- **Umfang und Entschädigung (`is_paid`, `committee`, `function_role`):** Neben Gremium und Funktion innerhalb der Organisation wird explizit festgehalten, ob die Position bezahlt ist – ein zentraler Transparenzaspekt.





## Class: InterestLink 


_An interest link (conflict of interest, political financing) of a person to an organization outside the actor schema._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| person_reference | 0..1 <br/> [PersonReference](#PersonReference) | Reference to a person with snapshot data at time of linking.  |
| interest_type | 1 <br/> [InterestTypeEnum](#InterestTypeEnum) | Type of interest link (professional activity, political office, association).  |
| organization_name | 0..1 <br/> [String](#String) | Name of the organization or enterprise.  |
| organization_uid | 0..1 <br/> [String](#String) | UID of the organization (eCH-0098 format: CHE-XXX.XXX.XXX of the federal UID register (uid.admin.ch).  |
| organization_address | 0..1 <br/> [String](#String) | Address of the organization.  |
| legal_form | 0..1 <br/> [LegalFormEnum](#LegalFormEnum) | Legal form of the organization. See controlled vocabulary: https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Indicates if the position is paid.  |
| committee | 0..1 <br/> [String](#String) | Committee or board within the organization (e.g., Verwaltungsrat, Stiftungsrat, Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung).  |
| function_role | 0..1 <br/> [String](#String) | Function or role in the organization (e.g., Präsident/in, Vizepräsident/in, Mitglied, Delegierter, Geschäftsführer/in, Berater/in).  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |





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
organization_name: Burkart Advisory GmbH, Baden
legal_form: '0107'
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_002

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Birchmeier Holding AG, Döttingen
legal_form: '0106'
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
organization_name: Bovida Real Estate AG, Baar
legal_form: '0106'
committee: Verwaltungsrat
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
organization_name: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: 0109
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_010

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Allianz Sicherheit Schweiz, Baden
legal_form: 0109
committee: Vorstand
function_role: Präsident
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_004

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: ELCA Group SA, Lausanne
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
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
organization_name: FONDATION SUISSE DE DEMINAGE (FSD), Genf
legal_form: '0110'
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_006

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FDP.Die Liberalen
legal_form: 0109
committee: Vorstand
function_role: Präsident
is_paid: true

```
#### Example: InterestLink-interest_links_il_burkart_011

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Verein Landesausstellung Svizra27, Aarau
legal_form: 0109
committee: Vorstand
function_role: Mitglied
is_paid: false

```
#### Example: InterestLink-interest_links_il_burkart_009

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: 0109
committee: Vorstand
function_role: Mitglied
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
organization_name: Stiebel Eltron AG, Lupfig
legal_form: '0106'
committee: Beirat
function_role: Beirat
is_paid: true

```






</div>

## Enum: InterestTypeEnum 




_Types of interest links (conflicts of interest, political financing)._

__



<div data-search-exclude markdown="1">

URI: [act:InterestTypeEnum](https://ld.ech.ch/schema/0294/actors/InterestTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| professional_activity |  Professional activity outside the political mandate (e.g., employment, self-employment, consulting, board mandates in private companies).  |
| | [act:enum/interest_type/professional_activity](act:enum/interest_type/professional_activity) |
| political_office |  Political office or mandate at other federal levels or in other bodies (e.g., cantonal/municipal parliament membership, government council, extra-parliamentary commission).  |
| | [act:enum/interest_type/political_office](act:enum/interest_type/political_office) |
| association |  Membership in associations, federations, or interest organizations (e.g., industry associations, professional associations, lobby organizations, foundations, charitable associations).  |
| | [act:enum/interest_type/association](act:enum/interest_type/association) |







</div>

## Enum: LegalFormEnum 




_Legal forms based on the Swiss UID register codelist (eCH-0108). See https://register.ld.admin.ch/i14y/concept/legalForm_

__



<div data-search-exclude markdown="1">

URI: [act:LegalFormEnum](https://ld.ech.ch/schema/0294/actors/LegalFormEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| 0101 |  Sole proprietorship. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0101](https://register.ld.admin.ch/i14y/concept/legalForm/0101) |
| 0103 |  General partnership (GP). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0103](https://register.ld.admin.ch/i14y/concept/legalForm/0103) |
| 0104 |  Limited partnership (LP). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0104](https://register.ld.admin.ch/i14y/concept/legalForm/0104) |
| 0105 |  Corporation with unlimited partners (CUP). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0105](https://register.ld.admin.ch/i14y/concept/legalForm/0105) |
| 0106 |  Corporation (Ltd). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0106](https://register.ld.admin.ch/i14y/concept/legalForm/0106) |
| 0107 |  Limited liability company (LLC). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0107](https://register.ld.admin.ch/i14y/concept/legalForm/0107) |
| 0108 |  Cooperative. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0108](https://register.ld.admin.ch/i14y/concept/legalForm/0108) |
| 0109 |  Association. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0109](https://register.ld.admin.ch/i14y/concept/legalForm/0109) |
| 0110 |  Foundation. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0110](https://register.ld.admin.ch/i14y/concept/legalForm/0110) |
| 0111 |  Branch of a foreign company. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0111](https://register.ld.admin.ch/i14y/concept/legalForm/0111) |
| 0113 |  Special legal form. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0113](https://register.ld.admin.ch/i14y/concept/legalForm/0113) |
| 0114 |  Limited Partnership for collective investment schemes (LPCI). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0114](https://register.ld.admin.ch/i14y/concept/legalForm/0114) |
| 0115 |  Limited Partnership for collective investment schemes with a variable capital (SICAV). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0115](https://register.ld.admin.ch/i14y/concept/legalForm/0115) |
| 0116 |  Limited Partnership for collective investment schemes with a fixed capital (SICAF). |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0116](https://register.ld.admin.ch/i14y/concept/legalForm/0116) |
| 0117 |  Public-law institution. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0117](https://register.ld.admin.ch/i14y/concept/legalForm/0117) |
| 0118 |  Non-commercial power of attorney. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0118](https://register.ld.admin.ch/i14y/concept/legalForm/0118) |
| 0119 |  Representative of the community of property. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0119](https://register.ld.admin.ch/i14y/concept/legalForm/0119) |
| 0151 |  Branch. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0151](https://register.ld.admin.ch/i14y/concept/legalForm/0151) |
| 0220 |  Administrative unit of the Confederation. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0220](https://register.ld.admin.ch/i14y/concept/legalForm/0220) |
| 0221 |  Administrative unit of the canton. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0221](https://register.ld.admin.ch/i14y/concept/legalForm/0221) |
| 0222 |  Administrative unit of the district. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0222](https://register.ld.admin.ch/i14y/concept/legalForm/0222) |
| 0223 |  Administrative unit of the commune. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0223](https://register.ld.admin.ch/i14y/concept/legalForm/0223) |
| 0224 |  Other public-law administrative unit. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0224](https://register.ld.admin.ch/i14y/concept/legalForm/0224) |
| 0230 |  Public-law institution of the Confederation. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0230](https://register.ld.admin.ch/i14y/concept/legalForm/0230) |
| 0231 |  Public-law institution of the canton. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0231](https://register.ld.admin.ch/i14y/concept/legalForm/0231) |
| 0232 |  Public-law institution of the district. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0232](https://register.ld.admin.ch/i14y/concept/legalForm/0232) |
| 0233 |  Public-law institution of the commune. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0233](https://register.ld.admin.ch/i14y/concept/legalForm/0233) |
| 0234 |  Other public-law institution. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0234](https://register.ld.admin.ch/i14y/concept/legalForm/0234) |
| 0302 |  Simple partnership. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0302](https://register.ld.admin.ch/i14y/concept/legalForm/0302) |
| 0312 |  Permanent establishment or swiss representation of a foreign company. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0312](https://register.ld.admin.ch/i14y/concept/legalForm/0312) |
| 0327 |  Foreign public company. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0327](https://register.ld.admin.ch/i14y/concept/legalForm/0327) |
| 0328 |  Foreign public administration. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0328](https://register.ld.admin.ch/i14y/concept/legalForm/0328) |
| 0329 |  International organisation. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0329](https://register.ld.admin.ch/i14y/concept/legalForm/0329) |
| 0355 |  Other cooperative. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0355](https://register.ld.admin.ch/i14y/concept/legalForm/0355) |
| 0361 |  Trust. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0361](https://register.ld.admin.ch/i14y/concept/legalForm/0361) |
| 0362 |  Fund. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0362](https://register.ld.admin.ch/i14y/concept/legalForm/0362) |
| 0441 |  Foreign company. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0441](https://register.ld.admin.ch/i14y/concept/legalForm/0441) |
| 0571 |  Legal form undefined or unknown. |
| | [https://register.ld.admin.ch/i14y/concept/legalForm/0571](https://register.ld.admin.ch/i14y/concept/legalForm/0571) |







</div>
\newpage

# Geteilte Elemente

## Reference Classes

`PersonReference` und `GroupReference` werden verwendet, um Personen bzw. Gruppen **lokal** innerhalb einer anderen Entität zu referenzieren. Neben dem eigentlichen Link zur vollständigen Entität werden dabei nur die relevanten Informationen zum **Zeitpunkt der Verknüpfung** gespeichert – es müssen also nicht alle Informationen einer Person oder Gruppe bei jeder Erwähnung wiederholt werden.

Ein Beispiel: Eine Motion verweist auf die Person, die sie eingereicht hat. Zusätzlich zum Link auf die vollständige Personen-Entität speichert die Motion lokal Informationen wie die politische Partei oder die Rolle der Person **zum Zeitpunkt der Einreichung**. Wechselt die Person später die Partei oder die Rolle, bleibt die Information in der Motion dennoch korrekt und unveränderlich.

Dies dient drei Zwecken:

- **Nützliche lokale Daten** ohne aufwändige Abfragen der vollständigen Entität
- **Keine Redundanz**, da nicht alle Informationen bei jeder Erwähnung wiederholt werden müssen
- **Implizite Versionierung**, da die lokale Referenz unverändert bleibt, auch wenn sich die verknüpfte Entität später ändert



## Class: PersonReference 


_Lightweight reference to a person with key identification data at time of linking. Preserves historical accuracy even if the person changes later._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 1 <br/> [String](#String) | Mandatory short display name to identify the person within the organisation (e.g. with added birth year to distinguish persons with the same name).  |
| label_long | 0..1 <br/> [String](#String) | Optional long display name including academic titles and full official name (e.g. "Dr. Maria Muster-Beispiel").  |
| group_label | 0..1 <br/> [String](#String) | Name of the body/group at time of linking.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |
| [InterestLink](#InterestLink) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |



















</div>



## Class: GroupReference 


_Lightweight reference to a group with key identification data at time of linking._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abbreviation (can be multilingual).  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [group_reference](#group_reference) | range | [GroupReference](#GroupReference) |



















</div>

## Mehrfach benutzte Klassen



## Class: Address 


_An address with a type (e.g., private address, business address) and a value._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| address_type | 0..1 <br/> [AddressTypeEnum](#AddressTypeEnum) | Type of address.  |
| address_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | URI of the address from the Swiss federal building address register. The layer can be accessed at https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis. Example of a valid URI: https://geo.ld.admin.ch/location/address/101904050  |
| street_address | 0..1 <br/> [String](#String) | Street address.  |
| postal_code | 0..1 <br/> [Integer](#Integer) | Postal code.  |
| postal_locality | 0..1 <br/> [String](#String) | Locality.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [addresses](#addresses) | range | [Address](#Address) |
| [Group](#Group) | [addresses](#addresses) | range | [Address](#Address) |














### Examples
#### Example: Address-swiss_politicians_Beat_Jans_1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```
#### Example: Address-douglas_adams_Douglas_Adams_1

```yaml
address_type: privateAddress
street_address: 1234 Fictional St, London, UK
postal_code: 12345
postal_locality: London

```






</div>

## Enum: AddressTypeEnum 




_Types of addresses._

__



<div data-search-exclude markdown="1">

URI: [act:AddressTypeEnum](https://ld.ech.ch/schema/0294/actors/AddressTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| privateAddress |  Private address.  |
| |  |
| businessAddress |  Business address.  |
| |  |
| localAddress |  Local address.  |
| |  |







</div>



## Class: Contact 


_Contact information of a person indicating a type (e.g., email, LinkedIn) and a value._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| contact_type | 0..1 <br/> [ContactTypeEnum](#ContactTypeEnum) | Type of contact information.  |
| value | 0..1 <br/> [String](#String) | The value of an information besides other attributes such as type, language, etc.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [contacts](#contacts) | range | [Contact](#Contact) |
| [Group](#Group) | [contacts](#contacts) | range | [Contact](#Contact) |



















</div>
