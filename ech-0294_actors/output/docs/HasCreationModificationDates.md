

# Class: HasCreationModificationDates 


_[de] Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderungsdaten einer Entität zur Verfügung stellt._

_[en] A mixin class that provides slots for modeling creation and modification dates of an entity._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'date_created',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das Datum, an dem eine Entität erstellt wurde.\n'
     '[en] The date when an entity was created.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateCreated',
  'owner': 'HasCreationModificationDates',
  'domain_of': ['HasCreationModificationDates'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde.
[en] The date when an entity was created.
 | direct |
| SlotDefinition({
  'name': 'datetime_created',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.\n'
     '[en] The date and time when an entity was created.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeCreated',
  'owner': 'HasCreationModificationDates',
  'domain_of': ['HasCreationModificationDates'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.
[en] The date and time when an entity was created.
 | direct |
| SlotDefinition({
  'name': 'date_modified',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das Datum, an dem eine Entität zuletzt geändert wurde.\n'
     '[en] The date when an entity was last modified.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateModified',
  'owner': 'HasCreationModificationDates',
  'domain_of': ['HasCreationModificationDates'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde.
[en] The date when an entity was last modified.
 | direct |
| SlotDefinition({
  'name': 'datetime_modified',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.\n'
     '[en] The date and time when an entity was last modified.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeModified',
  'owner': 'HasCreationModificationDates',
  'domain_of': ['HasCreationModificationDates'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.
[en] The date and time when an entity was last modified.
 | direct |



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







