

# Class: Membership 


_[de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe._

_[en] A membership relationship between a person and a group._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'person_reference',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der '
     'Verknüpfung.\n'
     '[en] Reference to a person with snapshot data at time of linking.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:personReference',
  'owner': 'Membership',
  'domain_of': ['Membership', 'InterestLink'],
  'range': 'PersonReference',
  'inlined': True
}) | 0..1 <br/> [PersonReference](PersonReference.md) | [de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.
[en] Reference to a person with snapshot data at time of linking.
 | direct |
| SlotDefinition({
  'name': 'group_reference',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der '
     'Verknüpfung.\n'
     '[en] Reference to a group with snapshot data at time of linking.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:groupReference',
  'owner': 'Membership',
  'domain_of': ['Membership'],
  'range': 'GroupReference',
  'inlined': True
}) | 0..1 <br/> [GroupReference](GroupReference.md) | [de] Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.
[en] Reference to a group with snapshot data at time of linking.
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
  'owner': 'Membership',
  'domain_of': ['PersonReference', 'Membership'],
  'range': 'RoleType'
}) | 0..1 <br/> [RoleType](RoleType.md) | [en] Role of the person in the membership or function.
[de] Rolle der Person in der Mitgliedschaft oder Funktion.
 | direct |
| SlotDefinition({
  'name': 'authorized_to_vote',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Gibt an, ob die Person stimmberechtigt ist.\n'
     '[en] Indicates if the person is authorized to vote.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:authorizedToVote',
  'owner': 'Membership',
  'domain_of': ['Membership'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Person stimmberechtigt ist.
[en] Indicates if the person is authorized to vote.
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
  'owner': 'Membership',
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
  'owner': 'Membership',
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
  'owner': 'Membership',
  'domain_of': ['HasIdentification'],
  'range': 'uriorcurie'
}) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z.B. https://www.wikidata.org/wiki/Q39 für die Schweiz.
[en] A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland.
 | [HasIdentification](HasIdentification.md) |
| SlotDefinition({
  'name': 'date_created',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das Datum, an dem eine Entität erstellt wurde.\n'
     '[en] The date when an entity was created.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateCreated',
  'owner': 'Membership',
  'domain_of': ['HasCreationModificationDates'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität erstellt wurde.
[en] The date when an entity was created.
 | [HasCreationModificationDates](HasCreationModificationDates.md) |
| SlotDefinition({
  'name': 'datetime_created',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.\n'
     '[en] The date and time when an entity was created.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeCreated',
  'owner': 'Membership',
  'domain_of': ['HasCreationModificationDates'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.
[en] The date and time when an entity was created.
 | [HasCreationModificationDates](HasCreationModificationDates.md) |
| SlotDefinition({
  'name': 'date_modified',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das Datum, an dem eine Entität zuletzt geändert wurde.\n'
     '[en] The date when an entity was last modified.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:dateModified',
  'owner': 'Membership',
  'domain_of': ['HasCreationModificationDates'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde.
[en] The date when an entity was last modified.
 | [HasCreationModificationDates](HasCreationModificationDates.md) |
| SlotDefinition({
  'name': 'datetime_modified',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.\n'
     '[en] The date and time when an entity was last modified.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'mcm:datetimeModified',
  'owner': 'Membership',
  'domain_of': ['HasCreationModificationDates'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.
[en] The date and time when an entity was last modified.
 | [HasCreationModificationDates](HasCreationModificationDates.md) |
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
  'owner': 'Membership',
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
  'owner': 'Membership',
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
  'owner': 'Membership',
  'domain_of': ['HasTemporalValidity'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist.
[en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available.
 | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [memberships](memberships.md) | range | [Membership](Membership.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Membership |
| native | act:Membership |







