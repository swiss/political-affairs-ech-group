

# Class: Training 


_[de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z.B. Schulabschluss, Universitätsabschluss, Militärdienst), eines Labels, eines ISCO-19 Codes und der zeitlichen Gültigkeit._

_[en] Training or education of a person indicating a type (e.g., school diploma, university degree, military service), a label, an ISCO-19 code, and temporal validity._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'training_type',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Typ der Ausbildung oder Bildung.\n[en] Type of training or education.\n',
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': 'schulabschluss'}), Example({'value': 'uni'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:trainingType',
  'owner': 'Training',
  'domain_of': ['Training'],
  'range': 'TrainingTypeEnum'
}) | 0..1 <br/> [TrainingTypeEnum](TrainingTypeEnum.md) | [de] Typ der Ausbildung oder Bildung.
[en] Type of training or education.
 | direct |
| SlotDefinition({
  'name': 'training_code',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] ISCO-19 Code der Ausbildung oder Bildung.\n'
     '[en] ISCO-19 code of the training or education.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:trainingCode',
  'owner': 'Training',
  'domain_of': ['Training'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] ISCO-19 Code der Ausbildung oder Bildung.
[en] ISCO-19 code of the training or education.
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
  'owner': 'Training',
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
  'owner': 'Training',
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
  'owner': 'Training',
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
  'owner': 'Training',
  'domain_of': ['HasTemporalValidity'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist.
[en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available.
 | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [trainings](trainings.md) | range | [Training](Training.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Training |
| native | act:Training |







