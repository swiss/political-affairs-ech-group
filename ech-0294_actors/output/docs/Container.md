---
search:
  boost: 10.0
---

# Class: Container 


_[de] Container für politische Akteure, Gruppen und Beziehungen._

_[en] Container for political actors, groups, and relationships._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [persons](persons.md) | * <br/> [Person](Person.md) | [de] Sammlung von Personen | direct |
| [groups](groups.md) | * <br/> [Group](Group.md) | [de] Sammlung von Gruppen | direct |
| [memberships](memberships.md) | * <br/> [Membership](Membership.md) | [de] Sammlung von Mitgliedschaften | direct |
| [interest_links](interest_links.md) | * <br/> [InterestLink](InterestLink.md) | [de] Sammlung von Interessenbindungen | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](HasIdentification.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Container |
| native | act:Container |




## Examples
### Example: Container-interest_links

```yaml
# Interessenbindungen Beispieldaten
# Quelle: https://api.openparldata.ch/v1/interests/ und parlament.ch
# Bodies: CHE (Bundesversammlung), ZH (Kanton Zürich), BS (Kanton Basel-Stadt),
#         261 (Stadt Zürich), 351 (Stadt Bern)

global_uri: act:interest_links_example
interest_links:
  
  # --- Thierry Burkart (FDP, Ständerat AG) ---
  
  # Berufliche Tätigkeit: eigene Beratungsfirma
  - global_uri: act:il_burkart_001
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

  # Verwaltungsrat AG
  - global_uri: act:il_burkart_002
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

  # Verwaltungsrat AG
  - global_uri: act:il_burkart_003
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

  # Verwaltungsrat IT-Unternehmen
  - global_uri: act:il_burkart_004
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

  # Verbandspräsidium (bezahlt)
  - global_uri: act:il_burkart_005
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

  # Parteiamt
  - global_uri: act:il_burkart_006
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

  # Stiftung (ehrenamtlich)
  - global_uri: act:il_burkart_007
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

  # Beirat Unternehmen
  - global_uri: act:il_burkart_008
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

  # Branchenverband (bezahlt)
  - global_uri: act:il_burkart_009
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

  # Ehrenamtliche Vereinsmitgliedschaften
  - global_uri: act:il_burkart_010
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

  - global_uri: act:il_burkart_011
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
### Example: Container-douglas_adams

```yaml
global_uri: act:douglas_adams_example
persons:
  - global_uri: https://www.wikidata.org/wiki/Q42
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
### Example: Container-swiss_politicians

```yaml
global_uri: act:swiss_politicians_example
persons:
  - local_id: 4032
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




