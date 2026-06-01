

## Class: HasTemporalValidity 


_[de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit einer Information (nicht eines Events) zur Verfügung stellt._

_[en] A mixin class that provides slots for modeling a temporal validity of information (not of an event)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| valid_from | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid.  |
| valid_through | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available.  |



### Mixin Usage

| mixed into | description |
| --- | --- |
| [Group](Group.md) | A political group, organization, or body (e |
| [Membership](Membership.md) | A membership relationship between a person and a group |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |
| [Name](Name.md) | A name with a type (e |
| [Citizenship](Citizenship.md) | Citizenship (also used for Nationality) of a person indicating the country an... |
| [Gender](Gender.md) | Gender of a person indicating a gender code and temporal validity |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |
| [Training](Training.md) | Training or education of a person indicating a type (e |
| [ElectoralDistrict](ElectoralDistrict.md) | Electoral district or region where a person is politically active; with tempo... |





















</div>