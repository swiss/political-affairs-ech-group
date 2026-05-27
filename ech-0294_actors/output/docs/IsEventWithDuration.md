

# Class: IsEventWithDuration 


_[de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder Vorkommnissen mit Zeitdauer zur Verfügung stellt._

_[en] A mixin class that provides slots for modeling events or occurrences with time duration._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'date_begin_actual',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit '
     'Zeitdauer.\n'
     '[en] The actual start date of an event or occurrence with time duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateBeginActual',
  'owner': 'IsEventWithDuration',
  'domain_of': ['IsEventWithDuration'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The actual start date of an event or occurrence with time duration.
 | direct |
| SlotDefinition({
  'name': 'datetime_begin_actual',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder '
     'Vorkommens mit Zeitdauer.\n'
     '[en] The actual start date and time of an event or occurrence with time '
     'duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeBeginActual',
  'owner': 'IsEventWithDuration',
  'domain_of': ['IsEventWithDuration'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The actual start date and time of an event or occurrence with time duration.
 | direct |
| SlotDefinition({
  'name': 'date_begin_planned',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit '
     'Zeitdauer.\n'
     '[en] The planned start date of an event or occurrence with time duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateBeginPlanned',
  'owner': 'IsEventWithDuration',
  'domain_of': ['IsEventWithDuration'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The planned start date of an event or occurrence with time duration.
 | direct |
| SlotDefinition({
  'name': 'datetime_begin_planned',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder '
     'Vorkommens mit Zeitdauer.\n'
     '[en] The planned start date and time of an event or occurrence with time '
     'duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeBeginPlanned',
  'owner': 'IsEventWithDuration',
  'domain_of': ['IsEventWithDuration'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The planned start date and time of an event or occurrence with time duration.
 | direct |
| SlotDefinition({
  'name': 'date_end_actual',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens mit '
     'Zeitdauer.\n'
     '[en] The actual end date of an event or occurrence with time duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateEndActual',
  'owner': 'IsEventWithDuration',
  'domain_of': ['IsEventWithDuration'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The actual end date of an event or occurrence with time duration.
 | direct |
| SlotDefinition({
  'name': 'datetime_end_actual',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder '
     'Vorkommens mit Zeitdauer.\n'
     '[en] The actual end date and time of an event or occurrence with time '
     'duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeEndActual',
  'owner': 'IsEventWithDuration',
  'domain_of': ['IsEventWithDuration'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The actual end date and time of an event or occurrence with time duration.
 | direct |
| SlotDefinition({
  'name': 'date_end_planned',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer.\n'
     '[en] The planned end date of an event or occurrence with time duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateEndPlanned',
  'owner': 'IsEventWithDuration',
  'domain_of': ['IsEventWithDuration'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The planned end date of an event or occurrence with time duration.
 | direct |
| SlotDefinition({
  'name': 'datetime_end_planned',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens '
     'mit Zeitdauer.\n'
     '[en] The planned end date and time of an event or occurrence with time '
     'duration.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeEndPlanned',
  'owner': 'IsEventWithDuration',
  'domain_of': ['IsEventWithDuration'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer.
[en] The planned end date and time of an event or occurrence with time duration.
 | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [IsProcessStep](IsProcessStep.md) | [de] Eine Mixin-Klasse für einen einzelnen Schritt in einem |














## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:IsEventWithDuration |
| native | act:IsEventWithDuration |







