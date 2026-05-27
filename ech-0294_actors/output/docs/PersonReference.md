

# Class: PersonReference 


_[de] Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung. Ermöglicht historische Korrektheit auch wenn sich die Person später ändert._

_[en] Lightweight reference to a person with key identification data at time of linking. Preserves historical accuracy even if the person changes later._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
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
  'owner': 'PersonReference',
  'domain_of': ['Person', 'Group', 'PersonReference', 'GroupReference', 'Occupation',
    'GroupType', 'RoleType'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).
[en] Option to assign a label to a structured piece of information (e.g., display name, position, etc.).
 | direct |
| SlotDefinition({
  'name': 'label_long',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel '
     'zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.).\n'
     '[en] Option to assign an extended label to a structured piece of information '
     '(e.g., display name with title, position, etc.).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:labelLong',
  'owner': 'PersonReference',
  'domain_of': ['Person', 'PersonReference'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.).
[en] Option to assign an extended label to a structured piece of information (e.g., display name with title, position, etc.).
 | direct |
| SlotDefinition({
  'name': 'role_type',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[en] Role of the person in the membership or function.\n'
     '[de] Rolle der Person in der Mitgliedschaft oder Funktion.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:roleType',
  'owner': 'PersonReference',
  'domain_of': ['PersonReference', 'Membership'],
  'range': 'RoleType'
}) | 0..1 <br/> [RoleType](RoleType.md) | [en] Role of the person in the membership or function.
[de] Rolle der Person in der Mitgliedschaft oder Funktion.
 | direct |
| SlotDefinition({
  'name': 'group_label',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Name des Gremiums zum Zeitpunkt der Verknüpfung.\n'
     '[en] Name of the body/group at time of linking.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:groupLabel',
  'owner': 'PersonReference',
  'domain_of': ['PersonReference'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Name des Gremiums zum Zeitpunkt der Verknüpfung.
[en] Name of the body/group at time of linking.
 | direct |
| SlotDefinition({
  'name': 'local_id',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.\n'
     '[en] Local identifier. For example, a UUID from the council information '
     'system.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:localId',
  'owner': 'PersonReference',
  'domain_of': ['HasIdentification'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.
[en] Local identifier. For example, a UUID from the council information system.
 | [HasIdentification](HasIdentification.md) |
| SlotDefinition({
  'name': 'global_uri',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Eine eindeutige, global gültige URI für die Entität.\n'
     '[en] A unique, globally valid URI for the entity.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:globalURI',
  'identifier': True,
  'owner': 'PersonReference',
  'domain_of': ['HasIdentification'],
  'range': 'uriorcurie',
  'required': True
}) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität.
[en] A unique, globally valid URI for the entity.
 | [HasIdentification](HasIdentification.md) |
| SlotDefinition({
  'name': 'wikidata_uri',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. '
     'https://www.wikidata.org/wiki/Q39 für die Schweiz.\n'
     '[en] A URI that refers to a Wikidata entity, e.g. '
     'https://www.wikidata.org/wiki/Q39 for Switzerland.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:wikidataUri',
  'owner': 'PersonReference',
  'domain_of': ['HasIdentification'],
  'range': 'uriorcurie'
}) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz.
[en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland.
 | [HasIdentification](HasIdentification.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [person_reference](person_reference.md) | range | [PersonReference](PersonReference.md) |
| [InterestLink](InterestLink.md) | [person_reference](person_reference.md) | range | [PersonReference](PersonReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:PersonReference |
| native | act:PersonReference |







