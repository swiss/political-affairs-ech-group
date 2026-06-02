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
| [HasCreationModificationDates](HasCreationModificationDates.md) | A mixin class that provides slots for modeling creation and modification date... |
| [HasIdentification](HasIdentification.md) | A mixin class that provides slots for the identification of an entity |
| [HasTemporalValidity](HasTemporalValidity.md) | A mixin class that provides slots for modeling a temporal validity of informa... |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |
| [IsEventWithDuration](IsEventWithDuration.md) | A mixin class that provides slots for modeling events or occurrences with tim... |
| [IsInstantaneousEvent](IsInstantaneousEvent.md) | A mixin class that provides slots for modeling instantaneous events or occurr... |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |
| [LanguageProficiency](LanguageProficiency.md) | Language proficiency of a person indicating the language and whether it is th... |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |
| [MultilingualValue](MultilingualValue.md) | A multilingual string with language specification |
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
| [address_uri](address_uri.md) | URI of the address from the Swiss federal building address register |
| [addresses](addresses.md) | Addresses with type (private, business, local) |
| [authorized_to_vote](authorized_to_vote.md) | Indicates if the person is authorized to vote in the group |
| [birth_date](birth_date.md) | Exact date of birth if available and public |
| [birth_year](birth_year.md) | Year of birth |
| [citizenships](citizenships.md) | Citizenships of the person |
| [committee](committee.md) | Committee or board within the organization (e |
| [contact_type](contact_type.md) | Type of contact information |
| [contacts](contacts.md) | Contact information (email, website, social media) |
| [country](country.md) | ISO 3166-1 alpha-2 country code |
| [date_actual](date_actual.md) | The actual date of an instantaneous event or occurrence (without time duratio... |
| [date_begin_actual](date_begin_actual.md) | The actual start date of an event or occurrence with time duration |
| [date_begin_planned](date_begin_planned.md) | The planned start date of an event or occurrence with time duration |
| [date_created](date_created.md) | The date when an entity was created |
| [date_end_actual](date_end_actual.md) | The actual end date of an event or occurrence with time duration |
| [date_end_planned](date_end_planned.md) | The planned end date of an event or occurrence with time duration |
| [date_modified](date_modified.md) | The date when an entity was last modified |
| [date_planned](date_planned.md) | The planned date of an instantaneous event or occurrence (without time durati... |
| [datetime_actual](datetime_actual.md) | The actual date and time of an instantaneous event or occurrence (without tim... |
| [datetime_begin_actual](datetime_begin_actual.md) | The actual start date and time of an event or occurrence with time duration |
| [datetime_begin_planned](datetime_begin_planned.md) | The planned start date and time of an event or occurrence with time duration |
| [datetime_created](datetime_created.md) | The date and time when an entity was created |
| [datetime_end_actual](datetime_end_actual.md) | The actual end date and time of an event or occurrence with time duration |
| [datetime_end_planned](datetime_end_planned.md) | The planned end date and time of an event or occurrence with time duration |
| [datetime_modified](datetime_modified.md) | The date and time when an entity was last modified |
| [datetime_planned](datetime_planned.md) | The planned date and time of an instantaneous event or occurrence (without ti... |
| [death_date](death_date.md) | Exact date of death |
| [description](description.md) | Description of the entity |
| [district](district.md) | Electoral district or region |
| [electoral_district](electoral_district.md) | Link to the electoral district |
| [function_role](function_role.md) | Function or role in the organization (e |
| [gender_code](gender_code.md) | Gender code |
| [genders](genders.md) | Gender of the person |
| [global_uri](global_uri.md) | A unique, globally valid URI for the entity |
| [group_label](group_label.md) | Name of the body/group at time of linking |
| [group_reference](group_reference.md) | Reference to a group with snapshot data at time of linking |
| [group_type](group_type.md) | Type of group (e |
| [group_type_enum](group_type_enum.md) | Link to the controlled vocabulary for group types |
| [groups](groups.md) | Collection of groups |
| [interest_links](interest_links.md) | Collection of interest links |
| [interest_type](interest_type.md) | Type of interest link (professional activity, political office, association) |
| [is_active](is_active.md) | Indicates whether the information is currently valid |
| [is_correspondence](is_correspondence.md) | Indicates if this is the preferred language |
| [is_native](is_native.md) | Indicates if this is the native language |
| [is_paid](is_paid.md) | Indicates if the position is paid |
| [label](label.md) | Assign a label to a structured piece of information (e |
| [label_long](label_long.md) | Assign an extended label to a structured piece of information (e |
| [landing_page](landing_page.md) | Website providing further information |
| [language](language.md) | Language code in ISO 639-1 format (two lowercase letters, e |
| [language_proficiencies](language_proficiencies.md) | Language proficiencies of the person |
| [legal_form](legal_form.md) | Legal form of the organization |
| [local_id](local_id.md) | Local identifier |
| [memberships](memberships.md) | Collection of memberships |
| [multilingual_value](multilingual_value.md) | A multilingual value with language specification |
| [name_type](name_type.md) | Type of name according to eCH-0011 (personNameData) |
| [names](names.md) | Names of the person with type and value |
| [occupation_code](occupation_code.md) | ISCO-19 code of the occupation |
| [occupations](occupations.md) | Occupations or professions of the person |
| [organization_address](organization_address.md) | Address of the organization |
| [organization_name](organization_name.md) | Name of the organization or enterprise |
| [organization_uid](organization_uid.md) | UID of the organization (eCH-0098 format: CHE-XXX |
| [parent_groups](parent_groups.md) | Link to parent groups |
| [party_color](party_color.md) | Party color as hexadecimal value (optional for parties, e |
| [person_reference](person_reference.md) | Reference to a person with snapshot data at time of linking |
| [persons](persons.md) | Collection of persons |
| [picture](picture.md) | Link to an image (preferred: PNG, then JPG, then GIF) |
| [postal_code](postal_code.md) | Postal code |
| [postal_locality](postal_locality.md) | Locality |
| [pronouns](pronouns.md) | Pronouns used by the person |
| [remark](remark.md) | Free-text remark or note for edge cases or additional context on a process st... |
| [role_label](role_label.md) | Descriptive label for the role when 'other' is selected in the RoleEnum |
| [role_type](role_type.md) | Role of the person in the membership or function |
| [role_type_enum](role_type_enum.md) | Role of the person in the membership or function |
| [spatial](spatial.md) | Spatial reference (fos-municipality number, fos-canton number, or country) |
| [statutes_url](statutes_url.md) | URL to party statutes (PDF or webpage; optional for parties) |
| [street_address](street_address.md) | Street address |
| [training_code](training_code.md) | ISCO-19 code of the training or education |
| [training_type](training_type.md) | Type of training or education |
| [trainings](trainings.md) | Trainings or educations of the person |
| [valid_from](valid_from.md) | The date from which the information is valid |
| [valid_through](valid_through.md) | The date until which the information is valid, inclusive |
| [value](value.md) | The value of an information besides other attributes such as type, language, ... |
| [wikidata_uri](wikidata_uri.md) | A URI that refers to a Wikidata entity, e |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AddressTypeEnum](AddressTypeEnum.md) | Types of addresses |
| [ContactTypeEnum](ContactTypeEnum.md) | Types of contact information |
| [GenderCodeEnum](GenderCodeEnum.md) | Gender codes for persons |
| [GroupTypeEnum](GroupTypeEnum.md) | Types of political groups and organizations |
| [InterestTypeEnum](InterestTypeEnum.md) | Types of interest links (conflicts of interest, political financing) |
| [LegalFormEnum](LegalFormEnum.md) | Legal forms based on the Swiss UID register codelist (eCH-0098) |
| [NameTypeEnum](NameTypeEnum.md) | Categories of name types according to eCH-0011 (personNameData) and https://d... |
| [RoleEnum](RoleEnum.md) | Roles a person can have within a membership |
| [TrainingTypeEnum](TrainingTypeEnum.md) | Types of training or education based on the Swiss BFS LEVEL_EDUC codelist |


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
