

## Class: Group 


_A political group, organization, or body (e.g., party, committee, parliament, department)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| group_type | 1 <br/> [GroupType](GroupType.md) | Type of group (e.g., party, commission, parliament, or similar). The exact naming and description of the group is provided via `label`.  |
| label | 1..* <br/> [MultilingualValue](MultilingualValue.md) | Name of the group, with the language it is published in. Where a group is officially named in several languages, one entry per language is recorded.  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abbreviation (can be multilingual).  |
| description | * <br/> [MultilingualValue](MultilingualValue.md) | Description of the entity.  |
| organization_uid | 0..1 <br/> [String](String.md) | UID of the organization (eCH-0097 format: CHE-XXX.XXX.XXX) from the federal UID register (uid.admin.ch).  |
| legal_form | 0..1 <br/> [LegalFormEnum](LegalFormEnum.md) | Legal form of the organization. See controlled vocabulary: https://register.ld.admin.ch/i14y/concept/legalForm  |
| landing_page | * <br/> [MultilingualUri](MultilingualUri.md) | Website providing further information. Where the site is published under a separate address per language, one entry per language is recorded.  |
| parent_groups | * <br/> [GroupReference](GroupReference.md) | Reference to the parent groups as a GroupReference, i.e. stated by their local_id or their global_uri. Only genuine super-/subordination belongs here: the parent party of a cantonal party, the hierarchy within the executive, a sub-commission under its commission, or a parliamentary group under its parliament. (parentGroup is typically used within the same group_type, but cross-type links are permitted, e.g. parliamentary group → parliament.) The parties carrying a parliamentary group are not a superordinate group of it and are therefore not stated here.  |
| spatial | 0..1 <br/> [String](String.md) | Spatial reference (fos-municipality number, fos-canton number, or country). Formats: municipality: ld.admin.ch/municipality/1234, canton: ld.admin.ch/canton/23, country: ld.admin.ch/country/CHE.  |
| contacts | * <br/> [Contact](Contact.md) | Contact information (email, website, social media). Guideline: email is quasi-mandatory and should always be provided where available.  |
| addresses | * <br/> [Address](Address.md) | Addresses with type (private, business, local).  |
| statutes_url | 0..1 <br/> [String](String.md) | URL to party statutes (PDF or webpage; optional for parties).  |
| party_color | 0..1 <br/> [String](String.md) | Party color as hexadecimal value (optional for parties, e.g., "#FF0000").  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [groups](groups.md) | range | [Group](Group.md) |














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
organization_uid: CHE-106.063.525
legal_form: 0109
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