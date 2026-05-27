

# Class: IsInstantaneousEvent 


_[de] Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereignissen oder Vorkommnissen (ohne Zeitdauer) zur Verfügung stellt._

_[en] A mixin class that provides slots for modeling instantaneous events or occurrences (without time duration)._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'date_actual',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommens '
     '(ohne Zeitdauer).\n'
     '[en] The actual date of an instantaneous event or occurrence (without time '
     'duration).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateActual',
  'owner': 'IsInstantaneousEvent',
  'domain_of': ['IsInstantaneousEvent'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommens (ohne Zeitdauer).
[en] The actual date of an instantaneous event or occurrence (without time duration).
 | direct |
| SlotDefinition({
  'name': 'datetime_actual',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses '
     'oder Vorkommens (ohne Zeitdauer).\n'
     '[en] The actual date and time of an instantaneous event or occurrence '
     '(without time duration).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeActual',
  'owner': 'IsInstantaneousEvent',
  'domain_of': ['IsInstantaneousEvent'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses oder Vorkommens (ohne Zeitdauer).
[en] The actual date and time of an instantaneous event or occurrence (without time duration).
 | direct |
| SlotDefinition({
  'name': 'date_planned',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das geplante Datum eines instantanen Ereignisses oder Vorkommens (ohne '
     'Zeitdauer).\n'
     '[en] The planned date of an instantaneous event or occurrence (without time '
     'duration).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datePlanned',
  'owner': 'IsInstantaneousEvent',
  'domain_of': ['IsInstantaneousEvent'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das geplante Datum eines instantanen Ereignisses oder Vorkommens (ohne Zeitdauer).
[en] The planned date of an instantaneous event or occurrence (without time duration).
 | direct |
| SlotDefinition({
  'name': 'datetime_planned',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder '
     'Vorkommens (ohne Zeitdauer).\n'
     '[en] The planned date and time of an instantaneous event or occurrence '
     '(without time duration).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimePlanned',
  'owner': 'IsInstantaneousEvent',
  'domain_of': ['IsInstantaneousEvent'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vorkommens (ohne Zeitdauer).
[en] The planned date and time of an instantaneous event or occurrence (without time duration).
 | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |














## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:IsInstantaneousEvent |
| native | act:IsInstantaneousEvent |







