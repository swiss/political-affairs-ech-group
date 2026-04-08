---
search:
  boost: 10.0
---

# Class: Membership 


_[de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe._

_[en] A membership relationship between a person and a group._

__



<div data-search-exclude markdown="1">



URI: [act:Membership](https://ld.ech.ch/schema/0294/actors/Membership)





## Inheritance
* **Membership** [ [HasIdentification](HasIdentification.md) [HasCreationModificationDates](HasCreationModificationDates.md) [HasTemporalValidity](HasTemporalValidity.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [concerned_person](concerned_person.md) | 0..1 <br/> [Person](Person.md) | [de] Link zu einer Person, auf die sich die Zugehörigkeit bezieht | direct |
| [concerned_group](concerned_group.md) | 0..1 <br/> [Group](Group.md) | [de] Link zu einer Gruppe, auf die sich die Zugehörigkeit bezieht | direct |
| [role_type](role_type.md) | 0..1 <br/> [RoleType](RoleType.md) | [en] Role of the person in the membership or function | direct |
| [authorized_to_vote](authorized_to_vote.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Person stimmberechtigt ist | direct |
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
| [Container](Container.md) | [memberships](memberships.md) | range | [Membership](Membership.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




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
description: '[de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe.

  [en] A membership relationship between a person and a group.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasIdentification
- HasCreationModificationDates
- HasTemporalValidity
slots:
- concerned_person
- concerned_group
- role_type
- authorized_to_vote

```
</details>

### Induced

<details>
```yaml
name: Membership
description: '[de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe.

  [en] A membership relationship between a person and a group.

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
    owner: Membership
    domain_of:
    - Membership
    - InterestLink
    range: Person
  concerned_group:
    name: concerned_group
    description: '[de] Link zu einer Gruppe, auf die sich die Zugehörigkeit bezieht.

      [en] Link to a group that the affiliation concerns.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:concernedGroup
    alias: concerned_group
    owner: Membership
    domain_of:
    - Membership
    range: Group
  role_type:
    name: role_type
    description: '[en] Role of the person in the membership or function.

      [de] Rolle der Person in der Mitgliedschaft oder Funktion.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:roleType
    alias: role_type
    owner: Membership
    domain_of:
    - Membership
    range: RoleType
  authorized_to_vote:
    name: authorized_to_vote
    description: '[de] Gibt an, ob die Person stimmberechtigt ist.

      [en] Indicates if the person is authorized to vote.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:authorizedToVote
    alias: authorized_to_vote
    owner: Membership
    domain_of:
    - Membership
    range: boolean
  local_id:
    name: local_id
    description: '[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

      [en] Local identifier. For example, a UUID from the council information system.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:localId
    alias: local_id
    owner: Membership
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
    owner: Membership
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
    owner: Membership
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
    owner: Membership
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
    owner: Membership
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
    owner: Membership
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
    owner: Membership
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
    owner: Membership
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
    owner: Membership
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
    owner: Membership
    domain_of:
    - HasTemporalValidity
    range: boolean

```
</details></div>