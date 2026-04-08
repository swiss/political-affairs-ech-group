---
search:
  boost: 10.0
---

# Class: IsInstantaneousEvent 


_[de] Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereignissen oder Vorkommnissen (ohne Zeitdauer) zur Verfügung stellt._

_[en] A mixin class that provides slots for modeling instantaneous events or occurrences (without time duration)._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [date_actual](date_actual.md) | 0..1 <br/> [Date](Date.md) | [de] Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommens (oh... | direct |
| [datetime_actual](datetime_actual.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses ode... | direct |
| [date_planned](date_planned.md) | 0..1 <br/> [Date](Date.md) | [de] Das geplante Datum eines instantanen Ereignisses oder Vorkommens (ohne Z... | direct |
| [datetime_planned](datetime_planned.md) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vo... | direct |



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







