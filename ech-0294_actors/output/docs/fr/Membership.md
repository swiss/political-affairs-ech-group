

## Classe: Membership 


_Une relation d'affiliation entre une personne et un groupe, représentant une appartenance formelle (p. ex. membre d'un parti, membre d'une commission, parlementaire). À distinguer de InterestLink, qui recouvre les liens d'intérêts externes et les conflits d'intérêts avec des organisations situées en dehors du schéma des acteurs._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| person_reference | 1 <br/> [PersonReference](PersonReference.md) | Référence abrégée à une personne, retenant ses caractéristiques au moment de la mise en relation.  |
| group_reference | 1 <br/> [GroupReference](GroupReference.md) | Référence abrégée à un groupe, retenant ses caractéristiques au moment de la mise en relation.  |
| electoral_district | 0..1 <br/> [ElectoralDistrict](ElectoralDistrict.md) | Circonscription électorale de l'affiliation. Indiquée lorsque le mandat a été obtenu dans une circonscription ; elle est donc rattachée à l'affiliation et non à la personne.  |
| role_type | 0..1 <br/> [RoleType](RoleType.md) | Rôle de la personne dans l'affiliation ou la fonction.  |
| authorized_to_vote | 0..1 <br/> [Boolean](Boolean.md) | Indique si la personne dispose du droit de vote au sein du groupe. Généralement false pour les membres suppléants (lorsqu'ils ne remplacent personne), les observateurs, les secrétaires et les invités.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indique si l'affiliation est actuellement active. Peut compléter ou remplacer `valid_from`/`valid_through`. Si cette valeur n'est pas renseignée, l'activité est déduite des champs de validité temporelle.  |
| date_created | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été créée. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | La date à laquelle une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure auxquelles une entité a été modifiée pour la dernière fois. <br/><br/>Héritage : [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | La date à partir de laquelle l'information est valable. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | La date jusqu'à laquelle l'information est valable, incluse. <br/><br/>Héritage : [HasTemporalValidity](HasTemporalValidity.md) |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](Container.md) | [memberships](memberships.md) | range | [Membership](Membership.md) |














### Exemples
#### Exemple Membership : Person and group from the same delivery with electoral district

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
    label:
    - value: Kleinbasel
      language: de
  role_type:
    role_type_enum: member
  authorized_to_vote: true
  valid_from: 2001-02-07
  valid_through: 2011-04-30
  is_active: false

```
#### Exemple Membership : Parliamentary group membership alongside the council mandate

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
#### Exemple Membership : Role outside the vocabulary named in the role label

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
#### Exemple Membership : Ongoing mandate without an end date

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
#### Exemple Membership : Party membership without temporal information

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
#### Exemple Membership : The same person at another level with another electoral district

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
    label:
    - value: Basel-Stadt
      language: de
  role_type:
    role_type_enum: member
    role_label:
    - value: Mitglied
      language: de
    - value: Membro
      language: it
  authorized_to_vote: true
  valid_from: 2010-05-31
  valid_through: 2011-12-04
  is_active: false

```
#### Exemple Membership : Executive mandate with a presiding role

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
#### Exemple Membership : Committee membership with a duration of its own

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






</div>