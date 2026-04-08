---
search:
  boost: 10.0
---

# Class: HasCreationModificationDates 


_[de] Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderungsdaten einer Entität zur Verfügung stellt._

_[en] A mixin class that provides slots for modeling creation and modification dates of an entity._

__



<div data-search-exclude markdown="1">



URI: [act:HasCreationModificationDates](https://ld.ech.ch/schema/0294/actors/HasCreationModificationDates)




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [date_created](date_created.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde | direct |
| [datetime_created](datetime_created.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde | direct |
| [date_modified](date_modified.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde | direct |
| [datetime_modified](datetime_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |














## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:HasCreationModificationDates |
| native | act:HasCreationModificationDates |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasCreationModificationDates
description: '[de] Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs-
  und Änderungsdaten einer Entität zur Verfügung stellt.

  [en] A mixin class that provides slots for modeling creation and modification dates
  of an entity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixin: true
slots:
- date_created
- datetime_created
- date_modified
- datetime_modified

```
</details>

### Induced

<details>
```yaml
name: HasCreationModificationDates
description: '[de] Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs-
  und Änderungsdaten einer Entität zur Verfügung stellt.

  [en] A mixin class that provides slots for modeling creation and modification dates
  of an entity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixin: true
attributes:
  date_created:
    name: date_created
    description: '[de] Das Datum, an dem eine Entität erstellt wurde.

      [en] The date when an entity was created.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:dateCreated
    alias: date_created
    owner: HasCreationModificationDates
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
    owner: HasCreationModificationDates
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
    owner: HasCreationModificationDates
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
    owner: HasCreationModificationDates
    domain_of:
    - HasCreationModificationDates
    range: datetime

```
</details></div>