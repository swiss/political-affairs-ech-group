

# Class: Person 


_[de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Berufen._

_[en] A person with identifiers, names, addresses, citizenships, and occupations._

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
  'owner': 'Person',
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
  'owner': 'Person',
  'domain_of': ['Person', 'PersonReference'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel zu vergeben (bspw. Anzeigename mit Titel, Anstellung, etc.).
[en] Option to assign an extended label to a structured piece of information (e.g., display name with title, position, etc.).
 | direct |
| SlotDefinition({
  'name': 'birth_year',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Geburtsjahr.\n'
     '[en] Year of birth. Only to be used, if there is no full `birthDate` '
     'available.\n'),
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': '1952'}), Example({'value': '1964'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:birthYear',
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'integer'
}) | 0..1 <br/> [Integer](Integer.md) | [de] Geburtsjahr.
[en] Year of birth. Only to be used, if there is no full `birthDate` available.
 | direct |
| SlotDefinition({
  'name': 'birth_date',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Genaues Geburtsdatum.\n'
     '[en] Exact date of birth if available and public. This field has precedence '
     'over the field `birthYear`.\n'),
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': '1952-03-11'}), Example({'value': '1964-07-12'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'schema:birthDate',
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Genaues Geburtsdatum.
[en] Exact date of birth if available and public. This field has precedence over the field `birthYear`.
 | direct |
| SlotDefinition({
  'name': 'death_date',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Genaues Todesdatum.\n[en] Exact date of death.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'schema:deathDate',
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'date'
}) | 0..1 <br/> [Date](Date.md) | [de] Genaues Todesdatum.
[en] Exact date of death.
 | direct |
| SlotDefinition({
  'name': 'picture',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF).\n'
     '[en] Link to an image (preferred: PNG, then JPG, then GIF).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'uri'
}) | 0..1 <br/> [Uri](Uri.md) | [de] Link zu einem Bild (bevorzugt: PNG, dann JPG, dann GIF).
[en] Link to an image (preferred: PNG, then JPG, then GIF).
 | direct |
| SlotDefinition({
  'name': 'names',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[en] Names of the person with type and value.\n'
     '[de] Namen der Person mit Typ und Wert.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:name',
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'Name',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [Name](Name.md) | [en] Names of the person with type and value.
[de] Namen der Person mit Typ und Wert.
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
  'owner': 'Person',
  'domain_of': ['Person', 'Group'],
  'range': 'Address',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [Address](Address.md) | [de] Adressen mit Typ (privat, geschäftlich, lokal).
[en] Addresses with type (private, business, local).
 | direct |
| SlotDefinition({
  'name': 'language_proficiencies',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Sprachkompetenzen der Person.\n'
     '[en] Language proficiencies of the person.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:languageProficiency',
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'LanguageProficiency',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [LanguageProficiency](LanguageProficiency.md) | [de] Sprachkompetenzen der Person.
[en] Language proficiencies of the person.
 | direct |
| SlotDefinition({
  'name': 'citizenships',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Staatsbürgerschaften der Person.\n[en] Citizenships of the person.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:citizenship',
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'Citizenship',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [Citizenship](Citizenship.md) | [de] Staatsbürgerschaften der Person.
[en] Citizenships of the person.
 | direct |
| SlotDefinition({
  'name': 'genders',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Geschlecht der Person.\n[en] Gender of the person.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:gender',
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'Gender',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [Gender](Gender.md) | [de] Geschlecht der Person.
[en] Gender of the person.
 | direct |
| SlotDefinition({
  'name': 'occupations',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Berufe oder Tätigkeiten der Person.\n'
     '[en] Occupations or professions of the person.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:occupation',
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'Occupation',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [Occupation](Occupation.md) | [de] Berufe oder Tätigkeiten der Person.
[en] Occupations or professions of the person.
 | direct |
| SlotDefinition({
  'name': 'trainings',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Ausbildungen oder Bildungen der Person.\n'
     '[en] Trainings or educations of the person.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:training',
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'Training',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [Training](Training.md) | [de] Ausbildungen oder Bildungen der Person.
[en] Trainings or educations of the person.
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
  'owner': 'Person',
  'domain_of': ['Person', 'Group'],
  'range': 'Contact',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [Contact](Contact.md) | [en] Contact information (email, website, social media).
[de] Kontaktinformationen (E-Mail, Website, Social Media).
 | direct |
| SlotDefinition({
  'name': 'electoral_district',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[de] Link zum Wahlbezirk.\n[en] Link to the electoral district.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:electoralDistrict',
  'owner': 'Person',
  'domain_of': ['Person'],
  'range': 'ElectoralDistrict'
}) | 0..1 <br/> [ElectoralDistrict](ElectoralDistrict.md) | [de] Link zum Wahlbezirk.
[en] Link to the electoral district.
 | direct |
| SlotDefinition({
  'name': 'interest_links',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Sammlung von Interessenbindungen.\n'
     '[en] Collection of interest links.range: InterestLink\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:interestLink',
  'owner': 'Person',
  'domain_of': ['Container', 'Person'],
  'range': 'InterestLink',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': True
}) | * <br/> [InterestLink](InterestLink.md) | [de] Sammlung von Interessenbindungen.
[en] Collection of interest links.range: InterestLink
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
  'owner': 'Person',
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
  'owner': 'Person',
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
  'owner': 'Person',
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
  'owner': 'Person',
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
  'owner': 'Person',
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
  'owner': 'Person',
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
  'owner': 'Person',
  'domain_of': ['HasCreationModificationDates'],
  'range': 'datetime'
}) | 0..1 <br/> [Datetime](Datetime.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.
[en] The date and time when an entity was last modified.
 | [HasCreationModificationDates](HasCreationModificationDates.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [persons](persons.md) | range | [Person](Person.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Person |
| native | act:Person |




## Examples
### Example: Person-swiss_politicians_Beat_Jans

```yaml
local_id: 4032
global_uri: https://data-example.parlament.ch/person/4032
wikidata_uri: https://www.wikidata.org/wiki/Q813067
label: Beat Jans
label_long: Beat Jans, dipl. nat. ETH
birth_year: 1964
birth_date: 1964-07-12
picture: https://commons.wikimedia.org/wiki/File:Beat_Jans_(2026)_(cropped).jpg
names:
- name_type: PersonFirstName
  value: Beat
- name_type: PersonOfficialName
  value: Jans
  valid_from: 1964-07-12
addresses:
- address_type: businessAddress
  postal_locality: Basel-Stadt
language_proficiencies:
- language: de
  is_correspondence: true
  is_native: true
citizenships:
- country: CH
  valid_from: 1964-07-12
genders:
- gender_code: male
  valid_from: 1964-07-12
occupations:
- label: Politiker
  valid_from: 1964-01-01
  is_active: true
trainings:
- training_type: uni
  value: dipl. nat. ETH
contacts:
- contact_type: email
  value: beat.jans@admin.ch
- contact_type: contact_website
  value: http://www.beat-jans.ch
electoral_district:
  district: Basel-Stadt
  valid_from: 2010-01-01

```
### Example: Person-douglas_adams_Douglas_Adams

```yaml
global_uri: https://www.wikidata.org/wiki/Q42
label: Douglas Adams
label_long: Douglas Noël Adams
birth_year: 1952
birth_date: 1952-03-11
picture: https://commons.wikimedia.org/wiki/File:Douglas_adams_portrait.jpg
names:
- name_type: PersonFirstName
  value: Douglas
- name_type: PersonOfficialName
  value: Adams
  valid_from: 1952-03-11
addresses:
- address_type: privateAddress
  address_uri: https://www.wikidata.org/wiki/Q42#P969
  street_address: 1234 Fictional St, London, UK
  postal_code: 12345
  postal_locality: London
language_proficiencies:
- language: en
  is_correspondence: true
  is_native: true
citizenships:
- country: GB
  valid_from: 1952-03-11
genders:
- gender_code: male
  valid_from: 1952-03-11
  pronouns:
  - he
  - him
occupations:
- label: writer
  valid_from: 1979-01-01
  valid_through: 2001-05-11
  is_active: false
  is_paid: true
trainings:
- training_type: schulabschluss
  value: High School Diploma
contacts:
- contact_type: email
  value: douglas.adams@adams-familiy.org
electoral_district:
  district: London Central
  valid_from: 2020-01-01
  valid_through: 2025-01-01

```




