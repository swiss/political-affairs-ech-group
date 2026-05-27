

# Class: InterestLink 


_[de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person zu einer Organisation._

_[en] An interest link (conflict of interest, political financing) of a person to an organization._

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
  'owner': 'InterestLink',
  'domain_of': ['Membership', 'InterestLink'],
  'range': 'PersonReference',
  'inlined': True
}) | 0..1 <br/> [PersonReference](PersonReference.md) | [de] Referenz auf eine Person mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.
[en] Reference to a person with snapshot data at time of linking.
 | direct |
| SlotDefinition({
  'name': 'interest_type',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, '
     'Verein).\n'
     '[en] Type of interest link (professional activity, political office, '
     'association).\n'),
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': 'association'}), Example({'value': 'professional_activity'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:interestType',
  'owner': 'InterestLink',
  'domain_of': ['InterestLink'],
  'range': 'InterestTypeEnum',
  'required': True
}) | 1 <br/> [InterestTypeEnum](InterestTypeEnum.md) | [de] Art der Interessenbindung (Berufliche Tätigkeit, Politische Ämter, Verein).
[en] Type of interest link (professional activity, political office, association).
 | direct |
| SlotDefinition({
  'name': 'organization_label',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[en] Label of the organization.\n[de] Bezeichnung der Organisation.\n',
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': 'ASTAG Schweizerischer Nutzfahrzeugverband, Bern'}),
    Example({'value': 'Allianz Sicherheit Schweiz, Baden'}),
    Example({'value': 'Birchmeier Holding AG, Döttingen'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:organizationLabel',
  'owner': 'InterestLink',
  'domain_of': ['InterestLink'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [en] Label of the organization.
[de] Bezeichnung der Organisation.
 | direct |
| SlotDefinition({
  'name': 'organization_uid',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[en] UID of the organization (for analysis with NOGA codes, etc.).\n'
     '[de] UID der Organisation (für Auswertungen mit NOGA-Codes, etc.).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:organizationUid',
  'owner': 'InterestLink',
  'domain_of': ['InterestLink'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [en] UID of the organization (for analysis with NOGA codes, etc.).
[de] UID der Organisation (für Auswertungen mit NOGA-Codes, etc.).
 | direct |
| SlotDefinition({
  'name': 'organization_address',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[en] Address of the organization.\n[de] Adresse der Organisation.\n',
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:organizationAddress',
  'owner': 'InterestLink',
  'domain_of': ['InterestLink'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [en] Address of the organization.
[de] Adresse der Organisation.
 | direct |
| SlotDefinition({
  'name': 'legal_form',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': '[en] Legal form of the organization.\n[de] Rechtsform der Organisation.\n',
  'alt_descriptions': JsonObj(),
  'examples': [Example({'value': 'Aktiengesellschaft'}),
    Example({'value': 'Gesellschaft mit beschränkter Haftung'}),
    Example({'value': 'Stiftung'})],
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:legalForm',
  'owner': 'InterestLink',
  'domain_of': ['InterestLink'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [en] Legal form of the organization.
[de] Rechtsform der Organisation.
 | direct |
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
  'owner': 'InterestLink',
  'domain_of': ['InterestLink', 'Occupation'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Position bezahlt ist.
[en] Indicates if the position is paid.
 | direct |
| SlotDefinition({
  'name': 'committee',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[en] Committee or board (e.g., foundation board, board of directors).\n'
     '[de] Gremium (z.B. Stiftungsrat, Verwaltungsrat).\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:committee',
  'owner': 'InterestLink',
  'domain_of': ['InterestLink'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [en] Committee or board (e.g., foundation board, board of directors).
[de] Gremium (z.B. Stiftungsrat, Verwaltungsrat).
 | direct |
| SlotDefinition({
  'name': 'function_role',
  'local_names': JsonObj(),
  'extensions': JsonObj(),
  'annotations': JsonObj(),
  'description': ('[en] Function or role in the organization.\n'
     '[de] Funktion oder Rolle in der Organisation.\n'),
  'alt_descriptions': JsonObj(),
  'from_schema': 'https://ld.ech.ch/schema/0294/actors',
  'rank': 1000,
  'slot_uri': 'act:functionRole',
  'owner': 'InterestLink',
  'domain_of': ['InterestLink'],
  'range': 'string'
}) | 0..1 <br/> [String](String.md) | [en] Function or role in the organization.
[de] Funktion oder Rolle in der Organisation.
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
  'owner': 'InterestLink',
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
  'owner': 'InterestLink',
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
  'owner': 'InterestLink',
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
  'owner': 'InterestLink',
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
  'owner': 'InterestLink',
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
  'owner': 'InterestLink',
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
  'owner': 'InterestLink',
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
  'owner': 'InterestLink',
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
  'owner': 'InterestLink',
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
  'owner': 'InterestLink',
  'domain_of': ['HasTemporalValidity'],
  'range': 'boolean'
}) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist.
[en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available.
 | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |
| [Person](Person.md) | [interest_links](interest_links.md) | range | [InterestLink](InterestLink.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:InterestLink |
| native | act:InterestLink |




## Examples
### Example: InterestLink-interest_links_il_burkart_003

```yaml
global_uri: act:il_burkart_003
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Bovida Real Estate AG, Baar
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_002

```yaml
global_uri: act:il_burkart_002
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Birchmeier Holding AG, Döttingen
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_001

```yaml
global_uri: act:il_burkart_001
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Burkart Advisory GmbH, Baden
legal_form: Gesellschaft mit beschränkter Haftung
committee: Geschäftsleitung
function_role: Geschäftsführer
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_004

```yaml
global_uri: act:il_burkart_004
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: ELCA Group SA, Lausanne
legal_form: Aktiengesellschaft
committee: Verwaltungsrat
function_role: Mitglied
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_011

```yaml
global_uri: act:il_burkart_011
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: Verein Landesausstellung Svizra27, Aarau
legal_form: Verein
committee: Vorstand
function_role: Mitglied
is_paid: false

```
### Example: InterestLink-interest_links_il_burkart_009

```yaml
global_uri: act:il_burkart_009
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: SUISSEDIGITAL Verband für Kommunikationsnetze
legal_form: Verein
committee: Vorstand
function_role: Mitglied
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_006

```yaml
global_uri: act:il_burkart_006
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: FDP.Die Liberalen
legal_form: Verein
committee: Vorstand
function_role: Präsident
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_008

```yaml
global_uri: act:il_burkart_008
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: professional_activity
organization_label: Stiebel Eltron AG, Lupfig
legal_form: Aktiengesellschaft
committee: Beirat
function_role: Beirat
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_005

```yaml
global_uri: act:il_burkart_005
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: ASTAG Schweizerischer Nutzfahrzeugverband, Bern
legal_form: Verein
committee: Zentralvorstand
function_role: Präsident
is_paid: true

```
### Example: InterestLink-interest_links_il_burkart_010

```yaml
global_uri: act:il_burkart_010
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: Allianz Sicherheit Schweiz, Baden
legal_form: Verein
committee: Vorstand
function_role: Präsident
is_paid: false

```
### Example: InterestLink-interest_links_il_burkart_007

```yaml
global_uri: act:il_burkart_007
person_reference:
  global_uri: https://www.wikidata.org/wiki/Q23060472
  label: Thierry Burkart
  group_label: FDP.Die Liberalen
interest_type: association
organization_label: FONDATION SUISSE DE DEMINAGE (FSD), Genf
legal_form: Stiftung
committee: Stiftungsrat
function_role: Vizepräsident
is_paid: false

```




