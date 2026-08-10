

## Class: Membership 


_A membership relationship between a person and a group, representing formal affiliation (e.g., party member, commission member, parliamentarian). Distinct from InterestLink, which covers external interest bindings and conflicts of interest to organizations outside the actor schema._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| person_reference | 1 <br/> [PersonReference](PersonReference.md) | Reference to a person with snapshot data at time of linking.  |
| group_reference | 1 <br/> [GroupReference](GroupReference.md) | Reference to a group with snapshot data at time of linking.  |
| electoral_district | 0..1 <br/> [ElectoralDistrict](ElectoralDistrict.md) | Electoral district of the membership. Stated where the mandate was won in an electoral district; it is therefore recorded on the membership and not on the person.  |
| role_type | 0..1 <br/> [RoleType](RoleType.md) | Role of the person in the membership or function.  |
| authorized_to_vote | 0..1 <br/> [Boolean](Boolean.md) | Indicates if the person is authorized to vote in the group. Typically false for substitute members (when not deputizing), observers, secretaries, and guests.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates if the membership is currently active. Can complement or replace `valid_from`/`valid_through`. If not set, activity is derived from the temporal validity fields.  |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [memberships](memberships.md) | range | [Membership](Membership.md) |














### Examples
#### Example Membership: The same person at another level with another electoral district

```yaml
memberships:
- global_uri: act:ms_jans_nationalrat
  person_reference:
    local_id: 4032
    global_uri: https://www.admin.ch/de/beat-jans
    label: Beat Jans
  group_reference:
    global_uri: https://www.parlament.ch/de/organe/nationalrat
    label: Nationalrat
  electoral_district:
    global_uri: https://ld.admin.ch/canton/12
    label: Basel-Stadt
  role_type:
    role_type_enum: member
  authorized_to_vote: true
  valid_from: 2010-05-31
  valid_through: 2011-12-04
  is_active: false

```
#### Example Membership: Executive mandate with a presiding role

```yaml
memberships:
- global_uri: act:ms_jans_regierungsrat_bs
  person_reference:
    local_id: 4032
    global_uri: https://www.admin.ch/de/beat-jans
    label: Beat Jans
  group_reference:
    local_id: 1300
    global_uri: https://www.regierungsrat.bs.ch/
    label: Regierungsrat Basel-Stadt
  role_type:
    role_type_enum: president
    role_label:
    - value: Regierungspräsident
      language: de
  authorized_to_vote: true
  valid_from: 2021-02-03
  valid_through: 2023-12-31
  is_active: false

```
#### Example Membership: Person and group from the same delivery with electoral district

```yaml
memberships:
- global_uri: act:ms_jans_grossrat_bs
  person_reference:
    local_id: 4032
    global_uri: https://www.admin.ch/de/beat-jans
    label: Beat Jans
  group_reference:
    local_id: 33
    global_uri: https://www.grosserrat.bs.ch/
    label: Grosser Rat Basel-Stadt
  electoral_district:
    global_uri: https://grosserrat.bs.ch/wahlkreise/kleinbasel
    label: Kleinbasel
  role_type:
    role_type_enum: member
  authorized_to_vote: true
  valid_from: 2001-02-07
  valid_through: 2011-04-30
  is_active: false

```
#### Example Membership: Ongoing mandate without an end date

```yaml
memberships:
- global_uri: act:ms_jans_bundesrat
  person_reference:
    local_id: 4032
    global_uri: https://www.admin.ch/de/beat-jans
    label: Beat Jans
  group_reference:
    global_uri: https://www.admin.ch/de/der-bundesrat
    label: Bundesrat
  role_type:
    role_type_enum: member
  authorized_to_vote: true
  valid_from: 2024-01-01
  is_active: true

```
#### Example Membership: Parliamentary group membership alongside the council mandate

```yaml
memberships:
- global_uri: act:ms_jans_fraktion_sp_bs
  person_reference:
    local_id: 4032
    global_uri: https://www.admin.ch/de/beat-jans
    label: Beat Jans
  group_reference:
    global_uri: https://grosserrat.bs.ch/gremien/parteien-und-fraktionen/sp
    label: Sozialdemokratische Partei (SP)
  role_type:
    role_type_enum: member
  authorized_to_vote: true
  valid_from: 2001-02-07
  valid_through: 2011-04-30
  is_active: false

```
#### Example Membership: Committee membership with a duration of its own

```yaml
memberships:
- global_uri: act:ms_jans_wak_bs
  person_reference:
    local_id: 4032
    global_uri: https://www.admin.ch/de/beat-jans
    label: Beat Jans
  group_reference:
    global_uri: https://grosserrat.bs.ch/gremien/sachkommissionen/wirtschaft-abgaben
    label: Wirtschafts- und Abgabekommission (WAK)
  role_type:
    role_type_enum: member
  authorized_to_vote: true
  valid_from: 2003-02-12
  valid_through: 2011-04-30
  is_active: false

```
#### Example Membership: Party membership without temporal information

```yaml
memberships:
- global_uri: act:ms_jans_partei_sp
  person_reference:
    local_id: 4032
    global_uri: https://www.admin.ch/de/beat-jans
    label: Beat Jans
  group_reference:
    global_uri: https://www.sp-ps.ch/
    label: Sozialdemokratische Partei der Schweiz
  role_type:
    role_type_enum: member
  is_active: true

```
#### Example Membership: Role outside the vocabulary named in the role label

```yaml
memberships:
- global_uri: act:ms_jans_ejpd
  person_reference:
    local_id: 4032
    global_uri: https://www.admin.ch/de/beat-jans
    label: Beat Jans
  group_reference:
    global_uri: https://www.ejpd.admin.ch/
    label: Eidgenössisches Justiz- und Polizeidepartement
  role_type:
    role_type_enum: other
    role_label:
    - value: Departementsvorsteher
      language: de
  valid_from: 2024-01-01
  is_active: true

```






</div>