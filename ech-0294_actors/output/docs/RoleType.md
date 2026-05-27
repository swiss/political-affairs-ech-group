

# Class: RoleType 


_[de] Rolle einer Person in einer Mitgliedschaft oder Funktion (z.B. Mitglied, Präsident, Stellvertreter)._

_[en] Role of a person in a membership or function (e.g., member, president, deputy)._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'role_type_enum',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[en] Role of the person in the membership or function.\n'
     '[de] Rolle der Person in der Mitgliedschaft oder Funktion.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:roleTypeEnum',
  'owner': 'RoleType',
  'domain_of': ['RoleType'],
  'range': 'RoleEnum'
}) | 0..1 <br/> [RoleEnum](RoleEnum.md) | [en] Role of the person in the membership or function.
[de] Rolle der Person in der Mitgliedschaft oder Funktion.
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
  'owner': 'RoleType',
  'domain_of': ['Person', 'Group', 'PersonReference', 'GroupReference', 'Occupation',
    'GroupType', 'RoleType'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).
[en] Option to assign a label to a structured piece of information (e.g., display name, position, etc.).
 | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PersonReference](PersonReference.md) | [role_type](role_type.md) | range | [RoleType](RoleType.md) |
| [Membership](Membership.md) | [role_type](role_type.md) | range | [RoleType](RoleType.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:RoleType |
| native | act:RoleType |







