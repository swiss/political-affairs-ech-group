# Actors Schema

A schema describing political actors including persons, groups, memberships, and interest links.


URI: https://ld.ech.ch/schema/0294/actors

Name: actors-schema



## Classes

| Class | Description |
| --- | --- |
| [Address](Address.md) | An address with a type (e |
| [Citizenship](Citizenship.md) | Citizenship (also used for Nationality) of a person indicating the country an... |
| [Contact](Contact.md) | Contact information of a person indicating a type (e |
| [Container](Container.md) | Container for political actors, groups, and relationships |
| [ElectoralDistrict](ElectoralDistrict.md) | Electoral district or region where a person is politically active; with tempo... |
| [Gender](Gender.md) | Gender of a person indicating a gender code and temporal validity |
| [Group](Group.md) | A political group, organization, or body (e |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |
| [GroupType](GroupType.md) | Type of group (e |
| [HasCreationModificationDates](HasCreationModificationDates.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Ä... |
| [HasIdentification](HasIdentification.md) | [de] Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Ve... |
| [HasTemporalValidity](HasTemporalValidity.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gülti... |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |
| [IsEventWithDuration](IsEventWithDuration.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder V... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von instantanen Ereign... |
| [IsProcessStep](IsProcessStep.md) | [de] Eine Mixin-Klasse für einen einzelnen Schritt in einem |
| [LanguageProficiency](LanguageProficiency.md) | Language proficiency of a person indicating the language and whether it is th... |
| [Membership](Membership.md) | A membership relationship between a person and a group |
| [MultilingualValue](MultilingualValue.md) | [de] Ein mehrsprachiger String mit Angabe der Sprache |
| [Name](Name.md) | A name with a type (e |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |
| [RoleType](RoleType.md) | Role of a person in a membership or function (e |
| [Training](Training.md) | Training or education of a person indicating a type (e |



## Slots

| Slot | Description |
| --- | --- |
| [abbreviation](abbreviation.md) | Abbreviation (can be multilingual) |
| [address_type](address_type.md) | Type of address |
| [address_uri](address_uri.md) | URI of the address |
| [addresses](addresses.md) | Addresses with type (private, business, local) |
| [authorized_to_vote](authorized_to_vote.md) | Indicates if the person is authorized to vote |
| [birth_date](birth_date.md) | Exact date of birth if available and public |
| [birth_year](birth_year.md) | Year of birth |
| [citizenships](citizenships.md) | Citizenships of the person |
| [committee](committee.md) | Committee or board (e |
| [contact_type](contact_type.md) | Type of contact information |
| [contacts](contacts.md) | Contact information (email, website, social media) |
| [country](country.md) | ISO 3166 country code |
| [date_actual](date_actual.md) | [de] Das tatsächliche Datum eines instantanen Ereignisses oder Vorkommens (oh... |
| [date_begin_actual](date_begin_actual.md) | [de] Das tatsächliche Startdatum eines Ereignisses oder Vorkommens mit Zeitda... |
| [date_begin_planned](date_begin_planned.md) | [de] Das geplante Startdatum eines Ereignisses oder Vorkommens mit Zeitdauer |
| [date_created](date_created.md) | [de] Das Datum, an dem eine Entität erstellt wurde |
| [date_end_actual](date_end_actual.md) | [de] Das tatsächliche Enddatum eines Ereignisses oder Vorkommens mit Zeitdaue... |
| [date_end_planned](date_end_planned.md) | [de] Das geplante Enddatum eines Ereignisses oder Vorkommens mit Zeitdauer |
| [date_modified](date_modified.md) | [de] Das Datum, an dem eine Entität zuletzt geändert wurde |
| [date_planned](date_planned.md) | [de] Das geplante Datum eines instantanen Ereignisses oder Vorkommens (ohne Z... |
| [datetime_actual](datetime_actual.md) | [de] Das tatsächliche Datum und die Uhrzeit eines instantanen Ereignisses ode... |
| [datetime_begin_actual](datetime_begin_actual.md) | [de] Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorko... |
| [datetime_begin_planned](datetime_begin_planned.md) | [de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommen... |
| [datetime_created](datetime_created.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde |
| [datetime_end_actual](datetime_end_actual.md) | [de] Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkomm... |
| [datetime_end_planned](datetime_end_planned.md) | [de] Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommens ... |
| [datetime_modified](datetime_modified.md) | [de] Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde |
| [datetime_planned](datetime_planned.md) | [de] Das geplante Datum und die Uhrzeit eines instantanen Ereignisses oder Vo... |
| [death_date](death_date.md) | Exact date of death |
| [description](description.md) | Description of the entity |
| [district](district.md) | Electoral district or region |
| [electoral_district](electoral_district.md) | Link to the electoral district |
| [enterprise](enterprise.md) | Name of the enterprise |
| [enterprise_uid](enterprise_uid.md) | UID of the enterprise |
| [function_role](function_role.md) | Function or role in the organization |
| [gender_code](gender_code.md) | Gender code (e |
| [genders](genders.md) | Gender of the person |
| [global_uri](global_uri.md) | [de] Eine eindeutige, global gültige URI für die Entität |
| [group_label](group_label.md) | Name of the body/group at time of linking |
| [group_reference](group_reference.md) | Reference to a group with snapshot data at time of linking |
| [group_type](group_type.md) | Link to the group type |
| [group_type_enum](group_type_enum.md) | Link to the controlled vocabulary for group types |
| [groups](groups.md) | Collection of groups |
| [interest_links](interest_links.md) | Collection of interest links |
| [interest_type](interest_type.md) | Type of interest link (professional activity, political office, association) |
| [is_active](is_active.md) | [de] Gibt an, ob die Information aktuell gültig ist |
| [is_correspondence](is_correspondence.md) | Indicates if this is the preferred language |
| [is_native](is_native.md) | Indicates if this is the native language |
| [is_paid](is_paid.md) | Indicates if the position is paid |
| [label](label.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... |
| [label_long](label_long.md) | [de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel z... |
| [landing_page](landing_page.md) | Website providing further information |
| [language](language.md) | [de] Sprachcode im ISO 639-1 Format |
| [language_proficiencies](language_proficiencies.md) | Language proficiencies of the person |
| [legal_form](legal_form.md) | Legal form of the organization |
| [local_id](local_id.md) | [de] Lokaler Identifikator |
| [memberships](memberships.md) | Collection of memberships |
| [multilingual_value](multilingual_value.md) | [de] Ein mehrsprachiger Wert mit Angabe der Sprache |
| [name_type](name_type.md) | Type of name |
| [names](names.md) | Names of the person with type and value |
| [occupation_code](occupation_code.md) | ISCO-19 code of the occupation |
| [occupations](occupations.md) | Occupations or professions of the person |
| [organization_address](organization_address.md) | Address of the organization |
| [organization_label](organization_label.md) | Label of the organization |
| [organization_uid](organization_uid.md) | UID of the organization (for analysis with NOGA codes, etc |
| [parent_groups](parent_groups.md) | Link to parent groups |
| [party_color](party_color.md) | Party color (optional for parties) |
| [person_reference](person_reference.md) | Reference to a person with snapshot data at time of linking |
| [persons](persons.md) | Collection of persons |
| [picture](picture.md) | Link to an image (preferred: PNG, then JPG, then GIF) |
| [postal_code](postal_code.md) | Postal code |
| [postal_locality](postal_locality.md) | Locality |
| [pronouns](pronouns.md) | Pronouns used by the person |
| [remark](remark.md) | [de] Freitext-Bemerkung oder Notiz für Sonderfälle oder zusätzlichen Kontext ... |
| [role_label](role_label.md) | Descriptive label for the role when 'other' is selected in the RoleEnum |
| [role_type](role_type.md) | Role of the person in the membership or function |
| [role_type_enum](role_type_enum.md) | Role of the person in the membership or function |
| [spatial](spatial.md) | Spatial reference (fos-municipality number, fos-canton number, e |
| [statutes_url](statutes_url.md) | URL to party statutes (optional for parties) |
| [street_address](street_address.md) | Street address |
| [training_code](training_code.md) | ISCO-19 code of the training or education |
| [training_type](training_type.md) | Type of training or education |
| [trainings](trainings.md) | Trainings or educations of the person |
| [valid_from](valid_from.md) | [de] Das Datum, ab dem die Information gültig ist |
| [valid_through](valid_through.md) | [de] Das Datum, bis und mit dem die Information gültig ist |
| [value](value.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ... |
| [wikidata_uri](wikidata_uri.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AddressTypeEnum](AddressTypeEnum.md) | Types of addresses |
| [ContactTypeEnum](ContactTypeEnum.md) | Types of contact information |
| [GroupTypeEnum](GroupTypeEnum.md) | Types of political groups and organizations |
| [InterestTypeEnum](InterestTypeEnum.md) | Types of interest links (conflicts of interest, political financing) |
| [NameTypeEnum](NameTypeEnum.md) | Categories of name types according to https://dam-api |
| [RoleEnum](RoleEnum.md) | Roles a person can have within a membership |
| [TrainingTypeEnum](TrainingTypeEnum.md) | Types of training or education |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
