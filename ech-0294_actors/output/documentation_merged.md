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


# Person

## Einführung und Zielsetzung

Das Personenschema beschreibt natürliche Personen im politischen Kontext und zielt darauf ab, eine präzise und gleichzeitig flexible Datenstruktur bereitzustellen. Die Umsetzung soll es ermöglichen, vorhandene Informationen hochgradig strukturiert abzubilden (z.B. der Name nach Typisierung vom BFS), aber auch Informationen, die weniger klar und vollständing sind, darzustellen. Das Ziel ist es zu ermöglichen die Qualität kontinuierlich zu verbessern.

**Kernziele:**

- **Präzision**: Unterstützung von zeitlich gültigen Attributen (z.B. Namen, Adressen, Geschlecht).
- **Flexibilität**: Optionale Felder erlauben schrittweise Datenanreicherung.
- **Interoperabilität**: URIs als globale Identifikatoren wo vorhanden, inklusive der Möglichkeit auf Wikidata Einträge zu verweisen.
- **Mehrsprachigkeit**: Unterstützung mehrsprachiger Inhalte gemäss Schweizer Anforderungen.

Notiz: Die Verknüpfung von Personen im öffentlichen Interesse (Politikerinnen und Politiker) über die federalen Ebenen hinweg wird als ein wichtiges Langzeitziel gesehen. Eine zentrale Datenbank oder Identifizierungstelle der Personen kann nicht durch die Fachgruppe realisiert werden. Es gibt Ansätze im Datenmodell, damit man kontinuierlich die Identifikatoren über die Stufen hinweg harmonisieren kann. Zum einen durch die Benutzung von Global eindeutigen Identifikatoren (URIs), sowie von Vorschlägen welche bestehenden offenen Datenbanken zu verwenden (Wikidata). 

## Technische Struktur

### Identifikatoren

Das Person-Schema verwendet:

1. **Interne Identifikator (`id`)**: Ein systeminterner Identifikator welcher vom publizierenden System genutzt wird, wenn nicht schon ausschliesslich eine URI benutzt wird.

2. **Globaler Identifikator (`uri`)**: Ein globaler Identifikator welcher über verschiedene Systeme hinweg gültig ist. Bei Personen kann dabei die URI der Person in Wikidata benutzt werden. Z.b. (http://www.wikidata.org/entity/Q115531 für Adolf Ogi).

TODO: notes
LocalID: 3456
Mandatory - Global URI: ld.bs.ch/personen_id/3456
WikiData: 

LocalID: 
Global URI: politics.ld.admin.ch/partyid/234

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

### Datenmodell einer Person
TODO: Einfügen des LinkML Snippets.


**Namenstypen** (`NameTypeEnum`):
TODO: Referenz auf BFS / und oder eCH Standard.

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

### Sprachen

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
gender:
  - value: female
    label: # Für Klarifikation von diverse.
    valid_from: 1978-05-23
    pronouns:
      - sie
      - ihr
```

- `value`: Geschlechtscode (male, female, diverse)
- `pronouns`: Bevorzugte Pronomen (mehrsprachig möglich)
- Unterstützt zeitliche Änderungen

### Staatsbürgerschaft

```yaml
citizenships:
  - country: IT
    valid_from: 1980-04-19
  - country: DE
    valid_from: 2005-01-15
    valid_until: 2020-12-31
```

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

## Globale Identifikation über Wikidata
### Umsetzung und Beispiele

### Diskussion
TODO: Pros und Cons


## Referenzen

Siehe vollständige LinkML-Schema-Dokumentation:

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
| [label](#label) | 0..1 <br/> [String](#String) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... | direct |
| [label_long](#label_long) | 0..1 <br/> [String](#String) | [de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel z... | direct |
| [birth_year](#birth_year) | 0..1 <br/> [Integer](#Integer) | [de] Geburtsjahr | direct |
| [birth_date](#birth_date) | 0..1 <br/> [Date](#Date) | [de] Genaues Geburtsdatum | direct |
| [death_date](#death_date) | 0..1 <br/> [Date](#Date) | [de] Genaues Todesdatum | direct |
| [picture](#picture) | 0..1 <br/> [Uri](#Uri) | [de] Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF) | direct |
| [names](#names) | * <br/> [Name](#Name) | [en] Names of the person with type and value | direct |
| [addresses](#addresses) | * <br/> [Address](#Address) | [de] Adressen mit Typ (privat, geschäftlich, lokal) | direct |
| [language_proficiencies](#language_proficiencies) | * <br/> [LanguageProficiency](#LanguageProficiency) | [de] Sprachkompetenzen der Person | direct |
| [citizenships](#citizenships) | * <br/> [Citizenship](#Citizenship) | [de] Staatsbürgerschaften der Person | direct |
| [genders](#genders) | * <br/> [Gender](#Gender) | [de] Geschlecht der Person | direct |
| [occupations](#occupations) | * <br/> [Occupation](#Occupation) | [de] Berufe oder Tätigkeiten der Person | direct |
| [trainings](#trainings) | * <br/> [Training](#Training) | [de] Ausbildungen oder Bildungen der Person | direct |
| [contacts](#contacts) | * <br/> [Contact](#Contact) | [en] Contact information (email, website, social media) | direct |
| [electoral_district](#electoral_district) | 0..1 <br/> [ElectoralDistrict](#ElectoralDistrict) | [de] Link zum Wahlbezirk | direct |
| [interest_links](#interest_links) | * <br/> [InterestLink](#InterestLink) | [de] Sammlung von Interessenbindungen | direct |
| [local_id](#local_id) | 0..1 <br/> [String](#String) | [de] Lokaler Identifikator | [HasIdentification](#de] Lokaler Identifikator | [HasIdentification) |
| [global_uri](#global_uri) | 1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](#de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification) |
| [wikidata_uri](#wikidata_uri) | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](#de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification) |
| [date_created](#date_created) | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates](#de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates) |
| [datetime_created](#datetime_created) | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates) |
| [date_modified](#date_modified) | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](#de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates) |
| [datetime_modified](#datetime_modified) | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [persons](#persons) | range | [Person](#Person) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Person |
| native | act:Person |




## Examples
### Example: Person-swiss_politicians_Beat_Jans

```yaml
global_uri: https://www.wikidata.org/wiki/Q813067
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
  pronouns:
  - er
  - ihm
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
### Example: Person-douglas_adams_Douglas_Adams

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
| `global_uri` | URI | Ja | Global gültiger Identifikator (z.B. `politics.ld.admin.ch/party/...`) |
| `local_id` | string | Nein | Lokaler Identifikator im publizierenden System |
| `wikidata_uri` | URI | Nein | Wikidata-Entität der Gruppe, falls vorhanden |

**Beispiel:**
```yaml
global_uri: https://politics.ld.admin.ch/party/sp_basel_stadt
local_id: act:sp_basel_stadt
```

### Datenmodell (LinkML-Auszug)

```yaml
global_uri: https://politics.ld.admin.ch/party/sp_basel_stadt
local_id: act:sp_basel_stadt
group_type:
  group_type_enum: party
label: SP Basel-Stadt
abbreviation:
  - value: SP
    language: de
parent_groups:
  - https://politics.ld.admin.ch/party/sp_schweiz
```

## Datenstruktur

### Pflichtfelder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `global_uri` | URI | Eindeutiger globaler Identifikator |
| `group_type` | GroupType | Art der Gruppe (`group_type_enum`, optional `label`) |

### Optionale Felder

| Attribut | Datentyp | Beschreibung |
|----------|----------|--------------|
| `local_id` | string | Lokaler Identifikator |
| `wikidata_uri` | URI | Wikidata-Referenz |
| `label` | string | Anzeigename der Gruppe |
| `valid_from` | date | Beginn der Gültigkeit |
| `valid_through` | date | Ende der Gültigkeit |
| `abbreviation` | MultilingualValue[] | Abkürzung (mehrsprachig, `value`/`language`) |
| `description` | MultilingualValue[] | Beschreibung (mehrsprachig) |
| `landing_page` | URI | URL mit weiteren Informationen |
| `parent_groups` | string[] | Übergeordnete Gruppen (0..n) |
| `spatial` | string | Räumliche Referenz (Gemeinde-/Kantonsnummer) |
| `contacts` | Contact[] | Kontaktinformationen |
| `addresses` | Address[] | Adressen |
| `statutes_url` | URI | URL zu Statuten (speziell für Parteien) |
| `party_color` | string | Parteifarbe (speziell für Parteien) |
| `datetime_modified` | datetime | Letzte Aktualisierung |
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
group_type:
  group_type_enum: parliament
label: Nationalrat
description:
  - value: Conseil national
    language: fr
  - value: Consiglio nazionale
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
group_type:
  group_type_enum: commission
  label: Ständige Aufsichtskommission
label: Geschäftsprüfungskommission des Nationalrats
parent_groups:
  - act:nationalrat
```

#### delegation (Delegation)
Parlamentarische Delegationen.

```yaml
group_type:
  group_type_enum: delegation
label: Delegation für internationale Finanzfragen
```

#### faction (Fraktion)
Parlamentsfraktionen.

```yaml
group_type:
  group_type_enum: faction
label: SP-Fraktion
abbreviation:
  - value: SP
    language: de
parent_groups:
  - act:nationalrat
```

#### parliamentary_bureau (Parlamentsbüro)
Organisatorisches Leitungsgremium.

```yaml
group_type:
  group_type_enum: parliamentary_bureau
label: Büro des Nationalrats
```

#### presidency (Präsidium)
Präsidium des Parlaments.

```yaml
group_type:
  group_type_enum: presidency
label: Präsidium der Bundesversammlung
```

### Exekutive

#### government (Regierung)
Regierung als Gesamtorgan.

**Beispiele:**
- Bundesrat
- Regierungsrat (Kantone)
- Stadtrat / Gemeinderat

```yaml
group_type:
  group_type_enum: government
label: Bundesrat
description:
  - value: Conseil fédéral
    language: fr
spatial: https://ld.admin.ch/country/1
```

#### department (Departement)
Verwaltungsdepartemente.

```yaml
group_type:
  group_type_enum: department
label: Eidgenössisches Departement des Innern
abbreviation:
  - value: EDI
    language: de
parent_groups:
  - act:bundesrat
```

#### office (Amt)
Ämter innerhalb von Departementen.

```yaml
group_type:
  group_type_enum: office
label: Bundesamt für Gesundheit
abbreviation:
  - value: BAG
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
group_type:
  group_type_enum: extraparliamentary_commission
label: Bankrat der SNB
```

#### workgroup (Arbeitsgruppe)
Ad-hoc-Arbeitsgruppen.

```yaml
group_type:
  group_type_enum: workgroup
label: Arbeitsgruppe Klimapolitik
valid_from: 2024-01-01
valid_through: 2024-12-31
```

### Judikative

#### court (Gericht)
Gerichte aller Instanzen.

**Beispiele:**
- Bundesgericht
- Kantonsgericht
- Bezirksgericht

```yaml
group_type:
  group_type_enum: court
label: Bundesgericht
description:
  - value: Tribunal fédéral
    language: fr
  - value: Tribunale federale
    language: it
spatial: https://ld.admin.ch/country/1
```

### Zivilgesellschaft

#### party (Partei)
Politische Parteien auf allen föderalen Ebenen.

Jede föderale Ebene wird als eigene Gruppe geführt.

```yaml
group_type:
  group_type_enum: party
label: SP Schweiz
abbreviation:
  - value: SP
    language: de
statutes_url: https://www.sp-ps.ch/sites/default/files/documents/statuten_sp_d_0.pdf
party_color: "#FF0000"
spatial: https://ld.admin.ch/country/1
```

**Hierarchie-Beispiel:**
```yaml
# SP Schweiz (Bund)
- global_uri: act:sp_schweiz
  group_type:
    group_type_enum: party
  label: SP Schweiz
  spatial: https://ld.admin.ch/country/1

# SP Basel-Stadt (Kanton)
- global_uri: act:sp_basel_stadt
  group_type:
    group_type_enum: party
  label: SP Basel-Stadt
  parent_groups: [act:sp_schweiz]
  spatial: https://ld.admin.ch/canton/12

# SP Riehen (Gemeinde)
- global_uri: act:sp_riehen
  group_type:
    group_type_enum: party
  label: SP Riehen
  parent_groups: [act:sp_basel_stadt]
  spatial: https://ld.admin.ch/municipality/2703
```

#### list (Liste)
Wahllisten, können Teil einer Partei sein oder unabhängig.

```yaml
group_type:
  group_type_enum: list
label: Liste 1 - SP
parent_groups:
  - act:sp_basel_stadt  # Optional: Zugehörigkeit zur Partei
```

#### interest_group (Interessengruppe)
Lobbyorganisationen und Interessenverbände.

```yaml
group_type:
  group_type_enum: interest_group
label: Economiesuisse
```

#### association (Verein)
Vereine und Verbände.

```yaml
group_type:
  group_type_enum: association
label: Pro Natura
```

#### petition_carrier (Petitionsträger)
Träger von Petitionen oder Volksinitiativen.

```yaml
group_type:
  group_type_enum: petition_carrier
label: Komitee für bezahlbare Krankenkassen
```

### Andere Organe

#### control_body (Kontrollorgan)
Kontroll- und Aufsichtsorgane.

**Beispiele:**
- Eidgenössische Finanzkontrolle (EFK)
- AB-BA (Aufsichtsbehörde)

```yaml
group_type:
  group_type_enum: control_body
label: Eidgenössische Finanzkontrolle
abbreviation:
  - value: EFK
    language: de
```

#### parliamentary_services (Parlamentsdienste)
Unterstützungsdienste des Parlaments.

```yaml
group_type:
  group_type_enum: parliamentary_services
label: Parlamentsdienste der Bundesversammlung
```

#### university (Universität)
Universitäten und Hochschulen (als ausgelagerte Träger öffentlicher Aufgaben).

```yaml
group_type:
  group_type_enum: university
label: Universität Zürich
abbreviation:
  - value: UZH
    language: de
```

## Hierarchien und parent_groups

Das Attribut `parent_groups` erlaubt die Abbildung von Organisationsstrukturen:

### Parteihierarchie (Föderalismus)

```yaml
# National
- global_uri: act:fdp_schweiz
  parent_groups: []

# Kantonal
- global_uri: act:fdp_zuerich
  parent_groups: [act:fdp_schweiz]

# Kommunal
- global_uri: act:fdp_winterthur
  parent_groups: [act:fdp_zuerich]
```

### Verwaltungshierarchie

```yaml
# Departement
- global_uri: act:edi
  parent_groups: [act:bundesrat]

# Amt
- global_uri: act:bag
  parent_groups: [act:edi]

# Abteilung
- global_uri: act:bag_abteilung_gesundheitspolitik
  parent_groups: [act:bag]
```

### Kommissionshierarchie

```yaml
# Hauptkommission
- global_uri: act:sik_nr
  label: Sicherheitspolitische Kommission NR
  parent_groups: [act:nationalrat]

# Subkommission
- global_uri: act:sik_nr_sub_cyber
  label: Subkommission Cybersicherheit
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
label: Bundesversammlung
description:
  - value: Assemblée fédérale
    language: fr
  - value: Assemblea federale
    language: it
  - value: Assamblea federala
    language: rm

abbreviation:
  - value: BVers
    language: de
  - value: AsFed
    language: fr
```

## Partei-spezifische Attribute

### statutes_url
Link zu den Parteistatuten (PDF oder Webseite).

```yaml
statutes_url: https://www.sp-ps.ch/sites/default/files/documents/statuten_sp_d_0.pdf
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
  - global_uri: act:sp_basel_stadt
    group_type:
      group_type_enum: party
    label: SP Basel-Stadt

memberships:
  - global_uri: act:membership_jans_sp
    person_reference:
      global_uri: https://www.wikidata.org/wiki/Q813067
      label: Beat Jans
    group_reference:
      global_uri: act:sp_basel_stadt
      label: SP Basel-Stadt
    role_type:
      role_type_enum: member
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
global_uri: https://politics.ld.admin.ch/parliament/nationalrat
local_id: act:nationalrat
group_type:
  group_type_enum: parliament
label: Nationalrat
description:
  - value: Conseil national
    language: fr
  - value: Consiglio nazionale
    language: it
abbreviation:
  - value: NR
    language: de
  - value: CN
    language: fr
landing_page: https://www.parlament.ch/de/organe/nationalrat
spatial: https://ld.admin.ch/country/1
datetime_created: 2024-01-01T00:00:00Z
```

### Beispiel 2: Geschäftsprüfungskommission

```yaml
global_uri: act:gpk_nr
group_type:
  group_type_enum: commission
  label: Ständige Aufsichtskommission
label: Geschäftsprüfungskommission des Nationalrats
abbreviation:
  - value: GPK-N
    language: de
parent_groups:
  - act:nationalrat
landing_page: https://www.parlament.ch/de/organe/kommissionen/aufsichtskommissionen/gpk
```

### Beispiel 3: Partei mit Hierarchie

```yaml
# Bundesebene
- global_uri: act:gruene_schweiz
  group_type:
    group_type_enum: party
  label: Grüne Schweiz
  description:
    - value: Les Verts Suisses
      language: fr
  abbreviation:
    - value: GPS
      language: de
  party_color: "#84B414"
  statutes_url: https://www.gruene.ch/statuten
  spatial: https://ld.admin.ch/country/1

# Kantonsebene
- global_uri: act:gruene_bern
  group_type:
    group_type_enum: party
  label: Grüne Kanton Bern
  parent_groups:
    - act:gruene_schweiz
  spatial: https://ld.admin.ch/canton/2
  landing_page: https://www.gruenebern.ch
```

### Beispiel 4: Bundesrat

```yaml
global_uri: https://politics.ld.admin.ch/government/bundesrat
local_id: act:bundesrat
group_type:
  group_type_enum: government
label: Bundesrat
description:
  - value: Conseil fédéral
    language: fr
  - value: Consiglio federale
    language: it
spatial: https://ld.admin.ch/country/1
landing_page: https://www.admin.ch/gov/de/start/bundesrat.html
contacts:
  - contact_type: email
    value: info@gs-uvek.admin.ch
  - contact_type: contact_website
    value: https://www.admin.ch/gov/de/start/bundesrat.html
addresses:
  - address_type: businessAddress
    street_address: Bundeshaus West
    postal_code: "3003"
    postal_locality: Bern
```

### Beispiel 5: Fraktion

```yaml
global_uri: act:sp_fraktion_nr
group_type:
  group_type_enum: faction
label: SP-Fraktion im Nationalrat
abbreviation:
  - value: SP
    language: de
parent_groups:
  - act:nationalrat
  - act:sp_schweiz  # Verbindung zur Partei
landing_page: https://www.sp-ps.ch/fraktion
```

## Referenzen

Siehe vollständige LinkML-Schema-Dokumentation:

---
search:
  boost: 10.0
---

# Class: Group 


_[de] Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission, Parlament, Departement)._

_[en] A political group, organization, or body (e.g., party, committee, parliament, department)._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [group_type](#group_type) | 0..1 <br/> [GroupType](#GroupType) | [de] Klasse der Gruppierung, wie z | direct |
| [label](#label) | 0..1 <br/> [String](#String) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... | direct |
| [abbreviation](#abbreviation) | * <br/> [MultilingualValue](#MultilingualValue) | [de] Abkürzung (kann mehrsprachig sein) | direct |
| [description](#description) | * <br/> [MultilingualValue](#MultilingualValue) | [de] Kurze Beschreibung der Gruppierung | direct |
| [landing_page](#landing_page) | 0..1 <br/> [Uri](#Uri) | [de] Website mit weiteren Informationen | direct |
| [parent_groups](#parent_groups) | * <br/> [Uriorcurie](#Uriorcurie) | [de] Übergeordneten Gruppe | direct |
| [spatial](#spatial) | 0..1 <br/> [String](#String) | [de] Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer, z | direct |
| [contacts](#contacts) | * <br/> [Contact](#Contact) | [en] Contact information (email, website, social media) | direct |
| [addresses](#addresses) | * <br/> [Address](#Address) | [de] Adressen mit Typ (privat, geschäftlich, lokal) | direct |
| [statutes_url](#statutes_url) | 0..1 <br/> [String](#String) | [de] URL zu Parteistatuten (optional für Parteien) | direct |
| [party_color](#party_color) | 0..1 <br/> [String](#String) | [de] Parteifarbe (optional für Parteien) | direct |
| [local_id](#local_id) | 0..1 <br/> [String](#String) | [de] Lokaler Identifikator | [HasIdentification](#de] Lokaler Identifikator | [HasIdentification) |
| [global_uri](#global_uri) | 1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](#de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification) |
| [wikidata_uri](#wikidata_uri) | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](#de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification) |
| [date_created](#date_created) | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates](#de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates) |
| [datetime_created](#datetime_created) | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates) |
| [date_modified](#date_modified) | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](#de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates) |
| [datetime_modified](#datetime_modified) | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates) |
| [valid_from](#valid_from) | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity) |
| [valid_through](#valid_through) | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity) |
| [is_active](#is_active) | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [groups](#groups) | range | [Group](#Group) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Group |
| native | act:Group |









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

---
search:
  boost: 10.0
---

# Class: Membership 


_[de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe._

_[en] A membership relationship between a person and a group._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [person_reference](#person_reference) | 0..1 <br/> [PersonReference](#PersonReference) | [de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfun... | direct |
| [group_reference](#group_reference) | 0..1 <br/> [GroupReference](#GroupReference) | [de] Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfun... | direct |
| [role_type](#role_type) | 0..1 <br/> [RoleType](#RoleType) | [en] Role of the person in the membership or function | direct |
| [authorized_to_vote](#authorized_to_vote) | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Person stimmberechtigt ist | direct |
| [local_id](#local_id) | 0..1 <br/> [String](#String) | [de] Lokaler Identifikator | [HasIdentification](#de] Lokaler Identifikator | [HasIdentification) |
| [global_uri](#global_uri) | 1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](#de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification) |
| [wikidata_uri](#wikidata_uri) | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](#de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification) |
| [date_created](#date_created) | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates](#de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates) |
| [datetime_created](#datetime_created) | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates) |
| [date_modified](#date_modified) | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](#de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates) |
| [datetime_modified](#datetime_modified) | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates) |
| [valid_from](#valid_from) | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity) |
| [valid_through](#valid_through) | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity) |
| [is_active](#is_active) | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [memberships](#memberships) | range | [Membership](#Membership) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Membership |
| native | act:Membership |







 

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

---
search:
  boost: 10.0
---

# Class: InterestLink 


_[de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation._

_[en] An interest link (conflict of interest, political financing) of a person to an organization._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [person_reference](#person_reference) | 0..1 <br/> [PersonReference](#PersonReference) | [de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfun... | direct |
| [interest_type](#interest_type) | 1 <br/> [InterestTypeEnum](#InterestTypeEnum) | [de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verei... | direct |
| [organization_label](#organization_label) | 0..1 <br/> [String](#String) | [en] Label of the organization | direct |
| [organization_uid](#organization_uid) | 0..1 <br/> [String](#String) | [en] UID of the organization (for analysis with NOGA codes, etc | direct |
| [organization_address](#organization_address) | 0..1 <br/> [String](#String) | [en] Address of the organization | direct |
| [legal_form](#legal_form) | 0..1 <br/> [String](#String) | [en] Legal form of the organization | direct |
| [is_paid](#is_paid) | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Position bezahlt ist | direct |
| [committee](#committee) | 0..1 <br/> [String](#String) | [en] Committee or board (e | direct |
| [function_role](#function_role) | 0..1 <br/> [String](#String) | [en] Function or role in the organization | direct |
| [local_id](#local_id) | 0..1 <br/> [String](#String) | [de] Lokaler Identifikator | [HasIdentification](#de] Lokaler Identifikator | [HasIdentification) |
| [global_uri](#global_uri) | 1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](#de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification) |
| [wikidata_uri](#wikidata_uri) | 0..1 <br/> [Uriorcurie](#Uriorcurie) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](#de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification) |
| [date_created](#date_created) | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates](#de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates) |
| [datetime_created](#datetime_created) | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates) |
| [date_modified](#date_modified) | 0..1 <br/> [Date](#Date) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](#de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates) |
| [datetime_modified](#datetime_modified) | 0..1 <br/> [Datetime](#Datetime) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](#de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates) |
| [valid_from](#valid_from) | 0..1 <br/> [Date](#Date) | [de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity](#de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity) |
| [valid_through](#valid_through) | 0..1 <br/> [Date](#Date) | [de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity](#de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity) |
| [is_active](#is_active) | 0..1 <br/> [Boolean](#Boolean) | [de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity](#de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](#Container) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |
| [Person](#Person) | [interest_links](#interest_links) | range | [InterestLink](#InterestLink) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:InterestLink |
| native | act:InterestLink |




## Examples
### Example: InterestLink-interest_links_il_burkart_003

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
### Example: InterestLink-interest_links_il_burkart_002

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
### Example: InterestLink-interest_links_il_burkart_001

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
### Example: InterestLink-interest_links_il_burkart_004

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
### Example: InterestLink-interest_links_il_burkart_011

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
### Example: InterestLink-interest_links_il_burkart_009

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
### Example: InterestLink-interest_links_il_burkart_006

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
### Example: InterestLink-interest_links_il_burkart_008

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
### Example: InterestLink-interest_links_il_burkart_005

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
### Example: InterestLink-interest_links_il_burkart_010

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
### Example: InterestLink-interest_links_il_burkart_007

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






* Überlegungen zu Datenschutz / Öffentlichkeitsrecht  (Christian schaut sich das an).
  * ein Kapitel mit Analyse des IST Zustands / Rechtsgrundlage oder Toolkit ?
  * Abklärung was ist rechtlich erlaubt.
  * Was wäre ethisch verantwortbar.
  * Personen des öffentlichen Interesses.
  
  * [Ersetzung der privaten Wohnadresse als Identifikator der Urheber von Volksinitiativen](https://www.parlament.ch/de/ratsbetrieb/suche-curia-vista/geschaeft?AffairId=20243425)
  * [Verhinderung der Pflicht zur Veröffentlichung der Wohnadressen von Parlamentsmitgliedern](https://www.parlament.ch/de/ratsbetrieb/suche-curia-vista/geschaeft?AffairId=20233913)

