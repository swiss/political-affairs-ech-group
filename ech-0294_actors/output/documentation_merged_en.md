---
title: "eCH-0294 Political Actors: Persons, Groups and Bodies"
lang: en
toc: false
---

|**Name**|**Political Actors: Persons, Groups and Bodies**|
|---|---|
|**eCH number**|eCH-0294|
|**Category**|Standard|
|**Maturity level**|Defined|
|**Version**|1.0.0|
|**Status**|Proposal|
|**Adopted on**||
|**Issue date**|2026-07-22|
|**Replaces version**||
|**Prerequisites**||
|**Annexes**|-|
|**Languages**|German (original) - English (data model)|
|**Authors**|Political Affairs specialist group: Julie Silberstein, Laurence Brandenberger, Daniela Koller, Thomas Roth, Stefan Oderbolz, Fabian Davolio, Orhan Saeedi, Christian Gutknecht, Michael Luggen|
|**Publisher / Distribution**|eCH Association, [Affolternstrasse 52, 8050 Zürich](https://geo.ld.admin.ch/location/address/101218624)|

\newpage

# Abstract

The standard eCH-0294 "Political Actors: Persons, Groups and Bodies" defines a uniform data model for the structured publication of political actors in Switzerland. It covers natural persons, political groups and bodies, memberships between persons and groups, as well as interest links. The aim is to provide comparable, machine-readable and reusable information across all federal levels in order to improve the transparency, traceability and analytical capability of political processes.

The standard is aimed at public bodies at all levels of government, political actors, the media, research and the general public, and it creates a foundation for interoperable political information systems in Switzerland.

\newpage

# Table of Contents

```{=openxml}
<w:p>
  <w:r>
    <w:fldChar w:fldCharType="begin" w:dirty="true"/>
  </w:r>
  <w:r>
    <w:instrText xml:space="preserve"> TOC \o "1-2" \h \z \u </w:instrText>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:t>Right-click &gt; "Update field" to generate the table of contents.</w:t>
  </w:r>
  <w:r>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
</w:p>
```

\newpage

# Introduction

## The "Political Affairs" standard family

Political activity in Switzerland takes place at federal, cantonal and communal level – in parliaments and communal assemblies, in executives and administrations, in consultations and hearings, as well as through the direct-democratic participation of eligible voters. To this end, the "Political Affairs" specialist group of the eCH Association is developing a family of coordinated standards that structure this data across all federal levels. The standards use common data elements (eCH-0292) and reference one another via unique identifiers.

The family comprises:

- **eCH-0292 – Common Data Elements (Meta):** Defines the cross-cutting data elements and meta-processes on which the other standards build.
- **eCH-0293 – Public Council Operations (Operations):** Describes public council operations – meetings, agenda items, statements, as well as votes and elections.
- **eCH-0294 – Political Actors (Actors) – this standard:** Defines persons, groups and bodies in the political context, as well as their memberships and interest links. The other standards reference these actors via their identifiers.
- **eCH-0295 – Parliamentary Affairs (Affairs):** Describes the life cycle of political affairs.
- **eCH-0296 – Enactments and Legal Texts (Laws):** Records the results of the parliamentary process – the adopted laws and enactments.
- **eCH-0297 – Public Consultations (Consultations):** Structures consultation procedures, which are often the starting point for parliamentary affairs.

The aim of this standard family is to create a commonly usable structure for political data and to provide organisations that publish information on political affairs with a robust data model.

## Distinction from the "Political Rights" specialist group

Alongside the "Political Affairs" specialist group, the eCH Association also maintains the "Political Rights" specialist group. Both concern the political domain, but cover different areas:

- **Political Affairs** (this standard family) describes the parliamentary and governmental process of forming opinions and reaching decisions: the actors (eCH-0294), council operations (eCH-0293), parliamentary affairs (eCH-0295), the enactments arising from them (eCH-0296), as well as the upstream consultations (eCH-0297).
- **Political Rights** deals with the exercise of political rights by eligible voters: voting and electoral registers, the conduct of popular votes and elections, electronic voting (eVoting), voting cards, as well as voting and election results (among others eCH-0045, eCH-0110, eCH-0155, eCH-0157, eCH-0159, eCH-0222, eCH-0228, eCH-0252, eCH-0310).

There are two points of contact:

- **Votes and elections:** eCH-0293 records votes and elections **within council operations** (e.g. recorded votes in parliament or the election of authority members by the council), whereas popular votes and popular elections, together with the associated registers, conduct and results, are covered by the "Political Rights" specialist group.
- **Elected persons:** Candidates and elected persons appear in the election results of the "Political Rights" specialist group. As soon as persons hold a mandate, they are recorded in eCH-0294 as political actors with their roles and memberships.

## The eCH-0294 standard – Political Actors: Persons, Groups and Bodies

This standard defines four main classes:

- **Person** – Natural persons in the political context
- **Group** – Committees, parties, parliamentary groups, councils, commissions, organisations, etc.
- **Membership** – Link between persons and groups
- **InterestLink** – Interest links of persons

`Membership` is the central connecting element between `Person` and `Group` and records in which parliament, in which commission, etc. a person is or was active. `InterestLink` enables the description of interest links.

\newpage

# Person

The person schema describes natural persons in the political context.

- **Stable person, temporally valid attributes:** The `Person` itself carries no temporal validity, but its attributes do – name, citizenship, gender, occupation and training each carry their own `valid_from`/`valid_through`. This keeps the identity of the person stable while individual details change over time and the history is preserved (e.g. a change of name upon marriage). The electoral district, by contrast, is not an attribute of the person: it is attached to the `Membership` (`electoral_district`) and inherits its temporal validity – a change of electoral district is therefore reflected in the respective membership.
- **Display name (`label`) mandatory, name structure (`names`) optional:** Every person has a short display name. This means a name is always available, even when the details are incomplete. The recommended combination is the official name (`PersonOfficialName`) and the call name (`PersonCallFirstName`). Academic titles can also be represented via `label_long`.
- **Name types according to the official taxonomy:** The name types (`NameTypeEnum`) adopt the taxonomy of the register harmonisation (including official name, original name, alliance name, call name, as well as variants for foreign identity documents). The authoritative reference is the [official catalogue of attributes](https://www.bfs.admin.ch/bfs/de/home/register/personenregister/registerharmonisierung/nomenklaturen.assetdetail.24565576.html), published by the Federal Statistical Office under Art. 4 of the Register Harmonisation Act (RHG, SR 431.02); the numbers in the value descriptions (211–224) are the attribute numbers of that catalogue. The corresponding exchange format is defined by the eCH standard [eCH-0011 Personal Data Standard](https://www.ech.ch/de/ech/ech-0011/9.0.0), on which this standard builds. This makes the names compatible with the official person registers and their semantics clear.
- **Date of birth at two levels of precision (`birth_year` / `birth_date`):** If the exact date of birth is not available or not intended for publication, only the year of birth may be given. If a `birth_date` is available, it takes precedence.
- **Multiple values instead of single values:** Names, citizenships and gender entries are modelled as lists with temporal validity – for example for dual citizenships, changes of name or a changing gender entry.
- **Gender: official codes plus an open category (`GenderCodeEnum`):** `male` and `female` correspond to the values of the register harmonisation and refer via `meaning` to the I14Y concepts `sex/1` and `sex/2`. For `non_binary` there is deliberately no counterpart: the official code list only knows "undefined" as its third value, which means something different from a positive statement beyond male and female. If the gender is not known, no entry is created at all — a missing entry and `non_binary` are to be clearly distinguished.
- **Harmonisation across federal levels (long-term goal):** Linking the same person across the federal levels is an important long-term goal. Building a central person database is beyond the means of the eCH specialist group. Since an open, established infrastructure already exists for this purpose, **Wikidata is recommended as a cross-cutting identifier** (`wikidata_uri`); together with globally unique identifiers (URIs), the mapping can thus be harmonised step by step across the systems.




## Class: Person 


_A person with identifiers, names, addresses, citizenships, and occupations._




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
| interest_links | * <br/> [InterestLink](#InterestLink) | Collection of interest links.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [persons](#persons) | range | [Person](#Person) |














### Examples
#### Example: Name variant alongside the official double name

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
#### Example: Call name differing from the official first name

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
#### Example: Non-binary gender entry with occupation and training

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
#### Example: Telling apart persons with identical names via the label

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
#### Example: Fully recorded person

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
#### Example: Telling apart persons with identical names via the label second person

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



## Class: Name 


_A name with a type (e.g., call name, official name), a value, and a temporal validity._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| name_type | 1 <br/> [NameTypeEnum](#NameTypeEnum) | Type of name according to eCH-0011 (personNameData).  |
| value | 1 <br/> [String](#String) | The value of an information besides other attributes such as type, language, etc.  |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [names](#names) | range | [Name](#Name) |



















</div>

## Enum: NameTypeEnum 




_Categories of name types according to eCH-0011 (personNameData) and the official catalogue of attributes of the register harmonisation (https://www.bfs.admin.ch/bfs/de/home/register/personenregister/registerharmonisierung/nomenklaturen.assetdetail.24565576.html), URI according to I14Y identifier but as class and not as attribute. Descriptions and translations according to I14Y._




<div data-search-exclude markdown="1">

URI: [act:NameTypeEnum](https://ld.ech.ch/schema/0294/actors/NameTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| PersonOfficialName |  Name according to official documents. The official name corresponds to the name appearing in the Swiss civil register. For foreign nationals with no civil status events in Switzerland, the official name corresponds to the name appearing on the foreign passport or identity card (see ‘Name according to foreign passport’ or SEM guidelines on the determination and spelling of names of foreign nationals dated 1 January 2012. If no official documents exist, see also ‘Name according to declaration’ (e.g. in the case of asylum seekers). The official name may consist of one or more parts. According to the official catalogue of attributes (No. 211) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personOfficialName](https://register.ld.admin.ch/i14y/concept/personOfficialName) |
| PersonOriginalName |  Name of filiation according to official documents, which corresponds to the person's name before their first marriage or registered partnership. It may also be a maiden name acquired by decision to change one's name (see Art. 24, para. 2 OEC, RS 211.112.2). According to the official catalogue of attributes (No. 212) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personOriginalName](https://register.ld.admin.ch/i14y/concept/personOriginalName) |
| PersonAllianceName |  The alliance name shows the connection between two people who are married or living in a registered partnership. An alliance name that has already been used may be retained after the dissolution of the marriage or partnership if the official name has not been changed upon dissolution. It is attached to the official name with a hyphen and is formed with the partner's maiden name or the person's own maiden name. Upon request, the alliance name may be entered in the passport or on the identity card. According to the official catalogue of attributes (No. 213) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personAllianceName](https://register.ld.admin.ch/i14y/concept/personAllianceName) |
| PersonNameOnForeignPassport |  For persons of foreign nationality. This name corresponds to the entry marked in the machine-readable zone of the passport. If this zone includes abbreviated surnames or first names, these must, as far as possible, be recorded in full, according to the entry in the passport. According to the official catalogue of attributes (No. 214) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personNameOnForeignPassport) |
| PersonAliasName |  Name (e.g. stage name, religious name) which, on the basis of an accepted application, may be used by the person. The alias name may consist of one or more parts (e.g. also the alias first name and alias surname). According to the official catalogue of attributes (No. 215) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personAliasName](https://register.ld.admin.ch/i14y/concept/personAliasName) |
| PersonOtherName |  Other official names according to Swiss civil status documents (Art. 24, para. 3 OEC) or according to foreign documents, which are neither surnames nor first names. According to the official catalogue of attributes (No. 216) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personOtherName](https://register.ld.admin.ch/i14y/concept/personOtherName) |
| PersonDeclaredForeignerName |  For foreign nationals who do not have official documents (mainly in the field of asylum). According to the official catalogue of attributes (No. 217) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerName) |
| PersonFirstName |  First names taken from the birth certificate, the civil registry (Infostar) in the order in which they appear, or taken from foreign identity documents. According to the official catalogue of attributes (No. 221) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstName](https://register.ld.admin.ch/i14y/concept/personFirstName) |
| PersonCallFirstName |  A person has the right to choose a common first name from the list of their official first names. The common first name may consist of one or more first names (from those listed under ‘official first names’). According to the official catalogue of attributes (No. 222) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personCallFirstName](https://register.ld.admin.ch/i14y/concept/personCallFirstName) |
| PersonFirstNameOnForeignPassport |  For persons of foreign nationality. To be used in combination with the name as it appears on the foreign passport. According to the official catalogue of attributes (No. 223) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport](https://register.ld.admin.ch/i14y/concept/personFirstNameOnForeignPassport) |
| PersonDeclaredForeignerFirstName |  For persons of foreign nationality who do not have official documents (mainly in the field of asylum). To be used in combination with the defined Name according to declaration. According to the official catalogue of attributes (No. 224) for the harmonisation of registers.  |
| | [https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName](https://register.ld.admin.ch/i14y/concept/personDeclaredForeignerFirstName) |







</div>



## Class: LanguageProficiency 


_Language proficiency of a person indicating the language and whether it is the preferred language or native language._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| language | 1 <br/> [String](#String) | Language code in ISO 639-1 format (two lowercase letters, e.g. "de", "fr", "it", "en").  |
| is_correspondence | 0..1 <br/> [Boolean](#Boolean) | Indicates if this is the preferred language.  |
| is_native | 0..1 <br/> [Boolean](#Boolean) | Indicates if this is the native language.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [language_proficiencies](#language_proficiencies) | range | [LanguageProficiency](#LanguageProficiency) |



















</div>



## Class: Citizenship 


_Citizenship (also used for Nationality) of a person indicating the country and temporal validity. If there is no `valid_from` provided, the information is not known. If it is known that the citizenship is valid from birth, the birthdate is to be repeated here. If there is no `valid_through`, the citizenship is still active._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| country | 1 <br/> [String](#String) | ISO 3166-1 alpha-2 country code.  |
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




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| gender_code | 1 <br/> [GenderCodeEnum](#GenderCodeEnum) | Gender code. Recommended values: male, female, non_binary.  |
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




_Gender codes for persons. If the gender is not known, no gender entry shall be added. The `non_binary` code shall be used together with a label to provide further details about the self-identified gender._




<div data-search-exclude markdown="1">

URI: [act:GenderCodeEnum](https://ld.ech.ch/schema/0294/actors/GenderCodeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| male |  Male. |
| | [https://register.ld.admin.ch/i14y/concept/sex/1](https://register.ld.admin.ch/i14y/concept/sex/1) |
| female |  Female. |
| | [https://register.ld.admin.ch/i14y/concept/sex/2](https://register.ld.admin.ch/i14y/concept/sex/2) |
| non_binary |  Diverse / non-binary. |







</div>



## Class: Occupation 


_Occupation or profession of a person indicating a label, an ISCO-19 code, whether the activity is paid, and temporal validity._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the activity is paid.  |
| occupation_code | 0..1 <br/> [String](#String) | ISCO-19 code of the occupation.  |
| label | 0..1 <br/> [String](#String) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| organization_uid | 0..1 <br/> [String](#String) | UID of the organization from the federal UID register (uid.admin.ch), in the exchange format of eCH-0108: CHE followed by nine digits, without separators (e.g. CHE106063525). The last digit is a check digit calculated modulo 11. The dotted form CHE-106.063.525 is the presentation used by uid.admin.ch and is not recorded here.  |
| organization_name | 0..1 <br/> [String](#String) | Name of the organization or enterprise.  |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |

##### Constraints


At least one of the following must be set:

- [occupation_code](#occupation_code)
- [label](#label)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [occupations](#occupations) | range | [Occupation](#Occupation) |














### Examples
#### Example: swiss politicians Sofia Fisch Juristin

```yaml
label: Jurist*in
is_active: true

```
#### Example: swiss politicians Beat Jans Politiker

```yaml
label: Politiker
valid_from: 1964-01-01
is_active: true

```






</div>



## Class: Training 


_Training or education of a person indicating a type (e.g., school diploma, university degree, military service), a label, an ISCO-19 code, and temporal validity._




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

##### Constraints


At least one of the following must be set:

- [training_type](#training_type)
- [training_code](#training_code)
- [value](#value)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [trainings](#trainings) | range | [Training](#Training) |



















</div>

## Enum: TrainingTypeEnum 




_Types of training or education based on the Swiss BFS LEVEL_EDUC codelist._




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







</div>

\newpage

# Groups and Bodies (Groups)

The group schema represents political groups, organisations and corporate bodies.

- **One generic model instead of many special classes:** Parliaments, parties, parliamentary groups, committees, departments, courts and civil-society organisations are all represented as *one* class `Group` and distinguished via `group_type`. This keeps the model simple and extensible without schema changes – the legislature, executive, judiciary and civil society can thus all be represented equally.
- **Groups and sub-groups via `parent_groups`:** Subordinate groups reference their superordinate group – e.g. a committee of the Council of States, a subcommittee within a committee, a cantonal party under its parent party, or an authority within a directorate. The hierarchy thus arises from these references rather than from a fixed level structure. It usually remains within the same `group_type`; however, cross-type references are possible (e.g. a parliamentary group that references its parliament). What counts is super-/subordination alone: the parties carrying a parliamentary group are not superordinate to it. Their relation to the group is deliberately not modelled in the standard – it is not a hierarchy, and no robust general form for it exists, since parliamentary groups are tied to parties more or less closely depending on the council. Where the affiliation has to be visible, it is so through the memberships of the individual persons. The reference takes the form of a `GroupReference` – the same form in which a membership names its group. That the link expresses a superordinate/subordinate relation is stated by the `parent_groups` slot itself; the reference merely carries the addressing. That addressing may use the `local_id` where the parent group is part of the same delivery, or the `global_uri` where it lies outside it – a cantonal party can thus reference its national party without that party having to be delivered. Where both are known, both are stated.
- **Temporal validity for groups as well:** Using `valid_from`/`valid_through`, it is possible to represent, for example, committees that exist only during a legislative period, or renamings and mergers of parties.



## Class: Group 


_A political group, organization, or body (e.g., party, committee, parliament, department)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| group_type | 1 <br/> [GroupType](#GroupType) | Type of group (e.g., party, commission, parliament, or similar). The exact naming and description of the group is provided via `label`.  |
| label | 1..* <br/> [MultilingualValue](#MultilingualValue) | Name of the group, with the language it is published in. Where a group is officially named in several languages, one entry per language is recorded.  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abbreviation (can be multilingual).  |
| description | * <br/> [MultilingualValue](#MultilingualValue) | Description of the entity.  |
| organization_uid | 0..1 <br/> [String](#String) | UID of the organization from the federal UID register (uid.admin.ch), in the exchange format of eCH-0108: CHE followed by nine digits, without separators (e.g. CHE106063525). The last digit is a check digit calculated modulo 11. The dotted form CHE-106.063.525 is the presentation used by uid.admin.ch and is not recorded here.  |
| legal_form | 0..1 <br/> [LegalFormEnum](#LegalFormEnum) | Legal form of the organization. See controlled vocabulary: https://register.ld.admin.ch/i14y/concept/legalForm  |
| landing_page | * <br/> [MultilingualUri](#MultilingualUri) | Website providing further information. Where the site is published under a separate address per language, one entry per language is recorded.  |
| parent_groups | * <br/> [GroupReference](#GroupReference) | Reference to the parent groups as a GroupReference, i.e. stated by their local_id or their global_uri. Only genuine super-/subordination belongs here: the parent party of a cantonal party, the hierarchy within the executive, a sub-commission under its commission, or a parliamentary group under its parliament. (parentGroup is typically used within the same group_type, but cross-type links are permitted, e.g. parliamentary group → parliament.) The parties carrying a parliamentary group are not a superordinate group of it and are therefore not stated here.  |
| spatial | 0..1 <br/> [String](#String) | Spatial reference to a LINDAS resource (fos-municipality number, fos-canton number, district, or country). Formats: municipality: https://ld.admin.ch/municipality/1234, district: https://ld.admin.ch/district/2301, canton: https://ld.admin.ch/canton/23, country: https://ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](#Contact) | Contact information (email, website, social media). Guideline: email is quasi-mandatory and should always be provided where available.  |
| addresses | * <br/> [Address](#Address) | Addresses with type (private, business, local).  |
| statutes_url | 0..1 <br/> [String](#String) | URL to party statutes (PDF or webpage; optional for parties).  |
| party_color | 0..1 <br/> [String](#String) | Party color as hexadecimal value (optional for parties, e.g., "#FF0000").  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
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














### Examples
#### Example: Parliamentary group referencing the parliament it belongs to

```yaml
local_id: 1266
global_uri: https://grosserrat.bs.ch/gremien/parteien-und-fraktionen/mitte-evp
label:
- value: Die Mitte / Evangelische Volkspartei
  language: de
group_type:
  group_type_enum: parliamentary_group
  label:
  - value: Fraktion
    language: de
spatial: https://ld.admin.ch/canton/12
parent_groups:
- local_id: 33
  global_uri: https://www.grosserrat.bs.ch/
  label: Grosser Rat Basel-Stadt

```
#### Example: Committee referencing its cantonal council

```yaml
groups:
- local_id: 3
  global_uri: >-
    https://ar.ch/kantonsrat/kommissionen/staendige-kommissionen-des-kantonsrates/geschaeftspruefungskommission/
  label:
  - value: Geschäftsprüfungskommission
    language: de
  abbreviation:
  - value: GPK
    language: de
  group_type:
    group_type_enum: committee
    label:
    - value: Kommission
      language: de
  spatial: https://ld.admin.ch/canton/15
  parent_groups:
  - local_id: 34
    global_uri: https://www.ar.ch/kantonsrat/
    label: Kantonsrat Appenzell Ausserrhoden

- local_id: 34
  global_uri: https://www.ar.ch/kantonsrat/
  label:
  - value: Kantonsrat Appenzell Ausserrhoden
    language: de
  group_type:
    group_type_enum: council_legislative
    label:
    - value: Parlament (Legislativrat)
      language: de
  spatial: https://ld.admin.ch/canton/15

```
#### Example: State chancellery referencing its government

```yaml
groups:
- local_id: 7172
  global_uri: https://www.bs.ch/regierungsrat/staatskanzlei
  label:
  - value: Staatskanzlei Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_secretariat
    label:
    - value: Staatskanzlei
      language: de
  spatial: https://ld.admin.ch/canton/12
  parent_groups:
  - local_id: 1300
    global_uri: https://www.regierungsrat.bs.ch/
    label: Regierungsrat Basel-Stadt

- local_id: 1300
  global_uri: https://www.regierungsrat.bs.ch/
  label:
  - value: Regierungsrat Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_executive
    label:
    - value: Regierung (Exekutivrat)
      language: de
  spatial: https://ld.admin.ch/canton/12

```
#### Example: Bilingual delegation to an intercantonal body

```yaml
local_id: 5000
global_uri: https://www.fr.ch/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
label:
- value: Freiburger Delegation IPK strafrechtliche Einschliessung
  language: de
- value: Délégation FR à la CIP détention pénale
  language: fr
abbreviation:
- value: Del-StRFE
  language: de
- value: Del-DetPen
  language: fr
description:
- value: >-
    Die Interparlamentarische Aufsichtskommission strafrechtliche Einschliessung besteht
    aus 18 Grossrätinnen und Grossräten aus den sechs Vertragskantonen Freiburg, Genf,
    Jura, Neuenburg, Waadt und Wallis.
  language: de
- value: >-
    La Commission interparlementaire de contrôle détention pénale est composée de
    18 députés issus des six cantons partenaires : Fribourg, Genève, Jura, Neuchâtel,
    Vaud et Valais.
  language: fr
landing_page:
- value: https://www.fr.ch/de/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
  language: de
- value: https://www.fr.ch/parlinfo/app/organizations/a1acb0c030d54b3baed840fe8bbed6b5
  language: fr
group_type:
  group_type_enum: delegation
  label:
  - value: Delegation
    language: de
  - value: Délégation
    language: fr
spatial: https://ld.admin.ch/canton/10
valid_from: 2007-12-12

```
#### Example: Extra-parliamentary commission with decision-making powers

```yaml
global_uri: https://www.weko.admin.ch/
label:
- value: Wettbewerbskommission
  language: de
- value: Commission de la concurrence
  language: fr
- value: Commissione della concorrenza
  language: it
abbreviation:
- value: WEKO
  language: de
- value: COMCO
  language: fr
- value: COMCO
  language: it
landing_page:
- value: https://www.weko.admin.ch/de
  language: de
- value: https://www.weko.admin.ch/fr
  language: fr
- value: https://www.weko.admin.ch/it
  language: it
group_type:
  group_type_enum: committee_extraparliamentary
  label:
  - value: Ausserparlamentarische Kommission
    language: de
spatial: https://ld.admin.ch/country/CHE

```
#### Example: Cantonal party referencing its national party

```yaml
global_uri: https://www.evp-bs.ch/
label:
- value: Evangelische Volkspartei Basel-Stadt
  language: de
abbreviation:
- value: EVP BS
  language: de
group_type:
  group_type_enum: party
  label:
  - value: Partei
    language: de
spatial: https://ld.admin.ch/canton/12
parent_groups:
- global_uri: https://www.evppev.ch/
  label: Evangelische Volkspartei der Schweiz
  abbreviation:
  - value: EVP
    language: de

```
#### Example: Municipal parliament with spatial reference

```yaml
local_id: 700
global_uri: >-
  https://www.stadt.sg.ch/home/verwaltung-politik/demokratie-politik/stadtparlament.html
label:
- value: Stadtparlament St. Gallen
  language: de
group_type:
  group_type_enum: council_legislative
  label:
  - value: Parlament (Legislativrat)
    language: de
spatial: https://ld.admin.ch/municipality/3203

```
#### Example: Association with UID and legal form from the commercial register

```yaml
global_uri: https://www.frc.ch/
organization_uid: CHE106063525
legal_form: '0109'
label:
- value: Fédération romande des consommateurs
  language: fr
abbreviation:
- value: FRC
  language: fr
group_type:
  group_type_enum: association
  label:
  - value: Verein
    language: de
spatial: https://ld.admin.ch/canton/22

```
#### Example: Council bureau referencing its parliament

```yaml
groups:
- local_id: 50
  global_uri: https://grosserrat.bs.ch/gremien/praesidium-und-buero
  label:
  - value: Büro des Grossen Rates
    language: de
  group_type:
    group_type_enum: council_bureau
    label:
    - value: Ratsbüro
      language: de
  spatial: https://ld.admin.ch/canton/12
  parent_groups:
  - local_id: 33
    global_uri: https://www.grosserrat.bs.ch/
    label: Grosser Rat Basel-Stadt

- local_id: 33
  global_uri: https://www.grosserrat.bs.ch/
  label:
  - value: Grosser Rat Basel-Stadt
    language: de
  group_type:
    group_type_enum: council_legislative
    label:
    - value: Parlament (Legislativrat)
      language: de
  spatial: https://ld.admin.ch/canton/12

```
#### Example: Cantonal party as its own group at its federal level

```yaml
global_uri: https://bs.die-mitte.ch/
label:
- value: Die Mitte Basel-Stadt
  language: de
group_type:
  group_type_enum: party
  label:
  - value: Partei
    language: de
spatial: https://ld.admin.ch/canton/12
parent_groups:
- global_uri: https://www.die-mitte.ch/
  label: Die Mitte Schweiz

```
#### Example: Interest group with a trilingual name and contact

```yaml
local_id: 6627
global_uri: https://www.parlament.ch/de/organe/gruppen/konsumenteninformation-und-schutz
label:
- value: Konsumenteninformation und -schutz
  language: de
- value: Information et défense des consommateurs
  language: fr
- value: Informazione e tutela dei consumatori
  language: it
description:
- value: >-
    L'intergroupe parlementaire « Information et défense des consommateurs » réunit
    toutes les sensibilités politiques. Cet intergroupe a pour mission d'informer
    et de sensibiliser les élu·e·s aux questions relatives à la défense des consommateur·rice·s
    en Suisse.
  language: fr
landing_page:
- value: https://www.parlament.ch/centers/documents/de/gruppen-der-bundesversammlung.pdf
  language: de
contacts:
- contact_type: email
  value: l.altwegg@frc.ch
  label: Sekretariat
- contact_type: phone
  value: +41 21 331 00 95
  label: Sekretariat
addresses:
- address_type: businessAddress
  address_uri: https://geo.ld.admin.ch/location/address/101009806
  street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale
    585
  postal_code: '1001'
  postal_locality: Lausanne
  country: CH
group_type:
  group_type_enum: interest_group
  label:
  - value: Interessengruppe
    language: de
  - value: Groupe d'intérêt
    language: fr
  - value: Gruppo d'interesse
    language: it
spatial: https://ld.admin.ch/country/CHE
valid_from: 2012-01-01

```






</div>



## Class: GroupType 


_Type of group (e.g., party, committee, parliament, department)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| group_type_enum | 1 <br/> [GroupTypeEnum](#GroupTypeEnum) | Link to the controlled vocabulary for group types.  |
| label | * <br/> [MultilingualValue](#MultilingualValue) | Designation of the type as used by the publishing body, with the language it is published in. Where a body publishes the designation in several languages, one entry per language is recorded.  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](#Group) | [group_type](#group_type) | range | [GroupType](#GroupType) |



















</div>

## Enum: GroupTypeEnum 




_Controlled vocabulary for the type of a group. It covers the councils and their organs, assemblies, committees and delegations, parties, parliamentary groups and electoral lists, the units of the administration, courts and oversight bodies, as well as organisations outside the state._


_A `group_type` must always be set. What counts is the political function, not the designation used locally; the latter is recorded in the label. Where no value fits, `other` is used._


_Legal form does not belong in this vocabulary but in `legal_form`._




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
| assembly |  Assembly of the persons entitled to vote acting as the legislative body, in particular the communal assembly ("Gemeindeversammlung") and, at cantonal level, the Landsgemeinde. Unlike a council, it is not an elected body.  |
| | [act:enum/group_type/assembly](act:enum/group_type/assembly) |
| council_legislative |  Parliament at federal, cantonal, or municipal level (e.g., Federal Assembly, National Council, Council of States, Grand Council, cantonal parliament, municipal parliament).  |
| | [act:enum/group_type/council_legislative](act:enum/group_type/council_legislative) |
| delegation |  Delegation.  |
| | [act:enum/group_type/delegation](act:enum/group_type/delegation) |
| committee |  Standing committee, including supervisory committees (e.g., CPC), subject commissions, parliamentary investigation commissions (PIC), and audit commissions.  |
| | [act:enum/group_type/committee](act:enum/group_type/committee) |
| committee_ad_hoc |  Committee set up for a single task and dissolved once it is completed, in contrast to a standing committee.  |
| | [act:enum/group_type/committee_ad_hoc](act:enum/group_type/committee_ad_hoc) |
| parliamentary_group |  Parliamentary faction.  |
| | [act:enum/group_type/parliamentary_group](act:enum/group_type/parliamentary_group) |
| council_bureau |  Body managing the business of a council, whatever it is called locally (bureau, council management, executive board). Used for the legislative as well as the executive council; the local designation is recorded in the label.  |
| | [act:enum/group_type/council_bureau](act:enum/group_type/council_bureau) |
| council_presidency |  Presidency of a council, for the legislative as well as the executive council.  |
| | [act:enum/group_type/council_presidency](act:enum/group_type/council_presidency) |
| council_executive |  Government / Executive as a collective body (e.g., Federal Council, Cantonal Government, City or Municipal Council).  |
| | [act:enum/group_type/council_executive](act:enum/group_type/council_executive) |
| department |  Government department, e.g. Departement or Direktion.  |
| | [act:enum/group_type/department](act:enum/group_type/department) |
| office |  Government office ("Amt"), usually the unit below a department.  |
| | [act:enum/group_type/office](act:enum/group_type/office) |
| committee_extraparliamentary |  Commission normally appointed by the government to advise the administration in its field and to give its business a first reading; some also hold decision-making powers of their own. What sets it apart from a parliamentary committee are its composition and its legal basis: its members are external experts and interest-group representatives rather than members of the council, and it rests on the law governing the organisation of the government and the administration rather than on parliament law. The type exists at federal and at cantonal level alike (e.g., the federal Competition Commission; the commissions extraparlementaires in the canton of Vaud). A committee whose members are members of the council is not covered by this value even when it is attached to the executive; it is recorded as a committee or an ad hoc committee with the executive council as its parent group.  |
| | [act:enum/group_type/committee_extraparliamentary](act:enum/group_type/committee_extraparliamentary) |
| interest_group |  Interest group on a subject matter: both the parliamentary interest group, in which members of the council join across party lines, and the interest group from civil society.  |
| | [act:enum/group_type/interest_group](act:enum/group_type/interest_group) |
| oversight_body |  Independent oversight or audit body that does not belong to the body overseen and does not report to it (e.g., Swiss Federal Audit Office SFAO and cantonal audit offices, Supervisory Authority for the Office of the Attorney General AS-OAG, Swiss Financial Market Supervisory Authority FINMA, ombudsman offices).  |
| | [act:enum/group_type/oversight_body](act:enum/group_type/oversight_body) |
| council_secretariat |  Administrative unit serving a council, whatever it is called locally (parliamentary services, council secretariat, state, cantonal or municipal chancellery). Used for the legislative as well as the executive council: the state chancellery is the staff unit of the executive council, the parliamentary services are that of the legislative council.  |
| | [act:enum/group_type/council_secretariat](act:enum/group_type/council_secretariat) |
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

# Memberships

The membership schema represents the relationship between persons and groups and is the central connecting element in the actor schema.

- **Distinction from interest links (`InterestLink`):** `Membership` records the *formal affiliation* of a person to a group within the actor schema (e.g. party, commission or parliament membership). Interest links and conflicts of interest with organisations *outside* the schema are deliberately kept separate and are represented via `InterestLink` (see the following chapter).
- **Reference with snapshot instead of embedding (`person_reference`/`group_reference`):** A membership refers to a person and a group and thereby records their most important identifying attributes at the time of linking. This keeps the entry historically correct even if the person or group changes later.
- **Activity explicit or derived (`is_active`):** Whether a membership is active can be set explicitly via `is_active` or derived from the temporal validity. If `is_active` is not set, activity is derived from `valid_from`/`valid_through`.
- **Membership ≠ voting right (`authorized_to_vote`):** The voting right is recorded separately from the membership – typically `false` for substitute members (except when on duty), observers, the secretariat and guests.
- **Role as a controlled vocabulary with free-text option (`role_type`):** The role in the group (e.g. member, presidency, deputy) is specified via a controlled vocabulary (`RoleEnum`); for roles not covered, the value `other` with a free-text designation is used.
- **Electoral district on the membership rather than on the person (`electoral_district`):** The electoral district describes the mandate, not the person – the same person may be elected from different districts over time or at different federal levels. `ElectoralDistrict` therefore carries no temporal validity of its own but inherits the `valid_from`/`valid_through` of the enclosing membership. For identification, the LINDAS resources for Swiss spatial units are intended (see `global_uri`).



## Class: Membership 


_A membership relationship between a person and a group, representing formal affiliation (e.g., party member, commission member, parliamentarian). Distinct from InterestLink, which covers external interest bindings and conflicts of interest to organizations outside the actor schema._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](#PersonReference) | Reference to a person with snapshot data at time of linking.  |
| group_reference | 1 <br/> [GroupReference](#GroupReference) | Reference to a group with snapshot data at time of linking.  |
| electoral_district | 0..1 <br/> [ElectoralDistrict](#ElectoralDistrict) | Link to the electoral district.  |
| role_type | 0..1 <br/> [RoleType](#RoleType) | Role of the person in the membership or function.  |
| authorized_to_vote | 0..1 <br/> [Boolean](#Boolean) | Indicates if the person is authorized to vote in the group. Typically false for substitute members (when not deputizing), observers, secretaries, and guests.  |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates if the membership is currently active. Can complement or replace `valid_from`/`valid_through`. If not set, activity is derived from the temporal validity fields.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
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



## Class: RoleType 


_Role of a person in a membership or function (e.g., member, president, deputy). If a role is not listed in the proposed RoleEnum vocabulary, the value 'other' can be used, and a descriptive label should be provided in the `role_label` slot. The label can also be used when a specific name is needed, even if a fitting semantic value exists in `role_type_enum`; it should be provided when `role_type_enum` is set to 'other'._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| role_type_enum | 0..1 <br/> [RoleEnum](#RoleEnum) | Role of the person in the membership or function.  |
| role_label | * <br/> [MultilingualValue](#MultilingualValue) | Specific role label. Use this when a specific role name is needed, even if a fitting semantic value exists in `role_type_enum`; provide this label when `role_type_enum` is set to 'other'. The designation is recorded with the language it is published in; where it is published in several languages, one entry per language is recorded.  |

##### Constraints


At least one of the following must be set:

- [role_type_enum](#role_type_enum)
- [role_label](#role_label)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [role_type](#role_type) | range | [RoleType](#RoleType) |




##### Rules


- If the role type is 'other', a descriptive label must be provided.

















</div>

## Enum: RoleEnum 




_Roles a person can have within a membership._




<div data-search-exclude markdown="1">

URI: [act:RoleEnum](https://ld.ech.ch/schema/0294/actors/RoleEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| member |  Regular member (default).  |
| president |  President or chair of the group.  |
| deputy |  Deputy or vice-chair role.  |
| other |  Other role; use role_label for a descriptive label.  |







</div>



## Class: ElectoralDistrict 


_Electoral district or region associated with a membership. The temporal validity is inherited from the enclosing membership._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | For IRI references, LINDAS resources should be used. The IRIs for the different administrative levels of Swiss spatial units are available at: https://ld.admin.ch/country/CHE. Under links in the schema:containsPlace section, the desired level can be selected. Examples for each administrative level: - Country - Switzerland: https://ld.admin.ch/country/CHE - Canton - Aargau: https://ld.admin.ch/canton/19 - District - Brig: https://ld.admin.ch/district/2301 - Municipality - Versoix: https://ld.admin.ch/municipality/6644 <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [electoral_district](#electoral_district) | range | [ElectoralDistrict](#ElectoralDistrict) |



















</div>

\newpage

# Interest Links

The InterestLink schema records interest links, conflicts of interest and entanglements of persons with organisations. It is based on the transparency requirements for members of parliament according to [Federal Assembly – Interest Links](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

- **Distinction from memberships (`Membership`):** `InterestLink` represents links to organisations *outside* the actor schema (conflicts of interest, political financing) – in contrast to the formal affiliation *within* the schema, which is recorded via `Membership`.
- **Mandatory classification (`interest_type`):** Every link is mandatorily categorised by type (professional activity, political offices, association), based on the disclosure categories of the Federal Assembly.
- **Organisation referenceable via UID (`organization_uid`):** If the organisation is recorded in the UID register, it is referenced via its UID – this enables analyses, e.g. with NOGA codes. What is recorded is the exchange format of eCH-0108, i.e. `CHE` followed by nine digits without separators (`CHE106063525`). For organisations without a UID, `organization_name`/`organization_address` are available; the legal form follows a controlled vocabulary (`LegalFormEnum`).
- **Scope and remuneration (`is_paid`, `committee`, `function_role`):** In addition to the committee and function within the organisation, it is explicitly recorded whether the position is paid – a central transparency aspect.





## Class: InterestLink 


_An interest link (conflict of interest, political financing) of a person to an organization outside the actor schema._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| person_reference | 1 <br/> [PersonReference](#PersonReference) | Reference to a person with snapshot data at time of linking.  |
| interest_type | 1 <br/> [InterestTypeEnum](#InterestTypeEnum) | Type of interest link (professional activity, political office, association).  |
| organization_name | 0..1 <br/> [String](#String) | Name of the organization or enterprise.  |
| organization_uid | 0..1 <br/> [String](#String) | UID of the organization from the federal UID register (uid.admin.ch), in the exchange format of eCH-0108: CHE followed by nine digits, without separators (e.g. CHE106063525). The last digit is a check digit calculated modulo 11. The dotted form CHE-106.063.525 is the presentation used by uid.admin.ch and is not recorded here.  |
| organization_address | 0..1 <br/> [String](#String) | Address of the organization.  |
| legal_form | 0..1 <br/> [LegalFormEnum](#LegalFormEnum) | Legal form of the organization. See controlled vocabulary: https://register.ld.admin.ch/i14y/concept/legalForm  |
| is_paid | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the activity is paid.  |
| committee | 0..1 <br/> [String](#String) | Committee or board within the organization (e.g., Verwaltungsrat, Stiftungsrat, Vorstand, Aufsichtsrat, Beirat, Geschäftsleitung).  |
| function_role | 0..1 <br/> [String](#String) | Function or role in the organization (e.g., Präsident/in, Vizepräsident/in, Mitglied, Delegierter, Geschäftsführer/in, Berater/in).  |
| local_id | 0..1 <br/> [String](#String) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| global_uri | 1 <br/> [Uriorcurie](#Uriorcurie) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](#HasIdentification) |
| date_created | 0..1 <br/> [Date](#Date) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_created | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| date_modified | 0..1 <br/> [Date](#Date) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| datetime_modified | 0..1 <br/> [Datetime](#Datetime) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](#HasCreationModificationDates) |
| valid_from | 0..1 <br/> [Date](#Date) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| valid_through | 0..1 <br/> [Date](#Date) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |
| is_active | 0..1 <br/> [Boolean](#Boolean) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](#HasTemporalValidity) |

##### Constraints


At least one of the following must be set:

- [organization_uid](#organization_uid)
- [organization_name](#organization_name)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |
| [Person](#Person) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |














### Examples
#### Example: Own company run operationally

```yaml
global_uri: act:il_burkart_001
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Burkart Advisory GmbH, Baden
legal_form: '0107'
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
#### Example: Unpaid presidency of a political alliance

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Allianz Sicherheit Schweiz, Baden
legal_form: '0109'
committee: Vorstand
function_role: Präsident
is_paid: false

```
#### Example: Board mandate in a holding company

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Birchmeier Holding AG, Döttingen
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: Board mandate in a real estate company

```yaml
global_uri: act:il_burkart_003
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Bovida Real Estate AG, Baar
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
#### Example: Membership in a sector association

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: '0109'
committee: Vorstand
function_role: Mitglied
is_paid: true

```
#### Example: Foundation board mandate with the organisations UID

```yaml
global_uri: act:il_burkart_007
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FONDATION SUISSE DE DEMINAGE (FSD), Genf
organization_uid: CHE109810537
legal_form: '0110'
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```
#### Example: Advisory board mandate without a governing function

```yaml
global_uri: act:il_burkart_008
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: Stiebel Eltron AG, Lupfig
legal_form: '0106'
committee: Beirat
function_role: Beirat
is_paid: true

```
#### Example: Voluntary involvement in the association carrying a major project

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: Verein Landesausstellung Svizra27, Aarau
legal_form: '0109'
committee: Vorstand
function_role: Mitglied
is_paid: false

```
#### Example: Presidency of a trade association

```yaml
global_uri: act:il_burkart_005
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: '0109'
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```
#### Example: Presidency of a national party

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_name: FDP.Die Liberalen
legal_form: '0109'
committee: Vorstand
function_role: Präsident
is_paid: true

```
#### Example: Board mandate in a technology company

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: http://www.wikidata.org/entity/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_name: ELCA Group SA, Lausanne
legal_form: '0106'
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```






</div>

## Enum: InterestTypeEnum 




_Types of interest links (conflicts of interest, political financing)._




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




_Legal forms according to the code list published by the Federal Statistical Office on the I14Y platform, conformant to eCH-0108 (business master data and business register). See https://register.ld.admin.ch/i14y/concept/legalForm_




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

# Shared Elements

## Reference Classes

`PersonReference` and `GroupReference` are used to reference persons or groups **locally** within another entity. In addition to the actual link to the complete entity, only the relevant information at the **time of linking** is stored – so it is not necessary to repeat all the information about a person or group at every mention.

An example: A motion references the person who submitted it. In addition to the link to the complete person entity, the motion stores locally information such as the person's political party or role **at the time of submission**. If the person later changes party or role, the information in the motion nevertheless remains correct and immutable.

This serves three purposes:

- **Useful local data** without costly queries of the complete entity
- **No redundancy**, since not all information has to be repeated at every mention
- **Implicit versioning**, since the local reference remains unchanged even if the linked entity changes later

Unlike an entity, a reference is not identified in its own right – it merely names an identified entity. The `global_uri` is therefore not mandatory here: all that is required is that at least one of `local_id` or `global_uri` is set. A system that only knows the local id of the referenced entity states that id; it is resolved within the same delivery. Beyond the delivery, the `global_uri` provides the link.



## Class: PersonReference 


_Lightweight reference to a person with key identification data at time of linking. Preserves historical accuracy even if the person changes later. The referenced person is identified by `local_id` or `global_uri`; at least one of the two is required._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 1 <br/> [String](#String) | Mandatory short display name to identify the person within the organisation (e.g. with added birth year to distinguish persons with the same name).  |
| label_long | 0..1 <br/> [String](#String) | Optional long display name including academic titles and full official name (e.g. "Dr. Maria Muster-Beispiel").  |
| group_label | 0..1 <br/> [String](#String) | Name of the body/group at time of linking.  |
| local_id | 0..1 <br/> [String](#String) | Local identifier of the referenced entity. It is resolved within the same delivery. <br/><br/>Inheritance: [HasReferenceIdentification](#HasReferenceIdentification) |
| global_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | The unique, globally valid URI of the referenced entity. Unlike a local_id it also resolves beyond the delivery. <br/><br/>Inheritance: [HasReferenceIdentification](#HasReferenceIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasReferenceIdentification](#HasReferenceIdentification) |

##### Constraints


At least one of the following must be set:

- [local_id](#local_id)
- [global_uri](#global_uri)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](#Membership) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |
| [InterestLink](#InterestLink) | [person_reference](#person_reference) | range | [PersonReference](#PersonReference) |



















</div>



## Class: GroupReference 


_Lightweight reference to a group with key identification data at time of linking. The referenced group is identified by `local_id` or `global_uri`; at least one of the two is required. A `local_id` is resolved within the same delivery, a `global_uri` also beyond it._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](#String) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| abbreviation | * <br/> [MultilingualValue](#MultilingualValue) | Abbreviation (can be multilingual).  |
| local_id | 0..1 <br/> [String](#String) | Local identifier of the referenced entity. It is resolved within the same delivery. <br/><br/>Inheritance: [HasReferenceIdentification](#HasReferenceIdentification) |
| global_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | The unique, globally valid URI of the referenced entity. Unlike a local_id it also resolves beyond the delivery. <br/><br/>Inheritance: [HasReferenceIdentification](#HasReferenceIdentification) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasReferenceIdentification](#HasReferenceIdentification) |

##### Constraints


At least one of the following must be set:

- [local_id](#local_id)
- [global_uri](#global_uri)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](#Group) | [parent_groups](#parent_groups) | range | [GroupReference](#GroupReference) |
| [Membership](#Membership) | [group_reference](#group_reference) | range | [GroupReference](#GroupReference) |



















</div>

## Reused Classes

An address is written in `street_address`, `postal_code`, `postal_locality` and `country` and may point into swisstopo's official building address register via `address_uri`. The final number of that URI is the EGAID, the federal building address identifier; `https://geo.ld.admin.ch/location/address/101009806` thus denotes "Rue de Genève 17, 1003 Lausanne" as an officially registered building address.

`address_uri` is optional. The written address on its own is permissible, but the reference via the EGAID is preferable: it is an unambiguous identifier and stable over time, whereas street names change, municipalities merge and postal codes are recut.

To arrive at the EGAID, one can use the [search API of geo.admin.ch](https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=Rue+de+Gen%C3%A8ve+17+1003+Lausanne&type=locations&origins=address) or match against the [official directory of building addresses](https://www.swisstopo.admin.ch/en/official-directory-of-building-addresses). The result is recorded in `address_uri`.



## Class: Address 


_An address with a type (e.g., private address, business address) and a value._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| address_type | 0..1 <br/> [AddressTypeEnum](#AddressTypeEnum) | Type of address.  |
| address_uri | 0..1 <br/> [Uriorcurie](#Uriorcurie) | URI of the address from the Swiss federal building address register (Amtliches Gebäudeadressverzeichnis, swisstopo). The final segment of the URI is the EGAID, the federal building address identifier of that register. Example of a valid URI: https://geo.ld.admin.ch/location/address/101904050 — the same register can be browsed as a map layer at https://map.geo.admin.ch/#/map?topic=ech&layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis  |
| street_address | 0..1 <br/> [String](#String) | Street address.  |
| postal_code | 0..1 <br/> [Integer](#Integer) | Postal code.  |
| postal_locality | 0..1 <br/> [String](#String) | Locality.  |
| country | 0..1 <br/> [String](#String) | ISO 3166-1 alpha-2 country code.  |

##### Constraints


At least one of the following must be set:

- [postal_locality](#postal_locality)
- [address_uri](#address_uri)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [addresses](#addresses) | range | [Address](#Address) |
| [Group](#Group) | [addresses](#addresses) | range | [Address](#Address) |














### Examples
#### Example: swiss politicians Beat Jans 1

```yaml
address_type: businessAddress
postal_locality: Basel-Stadt

```
#### Example: groups Konsumenteninformation und -schutz 1

```yaml
address_type: businessAddress
address_uri: https://geo.ld.admin.ch/location/address/101009806
street_address: Fédération romande des consommateurs, Rue de Genève 17, case postale
  585
postal_code: '1001'
postal_locality: Lausanne
country: CH

```






</div>

## Enum: AddressTypeEnum 




_Types of addresses._




<div data-search-exclude markdown="1">

URI: [act:AddressTypeEnum](https://ld.ech.ch/schema/0294/actors/AddressTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| privateAddress |  Private address.  |
| businessAddress |  Business address.  |
| localAddress |  Local address.  |







</div>



## Class: Contact 


_Contact information of a person indicating a type (e.g., email, LinkedIn) and a value._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| contact_type | 1 <br/> [ContactTypeEnum](#ContactTypeEnum) | Type of contact information.  |
| value | 1 <br/> [String](#String) | The value of an information besides other attributes such as type, language, etc.  |
| label | 0..1 <br/> [String](#String) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](#Person) | [contacts](#contacts) | range | [Contact](#Contact) |
| [Group](#Group) | [contacts](#contacts) | range | [Contact](#Contact) |



















</div>

\newpage

# Appendix A – References & Bibliography

The version stated is the one this standard was developed against.

## Standards of the "Political Affairs" specialist group

| | |
|---|---|
|[eCH-0292]|eCH-0292: Meta-processes for political affairs, version 1.0.0 – shared data elements: [https://www.ech.ch/de/ech/ech-0292](https://www.ech.ch/de/ech/ech-0292)|
|[eCH-0293]|eCH-0293: Public council operations, version 1.0.0: [https://www.ech.ch/de/ech/ech-0293](https://www.ech.ch/de/ech/ech-0293)|
|[eCH-0295]|eCH-0295: Parliamentary affairs, version 1.0.0: [https://www.ech.ch/de/ech/ech-0295](https://www.ech.ch/de/ech/ech-0295)|
|[eCH-0296]|eCH-0296: Legal acts and legislative texts, version 1.0.0: [https://www.ech.ch/de/ech/ech-0296](https://www.ech.ch/de/ech/ech-0296)|
|[eCH-0297]|eCH-0297: Public consultations, version 1.0.0: [https://www.ech.ch/de/ech/ech-0297](https://www.ech.ch/de/ech/ech-0297)|

## Further eCH standards

| | |
|---|---|
|[eCH-0011]|eCH-0011: Datenstandard Personendaten, version 9.0.0 (approved, 27.07.2023). Basis of the name types in `NameTypeEnum` (`personNameData`): [https://www.ech.ch/de/ech/ech-0011/9.0.0](https://www.ech.ch/de/ech/ech-0011/9.0.0)|
|[eCH-0108]|eCH-0108: Datenstandard: Unternehmensstammdaten und Unternehmensregister, version 6.0.0 (approved, 04.04.2024). Defines the exchange format of the UID (`organization_uid`) and is the standard the legal form code list in `LegalFormEnum` conforms to: [https://www.ech.ch/de/ech/ech-0108/6.0.0](https://www.ech.ch/de/ech/ech-0108/6.0.0)|

## Code lists and further sources

| | |
|---|---|
|[I14Y]|Interoperability platform of the Federal Statistical Office. Source of the code lists for legal form (`LegalFormEnum`) and sex (`GenderCodeEnum`): [https://www.i14y.admin.ch](https://www.i14y.admin.ch)|
|[LINDAS]|Linked Data Service of the Swiss federal administration. Identifiers of the Swiss spatial units (country, canton, district, municipality) for `spatial` and `ElectoralDistrict`: [https://ld.admin.ch](https://ld.admin.ch)|
|[NOGA]|General Classification of Economic Activities of the Federal Statistical Office. Enables analyses via the UID of referenced organisations.|
|[Wikidata]|Free knowledge base. Entity IRI (`http://www.wikidata.org/entity/Q…`) in `wikidata_uri`: [https://www.wikidata.org](https://www.wikidata.org)|
|[ISO 639-1]|ISO (International Organization for Standardization). Language codes, used in the `language` slot of `MultilingualValue`.|
|[schema.org]|Shared vocabulary for structured data. Source of several `slot_uri` assignments: [https://schema.org](https://schema.org)|
|[LinkML]|The modelling language in which this standard is defined: [https://linkml.io](https://linkml.io)|

