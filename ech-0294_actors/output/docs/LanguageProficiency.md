

# Class: LanguageProficiency 


_[de] Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um die bevorzugte Sprache oder die Muttersprache handelt._

_[en] Language proficiency of a person indicating the language and whether it is the preferred language or native language._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
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
  'owner': 'LanguageProficiency',
  'domain_of': ['LanguageProficiency', 'MultilingualValue'],
  'range': 'string',
  'pattern': '^[a-z]{2}$'
}) | 0..1 <br/> [String](String.md) | [de] Sprachcode im ISO 639-1 Format.
[en] Language code in ISO 639-1 format.
 | direct |
| SlotDefinition({
  'name': 'is_correspondence',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Gibt an, ob es sich um die bevorzugte Sprache handelt.\n'
     '[en] Indicates if this is the preferred language.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:isCorrespondence',
  'owner': 'LanguageProficiency',
  'domain_of': ['LanguageProficiency'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob es sich um die bevorzugte Sprache handelt.
[en] Indicates if this is the preferred language.
 | direct |
| SlotDefinition({
  'name': 'is_native',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Gibt an, ob es sich um die Muttersprache handelt.\n'
     '[en] Indicates if this is the native language.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:isNative',
  'owner': 'LanguageProficiency',
  'domain_of': ['LanguageProficiency'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob es sich um die Muttersprache handelt.
[en] Indicates if this is the native language.
 | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [language_proficiencies](language_proficiencies.md) | range | [LanguageProficiency](LanguageProficiency.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:LanguageProficiency |
| native | act:LanguageProficiency |







