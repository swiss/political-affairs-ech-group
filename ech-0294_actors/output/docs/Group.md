

# Class: Group 


_[de] Eine politische Gruppe, Organisation oder Körperschaft (z.B. Partei, Kommission, Parlament, Departement)._

_[en] A political group, organization, or body (e.g., party, committee, parliament, department)._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| --  | -- | ------- | -- |
| SlotDefinition({
  'name': 'group_type',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament oder '
     'ähnliches. Die genaue Bennenung und Beschreibung der Gruppierung wird über '
     '`name` gemacht.\n'
     '[en] Link to the group type.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:groupType',
  'owner': 'Group',
  'domain_of': ['Group', 'GroupReference'],
  'range': 'GroupType'
}) | 0..1 <br/> [GroupType](GroupType.md) | [de] Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament oder ähnliches. Die genaue Bennenung und Beschreibung der Gruppierung wird über `name` gemacht.
[en] Link to the group type.
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
  'owner': 'Group',
  'domain_of': ['Person', 'Group', 'PersonReference', 'GroupReference', 'Occupation',
    'GroupType', 'RoleType'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).
[en] Option to assign a label to a structured piece of information (e.g., display name, position, etc.).
 | direct |
| SlotDefinition({
  'name': 'abbreviation',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Abkürzung (kann mehrsprachig sein).\n'
     '[en] Abbreviation (can be multilingual).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'owner': 'Group',
  'domain_of': ['Group', 'GroupReference'],
  'range': 'MultilingualValue',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [MultilingualValue](MultilingualValue.md) | [de] Abkürzung (kann mehrsprachig sein).
[en] Abbreviation (can be multilingual).
 | direct |
| SlotDefinition({
  'name': 'description',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Kurze Beschreibung der Gruppierung.\n[en] Description of the entity.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'owner': 'Group',
  'domain_of': ['Group'],
  'range': 'MultilingualValue',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [MultilingualValue](MultilingualValue.md) | [de] Kurze Beschreibung der Gruppierung.
[en] Description of the entity.
 | direct |
| SlotDefinition({
  'name': 'landing_page',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Website mit weiteren Informationen.\n'
     '[en] Website providing further information.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:landingPage',
  'owner': 'Group',
  'domain_of': ['Group'],
  'range': 'uri'
}) | 0..1 <br/> [Uri](Uri.md) | [de] Website mit weiteren Informationen.
[en] Website providing further information.
 | direct |
| SlotDefinition({
  'name': 'parent_groups',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Übergeordneten Gruppe. Zum Beispiel die Mutterpartei, zu '
     'Kantonalenparteien. Oder zur Beschreibung der Hierarchie in Exekutive. '
     'Verknüpfung von Subkommissionen mit Kommissionen. (parentGroup wird immer im '
     'selben group_type verwendet.)\n'
     '[en] Link to parent groups.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:parentGroup',
  'owner': 'Group',
  'domain_of': ['Group'],
  'range': 'uriorcurie',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [Uriorcurie](Uriorcurie.md) | [de] Übergeordneten Gruppe. Zum Beispiel die Mutterpartei, zu Kantonalenparteien. Oder zur Beschreibung der Hierarchie in Exekutive. Verknüpfung von Subkommissionen mit Kommissionen. (parentGroup wird immer im selben group_type verwendet.)
[en] Link to parent groups.
 | direct |
| SlotDefinition({
  'name': 'spatial',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer, z.B. '
     'ld.admin.ch/municipality/1234, ld.admin.ch/canton/23).\n'
     '[en] Spatial reference (fos-municipality number, fos-canton number, e.g., '
     'ld.admin.ch/municipality/1234, ld.admin.ch/canton/23).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'owner': 'Group',
  'domain_of': ['Group'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer, z.B. ld.admin.ch/municipality/1234, ld.admin.ch/canton/23).
[en] Spatial reference (fos-municipality number, fos-canton number, e.g., ld.admin.ch/municipality/1234, ld.admin.ch/canton/23).
 | direct |
| SlotDefinition({
  'name': 'contacts',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[en] Contact information (email, website, social media).\n'
     '[de] Kontaktinformationen (E-Mail, Website, Social Media).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:contact',
  'owner': 'Group',
  'domain_of': ['Person', 'Group'],
  'range': 'Contact',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [Contact](Contact.md) | [en] Contact information (email, website, social media).
[de] Kontaktinformationen (E-Mail, Website, Social Media).
 | direct |
| SlotDefinition({
  'name': 'addresses',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Adressen mit Typ (privat, geschäftlich, lokal).\n'
     '[en] Addresses with type (private, business, local).\n'),
  'alt_descriptions': JsonObj(),
  'examples': [Example({
      'value': ("[{'address_type': 'businessAddress', 'address_URI': "
         "'https://ld.admin.ch/address/12345', 'street_address': 'Bundesplatz 3', "
         "'postal_code': '3003', 'postal_locality': 'Bern'}, {'address_type': "
         "'privateAddress', 'postal_locality': 'Zürich'}]")
    })],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:address',
  'owner': 'Group',
  'domain_of': ['Person', 'Group'],
  'range': 'Address',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [Address](Address.md) | [de] Adressen mit Typ (privat, geschäftlich, lokal).
[en] Addresses with type (private, business, local).
 | direct |
| SlotDefinition({
  'name': 'statutes_url',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] URL zu Parteistatuten (optional für Parteien).\n'
     '[en] URL to party statutes (optional for parties).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:statutesURL',
  'owner': 'Group',
  'domain_of': ['Group'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] URL zu Parteistatuten (optional für Parteien).
[en] URL to party statutes (optional for parties).
 | direct |
| SlotDefinition({
  'name': 'party_color',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Parteifarbe (optional für Parteien).\n'
     '[en] Party color (optional for parties).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:partyColor',
  'owner': 'Group',
  'domain_of': ['Group'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Parteifarbe (optional für Parteien).
[en] Party color (optional for parties).
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
  'owner': 'Group',
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
  'owner': 'Group',
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
  'owner': 'Group',
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
  'owner': 'Group',
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
  'owner': 'Group',
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
  'owner': 'Group',
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
  'owner': 'Group',
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
  'owner': 'Group',
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
  'owner': 'Group',
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
  'owner': 'Group',
  'domain_of': ['HasTemporalValidity'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist.
[en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available.
 | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [groups](groups.md) | range | [Group](Group.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Group |
| native | act:Group |







