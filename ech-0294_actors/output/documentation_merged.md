---
title: "eCH-0294 Politische Akteure: Personen, Gruppen und Organe"
lang: de
toc: false
---

| **Name**              | **Politische Akteure: Personen, Gruppen und Organe**                                                                                               |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------|
| **eCH-Nummer**        | eCH-0294                                                                                                                   |
| **Kategorie**         | Entwurf                                                                                                                    |
| **Reifegrad**         |                                                                                                                            |
| **Version**           | 0.1                                                                                                                        |
| **Status**            |                                                                                                                            |
| **Beschluss am**      |                                                                                                                            |
| **Ausgabedatum**      |                                                                                                                            |
| **Ersetzt Version**   | 0.0                                                                                                                        |
| **Voraussetzungen**   | ?                                                                                                                          |
| **Beilagen**          | -                                                                                                                          |
| **Sprachen**          | English (Original)                                                                                                         |
| **Autoren**           | Fachgruppe politische Geschäfte: Julie Silberstein, Laurence Brandenberger, Daniela Koller, Thomas Roth, Stefan Oderbolz, Fabian Davolio, Orhan Saeedi   |
| **Herausgeber / Vertrieb** | Verein eCH, Räffelstr. 20, 8045                                                                                       |

# Summary

Management summary of the document.

# Table of Contents

< manually insert TOC here >




# Introduction

## Scope of this Document

## Identified Gaps on Political Actors

## Goals of this Document



## Work Plan as of November 2025
Currently we are working in the following order on the different topics regarding political actors (agents):
1) Personen: Ratsmitglieder, Verwaltungsmitglieder
2) Gruppen / Organe / Interessengruppe: Parteien, Fraktionen, Gremien, Kommissionen, Verbände
3) Interessenbindungen / Konflikte (Politikfinanzierungen)
4) Verknüpfungen gleicher Personen übergreifend CH / Kanton


# Person

## Einführung und Zielsetzung

Das Person-Schema beschreibt natürliche Personen im politischen Kontext mit dem Ziel, eine präzise und gleichzeitig flexible Datenstruktur bereitzustellen. Der Standard ermöglicht es, sowohl hochgradig strukturierte als auch offene Informationen zu erfassen, um unterschiedliche Datenqualitäten und Verfügbarkeiten abzubilden.

**Kernziele:**
- **Präzision**: Unterstützung von zeitlich gültigen Attributen (z.B. Namen, Adressen, Geschlecht)
- **Flexibilität**: Optionale Felder erlauben schrittweise Datenanreicherung
- **Interoperabilität**: Verwendung von Wikidata-IDs und URIs als globale Identifikatoren
- **Mehrsprachigkeit**: Unterstützung mehrsprachiger Inhalte gemäß Schweizer Anforderungen

## Technische Struktur

### Identifikatoren

Das Person-Schema verwendet eine hierarchische Identifikationsstrategie:

1. **Primärer Identifikator (`id`)**:
   - **Präferenz**: Wikidata-ID (z.B. `https://www.wikidata.org/wiki/Q813067`)
   - **Alternative**: Lokaler URI (z.B. `act:person_12345`)
   - **Anforderung**: Eindeutig, persistent, global auflösbar (wenn möglich)

2. **Anzeigenamen**:
   - `label`: Kurzer Anzeigename (z.B. "Beat Jans")
   - `label_long`: Erweiterter Anzeigename mit Titeln (z.B. "Prof. Dr. iur. Andrea Caroni, MPA (Harvard)")

### Temporale Validität

Viele Attribute unterstützen zeitliche Gültigkeit durch `valid_from` und `valid_until`:

- **Name**: Namen können sich ändern (Heirat, Geschlechtsanpassung)
- **Adresse**: Wohn- und Geschäftsadressen ändern sich
- **Geschlecht**: Geschlechtsidentität kann sich entwickeln
- **Staatsbürgerschaft**: Mehrfache Staatsbürgerschaften mit unterschiedlichen Gültigkeitsperioden
- **Beruf**: Berufliche Tätigkeiten mit Start- und Enddatum
- **Wahlkreis**: Wahlkreis kann sich bei Neuwahlen ändern

**Beispiel:**
```yaml
names:
  - name_type: officialLastName
    value: Müller
    valid_from: 1980-01-01
    valid_until: 2010-06-15
  - name_type: officialLastName
    value: Meier-Müller
    valid_from: 2010-06-15
```

### Datentypen und Validierung

| Attribut | Datentyp | Pflicht | Beschreibung |
|----------|----------|---------|--------------|
| `id` | URI | Ja | Eindeutiger Identifikator |
| `label` | string | Ja | Anzeigename |
| `birthyear` | integer | Nein | Geburtsjahr (4-stellig) |
| `birthdate` | date | Nein | Exaktes Geburtsdatum (ISO 8601) |
| `picture` | URI | Nein | Link zu Profilbild (bevorzugt PNG) |
| `names` | Name[] | Nein | Liste strukturierter Namen |
| `addresses` | Address[] | Nein | Wohn- und Geschäftsadressen |
| `languages` | LanguageProficiency[] | Nein | Sprachkenntnisse |
| `ch_citizenship` | Validity | Nein | Schweizer Bürgerrecht (zeitlich) |
| `citizenships` | Citizenship[] | Nein | Weitere Staatsbürgerschaften |
| `genders` | Gender[] | Nein | Geschlechtsidentität(en) |
| `occupations` | Occupation[] | Nein | Berufliche Tätigkeiten |
| `trainings` | Training[] | Nein | Ausbildungen |
| `contacts` | Contact[] | Nein | Kontaktinformationen |
| `electoral_district` | ElectoralDistrict | Nein | Wahlkreis |
| `interest_links_person` | InterestLink[] | Nein | Interessenbindungen |

## Strukturierte Unterklassen

### Name

Namen werden nach eCH-0044 strukturiert erfasst:

```yaml
names:
  - name_type: officialGivenName
    value: Andrea
  - name_type: officialLastName
    value: Caroni
    valid_from: 1980-04-19
  - name_type: callName
    value: Andi
```

**Namenstypen** (`NameTypeEnum`):
- `officialGivenName`: Offizieller Vorname
- `officialLastName`: Offizieller Nachname
- `officialMiddleName`: Offizieller Mittelname
- `callName`: Rufname
- `familyNameOnForeignPassport`: Familienname auf ausländischem Pass

### Adresse

Adressen folgen eCH-0010 Standard:

```yaml
addresses:
  - address_type: businessAddress
    address_URI: https://ld.admin.ch/address/12345
    street_address: Bundesplatz 3
    postal_code: "3003"
    postal_locality: Bern
  - address_type: privateAddress
    postal_locality: Zürich
```

**Adresstypen** (`AddressTypeEnum`):
- `privateAddress`: Privatadresse
- `businessAddress`: Geschäftsadresse
- `localAddress`: Lokale Adresse (z.B. Parlamentsadresse)

### Sprachkenntnisse

```yaml
languages:
  - language: de
    correspondence: true
    native: true
  - language: fr
    correspondence: false
    native: false
```

- `language`: ISO 639-1 Sprachcode (de, fr, it, rm, en)
- `correspondence`: Bevorzugte Korrespondenzsprache
- `native`: Muttersprache

### Geschlecht

```yaml
genders:
  - value: female
    valid_from: 1978-05-23
    pronouns:
      - sie
      - ihr
```

- `value`: Geschlechtscode (male, female, diverse, etc.)
- `pronouns`: Bevorzugte Pronomen (mehrsprachig möglich)
- Unterstützt zeitliche Änderungen

### Staatsbürgerschaft

```yaml
ch_citizenship:
  valid_from: 1980-04-19

citizenships:
  - country: IT
    valid_from: 1980-04-19
  - country: DE
    valid_from: 2005-01-15
    valid_until: 2020-12-31
```

- `ch_citizenship`: Schweizer Bürgerrecht (Validity-Objekt)
- `citizenships`: Weitere Staatsbürgerschaften mit ISO 3166 Ländercodes

### Beruf und Ausbildung

```yaml
occupations:
  - value: Honorarprofessor
    occupation_isco19_code: "2421"
    valid_from: 2010-01-01
    active: true
    paid: true
    enterprise_uid: CHE-123.456.789
    enterprise: Universität St. Gallen

trainings:
  - type: uni
    value: Prof. Dr. iur.
    training_isco19_code: "0421"
  - type: uni
    value: MPA (Harvard)
```

- `occupation_isco19_code`: ISCO-19 Berufsklassifikation
- `enterprise_uid`: UID-Nummer des Unternehmens (eCH-0097)
- `active`: Aktuelle Tätigkeit
- `paid`: Bezahlte Position

**Ausbildungstypen** (`TrainingTypeEnum`):
- `schulabschluss`: Schulabschluss
- `efz`: Eidgenössisches Fähigkeitszeugnis
- `uni`: Universitätsabschluss
- `armee`: Militärdienst
- `zivi`: Zivildienst
- `zischutz`: Zivilschutz

### Kontaktinformationen

```yaml
contacts:
  - type: email
    value: andrea.caroni@parl.ch
  - type: contact_website
    value: http://www.andrea-caroni.ch
  - type: linked-in
    value: https://linkedin.com/in/andrea-caroni
  - type: twitter
    value: https://twitter.com/acaroni
```

**Kontakttypen** (`ContactTypeEnum`):
- `email`: E-Mail-Adresse
- `contact_website`: Persönliche Website
- `linked-in`: LinkedIn-Profil
- `twitter`: Twitter/X-Profil

### Wahlkreis

```yaml
electoral_district:
  district: Appenzell Ausserrhoden
  valid_from: 2015-01-01
  valid_until: 2023-11-30
```

## Interoperabilität

### Globale Identifikatoren

- **Wikidata**: Primäre Quelle für Personen-IDs
- **eCH-0285**: Kompatibilität mit eCH-Standard für semantische Identifikatoren
- **Linked Open Data**: URIs erlauben Verlinkung mit anderen Datenquellen

### Referenzierung in anderen Schemas

Personen werden in anderen eCH-Standards referenziert:
- **eCH-0293** (Operations): `actor_id` verweist auf Person
- **eCH-0294** (Actors): `person_id` in Memberships und InterestLinks
- **eCH-0295** (Affairs): Autoren, Einreicher, Mitunterzeichner

## Anwendungsbeispiele

### Beispiel 1: Nationalrat mit vollständigen Angaben

```yaml
id: https://www.wikidata.org/wiki/Q493598
label: Andrea Caroni
label_long: Prof. Dr. iur. Andrea Caroni, MPA (Harvard)
birthyear: 1980
birthdate: 1980-04-19
picture: https://www.parlament.ch/[...]
names:
  - name_type: officialGivenName
    value: Andrea
  - name_type: officialLastName
    value: Caroni
    valid_from: 1980-04-19
addresses:
  - address_type: businessAddress
    street_address: Poststrasse 1
    postal_code: "9100"
    postal_locality: Herisau
languages:
  - language: de
    correspondence: true
    native: true
ch_citizenship:
  valid_from: 1980-04-19
genders:
  - value: male
    valid_from: 1980-04-19
    pronouns:
      - er
      - ihm
occupations:
  - value: Honorarprofessor
    valid_from: 2010-01-01
    active: true
    paid: true
trainings:
  - type: uni
    value: Prof. Dr. iur.
  - type: uni
    value: MPA (Harvard)
contacts:
  - type: email
    value: andrea.caroni@parl.ch
  - type: contact_website
    value: http://www.andrea-caroni.ch
electoral_district:
  district: Appenzell Ausserrhoden
  valid_from: 2015-01-01
```

### Beispiel 2: Minimale Angaben

```yaml
id: act:person_local_123
label: Max Muster
names:
  - name_type: officialGivenName
    value: Max
  - name_type: officialLastName
    value: Muster
languages:
  - language: de
    native: true
ch_citizenship:
  valid_from: 1970-01-01
```

### Beispiel 3: Person mit Namensänderung

```yaml
id: https://www.wikidata.org/wiki/Q123456
label: Petra Meier-Schmidt
names:
  - name_type: officialGivenName
    value: Petra
  - name_type: officialLastName
    value: Schmidt
    valid_from: 1975-03-15
    valid_until: 2005-06-20
  - name_type: officialLastName
    value: Meier-Schmidt
    valid_from: 2005-06-20
```

## Referenzen

Siehe vollständige LinkML-Schema-Dokumentation:



# Class: Person 


_[en] A person with identifiers, names, addresses, citizenships, and occupations._

_[de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Berufen._

__





URI: [act:Person](https://ch.paf.link/schema/actors/Person)





```mermaid
 classDiagram
    class Person
    click Person href "../Person/"
      Person : addresses
        
          
    
        
        
        Person --> "*" Address : addresses
        click Address href "../Address/"
    

        
      Person : birthdate
        
      Person : birthyear
        
      Person : ch_citizenship
        
          
    
        
        
        Person --> "0..1" Validity : ch_citizenship
        click Validity href "../Validity/"
    

        
      Person : citizenships
        
          
    
        
        
        Person --> "*" Citizenship : citizenships
        click Citizenship href "../Citizenship/"
    

        
      Person : contacts
        
          
    
        
        
        Person --> "*" Contact : contacts
        click Contact href "../Contact/"
    

        
      Person : datetime_created
        
      Person : datetime_updated
        
      Person : electoral_district
        
          
    
        
        
        Person --> "0..1" ElectoralDistrict : electoral_district
        click ElectoralDistrict href "../ElectoralDistrict/"
    

        
      Person : genders
        
          
    
        
        
        Person --> "*" Gender : genders
        click Gender href "../Gender/"
    

        
      Person : id
        
      Person : interest_links_person
        
          
    
        
        
        Person --> "*" InterestLink : interest_links_person
        click InterestLink href "../InterestLink/"
    

        
      Person : label
        
      Person : label_long
        
      Person : languages
        
          
    
        
        
        Person --> "*" LanguageProficiency : languages
        click LanguageProficiency href "../LanguageProficiency/"
    

        
      Person : names
        
          
    
        
        
        Person --> "*" Name : names
        click Name href "../Name/"
    

        
      Person : occupations
        
          
    
        
        
        Person --> "*" Occupation : occupations
        click Occupation href "../Occupation/"
    

        
      Person : picture
        
      Person : trainings
        
          
    
        
        
        Person --> "*" Training : trainings
        click Training href "../Training/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](#id) | 1 <br/> [String](#String) | [en] Unique identifier (preferably Wikidata-ID or URI) | direct |
| [label](#label) | 1 <br/> [String](#String) | [en] Display name of the person | direct |
| [label_long](#label_long) | 0..1 <br/> [String](#String) | [en] Extended display name (with title, etc | direct |
| [birthyear](#birthyear) | 0..1 <br/> [Integer](#Integer) | [en] Year of birth | direct |
| [birthdate](#birthdate) | 0..1 <br/> [Date](#Date) | [en] Exact date of birth | direct |
| [picture](#picture) | 0..1 <br/> [String](#String) | [en] Link to an image (preferred: PNG, then JPG, then GIF) | direct |
| [names](#names) | * <br/> [Name](#Name) |  | direct |
| [addresses](#addresses) | * <br/> [Address](#Address) | [en] Addresses (private, business, local) | direct |
| [languages](#languages) | * <br/> [LanguageProficiency](#LanguageProficiency) |  | direct |
| [ch_citizenship](#ch_citizenship) | 0..1 <br/> [Validity](#Validity) |  | direct |
| [citizenships](#citizenships) | * <br/> [Citizenship](#Citizenship) |  | direct |
| [genders](#genders) | * <br/> [Gender](#Gender) |  | direct |
| [occupations](#occupations) | * <br/> [Occupation](#Occupation) |  | direct |
| [trainings](#trainings) | * <br/> [Training](#Training) |  | direct |
| [contacts](#contacts) | * <br/> [Contact](#Contact) | [en] Contact information (email, website, social media) | direct |
| [electoral_district](#electoral_district) | 0..1 <br/> [ElectoralDistrict](#ElectoralDistrict) |  | direct |
| [interest_links_person](#interest_links_person) | * <br/> [InterestLink](#InterestLink) | [en] Interest links of the person | direct |
| [datetime_updated](#datetime_updated) | 0..1 <br/> [Datetime](#Datetime) | [en] The last time this record was updated | direct |
| [datetime_created](#datetime_created) | 0..1 <br/> [Datetime](#Datetime) | [en] The time this record was created | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [persons](#persons) | range | [Person](#Person) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Person |
| native | act:Person |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Person
description: '[en] A person with identifiers, names, addresses, citizenships, and
  occupations.

  [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und
  Berufen.

  '
from_schema: https://ch.paf.link/schema/actors
slots:
- id
- label
- label_long
- birthyear
- birthdate
- picture
- names
- addresses
- languages
- ch_citizenship
- citizenships
- genders
- occupations
- trainings
- contacts
- electoral_district
- interest_links_person
- datetime_updated
- datetime_created

```
</details>

### Induced

<details>
```yaml
name: Person
description: '[en] A person with identifiers, names, addresses, citizenships, and
  occupations.

  [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und
  Berufen.

  '
from_schema: https://ch.paf.link/schema/actors
attributes:
  id:
    name: id
    description: '[en] Unique identifier (preferably Wikidata-ID or URI).

      [de] Eindeutiger Identifikator (vorzugsweise Wikidata-ID oder URI).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: dcterm:identifier
    identifier: true
    alias: id
    owner: Person
    domain_of:
    - Container
    - Person
    - Group
    - Membership
    - InterestLink
    - PersonReference
    - GroupReference
    range: string
    required: true
  label:
    name: label
    description: '[en] Display name of the person.

      [de] Anzeigename der Person.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: label
    owner: Person
    domain_of:
    - Person
    range: string
    required: true
  label_long:
    name: label_long
    description: '[en] Extended display name (with title, etc.).

      [de] Erweiterter Anzeigename (mit Titel, etc.).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: label_long
    owner: Person
    domain_of:
    - Person
    range: string
  birthyear:
    name: birthyear
    description: '[en] Year of birth.

      [de] Geburtsjahr.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: birthyear
    owner: Person
    domain_of:
    - Person
    range: integer
  birthdate:
    name: birthdate
    description: '[en] Exact date of birth.

      [de] Genaues Geburtsdatum.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: birthdate
    owner: Person
    domain_of:
    - Person
    range: date
  picture:
    name: picture
    description: '[en] Link to an image (preferred: PNG, then JPG, then GIF).

      [de] Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: picture
    owner: Person
    domain_of:
    - Person
    range: string
  names:
    name: names
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:name
    alias: names
    owner: Person
    domain_of:
    - Person
    range: Name
    multivalued: true
    inlined: true
    inlined_as_list: true
  addresses:
    name: addresses
    description: '[en] Addresses (private, business, local).

      [de] Adressen (privat, geschäftlich, lokal).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:address
    alias: addresses
    owner: Person
    domain_of:
    - Person
    - Group
    range: Address
    multivalued: true
    inlined: true
    inlined_as_list: true
  languages:
    name: languages
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:language
    alias: languages
    owner: Person
    domain_of:
    - Person
    range: LanguageProficiency
    multivalued: true
    inlined: true
    inlined_as_list: true
  ch_citizenship:
    name: ch_citizenship
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:chCitizenship
    alias: ch_citizenship
    owner: Person
    domain_of:
    - Person
    range: Validity
  citizenships:
    name: citizenships
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:citizenship
    alias: citizenships
    owner: Person
    domain_of:
    - Person
    range: Citizenship
    multivalued: true
    inlined: true
    inlined_as_list: true
  genders:
    name: genders
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:gender
    alias: genders
    owner: Person
    domain_of:
    - Person
    range: Gender
    multivalued: true
    inlined: true
    inlined_as_list: true
  occupations:
    name: occupations
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:occupation
    alias: occupations
    owner: Person
    domain_of:
    - Person
    range: Occupation
    multivalued: true
    inlined: true
    inlined_as_list: true
  trainings:
    name: trainings
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:training
    alias: trainings
    owner: Person
    domain_of:
    - Person
    range: Training
    multivalued: true
    inlined: true
    inlined_as_list: true
  contacts:
    name: contacts
    description: '[en] Contact information (email, website, social media).

      [de] Kontaktinformationen (E-Mail, Website, Social Media).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:contact
    alias: contacts
    owner: Person
    domain_of:
    - Person
    - Group
    range: Contact
    multivalued: true
    inlined: true
    inlined_as_list: true
  electoral_district:
    name: electoral_district
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:electoralDistrict
    alias: electoral_district
    owner: Person
    domain_of:
    - Person
    range: ElectoralDistrict
  interest_links_person:
    name: interest_links_person
    description: '[en] Interest links of the person.

      [de] Interessenbindungen der Person.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:interestLink
    alias: interest_links_person
    owner: Person
    domain_of:
    - Person
    range: InterestLink
    multivalued: true
    inlined: true
    inlined_as_list: true
  datetime_updated:
    name: datetime_updated
    description: '[en] The last time this record was updated.

      [de] Der Zeitpunkt, zu dem dieser Datensatz zuletzt aktualisiert wurde.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: datetime_updated
    owner: Person
    domain_of:
    - Person
    - Group
    - Membership
    - InterestLink
    range: datetime
  datetime_created:
    name: datetime_created
    description: '[en] The time this record was created.

      [de] Der Zeitpunkt, zu dem dieser Datensatz erstellt wurde.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: datetime_created
    owner: Person
    domain_of:
    - Person
    - Group
    - Membership
    - InterestLink
    range: datetime

```
</details> 



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

## Technische Struktur

### Identifikatoren

| Attribut | Typ | Pflicht | Beschreibung |
|----------|-----|---------|--------------|
| `id` | URI | Ja | Lokaler Identifikator |
| `uri` | URI | Nein | Global gültiger Identifikator (z.B. politics.ld.admin.ch/party/1) |

**Beispiel:**
```yaml
id: act:sp_basel_stadt
uri: https://politics.ld.admin.ch/party/sp_basel_stadt
```

## Datenstruktur

### Pflichtfelder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `id` | URI | Eindeutiger Identifikator |
| `group_type` | GroupTypeEnum | Art der Gruppe (siehe Klassifikation unten) |

### Optionale Felder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `uri` | URI | Global auflösbare URI (eCH-0285 kompatibel) |
| `type_label` | string | Spezifischer lokaler Typ-Name (wenn Enum nicht ausreicht) |
| `valid_from` | date | Beginn der Gültigkeit |
| `valid_until` | date | Ende der Gültigkeit |
| `name` | MultilingualString[] | Name (mehrsprachig) |
| `abbreviation` | MultilingualString[] | Abkürzung (mehrsprachig) |
| `description` | MultilingualString[] | Beschreibung |
| `landing_page` | URI | URL mit weiteren Informationen |
| `parent_groups` | string[] | Übergeordnete Gruppen (0..n) |
| `spatial` | string | Räumliche Referenz (Gemeinde-/Kantonsnummer) |
| `contacts` | Contact[] | Kontaktinformationen |
| `addresses` | Address[] | Adressen |
| `url_statutes` | URI | URL zu Statuten (speziell für Parteien) |
| `party_color` | string | Parteifarbe (speziell für Parteien) |
| `datetime_updated` | datetime | Letzte Aktualisierung |
| `datetime_created` | datetime | Erstellung |

## Klassifikation: GroupTypeEnum

### Legislative

#### parliament (Parlament)
Parlamente auf allen föderalen Ebenen.

**Beispiele:**
- Bundesversammlung (Bund)
- Nationalrat
- Ständerat
- Grosser Rat (Kanton)
- Kantonsrat
- Gemeindeparlament

```yaml
group_type: parliament
name:
  - text: Nationalrat
    language: de
  - text: Conseil national
    language: fr
  - text: Consiglio nazionale
    language: it
spatial: https://ld.admin.ch/country/1  # Schweiz
```

#### commission (Kommission)
Ständige oder Ad-hoc-Kommissionen.

**Untertypen:**
- Ständige Kommissionen (z.B. Finanzkommission)
- Ad-hoc-Kommissionen
- Aufsichtskommissionen (Geschäftsprüfungskommission, GPK)
- Sachkommissionen
- PUK (Parlamentarische Untersuchungskommission)
- Rechnungsprüfungskommission

```yaml
group_type: commission
name:
  - text: Geschäftsprüfungskommission des Nationalrats
    language: de
type_label: Ständige Aufsichtskommission
parent_groups:
  - act:nationalrat
```

#### delegation (Delegation)
Parlamentarische Delegationen.

```yaml
group_type: delegation
name:
  - text: Delegation für internationale Finanzfragen
    language: de
```

#### faction (Fraktion)
Parlamentsfraktionen.

```yaml
group_type: faction
name:
  - text: SP-Fraktion
    language: de
abbreviation:
  - text: SP
    language: de
parent_groups:
  - act:nationalrat
```

#### parliamentary_bureau (Parlamentsbüro)
Organisatorisches Leitungsgremium.

```yaml
group_type: parliamentary_bureau
name:
  - text: Büro des Nationalrats
    language: de
```

#### presidency (Präsidium)
Präsidium des Parlaments.

```yaml
group_type: presidency
name:
  - text: Präsidium der Bundesversammlung
    language: de
```

### Exekutive

#### government (Regierung)
Regierung als Gesamtorgan.

**Beispiele:**
- Bundesrat
- Regierungsrat (Kantone)
- Stadtrat / Gemeinderat

```yaml
group_type: government
name:
  - text: Bundesrat
    language: de
  - text: Conseil fédéral
    language: fr
spatial: https://ld.admin.ch/country/1
```

#### department (Departement)
Verwaltungsdepartemente.

```yaml
group_type: department
name:
  - text: Eidgenössisches Departement des Innern
    language: de
abbreviation:
  - text: EDI
    language: de
parent_groups:
  - act:bundesrat
```

#### office (Amt)
Ämter innerhalb von Departementen.

```yaml
group_type: office
name:
  - text: Bundesamt für Gesundheit
    language: de
abbreviation:
  - text: BAG
    language: de
parent_groups:
  - act:edi
```

#### extraparliamentary_commission (Ausserparlamentarische Kommission)
APK mit Regierungsauftrag.

**Beispiele:**
- Bankrat der Schweizerischen Nationalbank
- Eidgenössische Finanzmarktaufsicht (FINMA)

```yaml
group_type: extraparliamentary_commission
name:
  - text: Bankrat der SNB
    language: de
```

#### workgroup (Arbeitsgruppe)
Ad-hoc-Arbeitsgruppen.

```yaml
group_type: workgroup
name:
  - text: Arbeitsgruppe Klimapolitik
    language: de
valid_from: 2024-01-01
valid_until: 2024-12-31
```

### Judikative

#### court (Gericht)
Gerichte aller Instanzen.

**Beispiele:**
- Bundesgericht
- Kantonsgericht
- Bezirksgericht

```yaml
group_type: court
name:
  - text: Bundesgericht
    language: de
  - text: Tribunal fédéral
    language: fr
  - text: Tribunale federale
    language: it
spatial: https://ld.admin.ch/country/1
```

### Zivilgesellschaft

#### party (Partei)
Politische Parteien auf allen föderalen Ebenen.

Jede föderale Ebene wird als eigene Gruppe geführt.

```yaml
group_type: party
name:
  - text: SP Schweiz
    language: de
abbreviation:
  - text: SP
    language: de
url_statutes: https://www.sp-ps.ch/sites/default/files/documents/statuten_sp_d_0.pdf
party_color: "#FF0000"
spatial: https://ld.admin.ch/country/1
```

**Hierarchie-Beispiel:**
```yaml
# SP Schweiz (Bund)
- id: act:sp_schweiz
  group_type: party
  name: [{text: "SP Schweiz", language: de}]
  spatial: https://ld.admin.ch/country/1

# SP Basel-Stadt (Kanton)
- id: act:sp_basel_stadt
  group_type: party
  name: [{text: "SP Basel-Stadt", language: de}]
  parent_groups: [act:sp_schweiz]
  spatial: https://ld.admin.ch/canton/12

# SP Riehen (Gemeinde)
- id: act:sp_riehen
  group_type: party
  name: [{text: "SP Riehen", language: de}]
  parent_groups: [act:sp_basel_stadt]
  spatial: https://ld.admin.ch/municipality/2703
```

#### list (Liste)
Wahllisten, können Teil einer Partei sein oder unabhängig.

```yaml
group_type: list
name:
  - text: Liste 1 - SP
    language: de
parent_groups:
  - act:sp_basel_stadt  # Optional: Zugehörigkeit zur Partei
```

#### interest_group (Interessengruppe)
Lobbyorganisationen und Interessenverbände.

```yaml
group_type: interest_group
name:
  - text: Economiesuisse
    language: de
```

#### association (Verein)
Vereine und Verbände.

```yaml
group_type: association
name:
  - text: Pro Natura
    language: de
```

#### petition_carrier (Petitionsträger)
Träger von Petitionen oder Volksinitiativen.

```yaml
group_type: petition_carrier
name:
  - text: Komitee für bezahlbare Krankenkassen
    language: de
```

### Andere Organe

#### control_body (Kontrollorgan)
Kontroll- und Aufsichtsorgane.

**Beispiele:**
- Eidgenössische Finanzkontrolle (EFK)
- AB-BA (Aufsichtsbehörde)

```yaml
group_type: control_body
name:
  - text: Eidgenössische Finanzkontrolle
    language: de
abbreviation:
  - text: EFK
    language: de
```

#### parliamentary_services (Parlamentsdienste)
Unterstützungsdienste des Parlaments.

```yaml
group_type: parliamentary_services
name:
  - text: Parlamentsdienste der Bundesversammlung
    language: de
```

#### university (Universität)
Universitäten und Hochschulen (als ausgelagerte Träger öffentlicher Aufgaben).

```yaml
group_type: university
name:
  - text: Universität Zürich
    language: de
abbreviation:
  - text: UZH
    language: de
```

## Hierarchien und parent_groups

Das Attribut `parent_groups` erlaubt die Abbildung von Organisationsstrukturen:

### Parteihierarchie (Föderalismus)

```yaml
# National
- id: act:fdp_schweiz
  parent_groups: []

# Kantonal
- id: act:fdp_zuerich
  parent_groups: [act:fdp_schweiz]

# Kommunal
- id: act:fdp_winterthur
  parent_groups: [act:fdp_zuerich]
```

### Verwaltungshierarchie

```yaml
# Departement
- id: act:edi
  parent_groups: [act:bundesrat]

# Amt
- id: act:bag
  parent_groups: [act:edi]

# Abteilung
- id: act:bag_abteilung_gesundheitspolitik
  parent_groups: [act:bag]
```

### Kommissionshierarchie

```yaml
# Hauptkommission
- id: act:sik_nr
  name: [{text: "Sicherheitspolitische Kommission NR", language: de}]
  parent_groups: [act:nationalrat]

# Subkommission
- id: act:sik_nr_sub_cyber
  name: [{text: "Subkommission Cybersicherheit", language: de}]
  parent_groups: [act:sik_nr]
```

## Räumliche Referenz (spatial)

Das Attribut `spatial` verknüpft Gruppen mit Gemeinden, Kantonen oder dem Bund:

**Formate:**
- Gemeinde: `https://ld.admin.ch/municipality/[BFS-Nr]`
- Kanton: `https://ld.admin.ch/canton/[Kantonsnr]`
- Bund: `https://ld.admin.ch/country/1`

**Beispiele:**
```yaml
# Gemeinde Zürich (BFS 261)
spatial: https://ld.admin.ch/municipality/261

# Kanton Zürich
spatial: https://ld.admin.ch/canton/1

# Bund
spatial: https://ld.admin.ch/country/1
```

## Mehrsprachigkeit

Namen und Abkürzungen sind mehrsprachig erfassbar:

```yaml
name:
  - text: Bundesversammlung
    language: de
  - text: Assemblée fédérale
    language: fr
  - text: Assemblea federale
    language: it
  - text: Assamblea federala
    language: rm

abbreviation:
  - text: BVers
    language: de
  - text: AsFed
    language: fr
```

## Partei-spezifische Attribute

### url_statutes
Link zu den Parteistatuten (PDF oder Webseite).

```yaml
url_statutes: https://www.sp-ps.ch/sites/default/files/documents/statuten_sp_d_0.pdf
```

### party_color
Parteifarbe als Hexadezimalwert.

```yaml
party_color: "#FF0000"  # SP
party_color: "#0066CC"  # FDP
party_color: "#008000"  # Grüne
party_color: "#FF6600"  # SVP
party_color: "#FF9900"  # CVP/Mitte
```

## Interoperabilität

### Verknüpfung mit Memberships

Gruppen werden über Memberships mit Personen verbunden:

```yaml
# Container-Struktur
groups:
  - id: act:sp_basel_stadt
    group_type: party
    name: [{text: "SP Basel-Stadt", language: de}]

memberships:
  - id: act:membership_jans_sp
    person_id: https://www.wikidata.org/wiki/Q813067
    group_id: act:sp_basel_stadt
    role: Mitglied
    valid_from: 1990-01-01
```

### Verknüpfung mit eCH-0293 (Operations)

Gruppen werden in Operations als `actor_id` referenziert:

```yaml
# eCH-0293 Meeting
actor_id: act:nationalrat
actor_name: Nationalrat
```

## Anwendungsbeispiele

### Beispiel 1: Nationalrat

```yaml
id: act:nationalrat
uri: https://politics.ld.admin.ch/parliament/nationalrat
group_type: parliament
name:
  - text: Nationalrat
    language: de
  - text: Conseil national
    language: fr
  - text: Consiglio nazionale
    language: it
abbreviation:
  - text: NR
    language: de
  - text: CN
    language: fr
landing_page: https://www.parlament.ch/de/organe/nationalrat
spatial: https://ld.admin.ch/country/1
datetime_created: 2024-01-01T00:00:00Z
```

### Beispiel 2: Geschäftsprüfungskommission

```yaml
id: act:gpk_nr
group_type: commission
name:
  - text: Geschäftsprüfungskommission des Nationalrats
    language: de
abbreviation:
  - text: GPK-N
    language: de
type_label: Ständige Aufsichtskommission
parent_groups:
  - act:nationalrat
landing_page: https://www.parlament.ch/de/organe/kommissionen/aufsichtskommissionen/gpk
```

### Beispiel 3: Partei mit Hierarchie

```yaml
# Bundesebene
- id: act:gruene_schweiz
  group_type: party
  name:
    - text: Grüne Schweiz
      language: de
    - text: Les Verts Suisses
      language: fr
  abbreviation:
    - text: GPS
      language: de
  party_color: "#84B414"
  url_statutes: https://www.gruene.ch/statuten
  spatial: https://ld.admin.ch/country/1

# Kantonsebene
- id: act:gruene_bern
  group_type: party
  name:
    - text: Grüne Kanton Bern
      language: de
  parent_groups:
    - act:gruene_schweiz
  spatial: https://ld.admin.ch/canton/2
  landing_page: https://www.gruenebern.ch
```

### Beispiel 4: Bundesrat

```yaml
id: act:bundesrat
uri: https://politics.ld.admin.ch/government/bundesrat
group_type: government
name:
  - text: Bundesrat
    language: de
  - text: Conseil fédéral
    language: fr
  - text: Consiglio federale
    language: it
spatial: https://ld.admin.ch/country/1
landing_page: https://www.admin.ch/gov/de/start/bundesrat.html
contacts:
  - type: email
    value: info@gs-uvek.admin.ch
  - type: contact_website
    value: https://www.admin.ch/gov/de/start/bundesrat.html
addresses:
  - address_type: businessAddress
    street_address: Bundeshaus West
    postal_code: "3003"
    postal_locality: Bern
```

### Beispiel 5: Fraktion

```yaml
id: act:sp_fraktion_nr
group_type: faction
name:
  - text: SP-Fraktion im Nationalrat
    language: de
abbreviation:
  - text: SP
    language: de
parent_groups:
  - act:nationalrat
  - act:sp_schweiz  # Verbindung zur Partei
landing_page: https://www.sp-ps.ch/fraktion
```

## Referenzen

Siehe vollständige LinkML-Schema-Dokumentation:



# Class: Group 


_[en] A political group, organization, or body (e.g., party, committee, parliament, department)._

_[de] Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission, Parlament, Departement)._

__





URI: [act:Group](https://ch.paf.link/schema/actors/Group)





```mermaid
 classDiagram
    class Group
    click Group href "../Group/"
      Group : abbreviation
        
          
    
        
        
        Group --> "*" MultilingualString : abbreviation
        click MultilingualString href "../MultilingualString/"
    

        
      Group : addresses
        
          
    
        
        
        Group --> "*" Address : addresses
        click Address href "../Address/"
    

        
      Group : contacts
        
          
    
        
        
        Group --> "*" Contact : contacts
        click Contact href "../Contact/"
    

        
      Group : datetime_created
        
      Group : datetime_updated
        
      Group : description
        
          
    
        
        
        Group --> "*" MultilingualString : description
        click MultilingualString href "../MultilingualString/"
    

        
      Group : group_type
        
          
    
        
        
        Group --> "1" GroupTypeEnum : group_type
        click GroupTypeEnum href "../GroupTypeEnum/"
    

        
      Group : id
        
      Group : landing_page
        
      Group : name
        
          
    
        
        
        Group --> "*" MultilingualString : name
        click MultilingualString href "../MultilingualString/"
    

        
      Group : parent_groups
        
      Group : party_color
        
      Group : spatial
        
      Group : type_label
        
      Group : uri
        
      Group : url_statutes
        
      Group : valid_from
        
      Group : valid_until
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](#id) | 1 <br/> [String](#String) | [en] Unique identifier (preferably Wikidata-ID or URI) | direct |
| [uri](#uri) | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [en] Globally valid identifier (e | direct |
| [group_type](#group_type) | 1 <br/> [GroupTypeEnum](#GroupTypeEnum) | [en] Type of group (e | direct |
| [type_label](#type_label) | 0..1 <br/> [String](#String) | [en] Custom type label when standard type values don't apply | direct |
| [valid_from](#valid_from) | 0..1 <br/> [Date](#Date) | [en] Start date of validity period | direct |
| [valid_until](#valid_until) | 0..1 <br/> [Date](#Date) | [en] End date of validity period | direct |
| [name](#name) | * <br/> [MultilingualString](#MultilingualString) | [en] Name (can be multilingual) | direct |
| [abbreviation](#abbreviation) | * <br/> [MultilingualString](#MultilingualString) | [en] Abbreviation (can be multilingual) | direct |
| [description](#description) | * <br/> [MultilingualString](#MultilingualString) | [en] Description of the entity | direct |
| [landing_page](#landing_page) | 0..1 <br/> [String](#String) | [en] URL providing further information | direct |
| [parent_groups](#parent_groups) | * <br/> [String](#String) | [en] Parent group IDs (to model party hierarchy or bind parties to parliament... | direct |
| [spatial](#spatial) | 0..1 <br/> [String](#String) | [en] Spatial reference (municipality number, canton number, e | direct |
| [contacts](#contacts) | * <br/> [Contact](#Contact) | [en] Contact information (email, website, social media) | direct |
| [addresses](#addresses) | * <br/> [Address](#Address) | [en] Addresses (private, business, local) | direct |
| [url_statutes](#url_statutes) | 0..1 <br/> [String](#String) | [en] URL to party statutes (optional for parties) | direct |
| [party_color](#party_color) | 0..1 <br/> [String](#String) | [en] Party color (optional for parties) | direct |
| [datetime_updated](#datetime_updated) | 0..1 <br/> [Datetime](#Datetime) | [en] The last time this record was updated | direct |
| [datetime_created](#datetime_created) | 0..1 <br/> [Datetime](#Datetime) | [en] The time this record was created | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [groups](#groups) | range | [Group](#Group) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Group |
| native | act:Group |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Group
description: '[en] A political group, organization, or body (e.g., party, committee,
  parliament, department).

  [de] Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission,
  Parlament, Departement).

  '
from_schema: https://ch.paf.link/schema/actors
slots:
- id
- uri
- group_type
- type_label
- valid_from
- valid_until
- name
- abbreviation
- description
- landing_page
- parent_groups
- spatial
- contacts
- addresses
- url_statutes
- party_color
- datetime_updated
- datetime_created

```
</details>

### Induced

<details>
```yaml
name: Group
description: '[en] A political group, organization, or body (e.g., party, committee,
  parliament, department).

  [de] Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission,
  Parlament, Departement).

  '
from_schema: https://ch.paf.link/schema/actors
attributes:
  id:
    name: id
    description: '[en] Unique identifier (preferably Wikidata-ID or URI).

      [de] Eindeutiger Identifikator (vorzugsweise Wikidata-ID oder URI).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: dcterm:identifier
    identifier: true
    alias: id
    owner: Group
    domain_of:
    - Container
    - Person
    - Group
    - Membership
    - InterestLink
    - PersonReference
    - GroupReference
    range: string
    required: true
  uri:
    name: uri
    description: '[en] Globally valid identifier (e.g., politics.ld.admin.ch/party/1).

      [de] Global gültiger Identifikator (z.B. politics.ld.admin.ch/party/1).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: uri
    owner: Group
    domain_of:
    - Group
    - PersonReference
    - GroupReference
    range: uriorcurie
  group_type:
    name: group_type
    description: '[en] Type of group (e.g., party, committee, parliament, department).

      [de] Art der Gruppe (z.B. Partei, Kommission, Parlament, Departement).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:groupType
    alias: group_type
    owner: Group
    domain_of:
    - Group
    range: GroupTypeEnum
    required: true
  type_label:
    name: type_label
    description: '[en] Custom type label when standard type values don''t apply.

      [de] Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: type_label
    owner: Group
    domain_of:
    - Group
    range: string
  valid_from:
    name: valid_from
    description: '[en] Start date of validity period.

      [de] Startdatum der Gültigkeitsperiode.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:validFrom
    alias: valid_from
    owner: Group
    domain_of:
    - Group
    - Membership
    - InterestLink
    - Name
    - Validity
    - ElectoralDistrict
    range: date
  valid_until:
    name: valid_until
    description: '[en] End date of validity period.

      [de] Enddatum der Gültigkeitsperiode.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:validUntil
    alias: valid_until
    owner: Group
    domain_of:
    - Group
    - Membership
    - InterestLink
    - Name
    range: date
  name:
    name: name
    description: '[en] Name (can be multilingual).

      [de] Name (kann mehrsprachig sein).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: name
    owner: Group
    domain_of:
    - Group
    - PersonReference
    - GroupReference
    range: MultilingualString
    multivalued: true
    inlined: true
    inlined_as_list: true
  abbreviation:
    name: abbreviation
    description: '[en] Abbreviation (can be multilingual).

      [de] Abkürzung (kann mehrsprachig sein).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:abbreviation
    alias: abbreviation
    owner: Group
    domain_of:
    - Group
    range: MultilingualString
    multivalued: true
    inlined: true
    inlined_as_list: true
  description:
    name: description
    description: '[en] Description of the entity.

      [de] Beschreibung der Entität.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: description
    owner: Group
    domain_of:
    - Group
    range: MultilingualString
    multivalued: true
    inlined: true
    inlined_as_list: true
  landing_page:
    name: landing_page
    description: '[en] URL providing further information.

      [de] URL mit weiteren Informationen.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:landingPage
    alias: landing_page
    owner: Group
    domain_of:
    - Group
    range: string
  parent_groups:
    name: parent_groups
    description: '[en] Parent group IDs (to model party hierarchy or bind parties
      to parliaments).

      [de] Übergeordnete Gruppen-IDs (um Parteihierarchie oder Bindung an Parlamente
      abzubilden).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:parentGroup
    alias: parent_groups
    owner: Group
    domain_of:
    - Group
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  spatial:
    name: spatial
    description: '[en] Spatial reference (municipality number, canton number, e.g.,
      ld.admin.ch/municipality/234).

      [de] Räumliche Referenz (Gemeindenummer, Kantonsnummer, z.B. ld.admin.ch/municipality/234).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: spatial
    owner: Group
    domain_of:
    - Group
    range: string
  contacts:
    name: contacts
    description: '[en] Contact information (email, website, social media).

      [de] Kontaktinformationen (E-Mail, Website, Social Media).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:contact
    alias: contacts
    owner: Group
    domain_of:
    - Person
    - Group
    range: Contact
    multivalued: true
    inlined: true
    inlined_as_list: true
  addresses:
    name: addresses
    description: '[en] Addresses (private, business, local).

      [de] Adressen (privat, geschäftlich, lokal).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:address
    alias: addresses
    owner: Group
    domain_of:
    - Person
    - Group
    range: Address
    multivalued: true
    inlined: true
    inlined_as_list: true
  url_statutes:
    name: url_statutes
    description: '[en] URL to party statutes (optional for parties).

      [de] URL zu Parteistatuten (optional für Parteien).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:urlStatutes
    alias: url_statutes
    owner: Group
    domain_of:
    - Group
    range: string
  party_color:
    name: party_color
    description: '[en] Party color (optional for parties).

      [de] Parteifarbe (optional für Parteien).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:partyColor
    alias: party_color
    owner: Group
    domain_of:
    - Group
    range: string
  datetime_updated:
    name: datetime_updated
    description: '[en] The last time this record was updated.

      [de] Der Zeitpunkt, zu dem dieser Datensatz zuletzt aktualisiert wurde.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: datetime_updated
    owner: Group
    domain_of:
    - Person
    - Group
    - Membership
    - InterestLink
    range: datetime
  datetime_created:
    name: datetime_created
    description: '[en] The time this record was created.

      [de] Der Zeitpunkt, zu dem dieser Datensatz erstellt wurde.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: datetime_created
    owner: Group
    domain_of:
    - Person
    - Group
    - Membership
    - InterestLink
    range: datetime

```
</details>

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

Eine Membership verknüpft zwei Entitäten:

| Attribut | Typ | Pflicht | Beschreibung |
|----------|-----|---------|--------------|
| `id` | URI | Ja | Eindeutiger Identifikator der Mitgliedschaft |
| `person_id` | string | Ja | Referenz zur Person |
| `group_id` | string | Ja | Referenz zur Gruppe |

**Beispiel:**
```yaml
id: act:membership_jans_sp
person_id: https://www.wikidata.org/wiki/Q813067
group_id: act:sp_basel_stadt
```

## Datenstruktur

### Pflichtfelder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `id` | URI | Eindeutiger Identifikator der Mitgliedschaft |
| `person_id` | string | Referenz zur Person (Wikidata-ID oder lokale ID) |
| `group_id` | string | Referenz zur Gruppe (lokale ID) |

### Optionale Felder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `role` | string | Rolle/Funktion innerhalb der Gruppe |
| `valid_from` | date | Beginn der Mitgliedschaft |
| `valid_until` | date | Ende der Mitgliedschaft |
| `is_active` | boolean | Gibt an, ob die Mitgliedschaft derzeit aktiv ist |
| `authorized_to_vote` | boolean | Stimmberechtigung (relevant für Parlamente) |
| `datetime_updated` | datetime | Letzte Aktualisierung des Datensatzes |
| `datetime_created` | datetime | Erstellung des Datensatzes |

## Rollen (role)

Das Attribut `role` beschreibt die Funktion der Person in der Gruppe.

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

### valid_from und valid_until

Mitgliedschaften haben einen klar definierten Beginn und oft auch ein Ende:

```yaml
# Parlamentsmandat mit fester Amtszeit
id: act:membership_caroni_sr
person_id: https://www.wikidata.org/wiki/Q493598
group_id: act:staenderat
role: Mitglied
valid_from: 2015-12-07  # Amtsantritt nach Wahl
valid_until: 2023-11-30  # Ende der Amtsperiode
authorized_to_vote: true
```

```yaml
# Parteimitgliedschaft ohne Enddatum
id: act:membership_riniker_fdp
person_id: https://www.wikidata.org/wiki/Q77074968
group_id: act:fdp_aargau
role: Mitglied
valid_from: 2000-01-01
# valid_until nicht gesetzt = noch aktiv
is_active: true
```

### is_active

Alternative oder Ergänzung zu `valid_from`/`valid_until`:

- `true`: Mitgliedschaft ist derzeit aktiv
- `false`: Mitgliedschaft ist inaktiv/beendet
- Nicht gesetzt: Aktivität wird aus `valid_from`/`valid_until` abgeleitet

**Verwendung:**
```yaml
# Explizite Markierung als aktiv
is_active: true
valid_from: 2019-01-01

# Explizite Markierung als beendet
is_active: false
valid_from: 2015-01-01
valid_until: 2019-12-31
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
role: Mitglied
authorized_to_vote: true

# Nicht stimmberechtigtes Ersatzmitglied
role: Ersatzmitglied
authorized_to_vote: false

# Kommissionssekretär ohne Stimmrecht
role: Sekretär
authorized_to_vote: false
```

## Mehrfachmitgliedschaften

Eine Person kann gleichzeitig mehrere Mitgliedschaften haben:

```yaml
# Container-Struktur
persons:
  - id: https://www.wikidata.org/wiki/Q493598
    label: Andrea Caroni

memberships:
  # Parteimitgliedschaft
  - id: act:membership_caroni_fdp
    person_id: https://www.wikidata.org/wiki/Q493598
    group_id: act:fdp_appenzell
    role: Mitglied
    valid_from: 1998-01-01
    is_active: true

  # Parlamentsmandat
  - id: act:membership_caroni_sr
    person_id: https://www.wikidata.org/wiki/Q493598
    group_id: act:staenderat
    role: Mitglied
    valid_from: 2015-12-07
    authorized_to_vote: true
    is_active: true

  # Fraktionsmitgliedschaft
  - id: act:membership_caroni_fdp_fraktion
    person_id: https://www.wikidata.org/wiki/Q493598
    group_id: act:fdp_fraktion_sr
    role: Mitglied
    valid_from: 2015-12-07
    is_active: true

  # Kommissionsmitgliedschaft
  - id: act:membership_caroni_rk_sr
    person_id: https://www.wikidata.org/wiki/Q493598
    group_id: act:rechtskommission_sr
    role: Mitglied
    valid_from: 2016-01-01
    valid_until: 2019-12-31
    authorized_to_vote: true
    is_active: false
```

## Hierarchische Darstellung

Memberships können auch hierarchisch organisiert werden:

### Partei → Fraktion
```yaml
# Person ist Mitglied einer Partei
- id: act:membership_jans_sp
  person_id: https://www.wikidata.org/wiki/Q813067
  group_id: act:sp_schweiz
  role: Mitglied
  valid_from: 1980-01-01

# Person ist Mitglied der SP-Fraktion im Nationalrat
- id: act:membership_jans_sp_fraktion
  person_id: https://www.wikidata.org/wiki/Q813067
  group_id: act:sp_fraktion_nr
  role: Mitglied
  valid_from: 2010-12-06
```

Die Fraktion selbst hat eine `parent_groups`-Beziehung zur Partei (siehe Group-Schema).

## Wechsel und Nachfolge

### Parteiwechsel

```yaml
# SP-Mitgliedschaft (beendet)
- id: act:membership_mueller_sp
  person_id: act:person_mueller
  group_id: act:sp_zuerich
  role: Mitglied
  valid_from: 2010-01-01
  valid_until: 2018-06-30
  is_active: false

# Grüne-Mitgliedschaft (neu)
- id: act:membership_mueller_gruene
  person_id: act:person_mueller
  group_id: act:gruene_zuerich
  role: Mitglied
  valid_from: 2018-07-01
  is_active: true
```

### Rollenwechsel innerhalb einer Gruppe

```yaml
# Reguläres Mitglied
- id: act:membership_schmidt_kommission_1
  person_id: act:person_schmidt
  group_id: act:sik_nr
  role: Mitglied
  valid_from: 2016-01-01
  valid_until: 2019-12-31

# Präsidentin (Nachfolge-Membership)
- id: act:membership_schmidt_kommission_2
  person_id: act:person_schmidt
  group_id: act:sik_nr
  role: Präsidentin
  valid_from: 2020-01-01
  is_active: true
```

## Interoperabilität

### Verknüpfung im Container

```yaml
id: act:political_actors_dataset
persons:
  - id: https://www.wikidata.org/wiki/Q813067
    label: Beat Jans
    # ... weitere Person-Attribute

groups:
  - id: act:sp_basel_stadt
    group_type: party
    name: [{text: "SP Basel-Stadt", language: de}]
    # ... weitere Group-Attribute

memberships:
  - id: act:membership_jans_sp
    person_id: https://www.wikidata.org/wiki/Q813067
    group_id: act:sp_basel_stadt
    role: Mitglied
    valid_from: 1990-01-01
    is_active: true
```

### Auswertungen

**Nach Gruppe:**
```sparql
# Alle Mitglieder der SP Basel-Stadt
SELECT ?person ?role WHERE {
  ?membership a act:Membership ;
    act:group_id act:sp_basel_stadt ;
    act:person_id ?person ;
    act:role ?role ;
    act:isActive true .
}
```

**Nach Person:**
```sparql
# Alle Gruppen von Beat Jans
SELECT ?group ?role WHERE {
  ?membership a act:Membership ;
    act:person_id <https://www.wikidata.org/wiki/Q813067> ;
    act:group_id ?group ;
    act:role ?role ;
    act:isActive true .
}
```

## Anwendungsbeispiele

### Beispiel 1: Nationalratsmandat

```yaml
id: act:membership_riniker_nr
person_id: https://www.wikidata.org/wiki/Q77074968
group_id: act:nationalrat
role: Mitglied
valid_from: 2019-12-02  # Amtsantritt nach Wahl 2019
valid_until: 2023-11-30  # Ende der Legislaturperiode
authorized_to_vote: true
is_active: false  # Legislatur ist beendet
datetime_created: 2019-12-02T00:00:00Z
datetime_updated: 2023-11-30T00:00:00Z
```

### Beispiel 2: Kommissionsmitgliedschaft mit Präsidium

```yaml
# Reguläres Mitglied
id: act:membership_caroni_rk_1
person_id: https://www.wikidata.org/wiki/Q493598
group_id: act:rechtskommission_sr
role: Mitglied
valid_from: 2016-01-01
valid_until: 2019-12-31
authorized_to_vote: true
is_active: false

# Präsident
id: act:membership_caroni_rk_2
person_id: https://www.wikidata.org/wiki/Q493598
group_id: act:rechtskommission_sr
role: Präsident
valid_from: 2020-01-01
valid_until: 2023-12-31
authorized_to_vote: true
is_active: false
```

### Beispiel 3: Parteimitgliedschaft über alle Ebenen

```yaml
# Bundesebene
- id: act:membership_jans_sp_ch
  person_id: https://www.wikidata.org/wiki/Q813067
  group_id: act:sp_schweiz
  role: Mitglied
  valid_from: 1980-01-01
  is_active: true

# Kantonsebene
- id: act:membership_jans_sp_bs
  person_id: https://www.wikidata.org/wiki/Q813067
  group_id: act:sp_basel_stadt
  role: Mitglied
  valid_from: 1980-01-01
  is_active: true

# Gemeinde (optional)
- id: act:membership_jans_sp_basel
  person_id: https://www.wikidata.org/wiki/Q813067
  group_id: act:sp_stadt_basel
  role: Vorstandsmitglied
  valid_from: 2000-01-01
  valid_until: 2010-12-31
  is_active: false
```

### Beispiel 4: Bundesrat

```yaml
id: act:membership_luisier_vd_regierung
person_id: https://www.wikidata.org/wiki/Q24699807
group_id: act:regierungsrat_vaud
role: Conseillère d'État
valid_from: 2022-07-01
is_active: true
authorized_to_vote: true
datetime_created: 2022-07-01T00:00:00Z
```

### Beispiel 5: Fraktionsmitgliedschaft

```yaml
id: act:membership_riniker_fdp_fraktion
person_id: https://www.wikidata.org/wiki/Q77074968
group_id: act:fdp_fraktion_nr
role: Mitglied
valid_from: 2019-12-02
valid_until: 2023-11-30
is_active: false
datetime_created: 2019-12-02T00:00:00Z
```

### Beispiel 6: Ersatzmitglied

```yaml
id: act:membership_mueller_gpk_ersatz
person_id: act:person_mueller
group_id: act:gpk_nr
role: Ersatzmitglied
valid_from: 2020-01-01
valid_until: 2023-12-31
authorized_to_vote: false  # Ersatzmitglieder sind normalerweise nicht stimmberechtigt
is_active: false
```

### Beispiel 7: Delegation

```yaml
id: act:membership_caroni_delegation
person_id: https://www.wikidata.org/wiki/Q493598
group_id: act:delegation_europarat
role: Delegierter
valid_from: 2016-01-01
is_active: true
authorized_to_vote: true
```

## Auswertungsmöglichkeiten

### Aktive Mitgliedschaften

Filtern nach `is_active: true` oder `valid_until` nicht gesetzt:
```yaml
SELECT * FROM memberships
WHERE is_active = true
OR (valid_from <= CURRENT_DATE AND (valid_until IS NULL OR valid_until >= CURRENT_DATE))
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



# Class: Membership 


_[en] A membership relationship between a person and a group._

_[de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe._

__





URI: [act:Membership](https://ch.paf.link/schema/actors/Membership)





```mermaid
 classDiagram
    class Membership
    click Membership href "../Membership/"
      Membership : authorized_to_vote
        
      Membership : datetime_created
        
      Membership : datetime_updated
        
      Membership : group_id
        
      Membership : id
        
      Membership : is_active
        
      Membership : person_id
        
      Membership : role
        
      Membership : valid_from
        
      Membership : valid_until
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](#id) | 1 <br/> [String](#String) | [en] Unique identifier (preferably Wikidata-ID or URI) | direct |
| [person_id](#person_id) | 0..1 <br/> [String](#String) | [en] Reference to a person ID | direct |
| [group_id](#group_id) | 0..1 <br/> [String](#String) | [en] Reference to a group ID | direct |
| [role](#role) | 0..1 <br/> [String](#String) | [en] Role of the person in the membership or function | direct |
| [valid_from](#valid_from) | 0..1 <br/> [Date](#Date) | [en] Start date of validity period | direct |
| [valid_until](#valid_until) | 0..1 <br/> [Date](#Date) | [en] End date of validity period | direct |
| [is_active](#is_active) | 0..1 <br/> [Boolean](#Boolean) | [en] Indicates if the membership is currently active | direct |
| [authorized_to_vote](#authorized_to_vote) | 0..1 <br/> [Boolean](#Boolean) | [en] Indicates if the person is authorized to vote | direct |
| [datetime_updated](#datetime_updated) | 0..1 <br/> [Datetime](#Datetime) | [en] The last time this record was updated | direct |
| [datetime_created](#datetime_created) | 0..1 <br/> [Datetime](#Datetime) | [en] The time this record was created | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [memberships](#memberships) | range | [Membership](#Membership) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Membership |
| native | act:Membership |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Membership
description: '[en] A membership relationship between a person and a group.

  [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe.

  '
from_schema: https://ch.paf.link/schema/actors
slots:
- id
- person_id
- group_id
- role
- valid_from
- valid_until
- is_active
- authorized_to_vote
- datetime_updated
- datetime_created

```
</details>

### Induced

<details>
```yaml
name: Membership
description: '[en] A membership relationship between a person and a group.

  [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe.

  '
from_schema: https://ch.paf.link/schema/actors
attributes:
  id:
    name: id
    description: '[en] Unique identifier (preferably Wikidata-ID or URI).

      [de] Eindeutiger Identifikator (vorzugsweise Wikidata-ID oder URI).

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: dcterm:identifier
    identifier: true
    alias: id
    owner: Membership
    domain_of:
    - Container
    - Person
    - Group
    - Membership
    - InterestLink
    - PersonReference
    - GroupReference
    range: string
    required: true
  person_id:
    name: person_id
    description: '[en] Reference to a person ID.

      [de] Referenz zu einer Personen-ID.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: person_id
    owner: Membership
    domain_of:
    - Membership
    - InterestLink
    range: string
  group_id:
    name: group_id
    description: '[en] Reference to a group ID.

      [de] Referenz zu einer Gruppen-ID.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: group_id
    owner: Membership
    domain_of:
    - Membership
    range: string
  role:
    name: role
    description: '[en] Role of the person in the membership or function.

      [de] Rolle der Person in der Mitgliedschaft oder Funktion.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: role
    owner: Membership
    domain_of:
    - Membership
    - PersonReference
    - GroupReference
    range: string
  valid_from:
    name: valid_from
    description: '[en] Start date of validity period.

      [de] Startdatum der Gültigkeitsperiode.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:validFrom
    alias: valid_from
    owner: Membership
    domain_of:
    - Group
    - Membership
    - InterestLink
    - Name
    - Validity
    - ElectoralDistrict
    range: date
  valid_until:
    name: valid_until
    description: '[en] End date of validity period.

      [de] Enddatum der Gültigkeitsperiode.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:validUntil
    alias: valid_until
    owner: Membership
    domain_of:
    - Group
    - Membership
    - InterestLink
    - Name
    range: date
  is_active:
    name: is_active
    description: '[en] Indicates if the membership is currently active.

      [de] Gibt an, ob die Mitgliedschaft derzeit aktiv ist.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:isActive
    alias: is_active
    owner: Membership
    domain_of:
    - Membership
    range: boolean
  authorized_to_vote:
    name: authorized_to_vote
    description: '[en] Indicates if the person is authorized to vote.

      [de] Gibt an, ob die Person stimmberechtigt ist.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    slot_uri: act:authorizedToVote
    alias: authorized_to_vote
    owner: Membership
    domain_of:
    - Membership
    range: boolean
  datetime_updated:
    name: datetime_updated
    description: '[en] The last time this record was updated.

      [de] Der Zeitpunkt, zu dem dieser Datensatz zuletzt aktualisiert wurde.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: datetime_updated
    owner: Membership
    domain_of:
    - Person
    - Group
    - Membership
    - InterestLink
    range: datetime
  datetime_created:
    name: datetime_created
    description: '[en] The time this record was created.

      [de] Der Zeitpunkt, zu dem dieser Datensatz erstellt wurde.

      '
    from_schema: https://ch.paf.link/schema/actors
    rank: 1000
    alias: datetime_created
    owner: Membership
    domain_of:
    - Person
    - Group
    - Membership
    - InterestLink
    range: datetime

```
</details> 

* Überlegungen zu Datenschutz / Öffentlichkeitsrecht  (Christian schaut sich das an).
  * ein Kapitel mit Analyse des IST Zustands / Rechtsgrundlage oder Toolkit ?
  * Abklärung was ist rechtlich erlaubt.
  * Was wäre ethisch verantwortbar.
  * Personen des öffentlichen Interesses.
  
  * [Ersetzung der privaten Wohnadresse als Identifikator der Urheber von Volksinitiativen](https://www.parlament.ch/de/ratsbetrieb/suche-curia-vista/geschaeft?AffairId=20243425)
  * [Verhinderung der Pflicht zur Veröffentlichung der Wohnadressen von Parlamentsmitgliedern](https://www.parlament.ch/de/ratsbetrieb/suche-curia-vista/geschaeft?AffairId=20233913)

