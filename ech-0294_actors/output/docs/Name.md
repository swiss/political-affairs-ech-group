

# Class: Name 


_[de] Ein Name mit einem Typ (z.B. Rufname, amtlicher Name) und einem Wert und einer zeitlichen Gültigkeit._

_[en] A name with a type (e.g., call name, official name) and a value._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'name_type',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Typ des Namens.\n[en] Type of name.\n',
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': 'PersonFirstName'}),
    Example({'value': 'PersonOfficialName'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:nameType',
  'owner': 'Name',
  'domain_of': ['Name'],
  'range': 'NameTypeEnum'
}) | 0..1 <br/> [NameTypeEnum](NameTypeEnum.md) | [de] Typ des Namens.
[en] Type of name.
 | direct |
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
  'owner': 'Name',
  'domain_of': ['Name', 'Training', 'Contact', 'MultilingualValue'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.
[en] The value of an information besides other attributes such as type, language, etc.
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
  'owner': 'Name',
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
  'owner': 'Name',
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
  'owner': 'Name',
  'domain_of': ['HasTemporalValidity'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist.
[en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available.
 | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [names](names.md) | range | [Name](Name.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Name |
| native | act:Name |







