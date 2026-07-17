

## Class: Container 


_Container for political actors, groups, and relationships._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| persons | * <br/> [Person](Person.md) | Collection of persons.  |
| groups | * <br/> [Group](Group.md) | Collection of groups.  |
| memberships | * <br/> [Membership](Membership.md) | Collection of memberships.  |
| interest_links | * <br/> [InterestLink](InterestLink.md) | Collection of interest links.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |

















### Examples
#### Example: Container-interest_links

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
    organization_name: Burkart Advisory GmbH, Baden
    legal_form: "0107"  # GmbH
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
    organization_name: Birchmeier Holding AG, Döttingen
    legal_form: "0106"  # AG
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
    organization_name: Bovida Real Estate AG, Baar
    legal_form: "0106"  # AG
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
    organization_name: ELCA Group SA, Lausanne
    legal_form: "0106"  # AG
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
    organization_name: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
    legal_form: "0109"  # Verein
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
    organization_name: FDP.Die Liberalen
    legal_form: "0109"  # Verein
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
    organization_name: FONDATION SUISSE DE DEMINAGE (FSD), Genf
    legal_form: "0110"  # Stiftung
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
    organization_name: Stiebel Eltron AG, Lupfig
    legal_form: "0106"  # AG
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
    organization_name: SUISSEDIGITAL Verband für Kommunikationsnetze
    legal_form: "0109"  # Verein
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
    organization_name: Allianz Sicherheit Schweiz, Baden
    legal_form: "0109"  # Verein
    committee: Vorstand
    function_role: Präsident
    is_paid: false

  - global_uri: act:il_burkart_011
    person_reference:
      global_uri: https://www.wikidata.org/wiki/Q23060472
      label: Thierry Burkart
      group_label: FDP.Die Liberalen
    interest_type: association
    organization_name: Verein Landesausstellung Svizra27, Aarau
    legal_form: "0109"  # Verein
    committee: Vorstand
    function_role: Mitglied
    is_paid: false
```
#### Example: Container-swiss_politicians

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
      - training_type: "3223"  # Master Universität, ETH (inklusive Lizentiat / Diplom)
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