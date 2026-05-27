

# Class: Contact 


_[de] Kontaktinformation einer Person mit Angabe eines Typs (z.B. E-Mail, LinkedIn) und eines Werts._

_[en] Contact information of a person indicating a type (e.g., email, LinkedIn) and a value._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'contact_type',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Typ der Kontaktinformation.\n[en] Type of contact information.\n',
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': 'contact_website'}), Example({'value': 'email'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:contactType',
  'owner': 'Contact',
  'domain_of': ['Contact'],
  'range': 'ContactTypeEnum'
}) | 0..1 <br/> [ContactTypeEnum](ContactTypeEnum.md) | [de] Typ der Kontaktinformation.
[en] Type of contact information.
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
  'owner': 'Contact',
  'domain_of': ['Name', 'Training', 'Contact', 'MultilingualValue'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.
[en] The value of an information besides other attributes such as type, language, etc.
 | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |
| [Group](Group.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Contact |
| native | act:Contact |







