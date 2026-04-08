---
search:
  boost: 10.0
---

# Class: InterestLink 


_[de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation._

_[en] An interest link (conflict of interest, political financing) of a person to an organization._

__



<div data-search-exclude markdown="1">



URI: [act:InterestLink](https://ld.ech.ch/schema/0294/actors/InterestLink)





## Inheritance
* **InterestLink** [ [HasIdentification](HasIdentification.md) [HasCreationModificationDates](HasCreationModificationDates.md) [HasTemporalValidity](HasTemporalValidity.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [concerned_person](concerned_person.md) | 0..1 <br/> [Person](Person.md) | [de] Link zu einer Person, auf die sich die Zugehörigkeit bezieht | direct |
| [interest_type](interest_type.md) | 1 <br/> [InterestTypeEnum](InterestTypeEnum.md) | [de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verei... | direct |
| [organization_label](organization_label.md) | 0..1 <br/> [String](String.md) | [en] Label of the organization | direct |
| [organization_uid](organization_uid.md) | 0..1 <br/> [String](String.md) | [en] UID of the organization (for analysis with NOGA codes, etc | direct |
| [organization_address](organization_address.md) | 0..1 <br/> [String](String.md) | [en] Address of the organization | direct |
| [legal_form](legal_form.md) | 0..1 <br/> [String](String.md) | [en] Legal form of the organization | direct |
| [is_paid](is_paid.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Position bezahlt ist | direct |
| [committee](committee.md) | 0..1 <br/> [String](String.md) | [en] Committee or board (e | direct |
| [function_role](function_role.md) | 0..1 <br/> [String](String.md) | [en] Function or role in the organization | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](HasIdentification.md) |
| [date_created](date_created.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_created](datetime_created.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [date_modified](date_modified.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [datetime_modified](datetime_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | [HasCreationModificationDates](HasCreationModificationDates.md) |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [valid_through](valid_through.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [is_active](is_active.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |
| [Person](Person.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:InterestLink |
| native | act:InterestLink |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InterestLink
description: '[de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung)
  einer Person zu einer Organisation.

  [en] An interest link (conflict of interest, political financing) of a person to
  an organization.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasIdentification
- HasCreationModificationDates
- HasTemporalValidity
slots:
- concerned_person
- interest_type
- organization_label
- organization_uid
- organization_address
- legal_form
- is_paid
- committee
- function_role

```
</details>

### Induced

<details>
```yaml
name: InterestLink
description: '[de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung)
  einer Person zu einer Organisation.

  [en] An interest link (conflict of interest, political financing) of a person to
  an organization.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasIdentification
- HasCreationModificationDates
- HasTemporalValidity
attributes:
  concerned_person:
    name: concerned_person
    description: '[de] Link zu einer Person, auf die sich die Zugehörigkeit bezieht.

      [en] Link to a person that the affiliation concerns.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:concernedPerson
    alias: concerned_person
    owner: InterestLink
    domain_of:
    - Membership
    - InterestLink
    range: Person
  interest_type:
    name: interest_type
    description: '[de] Art der Interessenbindung (Berufliche Tätigkeit, Politische
      Ämter, Verein).

      [en] Type of interest link (professional activity, political office, association).

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:interestType
    alias: interest_type
    owner: InterestLink
    domain_of:
    - InterestLink
    range: InterestTypeEnum
    required: true
  organization_label:
    name: organization_label
    description: '[en] Label of the organization.

      [de] Bezeichnung der Organisation.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:organizationLabel
    alias: organization_label
    owner: InterestLink
    domain_of:
    - InterestLink
    range: string
  organization_uid:
    name: organization_uid
    description: '[en] UID of the organization (for analysis with NOGA codes, etc.).

      [de] UID der Organisation (für Auswertungen mit NOGA-Codes, etc.).

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:organizationUid
    alias: organization_uid
    owner: InterestLink
    domain_of:
    - InterestLink
    range: string
  organization_address:
    name: organization_address
    description: '[en] Address of the organization.

      [de] Adresse der Organisation.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:organizationAddress
    alias: organization_address
    owner: InterestLink
    domain_of:
    - InterestLink
    range: string
  legal_form:
    name: legal_form
    description: '[en] Legal form of the organization.

      [de] Rechtsform der Organisation.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:legalForm
    alias: legal_form
    owner: InterestLink
    domain_of:
    - InterestLink
    range: string
  is_paid:
    name: is_paid
    description: '[de] Gibt an, ob die Position bezahlt ist.

      [en] Indicates if the position is paid.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:isPaid
    alias: is_paid
    owner: InterestLink
    domain_of:
    - InterestLink
    - Occupation
    range: boolean
  committee:
    name: committee
    description: '[en] Committee or board (e.g., foundation board, board of directors).

      [de] Gremium (z.B. Stiftungsrat, Verwaltungsrat).

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:committee
    alias: committee
    owner: InterestLink
    domain_of:
    - InterestLink
    range: string
  function_role:
    name: function_role
    description: '[en] Function or role in the organization.

      [de] Funktion oder Rolle in der Organisation.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:functionRole
    alias: function_role
    owner: InterestLink
    domain_of:
    - InterestLink
    range: string
  local_id:
    name: local_id
    description: '[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

      [en] Local identifier. For example, a UUID from the council information system.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:localId
    alias: local_id
    owner: InterestLink
    domain_of:
    - HasIdentification
    range: string
  global_uri:
    name: global_uri
    description: '[de] Eine eindeutige, global gültige URI für die Entität.

      [en] A unique, globally valid URI for the entity.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:globalURI
    identifier: true
    alias: global_uri
    owner: InterestLink
    domain_of:
    - HasIdentification
    range: uriorcurie
    required: true
  wikidata_uri:
    name: wikidata_uri
    description: '[de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39
      für die Schweiz.

      [en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39
      for Switzerland.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:wikidataUri
    alias: wikidata_uri
    owner: InterestLink
    domain_of:
    - HasIdentification
    range: uriorcurie
  date_created:
    name: date_created
    description: '[de] Das Datum, an dem eine Entität erstellt wurde.

      [en] The date when an entity was created.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:dateCreated
    alias: date_created
    owner: InterestLink
    domain_of:
    - HasCreationModificationDates
    range: date
  datetime_created:
    name: datetime_created
    description: '[de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.

      [en] The date and time when an entity was created.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:datetimeCreated
    alias: datetime_created
    owner: InterestLink
    domain_of:
    - HasCreationModificationDates
    range: datetime
  date_modified:
    name: date_modified
    description: '[de] Das Datum, an dem eine Entität zuletzt geändert wurde.

      [en] The date when an entity was last modified.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:dateModified
    alias: date_modified
    owner: InterestLink
    domain_of:
    - HasCreationModificationDates
    range: date
  datetime_modified:
    name: datetime_modified
    description: '[de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert
      wurde.

      [en] The date and time when an entity was last modified.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:datetimeModified
    alias: datetime_modified
    owner: InterestLink
    domain_of:
    - HasCreationModificationDates
    range: datetime
  valid_from:
    name: valid_from
    description: '[de] Das Datum, ab dem die Information gültig ist.

      [en] The date from which the information is valid.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: schema:validFrom
    alias: valid_from
    owner: InterestLink
    domain_of:
    - HasTemporalValidity
    range: date
  valid_through:
    name: valid_through
    description: '[de] Das Datum, bis und mit dem die Information gültig ist.

      [en] The date until which the information is valid, inclusive.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: schema:validThrough
    alias: valid_through
    owner: InterestLink
    domain_of:
    - HasTemporalValidity
    range: date
  is_active:
    name: is_active
    description: '[de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich
      sein, wenn diese Information explizit vorhanden ist.

      [en] Indicates whether the information is currently valid. Can be useful when
      this information is explicitly available.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:isCurrent
    alias: is_active
    owner: InterestLink
    domain_of:
    - HasTemporalValidity
    range: boolean

```
</details></div>