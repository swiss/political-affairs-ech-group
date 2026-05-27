

# Class: Occupation 


_[de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Codes, ob die Position bezahlt ist, und der zeitlichen Gültigkeit._

_[en] Occupation or profession of a person indicating a label, an ISCO-19 code, whether the position is paid, and temporal validity._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'is_paid',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Gibt an, ob die Position bezahlt ist.\n'
     '[en] Indicates if the position is paid.\n'),
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': 'False'}), Example({'value': 'True'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:isPaid',
  'owner': 'Occupation',
  'domain_of': ['InterestLink', 'Occupation'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Position bezahlt ist.
[en] Indicates if the position is paid.
 | direct |
| SlotDefinition({
  'name': 'occupation_code',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] ISCO-19 Code der Tätigkeit.\n[en] ISCO-19 code of the occupation.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:occupationCode',
  'owner': 'Occupation',
  'domain_of': ['Occupation'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] ISCO-19 Code der Tätigkeit.
[en] ISCO-19 code of the occupation.
 | direct |
| SlotDefinition({
  'name': 'label',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben '
     '(bspw. Anzeigename, Anstellung, etc.).\n'
     '[en] Option to assign a label to a structured piece of information (e.g., '
     'display name, position, etc.).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:label',
  'owner': 'Occupation',
  'domain_of': ['Person', 'Group', 'PersonReference', 'GroupReference', 'Occupation',
    'GroupType', 'RoleType'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).
[en] Option to assign a label to a structured piece of information (e.g., display name, position, etc.).
 | direct |
| SlotDefinition({
  'name': 'enterprise_uid',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] UID des Unternehmens.\n[en] UID of the enterprise.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:enterpriseUid',
  'owner': 'Occupation',
  'domain_of': ['Occupation'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] UID des Unternehmens.
[en] UID of the enterprise.
 | direct |
| SlotDefinition({
  'name': 'enterprise',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Name des Unternehmens.\n[en] Name of the enterprise.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:enterprise',
  'owner': 'Occupation',
  'domain_of': ['Occupation'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Name des Unternehmens.
[en] Name of the enterprise.
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
  'owner': 'Occupation',
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
  'owner': 'Occupation',
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
  'owner': 'Occupation',
  'domain_of': ['HasTemporalValidity'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist.
[en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available.
 | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [occupations](occupations.md) | range | [Occupation](Occupation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Occupation |
| native | act:Occupation |




## Examples
### Example: Occupation-douglas_adams_Douglas_Adams_writer

```yaml
label: writer
valid_from: 1979-01-01
valid_through: 2001-05-11
is_active: false
is_paid: true

```
### Example: Occupation-swiss_politicians_Beat_Jans_Politiker

```yaml
label: Politiker
valid_from: 1964-01-01
is_active: true

```




