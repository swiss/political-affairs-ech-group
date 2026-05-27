

# Class: MultilingualValue 


_[de] Ein mehrsprachiger String mit Angabe der Sprache._

_[en] A multilingual string with language specification._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'value',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Der eigentliche Wert einer Information neben weiteren attributen wie '
     'Typ, Sprache, etc.\n'
     '[en] The value of an information besides other attributes such as type, '
     'language, etc.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:value',
  'owner': 'MultilingualValue',
  'domain_of': ['Name', 'Training', 'Contact', 'MultilingualValue'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.
[en] The value of an information besides other attributes such as type, language, etc.
 | direct |
| SlotDefinition({
  'name': 'language',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Sprachcode im ISO 639-1 Format.\n'
     '[en] Language code in ISO 639-1 format.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:language',
  'owner': 'MultilingualValue',
  'domain_of': ['LanguageProficiency', 'MultilingualValue'],
  'range': 'string',
  'pattern': '^[a-z]{2}$'
}) | 0..1 <br/> [String](String.md) | [de] Sprachcode im ISO 639-1 Format.
[en] Language code in ISO 639-1 format.
 | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [abbreviation](abbreviation.md) | range | [MultilingualValue](MultilingualValue.md) |
| [Group](Group.md) | [description](description.md) | range | [MultilingualValue](MultilingualValue.md) |
| [GroupReference](GroupReference.md) | [abbreviation](abbreviation.md) | range | [MultilingualValue](MultilingualValue.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:MultilingualValue |
| native | act:MultilingualValue |







