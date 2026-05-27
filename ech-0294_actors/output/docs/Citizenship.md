

# Class: Citizenship 


_[de] Staatsangehörigkeit einer Person unter Angabe des Landes und der zeitlichen Gültigkeit. Wenn kein `valid_from` angegeben ist, ist diese Information nicht bekannt. Ist bekannt, dass die Staatsangehörigkeit seit der Geburt gültig ist, ist das Geburtsdatum hier anzugeben. Wenn kein `valid_through` angegeben ist, ist die Staatsangehörigkeit weiterhin gültig._

_[en] Citizenship (also used for Nationality) of a person indicating the country and temporal validity. If there is no `valid_from` provided, the information is not known. If it is known that the citizenship is valid from birth, the birthdate is to be repeated here. If there is no `valid_through`, the citizenship is still active._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'country',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] ISO 3166 Ländercode.\n[en] ISO 3166 country code.\n',
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': 'CH'}), Example({'value': 'GB'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:country',
  'owner': 'Citizenship',
  'domain_of': ['Citizenship'],
  'range': 'string',
  'pattern': '^[A-Z]{2}$'
}) | 0..1 <br/> [String](String.md) | [de] ISO 3166 Ländercode.
[en] ISO 3166 country code.
 | direct |
| SlotDefinition({
  'name': 'valid_from',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das Datum, ab dem die Information gültig ist.\n'
     '[en] The date from which the information is valid.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'schema:validFrom',
  'owner': 'Citizenship',
  'domain_of': ['HasTemporalValidity'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist.
[en] The date from which the information is valid.
 | [HasTemporalValidity](HasTemporalValidity.md) |
| SlotDefinition({
  'name': 'valid_through',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das Datum, bis und mit dem die Information gültig ist.\n'
     '[en] The date until which the information is valid, inclusive.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'schema:validThrough',
  'owner': 'Citizenship',
  'domain_of': ['HasTemporalValidity'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist.
[en] The date until which the information is valid, inclusive.
 | [HasTemporalValidity](HasTemporalValidity.md) |
| SlotDefinition({
  'name': 'is_active',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, '
     'wenn diese Information explizit vorhanden ist.\n'
     '[en] Indicates whether the information is currently valid. Can be useful '
     'when this information is explicitly available.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:isCurrent',
  'owner': 'Citizenship',
  'domain_of': ['HasTemporalValidity'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist.
[en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available.
 | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [citizenships](citizenships.md) | range | [Citizenship](Citizenship.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Citizenship |
| native | act:Citizenship |







